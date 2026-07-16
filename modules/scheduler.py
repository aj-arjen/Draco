import asyncio
import json
import os
from datetime import datetime, timezone

import discord
from discord.ext import commands

print(">>> scheduler.py imported <<<")

EVENTS_FILE = "data/events/events.json"


def load_events():
    if not os.path.exists(EVENTS_FILE):
        return []
    with open(EVENTS_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_events(events):
    os.makedirs(os.path.dirname(EVENTS_FILE), exist_ok=True)
    with open(EVENTS_FILE, "w", encoding="utf-8") as f:
        json.dump(events, f, indent=4)


class Scheduler(commands.Cog):

    def __init__(self, bot):
        print(">>> Scheduler __init__ <<<")
        self.bot = bot
        task = self.bot.loop.create_task(self.scheduler_loop())
        print(">>> Scheduler task created <<<", task)

    async def send_reminder(self, event, reminder_type):
        channel = self.bot.get_channel(event["channel_id"])
        if channel is None:
            print(f"Channel {event['channel_id']} not found")
            return

        titles = {
            "today": "🌅 Today's Battle Awaits!",
            "hour": "⏰ Battle Begins in 1 Hour!",
            "final": "🔥 Battle Begins in 10 Minutes!",
        }

        embed = discord.Embed(
            title=titles[reminder_type],
            color=discord.Color.orange()
        )
        embed.add_field(name="⚔️ Event", value=event["event"], inline=False)
        embed.add_field(name="🕒 Starts", value=f"<t:{event['timestamp']}:F>", inline=False)

        await channel.send(embed=embed)
        print(f"Sent {reminder_type} reminder for {event['event']}")

    async def scheduler_loop(self):
        print(">>> scheduler_loop entered <<<")
        await self.bot.wait_until_ready()
        print("Scheduler started")

        while not self.bot.is_closed():
            events = load_events()
            now = int(datetime.now(timezone.utc).timestamp())

            changed = False

            for event in events:
                remaining = event["timestamp"] - now
                print(f"{event['event']} remaining={remaining}")

                if remaining <= 600 and not event.get("final_sent", False):
                    await self.send_reminder(event, "final")
                    event["final_sent"] = True
                    changed = True

                elif remaining <= 3600 and not event.get("hour_sent", False):
                    await self.send_reminder(event, "hour")
                    event["hour_sent"] = True
                    changed = True

                elif remaining <= 86400 and not event.get("today_sent", False):
                    await self.send_reminder(event, "today")
                    event["today_sent"] = True
                    changed = True

            if changed:
                save_events(events)

            await asyncio.sleep(60)


async def setup(bot):
    await bot.add_cog(Scheduler(bot))
