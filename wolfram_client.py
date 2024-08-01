import wolframalpha
from config import APP_ID

# Create a Wolfram Alpha client
wolfram_client = wolframalpha.Client(APP_ID)

def get_image_urls_and_titles(res):
    """Extract and return the first three image URLs and their titles from Wolfram Alpha query result."""
    image_data = []
    for pod in res.pods:
        for subpod in pod.subpods:
            if subpod.img is not None:
                image_data.append((pod.title, subpod.img.src))
            if len(image_data) == 10:
                break
        if len(image_data) == 10:
            break
    return image_data
