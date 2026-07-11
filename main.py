import os

from dotenv import load_dotenv

from bot import DracoBot

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN ontbreekt.")

bot = DracoBot()


@bot.tree.command(
    name="ping",
    description="Check if Draco is online."
)
async def ping(interaction):
    await interaction.response.send_message(
        "🏓 Pong! Draco is online.",
        ephemeral=True
    )


bot.run(TOKEN)