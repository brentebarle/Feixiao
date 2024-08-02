import discord
import asyncio
import random
from wolfram_client import wolfram_client
from config import TOKEN, sample_queries

# Create a Discord client with intents
intents = discord.Intents.default()
intents.typing = True
intents.message_content = True
intents.presences = True
intents.messages = True

client = discord.Client(intents=intents)

# Dictionary to store query results, user states, and message IDs
query_results = {}
user_states = {}
user_states_time = {}
message_ids = {}

# Timeout duration in seconds
TIMEOUT = 15

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    spinner = ['with brotAI // Computational', 'with brotAI // Powered by WolframAlpha']
    while True:
        for char in spinner:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{char}"))
            await asyncio.sleep(30)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower().strip()

    # Check if the message starts with "hey feixiao"
    if content.startswith('hey feixiao'):
        query = content[len('hey feixiao'):].strip()
        if query:
            user_states[message.author.id] = 'active'
            await handle_query(message, query)
            return
        else:
            user_states[message.author.id] = 'waiting_for_query'
            user_states_time[message.author.id] = asyncio.get_event_loop().time()
            random_query = random.choice(sample_queries)
            embed = discord.Embed(color=discord.Color.green(), description=f"What's up? Got any questions? You can start by asking something like '{random_query}'.")
            msg = await message.reply(embed=embed)
            message_ids[message.author.id] = msg.id
        return

    if content in ['never mind', 'nvm']:
        if message.author.id in user_states:
            del user_states[message.author.id]
            del user_states_time[message.author.id]
            if message.author.id in message_ids:
                msg = await message.channel.fetch_message(message_ids[message.author.id])
                await msg.edit(embed=discord.Embed(color=discord.Color.orange(), description="Stopped waiting for a query."))
                del message_ids[message.author.id]
            return

    if user_states.get(message.author.id) == 'waiting_for_query':
        current_time = asyncio.get_event_loop().time()
        if current_time - user_states_time.get(message.author.id, 0) > TIMEOUT:
            del user_states[message.author.id]
            del user_states_time[message.author.id]
            if message.author.id in message_ids:
                msg = await message.channel.fetch_message(message_ids[message.author.id])
                await msg.edit(embed=discord.Embed(color=discord.Color.red(), description="Timed out. Please start a new query."))
                del message_ids[message.author.id]
            return

        # Handle the next message as the query if the user is in waiting_for_query state
        user_states[message.author.id] = 'active'
        await handle_query(message, content)
        return

    if client.user.mention in content:
        query = content.replace(client.user.mention, '').strip()
        if not query:
            embed = discord.Embed(color=discord.Color.green(), description="Please provide a query after mentioning the bot.")
            await message.reply(embed=embed)
            return
        user_states[message.author.id] = 'active'
        await handle_query(message, query)
        return

    if user_states.get(message.author.id) == 'active':
        query = content
        await handle_query(message, query)
        return

async def handle_query(message, query):
    try:
        async with message.channel.typing():
            # Query Wolfram Alpha with closest interpretation
            res = await client.loop.run_in_executor(None, lambda: wolfram_client.query(query))

            # Extract the closest interpretation if available
            closest_interpretation = None
            if 'interpretation' in res:
                closest_interpretation = res['interpretation']

            # Construct result message
            result_message = "Results:\n"
            if closest_interpretation:
                result_message += f"Closest interpretation: {closest_interpretation}\n"

            query_results[message.id] = {
                'query': query,
                'results': res.pods
            }

            raw_text = None
            chosen_image_url = None
            title = None

            for pod in res.pods:
                if pod.title.lower() in ["input", "input interpretation"]:
                    raw_text = "\n".join(subpod.plaintext for subpod in pod.subpods if subpod.plaintext)
                    title = pod.title
                    break

            image_data = []
            for pod in res.pods:
                if pod.title.lower() not in ["input", "input interpretation"]:
                    image_data.extend(subpod.img.src for subpod in pod.subpods if subpod.img)

            if image_data:
                chosen_image_url = image_data[0]

            embed = discord.Embed(color=discord.Color.blue())
            if title:
                embed.title = f"Feixiao // {title} - Results for [{raw_text}]"
            if chosen_image_url:
                embed.set_image(url=chosen_image_url)
            if not title and not chosen_image_url:
                # Create a red embed for no relevant data found
                embed = discord.Embed(color=discord.Color.red(), title="Feixiao // No Results", description="No relevant data found for the query.")

            await message.reply(embed=embed)

    except Exception as e:
        print(f'Error: {e}')
        error_embed = discord.Embed(color=discord.Color.red(), title="Error", description=f"Sorry, I could not process your question.\n\nDetails: {e}")
        await message.reply(embed=error_embed)

    if message.author.id in user_states:
        del user_states[message.author.id]
        del user_states_time[message.author.id]
        if message.author.id in message_ids:
            del message_ids[message.author.id]

async def run_bot():
    await client.start(TOKEN)
