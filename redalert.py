import discord

RED_ALERTS = {
    "DEN": {
        "title": "🛡️ DEN HIVE UNDER ATTACK 🛡️",
        "image": "den.png"
    },
    "ACE": {
        "title": "🛡️ ACE HIVE UNDER ATTACK 🛡️",
        "image": "ace.png"
    },
    "OFA": {
        "title": "🛡️ OFA HIVE UNDER ATTACK 🛡️",
        "image": "ofa.png"
    },
    "NVN": {
        "title": "🛡️ NVN HIVE UNDER ATTACK 🛡️",
        "image": "nvn.png"
    },
    "OBS": {
        "title": "🛡️ OBS HIVE UNDER ATTACK 🛡️",
        "image": "obs.png"
    },
    "CITADEL": {
        "title": "🏰 CITADEL UNDER ATTACK 🏰",
        "image": "citadel.png"
    }
}


class RedAlertSelect(discord.ui.Select):

    def __init__(self):

        options = [
            discord.SelectOption(
                label="DEN Hive",
                emoji="🛡️",
                value="DEN"
            ),
            discord.SelectOption(
                label="ACE Hive",
                emoji="🛡️",
                value="ACE"
            ),
            discord.SelectOption(
                label="OFA Hive",
                emoji="🛡️",
                value="OFA"
            ),
            discord.SelectOption(
                label="NVN Hive",
                emoji="🛡️",
                value="NVN"
            ),
            discord.SelectOption(
                label="OBS Hive",
                emoji="🛡️",
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

    async def callback(
        self,
        interaction: discord.Interaction
    ):

        await interaction.response.send_message(
            f"🚨 {RED_ALERTS[self.values[0]]['title']}",
            ephemeral=True
        )


class RedAlertView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=60)

        self.add_item(RedAlertSelect())