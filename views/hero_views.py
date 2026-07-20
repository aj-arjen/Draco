import discord
from discord.ui import Select, View
from utils.hero_loader import get_factions, get_rarities, get_heroes, load_hero
from utils.hero_embed import build_hero_embed

class FactionSelect(Select):
    def __init__(self):
        options=[discord.SelectOption(label=f,value=f) for f in get_factions()]
        super().__init__(placeholder='Choose a faction...',options=options)
    async def callback(self,interaction:discord.Interaction):
        await interaction.response.edit_message(content='Choose a rarity:',view=RarityView(self.values[0]))

class FactionView(View):
    def __init__(self):
        super().__init__(timeout=180)
        self.add_item(FactionSelect())

class RaritySelect(Select):
    def __init__(self,faction:str):
        self.faction=faction
        options=[discord.SelectOption(label=r,value=r) for r in get_rarities(faction)]
        super().__init__(placeholder='Choose a rarity...',options=options)
    async def callback(self,interaction:discord.Interaction):
        await interaction.response.edit_message(content='Choose a hero:',view=HeroView(self.faction,self.values[0]))

class RarityView(View):
    def __init__(self,faction:str):
        super().__init__(timeout=180)
        self.add_item(RaritySelect(faction))

class HeroSelect(Select):
    def __init__(self,faction:str,rarity:str):
        options = [
            discord.SelectOption(
                label=h.replace("_", " ").title(),
                value=h
            )
            for h in get_heroes(faction, rarity)
        ]
        super().__init__(placeholder='Choose a hero...',options=options)
    async def callback(self,interaction:discord.Interaction):
        hero=load_hero(self.values[0])
        if hero is None:
            await interaction.response.send_message('Hero could not be loaded.',ephemeral=True)
            return
        embed,file=build_hero_embed(hero)
        await interaction.response.edit_message(content=None,embed=embed,attachments=[file],view=None)

class HeroView(View):
    def __init__(self,faction:str,rarity:str):
        super().__init__(timeout=180)
        self.add_item(HeroSelect(faction,rarity))
