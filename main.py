import discord
from flask import Flask
from threading import Thread
import os

from bot import Draco
from settings import TOKEN

print("========== MAIN.PY STARTED ==========")

app = Flask(__name__)

@app.route("/")
def home():
    return "DracoBot is running!", 200

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web, daemon=True).start()

bot = Draco()

@bot.event
async def on_ready():
    print("=" * 40)
    print(f"Logged in as: {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")
    print("=" * 40)

    modules = [
        "setup",
        "modules.draco",
        "modules.command_center",
        "modules.timezone",
        "modules.victory",
    ]

    for module in modules:
        try:
            print(f"Loading {module}...")
            await bot.load_extension(module)
            print(f"Loaded {module}")
        except Exception as e:
            print(f"FAILED: {module}")
            print(repr(e))

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Slash sync failed: {e}")

print("Starting Draco...")
bot.run(TOKEN)
