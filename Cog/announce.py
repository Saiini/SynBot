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
        channel = ctx.guild.get_channel(492621819950661653)  # CHANGE IF THIS HAS BEEN REMOVED
        await channel.send(embed=discord.Embed(color=0x010000, title=u"\u200B", description=announcement))
def setup(bot):
    bot.add_cog(announce(bot))
