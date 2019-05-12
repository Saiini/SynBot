import discord
from discord.ext import commands
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        '''ban someone'''
        dm = f"You have been banned from **{ctx.guild.name}**."
        dm += f" Reason: **{reason}**"
        try:
            await member.send(dm)
        except Exception:
            await ctx.send("This members DM's are not open! So i didnt send their reason of why they are banned!")
        await member.ban(reason=reason)
        embed = discord.Embed(color=0x7027F0)
        embed.add_field(name=f"Banned user: {member.display_name}", value=f"\n   └ Reason: {reason}\n└ 🏷: {member}")
        await ctx.send(embed=embed)
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason: str = None):
        await member.kick(reason=reason)
        embed = discord.Embed(color=0x7127F0)
        embed.add_field(name=f"Kick user: {member.display_name}", value=f"\n └ Reason: {reason}")
        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(Admin(bot))
