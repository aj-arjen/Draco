import discord

from utils.relic_loader import load_all_relics, load_relic
from utils.relic_embed import create_relic_embed


# =========================
# Main View (/relic)
# =========================

class RelicMainView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(MainSelect())


# =========================
# Main Select
# =========================

class MainSelect(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="Select Relic",
                value="select_relic",
                description="Browse all relics.",
                emoji="🔍"
            ),
            discord.SelectOption(
                label="Faction",
                value="faction",
                description="Browse recommended relics by faction.",
                emoji="🏰"
            )
        ]

        super().__init__(
            placeholder="Choose an option...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        if self.values[0] == "select_relic":

            embed = discord.Embed(
                title="Select a Relic",
                description="Choose a relic from the dropdown below.",
                color=discord.Color.gold()
            )

            await interaction.response.edit_message(
                embed=embed,
                view=RelicSelectView()
            )

        elif self.values[0] == "faction":

            embed = discord.Embed(
                title="Choose a Faction",
                description="Select a faction to view the best relic recommendations.",
                color=discord.Color.green()
            )

            await interaction.response.edit_message(
                embed=embed,
                view=FactionView()
            )


# =========================
# Faction View
# =========================

class FactionView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(FactionSelect())


# =========================
# Faction Select
# =========================

class FactionSelect(discord.ui.Select):
    def __init__(self):

        options = [
            discord.SelectOption(
                label="League",
                value="League",
                emoji="🏰"
            ),
            discord.SelectOption(
                label="Horde",
                value="Horde",
                emoji="🪓"
            ),
            discord.SelectOption(
                label="Nature",
                value="Nature",
                emoji="🌿"
            )
        ]

        super().__init__(
            placeholder="Choose a faction...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        faction = self.values[0]

        embed = discord.Embed(
            title=f"{faction} Relics",
            description="Choose a category.",
            color=discord.Color.blurple()
        )

        await interaction.response.edit_message(
            embed=embed,
            view=FactionOptionView(faction)
        )

# =========================
# Faction Option View
# =========================

class FactionOptionView(discord.ui.View):
    def __init__(self, faction: str):
        super().__init__(timeout=180)
        self.add_item(FactionOptionSelect(faction))


# =========================
# Faction Option Select
# =========================

class FactionOptionSelect(discord.ui.Select):
    def __init__(self, faction: str):

        self.faction = faction

        options = [
            discord.SelectOption(
                label="Top 3 Picks",
                value="top3",
                description=f"Best relics for {faction}",
                emoji="⭐"
            ),
            discord.SelectOption(
                label="Top 3 F2P Picks",
                value="f2p",
                description=f"Best free-to-play relics for {faction}",
                emoji="🆓"
            )
        ]

        super().__init__(
            placeholder="Choose a category...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        choice = self.values[0]

        if choice == "top3":

            embed = discord.Embed(
                title=f"⭐ {self.faction} • Top 3 Picks",
                description="Coming soon...",
                color=discord.Color.gold()
            )

        else:

            embed = discord.Embed(
                title=f"🆓 {self.faction} • Top 3 F2P Picks",
                description="Coming soon...",
                color=discord.Color.green()
            )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )

# =========================
# Relic Select View
# =========================

class RelicSelectView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(RelicSelect())


# =========================
# Relic Select
# =========================

class RelicSelect(discord.ui.Select):
    def __init__(self):

        relics = load_all_relics()

        options = []

        for relic in sorted(relics, key=lambda r: r["name"]):

            options.append(
                discord.SelectOption(
                    label=relic["name"],
                    value=relic["id"]
                )
            )

        super().__init__(
            placeholder="Choose a relic...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        relic_id = self.values[0]

        relic = load_relic(relic_id)

        if relic is None:

            await interaction.response.send_message(
                "Relic not found.",
                ephemeral=True
            )
            return

        embed, file = create_relic_embed(relic)

        if file:

            await interaction.response.edit_message(
                embed=embed,
                attachments=[file],
                view=None
            )

        else:

            await interaction.response.edit_message(
                embed=embed,
                view=None
            )