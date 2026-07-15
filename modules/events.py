import discord
from discord.ext import commands
from discord import app_commands

from config.config import (
    LEADER_ROLES,
    EVENT_REMINDER_CHANNELS,
)


class Events(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="eventadd",
        description="Create a guild event."
    )
    @app_commands.describe(
        event="Event name"
    )
    async def eventadd(
        self,
        interaction: discord.Interaction,
        event: str
    ):

        guild_name = None

        for name, role_id in LEADER_ROLES.items():
            if discord.utils.get(interaction.user.roles, id=role_id):
                guild_name = name
                break

        if guild_name is None:
            await interaction.response.send_message(
                "❌ Only Guild Leaders can create events.",
                ephemeral=True
            )
            return

        channel_id = EVENT_REMINDER_CHANNELS[guild_name]
        channel = self.bot.get_channel(channel_id)

        await channel.send(
            f"📅 **{guild_name} Event**\n\n"
            f"⚔️ **{event}**"
        )

        await interaction.response.send_message(
            f"✅ Event posted in {channel.mention}.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Events(bot))