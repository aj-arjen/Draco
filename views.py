import discord

from config import (
    VERIFIED_ROLE,
    PENDING_ROLE,
    BOT_LOG_CHANNEL,
    LANGUAGE_ROLES,
    GUILD_ROLES,
    MEMBER_ROLES,
    LEADER_ROLES,
)


class LanguageView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=300)

    @discord.ui.select(
        placeholder="🌍 Select your language...",
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
        placeholder="🏰 Select your guild...",
        custom_id="guild_select",
        options=[
            discord.SelectOption(label="DEN"),
            discord.SelectOption(label="ACE"),
            discord.SelectOption(label="NVN"),
            discord.SelectOption(label="OBS"),
            discord.SelectOption(label="OFA"),
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
        placeholder="⭐ Select your rank...",
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
                self.language,
                self.guild,
                select.values[0]
            )
        )


class ApplicationModal(discord.ui.Modal, title="Dragons Den Application"):

    ingame_name = discord.ui.TextInput(
        label="🎮 In-game Name",
        placeholder="Enter your in-game name...",
        required=True,
        max_length=30
    )

    def __init__(self, language, guild, rank):
        super().__init__()

        self.language = language
        self.guild = guild
        self.rank = rank

    async def on_submit(
        self,
        interaction: discord.Interaction
    ):

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
            name="⭐ Rank",
            value=self.rank.title(),
            inline=False
        )

        embed.add_field(
            name="🎮 In-game Name",
            value=self.ingame_name.value,
            inline=False
        )

        embed.add_field(
            name="👤 Discord",
            value=interaction.user.mention,
            inline=False
        )

        embed.set_footer(
            text=f"User ID: {interaction.user.id}"
        )

        review_channel = interaction.guild.get_channel(
            1525524957042573312
        )

        if review_channel is None:
            await interaction.response.send_message(
                "❌ Review channel not found.",
                ephemeral=True
            )
            return

        await review_channel.send(
            embed=embed,
            view=ReviewView(
                interaction.user.id,
                self.language,
                self.guild,
                self.rank,
                self.ingame_name.value
            )
        )

        await interaction.response.send_message(
            "✅ Your application has been submitted successfully!",
            ephemeral=True
        )
class ReviewView(discord.ui.View):
    def __init__(
        self,
        user_id,
        language,
        guild,
        rank,
        ign
    ):
        super().__init__(timeout=None)

        self.user_id = user_id
        self.language = language
        self.guild = guild
        self.rank = rank
        self.ign = ign

    @discord.ui.button(
        label="Accept",
        emoji="✅",
        style=discord.ButtonStyle.green,
        custom_id="application_accept"
    )
    async def accept(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        for item in self.children:
            item.disabled = True

        await interaction.response.edit_message(view=self)
        print("=== ACCEPT PRESSED ===")
        print(f"BOT_LOG_CHANNEL = {BOT_LOG_CHANNEL}")

        member = interaction.guild.get_member(self.user_id)

        if member is None:
            await interaction.followup.send(
                "❌ Member not found.",
                ephemeral=True
            )
            return

        roles_to_add = []

        verified = interaction.guild.get_role(
            VERIFIED_ROLE
        )

        if verified:
            roles_to_add.append(verified)

        language = interaction.guild.get_role(
            LANGUAGE_ROLES[self.language]
        )

        if language:
            roles_to_add.append(language)

        guild = interaction.guild.get_role(
            GUILD_ROLES[self.guild]
        )

        if guild:
            roles_to_add.append(guild)

        if self.rank == "leader":

            leader = interaction.guild.get_role(
                LEADER_ROLES[self.guild]
            )

            if leader:
                roles_to_add.append(leader)

        if roles_to_add:
            await member.add_roles(*roles_to_add)

        pending = interaction.guild.get_role(
            PENDING_ROLE
        )

        if pending:
            await member.remove_roles(pending)

        try:
            await member.edit(
                nick=self.ign
            )
        except discord.Forbidden:
            pass

        try:
            await member.send(
                f"🎉 Congratulations!\n\n"
                f"Your application for **{self.guild}** "
                f"has been accepted.\n\n"
                f"Welcome to Dragons Den! 🐉"
            )
        except discord.Forbidden:
            pass

            log_channel = interaction.guild.get_channel(BOT_LOG_CHANNEL)
            print(f"BOT_LOG_CHANNEL = {BOT_LOG_CHANNEL}")
            print(f"log_channel = {log_channel}")

            if log_channel:

                log_embed = discord.Embed(
                    title="🟢 Application Accepted",
                    color=discord.Color.green()
                )

                log_embed.add_field(
                    name="👤 Applicant",
                    value=member.mention,
                    inline=False
                )

                log_embed.add_field(
                    name="🎮 In-game Name",
                    value=self.ign,
                    inline=True
                )

                log_embed.add_field(
                    name="🏰 Guild",
                    value=self.guild,
                    inline=True
                )

                log_embed.add_field(
                    name="⭐ Rank",
                    value=self.rank.title(),
                    inline=True
                )

                log_embed.add_field(
                    name="👮 Approved by",
                    value=interaction.user.mention,
                    inline=False
                )

                log_embed.timestamp = discord.utils.utcnow()

                await log_channel.send(embed=log_embed)

        await interaction.followup.send(
            f"✅ Application accepted by {interaction.user.mention}"
        )

    @discord.ui.button(
        label="Decline",
        emoji="❌",
        style=discord.ButtonStyle.red,
        custom_id="application_decline"
    )
    async def decline(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):

        for item in self.children:
            item.disabled = True

        await interaction.response.edit_message(
            view=self
        )

        member = interaction.guild.get_member(
            self.user_id
        )

        if member:

            pending = interaction.guild.get_role(
                PENDING_ROLE
            )

            if pending:
                await member.remove_roles(
                    pending
                )

            try:
                await member.send(
                    "❌ Unfortunately your application "
                    "has been declined.\n\n"
                    "If you think this is a mistake, "
                    "please contact a Guild Leader."
                )
            except discord.Forbidden:
                pass

        await interaction.followup.send(
            f"❌ Application declined by "
            f"{interaction.user.mention}"
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
