import asyncio
import json
import os
from datetime import datetime, timezone

import discord
from discord.ext import commands

EVENTS_FILE = "data/events/events.json"


def load_events():

    if not os.path.exists(EVENTS_FILE):
        return []

    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_events(events):

    os.makedirs(os.path.dirname(EVENTS_FILE), exist_ok=True)

    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4)

class Scheduler(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
        self.bot.loop.create_task(self.scheduler_loop())


async def send_reminder(
    self,
    event,
    reminder_type,
):

    channel = self.bot.get_channel(
        event["channel_id"]
    )

    if channel is None:
        return

    images = {
        "today": "assets/alerts/draco_event_today.png",
        "hour": "assets/alerts/draco_event_hour.png",
        "final": "assets/alerts/draco_event_final.png",
    }

    titles = {
        "today": "🌅 Today's Battle Awaits!",
        "hour": "⏰ Battle Begins in 1 Hour!",
        "final": "🔥 Battle Begins in 10 Minutes!",
    }

    descriptions = {
        "today": (
            "The battlefield awaits your arrival.\n\n"
            "Review today's strategy and be ready when the time comes."
        ),
        "hour": (
            "Suit up. The clock is ticking.\n\n"
            "Every victory starts with good preparation."
        ),
        "final": (
            "Final preparations. Sharpen your blades.\n\n"
            "Time to show your strength. Good luck, Warriors!"
        ),
    }

    guild_icons = {
        "DEN": "🟠",
        "ACE": "🔵",
        "NVN": "🟢",
        "OBS": "🔴",
        "OFA": "🟣",
    }

    colors = {
        "DEN": 0xF39C12,
        "ACE": 0x3498DB,
        "NVN": 0x2ECC71,
        "OBS": 0xE74C3C,
        "OFA": 0x9B59B6,
    }

    embed = discord.Embed(
        title=titles[reminder_type],
        description=descriptions[reminder_type],
        color=colors.get(event["guild"], 0xF39C12),
    )

    embed.add_field(
        name="⚔️ Event",
        value=event["event"],
        inline=False,
    )

    embed.add_field(
        name="🕒 Starts",
        value=f"<t:{event['timestamp']}:F>",
        inline=False,
    )

    embed.set_author(
        name=f"{guild_icons[event['guild']]} {event['guild']} Event Reminder"
    )

    file = discord.File(
        images[reminder_type],
        filename="event.png",
    )

    embed.set_image(
        url="attachment://event.png"
    )

    await channel.send(
        file=file,
        embed=embed,
    )

    async def scheduler_loop(self):

        await self.bot.wait_until_ready()

        while not self.bot.is_closed():

            events = load_events()

            now = int(datetime.now(timezone.utc).timestamp())

            for event in events:

                remaining = event["timestamp"] - now

                #
                # Today reminder
                #

                if (
                    remaining <= 86400
                    and not event["today_sent"]
                ):

                    await self.send_reminder(
                        event,
                        "today",
                    )

                    event["today_sent"] = True

                #
                # 1 Hour reminder
                #

                if (
                    remaining <= 3600
                    and not event["hour_sent"]
                ):

                    await self.send_reminder(
                        event,
                        "hour",
                    )

                    event["hour_sent"] = True

                #
                # 10 Minutes reminder
                #

                if (
                    remaining <= 600
                    and not event["final_sent"]
                ):

                    await self.send_reminder(
                        event,
                        "final",
                    )

                    event["final_sent"] = True

            save_events(events)

            await asyncio.sleep(60)


async def setup(bot):

    await bot.add_cog(Scheduler(bot))