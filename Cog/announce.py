import discord
from discord.ext import commands
class announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def announce(self, ctx, *, announcement : str = None):
        vored_sent = announcement.replace(".", "\n")
        channel = ctx.guild.get_channel(492621819950661653)
        embed = discord.Embed(color=0xE3AA44, title=vored_sent)
        await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(announce(bot))
