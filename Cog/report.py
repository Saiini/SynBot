import discord
from discord.ext import commands
class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def report(self, ctx):
        author = ctx.message.author
        await ctx.author.send(f"Hello {author}! So you would like to report someone huh? Well, please provide their **__IGN__**")
def setup(bot):
    bot.add_cog(report(bot))