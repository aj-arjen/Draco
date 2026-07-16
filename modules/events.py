import json
import os
from datetime import datetime
from zoneinfo import ZoneInfo
import traceback

import discord
from discord.ext import commands
from discord import app_commands

from config.config import (
    LEADER_ROLES,
    EVENT_REMINDER_CHANNELS,
)

EVENTS_FILE = "data/events/events.json"
TIMEZONE_FILE = "data/timezones/timezones.json"


# ==========================================================
# JSON HELPERS
# ==========================================================

def load_events():

    if not os.path.exists(EVENTS_FILE):
        return []

    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_events(events):

    os.makedirs(os.path.dirname(EVENTS_FILE), exist_ok=True)

    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4)


def load_timezones():

    if not os.path.exists(TIMEZONE_FILE):
        return {}

    with open(TIMEZONE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


# ==========================================================
# GUILD HELPERS
# ==========================================================

def get_user_guild(member):

    for guild_name, role_id in LEADER_ROLES.items():

        if guild_name == "Other":
            continue

        if discord.utils.get(member.roles, id=role_id):
            return guild_name

    return None


def get_event_channel(bot, guild_name):

    channel_id = EVENT_REMINDER_CHANNELS.get(guild_name)

    if channel_id is None:
        return None

    return bot.get_channel(channel_id)


# ==========================================================
# TIMEZONE HELPERS
# ==========================================================

def get_user_timezone(user_id):

    data = load_timezones()

    return data.get(str(user_id))
# ==========================================================
# TIME HELPERS
# ==========================================================

def create_timestamp(date_string, time_string, timezone_name):

    dt = datetime.strptime(
        f"{date_string} {time_string}",
        "%d %B %Y %H:%M"
    )

    dt = dt.replace(
        tzinfo=ZoneInfo(timezone_name)
    )

    return int(dt.timestamp())


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="eventadd",
        description="Schedule a new guild event."
    )
    @app_commands.describe(
        event="Event name",
        date="Example: 20 July 2026",
        time="Example: 20:00"
    )
    async def eventadd(
        self,
        interaction: discord.Interaction,
        event: str,
        date: str,
        time: str,
    ):

        try:

            guild_name = get_user_guild(interaction.user)

            if guild_name is None:

                await interaction.response.send_message(
                    "❌ Only Guild Leaders can create events.",
                    ephemeral=True
                )
                return

            timezone_name = get_user_timezone(
                interaction.user.id
            )

            if timezone_name is None:

                await interaction.response.send_message(
                    "🌍 Please set your timezone first using **/timezone**.",
                    ephemeral=True
                )
                return

            timestamp = create_timestamp(
                date,
                time,
                timezone_name,
            )

            channel = get_event_channel(
                self.bot,
                guild_name,
            )

            if channel is None:

                await interaction.response.send_message(
                    "❌ Event reminder channel not found.",
                    ephemeral=True
                )
                return

            events = load_events()

            event_id = len(events) + 1
           
            events.append(
                {
                    "id": event_id,
                    "guild": guild_name,
                    "event": event,
                    "timestamp": timestamp,
                    "channel_id": channel.id,
                    "today_sent": False,
                    "hour_sent": False,
                    "final_sent": False,
                    "created_by": interaction.user.id,
                }
            )

            save_events(events)

            embed = discord.Embed(
                title="✅ Event Scheduled",
                color=discord.Color.green(),
            )

            embed.add_field(
                name="⚔️ Event",
                value=event,
                inline=False,
            )

            embed.add_field(
                name="🏰 Guild",
                value=guild_name,
                inline=True,
            )

            embed.add_field(
                name="🕒 Starts",
                value=f"<t:{timestamp}:F>",
                inline=True,
            )

            embed.set_footer(
                text=(
                    "Draco will automatically send the "
                    "Today, 1 Hour and 10 Minutes reminders."
                )
            )

            await interaction.response.send_message(
                embed=embed,
                ephemeral=True,
            )

        except Exception:

            traceback.print_exc()

            if not interaction.response.is_done():

                await interaction.response.send_message(
                    "❌ An unexpected error occurred.",
                    ephemeral=True,
                )


async def setup(bot):
    await bot.add_cog(Events(bot))
