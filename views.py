import discord

from config import (
    VERIFIED_ROLE,
    PENDING_ROLE,
    LANGUAGE_ROLES,
    GUILD_ROLES,
    MEMBER_ROLES,
    LEADER_ROLES,
)


class LanguageView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.select(
        placeholder="Select your language...",
        custom_id="language_select",
        options=[
            discord.SelectOption(label="English"),
            discord.SelectOption(label="Deutsch"),
            discord.SelectOption(label="Français"),
            discord.SelectOption(label="Español"),
            discord.SelectOption(label="Português"),
            discord.SelectOption(label="中文"),
            discord.SelectOption(label="Tiếng Việt"),
            discord.SelectOption(label="ไทย"),
            discord.SelectOption(label="Русский"),
            discord.SelectOption(label="日本語"),
            discord.SelectOption(label="Nederlands"),
            discord.SelectOption(label="Italiano"),
            discord.SelectOption(label="العربية"),
            discord.SelectOption(label="עברית"),
        ]
    )
    async def language_select(
        self,
        interaction: discord.Interaction,
        select: discord.ui.Select
    ):
        await interaction.response.edit_message(
            content="🏰 Select your guild:",
            view=GuildView(select.values[0])
        )


class GuildView(discord.ui.View):
    def __init__(self, language):
        super().__init__(timeout=300)
        self.language = language

    @discord.ui.select(
        placeholder="Select your guild...",
        custom_id="guild_select",
        options=[
            discord.SelectOption(label="DEN"),
            discord.SelectOption(label="ACE"),
            discord.SelectOption(label="NVN"),
            discord.SelectOption(label="OFA"),
            discord.SelectOption(label="OBS"),
            discord.SelectOption(label="Other"),
        ]
    )
    async def guild_select(
        self,
        interaction: discord.Interaction,
        select: discord.ui.Select
    ):
        await interaction.response.edit_message(
            content="⭐ Select your rank:",
            view=RankView(
                self.language,
                select.values[0]
            )
        )
class RankView(discord.ui.View):
    def __init__(self, language, guild):
        super().__init__(timeout=300)
        self.language = language
        self.guild = guild

    @discord.ui.select(
        placeholder="Select your rank...",
        custom_id="rank_select",
        options=[
            discord.SelectOption(
                label="R1 / R2 / R3",
                value="member"
            ),
            discord.SelectOption(
                label="R4 / R5",
                value="leader"
            ),
        ]
    )
    async def rank_select(
        self,
        interaction: discord.Interaction,
        select: discord.ui.Select
    ):
        await interaction.response.send_modal(
            ApplicationModal(
                language=self.language,
                guild=self.guild,
                rank=select.values[0]
            )
        )
class ReviewView(discord.ui.View):
    def __init__(self, user_id, language, guild, rank):
        super().__init__(timeout=None)

        self.user_id = user_id
        self.language = language
        self.guild = guild
        self.rank = rank

    @discord.ui.button(
        label="Accept",
        emoji="✅",
        style=discord.ButtonStyle.green,
        custom_id="accept_application"
    )
    async def accept(
    self,
    interaction: discord.Interaction,
    button: discord.ui.Button
):
    for item in self.children:
        item.disabled = True

    await interaction.response.edit_message(view=self)

    member = interaction.guild.get_member(self.user_id)

    if member is None:
        await interaction.followup.send(
            "❌ Member could not be found."
        )
        return

    verified_role = interaction.guild.get_role(VERIFIED_ROLE)
    pending_role = interaction.guild.get_role(PENDING_ROLE)

    guild_role = interaction.guild.get_role(
        GUILD_ROLES[self.guild]
    )

    language_role = interaction.guild.get_role(
        LANGUAGE_ROLES[self.language]
    )

    if self.rank == "leader":
        rank_role = interaction.guild.get_role(
            LEADER_ROLES[self.guild]
        )
    else:
        rank_role = interaction.guild.get_role(
            MEMBER_ROLES[self.guild]
        )

    if verified_role:
        await member.add_roles(verified_role)

    if pending_role:
        await member.remove_roles(pending_role)

    if guild_role:
        await member.add_roles(guild_role)

    if language_role:
        await member.add_roles(language_role)

    if rank_role:
        await member.add_roles(rank_role)

    try:
        await member.send(
            f"🎉 Congratulations!\n\n"
            f"Your application for **{self.guild}** has been approved.\n\n"
            f"Welcome to **Dragons Den**! 🐉"
        )
    except discord.Forbidden:
        pass

    await interaction.followup.send(
        f"✅ Application accepted by {interaction.user.mention}"
    )

    @discord.ui.button(
        label="Deny",
        emoji="❌",
        style=discord.ButtonStyle.red,
        custom_id="deny_application"
    )
    async def deny(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        for item in self.children:
            item.disabled = True

        await interaction.response.edit_message(view=self)

        await interaction.followup.send(
            f"❌ Application denied by {interaction.user.mention}"
        )
class ApplicationModal(discord.ui.Modal, title="Dragons Den Application"):
    def __init__(self, language, guild, rank):
        super().__init__()

        self.language = language
        self.guild = guild
        self.rank = rank

    ingame_name = discord.ui.TextInput(
        label="In-game Name",
        placeholder="Enter your in-game name...",
        required=True,
        max_length=30
    )

    async def on_submit(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="📋 New Application",
            color=0xC49A3A
        )

        embed.add_field(
            name="🌍 Language",
            value=self.language,
            inline=False
        )

        embed.add_field(
            name="🏰 Guild",
            value=self.guild,
            inline=False
        )

        embed.add_field(
            name="⚔️ Rank",
            value=self.rank,
            inline=False
        )

        embed.add_field(
            name="🎮 In-game Name",
            value=self.ingame_name.value,
            inline=False
        )

        embed.set_footer(
            text=f"Discord User: {interaction.user}"
        )

        review_channel = interaction.guild.get_channel(1525524957042573312)

        if review_channel is None:
            await interaction.response.send_message(
                "❌ The review channel could not be found.",
                ephemeral=True
            )
            return

        await review_channel.send(
            embed=embed,
            view=ReviewView(
                interaction.user.id,
                self.language,
                self.guild,
                self.rank
            )
        )

        await interaction.response.send_message(
            "✅ Your application has been submitted!",
            ephemeral=True
        )


class ApplyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Apply",
        emoji="📝",
        style=discord.ButtonStyle.green,
        custom_id="apply_button"
    )
    async def apply(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "🌍 Select your language:",
            view=LanguageView(),
            ephemeral=True
        )