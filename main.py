import discord
from discord.ext import commands

from flask import Flask
from threading import Thread
import os

from bot import Draco
from settings import TOKEN
from views import ApplyView
from giftcodes import post_giftcode
from giftcode_watcher import GiftCodeWatcher
from redalert import RedAlertView

bot = Draco()

giftcode_watcher = GiftCodeWatcher(bot)


@bot.event
async def on_ready():

    if not giftcode_watcher.check_giftcodes.is_running():
        giftcode_watcher.start()

    print(f"Logged in as {bot.user}")


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )


@bot.tree.command(
    name="gifttest",
    description="Post a test gift code."
)
async def gifttest(interaction: discord.Interaction):

    code = "DRACO2026"

    await post_giftcode(
        interaction.channel,
        code
    )

    await interaction.response.send_message(
        "✅ Gift code posted.",
        ephemeral=True
    )


@bot.tree.command(
    name="alert",
    description="Create a Draco Red Alert."
)
async def alert(interaction: discord.Interaction):

    await interaction.response.send_message(
        "🚨 Select the alert type:",
        view=RedAlertView(),
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