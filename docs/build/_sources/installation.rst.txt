Installation
============

Follow these steps to set up the Feixiao Discord bot:

1. **Clone the Repository**:

   .. code-block:: bash
   
      git clone https://gitlab.com/brentebarle/feixiao.git
      cd feixiao

2. **Set Up Environment Variables**: Create a ``.env`` file in the root directory and include your Wolfram Alpha API key and Discord bot token:
    
   .. code-block:: makefile
   
      WOLFRAM_ALPHA_APP_ID=your_app_id
      DISCORD_TOKEN=your_discord_token

3. **Install Dependencies**:
    
   .. code-block:: bash
   
      pip install -r requirements.txt

4. **Run the Bot**:
    
   .. code-block:: bash
   
      python main.py
