import discord
from discord import app_commands
from discord.ext import commands

from config.config import DRACO_OWNER, GIFTCODE_CHANNEL
from modules.giftcodes import post_giftcode


class GiftCode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="giftcode",
        description="Post a Top Heroes gift code."
    )
    @app_commands.describe(
        code="The gift code to post."
    )
    async def giftcode(
        self,
        interaction: discord.Interaction,
        code: str
    ):
        if interaction.user.id != DRACO_OWNER:
            await interaction.response.send_message(
                "🐉 Draco only answers to his Keeper.",
                ephemeral=True
            )
            return

        await interaction.response.send_message(
            "✅ Gift code posted.",
            ephemeral=True
        )

        channel = self.bot.get_channel(GIFTCODE_CHANNEL)

        if channel is None:
            await interaction.followup.send(
            "❌ Giftcode channel not found.",
            ephemeral=True
        )
        return

    await post_giftcode(
        channel,
        code
    )


async def setup(bot):
    await bot.add_cog(GiftCode(bot))