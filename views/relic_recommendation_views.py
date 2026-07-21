import discord
from discord.ui import View, Select

from utils.relic_recommendations import RECOMMENDATIONS
from utils.relic_loader import load_relic
from utils.relic_embed import create_relic_embed

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