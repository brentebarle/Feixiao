Feixiao - Documentation
=======================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   features
   installation
   usage
   contributing

Introduction
============

Feixiao is a powerful Discord bot integrating brotAI and WolframAlpha, designed to deliver computational intelligence right within your Discord server. Effortlessly obtain precise answers and stunning visualizations with Feixiao.

Features
========

- **Natural Language Processing**: Ask questions in plain language and get accurate answers from WolframAlpha.
- **Rich Embeds**: Responses come in well-formatted embeds with images, plots, and plaintext results.
- **Status Monitoring**: Includes a Flask-based HTTP server for monitoring the bot's status and ensuring smooth operation.

File Structure
--------------

- **config.py**: Manages environment variables and configuration settings.
- **wolfram_client.py**: Handles interactions with the WolframAlpha API and formats responses.
- **discord_client.py**: Manages Discord bot events and interactions.
- **http_server.py**: Sets up a Flask server for status monitoring.
- **main.py**: Entry point to start both the HTTP server and the Discord bot.

Installation
============

1. **Clone the Repository**:

   .. code-block:: bash

      git clone https://gitlab.com/brentebarle/feixiao.git
      cd feixiao

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed, then install the required packages:

   .. code-block:: bash

      pip install -r requirements.txt

3. **Set Up Environment Variables**:
   Create a ``.env`` file in the root directory with the following content:

   .. code-block:: text

      WOLFRAM_ALPHA_APP_ID=your_wolfram_alpha_app_id
      DISCORD_TOKEN=your_discord_bot_token

4. **Run the Bot**:
   Start the bot by executing the ``main.py`` script:

   .. code-block:: bash

      python main.py

Usage
=====

To interact with the bot, mention it with "hey feixiao" followed by your query. For example:

   .. code-block:: text

      hey feixiao, what is the integral of x^2?

Contributing
============

Contributions are welcome! Fork the repository, make improvements, and submit pull requests. For issues or feature requests, open an issue on GitLab.

License
=======

This project is licensed under the MIT License. See the LICENSE file for details.
