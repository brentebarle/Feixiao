Feixiao - Documentation
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   features
   installation
   usage
   contributing
   api_reference

Introduction
============

Feixiao is a Discord bot that harnesses the power of brotAI and WolframAlpha to provide computational intelligence directly within your Discord server. With Feixiao, you can effortlessly get precise answers and stunning visualizations from your queries.

Features
========

- **Natural Language Processing**: Ask questions in plain language and receive accurate answers from WolframAlpha.
- **Rich Embeds**: Responses are displayed as well-formatted embeds, featuring images, plots, and plaintext results.
- **Status Monitoring**: Includes a Flask-based HTTP server to monitor the bot's status and ensure it’s always running smoothly.

File Structure
--------------

- **config.py**: Manages environment variables and configuration settings.
- **wolfram_client.py**: Contains the logic for interacting with the WolframAlpha API and formatting responses.
- **discord_client.py**: Handles the Discord bot’s events and interactions.
- **http_server.py**: Sets up a Flask server for status monitoring.
- **main.py**: The entry point to start both the HTTP server and the Discord bot.

Installation
============

1. **Clone the Repository**:
   .. code-block:: bash

      git clone https://gitlab.com/brentebarle/feixiao.git
      cd feixiao

2. **Install Dependencies**:
   Make sure you have Python 3.8+ installed. Then, install the required packages:
   .. code-block:: bash

      pip install -r requirements.txt

3. **Set Up Environment Variables**:
   Create a .env file in the root directory with the following content:
   .. code-block:: text

      WOLFRAM_ALPHA_APP_ID=your_wolfram_alpha_app_id
      DISCORD_TOKEN=your_discord_bot_token

4. **Run the Bot**:
   Start the bot by executing the main.py script:
   .. code-block:: bash

      python main.py

Usage
=====

Interaction: Mention the bot with "hey feixiao" followed by your query. For example:
.. code-block:: text

   hey feixiao, what is the integral of x^2?

Contributing
============

Contributions are welcome! Feel free to fork the repository, make improvements, and submit pull requests. For any issues or feature requests, open an issue on GitLab.

API Reference
=============

.. automodule:: config
   :members:

.. automodule:: wolfram_client
   :members:

.. automodule:: discord_client
   :members:

License
=======

This project is licensed under the MIT License. See the LICENSE file for details.
