import discord
import asyncio
from wolfram_client import wolfram_client, create_embed_response
from config import TOKEN

# Create a Discord client with intents
intents = discord.Intents.default()
intents.typing = True
intents.message_content = True
intents.presences = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    
    # Define the rotation characters
    spinner = ['with brotAI | Computational', 'with brotAI | Powered by WolframAlpha']
    
    while True:
        for char in spinner:
            # Update the activity with the rotating character
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{char}"))
            # Wait for a short period before updating again
            await asyncio.sleep(10)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'hey feixiao' in message.content.lower():
        query = message.content.lower().replace('hey feixiao', '').strip()
        try:
            async with message.channel.typing():
                res = await client.loop.run_in_executor(None, lambda: wolfram_client.query(query))
                
                if 'devrawtext' in message.content.lower():
                    raw_response = res['pod']
                    formatted_raw_response = '\n'.join(f"{pod.title}: {pod.text}" for pod in raw_response)
                    await message.reply(f"```\n{formatted_raw_response}\n```")
                else:
                    embed = create_embed_response(res)
                    await message.reply(embed=embed)
        except Exception as e:
            print(f'Error: {e}')
            await message.reply('Sorry, I could not process your question.')

async def run_bot():
    await client.start(TOKEN)
