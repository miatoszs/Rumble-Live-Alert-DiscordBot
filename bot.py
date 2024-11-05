import subprocess
import json
import discord
import asyncio

# Load configurations from config.json
with open("config.json") as config_file:
    config = json.load(config_file)

DISCORD_TOKEN = config["discord_token"]
CHANNEL_ID = config["channel_id"]
RUMBLE_API_URL = config["rumble_api_url"]
STREAM_URL = config["stream_url"]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
STREAM_DETECTED = False

def is_streaming():
    try:
        result = subprocess.run(
            ["curl", "-s", RUMBLE_API_URL],
            capture_output=True,
            text=True
        )
        data = json.loads(result.stdout)
        
        livestreams = data.get("livestreams", [])
        for stream in livestreams:
            if stream.get("is_live"):
                print("You are currently streaming!")
                return True

        print("You are not streaming.")
        return False
    except json.JSONDecodeError:
        print("Failed to parse JSON response.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False

@client.event
async def on_ready():
    print(f'{client.user} is connected to Discord!')
    client.loop.create_task(check_rumble_stream())

async def check_rumble_stream():
    global STREAM_DETECTED
    while True:
        try:
            is_live = is_streaming()

            if is_live and not STREAM_DETECTED:
                STREAM_DETECTED = True
                channel = client.get_channel(CHANNEL_ID)
                await channel.send(f"🔴 Your Rumble stream is now live! Watch here: {STREAM_URL}")
                print("Stream is now live!")

            elif not is_live and STREAM_DETECTED:
                STREAM_DETECTED = False
                print("Stream is not live.")

            # Log the current status
            if is_live:
                print("Status: Online")
            else:
                print("Status: Not Streaming")

        except Exception as e:
            print(f"An error occurred during the check: {e}")

        await asyncio.sleep(300)  # Wait 5 minutes before checking again

# Run the bot using asyncio.run()
async def main():
    await client.start(DISCORD_TOKEN)

asyncio.run(main())

