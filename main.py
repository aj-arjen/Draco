import discord
from discord.ext import commands

from flask import Flask
from threading import Thread
import os

from bot import Draco
from settings import TOKEN
from views import ApplyView
from giftcodes import GiftCodeView
from giftcode_watcher import GiftCodeWatcher

bot = Draco()
giftcode_watcher = GiftCodeWatcher(bot)


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

    ...

    embed = discord.Embed(
        title="🎁 New Top Heroes Gift Code",
        color=0xC49A3A
    )

    embed.description = (
        "A new gift code is available!\n\n"
        f"```{code}```"
    )

    embed.add_field(
        name="Status",
        value="🟢 Active",
        inline=True
    )

    embed.set_footer(
        text="Powered by Draco 🐉"
    )

    await interaction.channel.send(
        embed=embed,
        view=GiftCodeView(code)
    )

    await interaction.response.send_message(
        "✅ Gift code posted.",
        ephemeral=True
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

giftcode_watcher.start()

bot.run(TOKEN)