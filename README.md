To install the required packages, you'll need to have `discord.py` and any other dependencies for your bot. Here’s a command to set up a virtual environment, install `discord.py`, and any additional Python packages you may need.

1. **Clone the repo**:
   ```bash
   git clone https://github.com/miatoszs/Rumble-Live-Alert-DiscordBot.git
   ```

2. **Navigate to your project directory**:
   ```bash
   cd Rumble-Live-Alert-DiscordBot
   ```

3. **Create a virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   ```

4. **Activate the virtual environment**:
   ```bash
   source venv/bin/activate
   ```

5. **Install requirements**:
   Create a `requirements.txt` file if you haven't already, and add necessary packages like `discord.py`. Then use:

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if you just need `discord.py` and `requests` for HTTP calls, you can install them directly:

   ```bash
   pip install discord.py requests
   ```

6. **Edit the config**:
   You need to edit the `config.json`

7. **Start the bot**:
   ```bash
   python3 bot.py
   ```
