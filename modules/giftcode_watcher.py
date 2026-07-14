import discord
from discord.ext import tasks

class GiftCodeWatcher:

    def __init__(self, bot):
        self.bot = bot
        self.last_code = None

    @tasks.loop(minutes=1)
    async def check_giftcodes(self):

        print("🔍 Checking for new gift codes...")

    @check_giftcodes.before_loop
    async def before_check(self):

        await self.bot.wait_until_ready()

    def start(self):

        self.check_giftcodes.start()