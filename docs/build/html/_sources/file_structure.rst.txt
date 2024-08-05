Project File Structure
=======================

Below is a breakdown of the primary files in the Feixiao Discord bot project.

- **``config.py``**: Configuration file for storing environment variables such as the Wolfram Alpha API key and Discord bot token.
- **``discord_client.py``**: Contains the bot's main logic, handling messages, queries, and interactions.
- **``http_server.py``**: Sets up a Flask server for monitoring the bot's status.
- **``main.py``**: Entry point of the bot, initializing both the HTTP server and the Discord client.
- **``wolfram_client.py``**: Interacts with the Wolfram Alpha API to fetch query results.
- **``requirements.txt``**: Lists the dependencies required for the project.
- **``license``**: MIT License governing the use of this software.
- **``policy.md``**: Outlines the privacy policy for Feixiao users.
- **``terms.md``**: Details the terms of service for using Feixiao.
