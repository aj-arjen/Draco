import discord
from discord.ext import commands


class CommandCenter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="commandcenter",
        description="Post the Draco Command Center."
    )
    async def commandcenter(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🐉 Draco Command Center",
            description=(
                "Welcome!\n\n"
                "Choose a category below to discover "
                "Draco's commands."
            ),
            color=0xC49A3A
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
            file=file
        )


async def setup(bot):
    await bot.add_cog(CommandCenter(bot))