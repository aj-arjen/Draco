import os
from flask import Flask
from threading import Thread

from dotenv import load_dotenv

from bot import Draco

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN ontbreekt.")

bot = DracoBot()


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction):
    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )

app = Flask(__name__)

@app.route("/")
def home():
    return "Draco is online!"

def run_web():
    app.run(host="0.0.0.0", port=10000)

Thread(target=run_web).start()
import asyncio

async def load_extensions():
    await bot.load_extension("cogs.setup")

asyncio.run(load_extensions())

bot.run(TOKEN)
