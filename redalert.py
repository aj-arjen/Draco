import discord

RED_ALERT_CHANNEL_ID = 1526579916408225802

RED_ALERTS = {
    "DEN": "🟡 DEN HIVE UNDER ATTACK 🟡",
    "ACE": "🔵 ACE HIVE UNDER ATTACK 🔵",
    "OFA": "🟣 OFA HIVE UNDER ATTACK 🟣",
    "NVN": "🟢 NVN HIVE UNDER ATTACK 🟢",
    "OBS": "🔴 OBS HIVE UNDER ATTACK 🔴",
    "CITADEL": "🏰 CITADEL UNDER ATTACK 🏰",
}

ALERT_IMAGES = {
    "DEN": "assets/alerts/den_alert.png",
    "ACE": "assets/alerts/ace_alert.png",
    "OFA": "assets/alerts/ofa_alert.png",
    "NVN": "assets/alerts/nvn_alert.png",
    "OBS": "assets/alerts/obs_alert.png",
    "CITADEL": "assets/alerts/citadel_alert.png",
}


class RedAlertSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(
                label="DEN Hive",
                emoji="🟡",
                value="DEN"
            ),
            discord.SelectOption(
                label="ACE Hive",
                emoji="🔵",
                value="ACE"
            ),
            discord.SelectOption(
                label="OFA Hive",
                emoji="🟣",
                value="OFA"
            ),
            discord.SelectOption(
                label="NVN Hive",
                emoji="🟢",
                value="NVN"
            ),
            discord.SelectOption(
                label="OBS Hive",
                emoji="🔴",
                value="OBS"
            ),
            discord.SelectOption(
                label="Citadel",
                emoji="🏰",
                value="CITADEL"
            ),
        ]

        super().__init__(
            placeholder="Select a Red Alert...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        channel = interaction.client.get_channel(
            RED_ALERT_CHANNEL_ID
        )

        if channel is None:

            await interaction.response.send_message(
                "❌ Red Alert channel not found.",
                ephemeral=True
            )
            return

        image_path = ALERT_IMAGES[self.values[0]]

        filename = image_path.split("/")[-1]

        file = discord.File(
            image_path,
            filename=filename
        )

        embed = discord.Embed(
            title="🚨 DRACO RED ALERT 🚨",
            description=(
                f"## {RED_ALERTS[self.values[0]]}\n\n"
                "⚔️ **EVERYONE, PREPARE TO DEFEND!**\n\n"
                f"👤 Reported by {interaction.user.mention}"
            ),
            color=discord.Color.red()
        )

        embed.set_image(
            url=f"attachment://{filename}"
        )

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

        self.add_item(
            RedAlertSelect()
        )