import discord
from discord.ext import commands
class announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def announce(self, ctx, *, announcement: str = None):
        """So you want to announce something huh? well... Do it!"""
        await ctx.send('Sending...')
        body = ""  # Body
        footer = ""
        channel = ctx.guild.get_channel(492621819950661653)  # CHANGE IF THIS HAS BEEN REMOVED
        announcer = ctx.message.author
        footer += f"-{announcer}"
        body += f"{announcement}\n"
        embed = discord.Embed(color=0xDC143C)
        embed.add_field(name=f"{body}", value=footer)
        await ctx.send('Announced!')
        await channel.send(embed=embed)
        await channel.send("@everyone")
        await ctx.channel.purge(limit=1)
def setup(bot):
    bot.add_cog(announce(bot))
