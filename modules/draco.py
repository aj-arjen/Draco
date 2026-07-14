import discord
from discord.ext import commands


COMMAND_CENTER_URL = (
    "https://discord.com/channels/"
    "1525494223040942192/"
    "1526711476285472900"
)


class Draco(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="draco",
        description="Open the Draco Command Center."
    )
    async def draco(
        self,
        interaction: discord.Interaction
    ):

        embed = discord.Embed(
            title="🐉 Draco Command Center",
            description=(
                "🔥 **Hey! I'm Draco, your fiery assistant.**\n\n"
                "Curious what I can do?\n"
                "Click the button below to explore all my "
                "commands and features."
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

        view = discord.ui.View()

        view.add_item(
            discord.ui.Button(
                label="Open Command Center",
                emoji="❓",
                style=discord.ButtonStyle.link,
                url=COMMAND_CENTER_URL
            )
        )

        await interaction.response.send_message(
            embed=embed,
            file=file,
            view=view,
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(Draco(bot))