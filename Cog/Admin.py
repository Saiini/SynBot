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
        embed.add_field(name=f"Banned user: {member.display_name}", value=f"\n   └ Reason: {reason}\n")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason: str = None):
        await member.kick(reason=reason)
        embed = discord.Embed(color=0x7127F0)
        embed.add_field(name=f"Kick user: {member.display_name}", value=f"\n └ Reason: {reason}")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, member : discord.Member, *, reason : str = None):
        dm = f"You have been muted in **{ctx.guild.name}** for **{reason}**"
        try:
            await member.send(dm)
        except Exception:
            pass
        embed = discord.Embed(color=0x0000)
        embed.add_field(name=f"Muted user: {member.display_name}", value=f"\n   └ Reason: {reason}\n")
        await ctx.send(embed=embed)
        role = discord.utils.get(member.guild.roles, name="Muted")
        try:
            await member.add_roles(role)
            return
        except:
            await ctx.send("It appears you do not have enough permission to do that - sorry!")
            return

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, member : discord.Member, *, reason : str = None):
        dm = f"You have been Un-Muted in **{ctx.guild.name}**. Meaning you can now chat there again. Please make sure you read the rules so this doesn't happen again!"
        try:
            await member.send(dm)
        except:
            await ctx.send(member.mention + "has been un-muted")
        role = discord.utils.get(member.guild.roles, name="Muted")
        if role == None:
            await ctx.send("That user isnt muted!")
        try:
            await member.remove_roles(role)
            return
        except:
            await ctx.send("It appears you do not have enough permission to do that - sorry!")
            return

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def warn(self, ctx, member : discord.Member, *, reason : str = None):
        await ctx.send(f"{member.mention} has been warned!")
        dm = f"You have been warned in **{ctx.guild.name}**!"
        try:
            await member.send(dm)
        except:
            return
        warning_1 = discord.utils.get(member.guild.roles, name="Warned")
        await member.add_roles(warning_1)

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def purge(self, ctx, msg : int):
        try:
            await ctx.channel.purge(limit=msg+1)
        except:
            return
'''@commands.command()
@commands.has_permissions(ban_members=True)
async def hackban(self, ctx, user : str = None):'''
def setup(bot):
    bot.add_cog(Admin(bot))
