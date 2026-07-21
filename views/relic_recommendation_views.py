import discord
from discord.ui import View, Select

from utils.relic_recommendations import RECOMMENDATIONS
from utils.relic_loader import load_relic
from utils.relic_embed import create_relic_embed
from utils.relic_recommendation_embed import create_recommendation_embed

class RecommendationMainView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RecommendationSelect())
        
class RecommendationSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="League",
                emoji="🟦"
            ),
            discord.SelectOption(
                label="Horde",
                emoji="🟥"
            ),
            discord.SelectOption(
                label="Nature",
                emoji="🟩"
            ),
        ]

        super().__init__(
            placeholder="Select a faction...",
            options=options
        )
    async def callback(self, interaction: discord.Interaction):
        faction = self.values[0]

        embed = create_recommendation_embed(faction)

        await interaction.response.edit_message(
            embed=embed,
            view=RecommendationView(faction)
        )
class RecommendationView(View):
    def __init__(self, faction: str, f2p: bool = False):
        super().__init__(timeout=None)

        self.faction = faction
        self.f2p = f2p

        if f2p:
            self.add_item(BestSetButton(faction))
        else:
            self.add_item(F2PSetButton(faction))

        self.add_item(BackButton())
        
class F2PSetButton(discord.ui.Button):
    def __init__(self, faction: str):
        super().__init__(
            label="🆓 F2P Set",
            style=discord.ButtonStyle.primary
        )

        self.faction = faction

    async def callback(self, interaction: discord.Interaction):
        embed = create_recommendation_embed(
            self.faction,
            f2p=True
        )

        await interaction.response.edit_message(
            embed=embed,
            view=RecommendationView(
                self.faction,
                f2p=True
            )
        )


class BestSetButton(discord.ui.Button):
    def __init__(self, faction: str):
        super().__init__(
            label="🏆 Best Set",
            style=discord.ButtonStyle.success
        )

        self.faction = faction

    async def callback(self, interaction: discord.Interaction):
        pass


class BackButton(discord.ui.Button):
    def __init__(self):
        super().__init__(
            label="⬅ Back",
            style=discord.ButtonStyle.secondary
        )

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(
            title="Relic Recommendations",
            description="Choose a faction.",
            color=discord.Color.green()
        )

        await interaction.response.edit_message(
            embed=embed,
            view=RecommendationMainView()
        )