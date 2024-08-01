import discord
import wolframalpha
from config import APP_ID, PRIORITY_LIST

# Create a Wolfram Alpha client
wolfram_client = wolframalpha.Client(APP_ID)

def create_embed_response(res):
    """Create an embed response from Wolfram Alpha query result."""
    embed = discord.Embed(title="Feixiao | WolframAlpha results", color=discord.Color.gold())
    
    combined_results = {}
    
    # Collect results by pod title
    for pod in res.pods:
        if pod.title in combined_results:
            combined_results[pod.title].append(pod)
        else:
            combined_results[pod.title] = [pod]

    # Add thumbnail if available
    for pod in res.pods:
        if pod.title in ['Input interpretation', 'Input']:
            for subpod in pod.subpods:
                if subpod.img is not None:
                    embed.set_thumbnail(url=subpod.img.src)
                    break

    # Add plot/image if available
    plot_found = False
    for pod_title, pod_list in combined_results.items():
        for pod in pod_list:
            if 'plot' in pod.title.lower() or 'image' in pod.title.lower():
                for subpod in pod.subpods:
                    if subpod.img is not None:
                        embed.set_image(url=subpod.img.src)
                        plot_found = True
                        break
                if plot_found:
                    break
        if plot_found:
            break

    # Add plaintext results
    for pod_title, pod_list in combined_results.items():
        if 'plot' not in pod_title.lower() and 'image' not in pod_title.lower():
            field_value = ''
            for pod in pod_list:
                for subpod in pod.subpods:
                    if subpod.plaintext is not None:
                        field_value += subpod.plaintext + "\n"
            if field_value.strip():  # Ensure it's not empty
                embed.add_field(name=pod_title, value=field_value.strip(), inline=False)

    # Add prioritized plot/plaintext results
    if plot_found:
        for pod_title, pod_list in combined_results.items():
            if any(priority in pod_title.lower() for priority in PRIORITY_LIST):
                plot_plaintext = ''
                for pod in pod_list:
                    for subpod in pod.subpods:
                        if subpod.plaintext is not None:
                            plot_plaintext += subpod.plaintext + "\n"
                embed.add_field(name=pod_title, value=plot_plaintext.strip(), inline=False)
                break

    # Handle results that may have images but no specific pod title
    for pod_title, pod_list in combined_results.items():
        for pod in pod_list:
            if 'image' in pod_title.lower() and not plot_found:
                for subpod in pod.subpods:
                    if subpod.img is not None:
                        embed.add_field(name="Image", value=subpod.img.src, inline=False)
                        break

    return embed
