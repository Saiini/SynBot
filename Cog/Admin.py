import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
            await member.ban(reason=reason)
            embed = discord.Embed(color=0x5F8460)
            embed.add_field(name=f"Banned user: {member}", value=f"└─ Reason: {reason}")
            await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        await member.kick(reason=reason)
        embed = discord.Embed(color=0xD5FB49)
        embed.add_field(name=f"Kick user: {member}", value=f"└─ Reason: {reason}")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Admin(bot))