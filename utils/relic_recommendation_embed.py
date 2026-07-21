import discord

from utils.relic_recommendations import RECOMMENDATIONS
from utils.relic_loader import load_relic


def create_recommendation_embed(faction: str, f2p: bool = False):
    data = RECOMMENDATIONS[faction]

    relics = data["f2p"] if f2p else data["best"]

    attack = load_relic(relics["Attack"])
    control = load_relic(relics["Control"])
    support = load_relic(relics["Support"])

    title = (
        f"🆓 {faction} F2P Relic Set"
        if f2p
        else f"🏆 {faction} Best Relic Set"
    )

    embed = discord.Embed(
        title=title,
        color=discord.Color.gold()
    )

    embed.add_field(
        name="⚔️ Attack",
        value=attack["name"],
        inline=False
    )

    embed.add_field(
        name="🌀 Control",
        value=control["name"],
        inline=False
    )

    embed.add_field(
        name="🛡️ Support",
        value=support["name"],
        inline=False
    )

    return embed