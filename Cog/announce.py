import discord
from discord.ext import commands

class announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def announce(self, ctx, *, announcement : str = None):
        """So you want to announce something huh? well... Do it!"""
        await ctx.send('Sending...')
        header = ""
        body = ""
        footer = ""
        channel = ctx.guild.get_channel(492621819950661653)  # CHANGE IF THIS HAS BEEN REMOVED
        announcer = ctx.message.author
        embed = discord.Embed(color=0x010000)
        header += f"{announcement}"
        footer += f"\n - {announcer}"
        embed.add_field(name=u"\u200B", value=header)
        rpf = announcer.avatar_url
        embed.set_footer(text=footer, icon_url=rpf)
        await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(announce(bot))
