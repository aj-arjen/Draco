import discord
from discord.ext import commands

from views.command_center_view import CommandCenterView


class CommandCenter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="commandcenter",
        description="Post the Draco Command Center."
    )
    @discord.app_commands.default_permissions(
        administrator=True
    )
    async def commandcenter(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🐉 Draco Command Center",
            description=(
                "🔥 **Welcome, Warrior!**\n\n"
                "Select a category below to explore "
                "everything I can do."
            ),
            color=0xC49A3A
        )

        embed.set_footer(
            text="Draco • Your Fiery Assistant 🐉"
        )

        file = discord.File(
            "assets/reactions/draco_help.png",
            filename="draco_help.png"
        )

        embed.set_image(
            url="attachment://draco_help.png"
        )

        await interaction.response.send_message(
            embed=embed,
            file=file,
            view=CommandCenterView()
        )


async def setup(bot):
    await bot.add_cog(CommandCenter(bot))