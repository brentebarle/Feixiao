import os
from dotenv import load_dotenv

load_dotenv()

APP_ID = os.getenv('WOLFRAM_ALPHA_APP_ID')
TOKEN = os.getenv('DISCORD_TOKEN')
PRIORITY_LIST = ["3d plots", "3d plot", "2d plots", "2d plot", "image"]
