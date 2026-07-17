import discord
from discord.ext import commands

RED_ALERT_CHANNEL_ID = 1526579916408225802

ALERT_IMAGES = {
    "DEN": "assets/alerts/den_alert.png",
    "ACE": "assets/alerts/ace_alert.png",
    "OFA": "assets/alerts/ofa_alert.png",
    "NVN": "assets/alerts/nvn_alert.png",
    "OBS": "assets/alerts/obs_alert.png",
    "CITADEL": "assets/alerts/citadel_alert.png",
}

EMBED_COLORS = {
    "DEN": discord.Color.gold(),
    "ACE": discord.Color.blue(),
    "NVN": discord.Color.green(),
    "OFA": discord.Color.purple(),
    "OBS": discord.Color.red(),
    "CITADEL": discord.Color.light_grey(),
}


class RedAlertSelect(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(label="ACE", emoji="🔵", value="ACE"),
            discord.SelectOption(label="DEN", emoji="🟡", value="DEN"),
            discord.SelectOption(label="OFA", emoji="🟣", value="OFA"),
            discord.SelectOption(label="NVN", emoji="🟢", value="NVN"),
            discord.SelectOption(label="OBS", emoji="🔴", value="OBS"),
            discord.SelectOption(label="Citadel", emoji="🏛️", value="CITADEL"),
        ]

        super().__init__(
            placeholder="Select the guild under attack...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        channel = interaction.client.get_channel(RED_ALERT_CHANNEL_ID)

        if channel is None:
            await interaction.response.send_message(
                "❌ Red Alert channel not found.",
                ephemeral=True
            )
            return

        guild = self.values[0]

        image_path = ALERT_IMAGES[guild]
        filename = image_path.split("/")[-1]

        file = discord.File(image_path, filename=filename)

        if guild == "CITADEL":
            description = (
                "🏛THE CITADEL IS UNDER ATTACK!**\n\n"
                f"Reported by {interaction.user.mention}"
            )
        else:
            description = (
                f"⚔️ **{guild} IS UNDER ATTACK!**\n\n"
                f"Reported by {interaction.user.mention}"
            )

        embed = discord.Embed(
            title="🚨 DRACO RED ALERT 🚨",
            description=description,
            color=EMBED_COLORS[guild]
        )

        embed.set_image(url=f"attachment://{filename}")

        await channel.send(
            content="@everyone",
            embed=embed,
            file=file
        )

        await interaction.response.send_message(
            "✅ Red Alert sent.",
            ephemeral=True
        )


class RedAlertView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=60)
        self.add_item(RedAlertSelect())


class RedAlert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(
        name="alert",
        description="Send a Red Alert."
    )
    async def alert(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "🚨 Select the guild under attack:",
            view=RedAlertView(),
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(RedAlert(bot))