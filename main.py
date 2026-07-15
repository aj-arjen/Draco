import discord
from discord.ext import commands

from flask import Flask
from threading import Thread
import os

from bot import Draco
from settings import TOKEN
from views.views import ApplyView
from modules.giftcodes import post_giftcode
from modules.giftcode_watcher import GiftCodeWatcher
from modules.redalert import RedAlertView

print("========== MAIN.PY STARTED ==========")

bot = Draco()

giftcode_watcher = GiftCodeWatcher(bot)

GIFTCODE_CHANNEL_ID = 1526281607411925173
VERIFIED_ROLE_ID = 1525534814722064545


@bot.event
async def on_ready():

    print("========== BOT READY ==========")
    print(f"Logged in as: {bot.user}")
    print(f"Guilds: {len(bot.guilds)}")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"Slash sync failed: {e}")

    if not giftcode_watcher.check_giftcodes.is_running():
        giftcode_watcher.start()
        print("GiftCodeWatcher started.")

    print("===============================")


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction: discord.Interaction):

    print("PING COMMAND CALLED")

    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )


from discord import app_commands

@bot.tree.command(
    name="giftcode",
    description="Post a new Top Heroes gift code."
)
@app_commands.describe(
    code="Enter the gift code"
)
async def giftcode(
    interaction: discord.Interaction,
    code: str
):

    print("GIFTCODE COMMAND CALLED")

    verified_role = interaction.guild.get_role(VERIFIED_ROLE_ID)

    if verified_role not in interaction.user.roles:
        await interaction.response.send_message(
            "❌ You don't have permission to use this command.",
            ephemeral=True
        )
        return

    channel = bot.get_channel(GIFTCODE_CHANNEL_ID)

    if channel is None:
        await interaction.response.send_message(
            "❌ Gift code channel not found.",
            ephemeral=True
        )
        return

    await post_giftcode(
        channel,
        code
    )

    await interaction.response.send_message(
        "✅ Gift code posted successfully!",
        ephemeral=True
    )


app = Flask(__name__)


@app.route("/")
def home():
    return "DracoBot is running!", 200


def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(
        host="0.0.0.0",
        port=port
    )


Thread(target=run_web, daemon=True).start()

print("Starting Draco...")

bot.run(TOKEN)