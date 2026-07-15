import json
import os

import discord
from discord.ext import commands
from discord import app_commands

TIMEZONE_FILE = "data/timezones/timezones.json"

TIMEZONES = [
    "Europe/Amsterdam",
    "Europe/London",
    "Europe/Istanbul",
    "America/New_York",
    "America/Chicago",
    "America/Denver",
    "America/Los_Angeles",
    "America/Sao_Paulo",
    "Asia/Dubai",
    "Asia/Kolkata",
    "Asia/Bangkok",
    "Asia/Ho_Chi_Minh",
    "Asia/Shanghai",
    "Asia/Seoul",
    "Asia/Tokyo",
    "Australia/Sydney",
]



def load_timezones():

    if not os.path.exists(TIMEZONE_FILE):
        return {}

    with open(TIMEZONE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_timezones(data):

    with open(TIMEZONE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


async def timezone_autocomplete(
    interaction: discord.Interaction,
    current: str,
):

    return [
        app_commands.Choice(
            name=tz,
            value=tz,
        )
        for tz in TIMEZONES
        if current.lower() in tz.lower()
    ][:25]


class Timezone(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="timezone",
        description="Set your local timezone."
    )
    @app_commands.autocomplete(
        timezone=timezone_autocomplete
    )
    async def timezone(
        self,
        interaction: discord.Interaction,
        timezone: str,
    ):

        if timezone not in TIMEZONES:

            await interaction.response.send_message(
                "❌ Invalid timezone.",
                ephemeral=True
            )
            return

        data = load_timezones()

        data[str(interaction.user.id)] = timezone

        save_timezones(data)

        await interaction.response.send_message(
            f"✅ Your timezone has been set to **{timezone}**.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Timezone(bot))