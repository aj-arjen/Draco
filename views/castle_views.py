import discord

from utils.castle_loader import load_all_castles, load_castle
from utils.castle_embed import create_castle_embed


# =========================
# Main View
# =========================

class CastleMainView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(CastleSelect())


# =========================
# Castle Select
# =========================

class CastleSelect(discord.ui.Select):
    def __init__(self):

        castles = load_all_castles()

        options = []

        for castle in sorted(castles, key=lambda c: c["name"]):

            options.append(
                discord.SelectOption(
                    label=castle["name"],
                    value=castle["id"]
                )
            )

        super().__init__(
            placeholder="Choose a Castle Skin...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        castle_id = self.values[0]

        castle = load_castle(castle_id)

        if castle is None:

            await interaction.response.send_message(
                "Castle not found.",
                ephemeral=True
            )

            return

        embed, file = create_castle_embed(castle)

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