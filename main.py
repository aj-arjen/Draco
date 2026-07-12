import discord
from discord.ext import commands

from flask import Flask
from threading import Thread
import os

from bot import Draco
from settings import TOKEN
from views import ApplyView

bot = Draco()


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )

app = Flask(__name__)

@app.route("/")
def home():
    return "DracoBot is running!"

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

Thread(target=run_web).start()
bot.run(TOKEN)