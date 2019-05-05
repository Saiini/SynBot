import discord
from discord.ext import commands
import random
class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason : str = None):
        try:
            banned_user = member.mention
            await ctx.user.send(f"Banned user **{banned_user}**, reason: {reason}")
            member.ban(reason=reason)
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
def setup(bot):
    bot.add_cog(Admin(bot))