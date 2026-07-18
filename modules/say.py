import discord
from discord import app_commands
from discord.ext import commands

from config.config import DRACO_OWNER
from config.draco_assets import DRACO_IMAGES



class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
        name="say",
        description="Make Draco speak."
    )
    @app_commands.choices(
    emotion=[
        app_commands.Choice(name="Yes", value="yes"),
        app_commands.Choice(name="No", value="no"),
        app_commands.Choice(name="Shy", value="shy"),
        app_commands.Choice(name="Celebrate", value="celebrate"),
        app_commands.Choice(name="Thinks", value="thinks"),
        app_commands.Choice(name="Serious", value="serious"),
        app_commands.Choice(name="Confused", value="confused"),
        app_commands.Choice(name="Heart", value="heart"),
        app_commands.Choice(name="Cry", value="cry"),
        app_commands.Choice(name="Hype", value="hype"),
    ]
)
    @app_commands.describe(
        message="Message Draco should send.",
        emotion="Choose Draco's emotion."
    )
    async def say(
        self,
        interaction: discord.Interaction,
        message: str,
        emotion: app_commands.Choice[str]
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
        file = discord.File(
            DRACO_IMAGES[emotion.value],
            filename="draco.png"        
        )

        await interaction.channel.send(
            message,
            file=file
        )


async def setup(bot):
    await bot.add_cog(Say(bot))