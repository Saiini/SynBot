import random

import discord
from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        try:
            await member.ban(reason=reason)
            embed = discord.Embed(color=0x7027F0)
            embed.add_field(name=f"Banned user: {member.display_name}", value=f"\n └Reason: {reason}")
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            NoPermList = [
                "I do not have permission to use that command!",
                "I cannot use that command!",
                "Im afriad I cannot run that command!",
            ]
            await ctx.send(random.choice(NoPermList))
            return
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            NoPermArray = [
                "You do nor have permission to use that command!",
                "It appears you do not have permission to run that command!",
                "I cannot ban that user due to your perms!",
                "Sorry! Please check your perms and try again",
            ]
            await ctx.send(random.choice(NoPermArray))
            return

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason: str = None):
        try:
            await member.kick(reason=reason)
            embed = discord.Embed(color=0x3A1B36)
            embed.add_field(name=f"Kicked user: {member.display_name}", value=f"\n └Reason: {reason}")
            await ctx.send(embed=embed)
        except discord.errors.Forbidden:
            await ctx.send("Looks like i dont have perms to use that command!")
            return

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            NoPermArray = [
                "You do nor have permission to use that command!",
                "It appears you do not have permission to run that command!",
                "I cannot ban that user due to your perms!",
                "Sorry! Please check your perms and try again",
            ]
            await ctx.send(random.choice(NoPermArray))
        return
def setup(bot):
    bot.add_cog(Admin(bot))