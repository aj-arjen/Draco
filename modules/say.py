import discord
from discord import app_commands
from discord.ext import commands

from config.config import DRACO_OWNER



class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="say",
        description="Make Draco speak."
    )
    @app_commands.describe(
        message="Message Draco should send."
    )
    async def say(
        self,
        interaction: discord.Interaction,
        message: str
    ):

        if interaction.user.id != DRACO_OWNER:
            await interaction.response.send_message(
                "🐉 Draco only answers to his Keeper.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "✅ Message sent.",
            ephemeral=True
        )

        await interaction.channel.send(message)


async def setup(bot):
    await bot.add_cog(Say(bot))