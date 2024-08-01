import asyncio
from threading import Thread
from http_server import start_http_server
from discord_client import run_bot

async def main():
    # Start the HTTP server in a separate thread
    http_thread = Thread(target=start_http_server)
    http_thread.start()

    # Start the bot
    await run_bot()

if __name__ == '__main__':
    asyncio.run(main())
