import discord
from discord.ext import commands
import re
# i had to fix this shit in vim
# - saiini
class announce(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def announce(self, ctx, *, announcement : str = None):
        enders = re.compile("[~]")
        summonText = enders.split(announcement)
        channel = ctx.guild.get_channel(492621819950661653)
        embed = discord.Embed(color=0xE3AA44, title=f"**{summonText[0]}**", description=f"{''.join(summonText[1:])}")
        await channel.send(embed=embed)
def setup(bot):
    bot.add_cog(announce(bot))
