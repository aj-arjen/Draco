import discord

from utils.relic_loader import load_all_relics, load_relic
from utils.relic_embed import create_relic_embed
from views.relic_recommendation_views import RecommendationMainView


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

            embed = discord.Embed(
                title="Relic Recommendations",
                description="Choose a faction.",
                color=discord.Color.green()
)

            await interaction.response.edit_message(
                embed=embed,
                view=RecommendationMainView()
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