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

   This Discord bot is designed to notify a specific channel when a Rumble livestream goes live. Here’s a breakdown of its functionality:

### Description

The Rumble Stream Notification Bot is a simple, automated bot that monitors a user’s Rumble streaming status and sends a notification to a designated Discord channel when the stream goes live. Using `discord.py`, the bot checks Rumble's API at regular intervals (every 5 minutes) to see if there is an active livestream. If a stream is detected, it sends a message in the configured channel with a link to the stream. 

### Key Features

- **Automated Stream Detection**: The bot periodically checks the Rumble API for live streaming status. This check is set to run every 5 minutes, allowing for near real-time updates without overwhelming the API.
  
- **Discord Channel Notifications**: Once a live stream is detected, the bot posts an alert in a specific Discord channel, tagging it with a "live" icon (🔴) and providing a link to the stream. This link is configurable in `config.json` for easy updates.

- **Flexible Configuration**: Key bot configurations, including the Discord bot token, channel ID, Rumble API URL, and stream URL, are stored in `config.json` for easy access and adjustment.

### How It Works

1. **API Call to Rumble**: The bot uses `subprocess` to call `curl` and fetch JSON data from the Rumble API. It checks if any stream in the response is flagged as "live."
  
2. **Notification Logic**: When a live stream is detected, the bot sets a flag (`STREAM_DETECTED`) to avoid duplicate notifications. It sends a Discord message only the first time a live stream is detected or when a previous stream has ended and a new one begins.

3. **Error Handling**: The bot includes basic error handling to log issues such as JSON parsing errors or network problems, ensuring it continues to run smoothly.

### Use Cases

- **Content Creators**: Ideal for streamers on Rumble who want to keep their Discord community engaged by notifying them when they go live.
  
- **Community Engagement**: Great for community managers who want to automate live stream notifications for their audience without manually sending alerts.

This bot is straightforward, reliable, and tailored for real-time engagement with Discord users, making it an excellent tool for content creators and community managers.
