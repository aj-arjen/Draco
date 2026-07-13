import discord

REDEEM_URL = "https://topheroes.store.kopglobal.com/en"


class GiftCodeView(discord.ui.View):
    def __init__(self, code):
        super().__init__(timeout=None)

        self.code = code

        redeem = discord.ui.Button(
            label="Redeem",
            emoji="🌐",
            url=REDEEM_URL
        )

        self.add_item(redeem)

    @discord.ui.button(
        label="Copy Code",
        emoji="📋",
        style=discord.ButtonStyle.blurple,
        custom_id="copy_giftcode"
    )
    async def copy_code(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        await interaction.response.send_message(
            f"📋 Copy this code:\n```{self.code}```",
            ephemeral=True
        )


async def post_giftcode(channel, code):

    embed = discord.Embed(
        title="🎁 New Top Heroes Gift Code",
        color=0xC49A3A
    )

    embed.description = (
        "A new gift code is available!\n\n"
        f"```{code}```"
    )

    embed.add_field(
        name="Status",
        value="🟢 Active",
        inline=True
    )

    embed.set_footer(
        text="Powered by Draco 🐉"
    )

    await channel.send(
        embed=embed,
        view=GiftCodeView(code)
    )