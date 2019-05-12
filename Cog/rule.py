import discord
from discord.ext import commands
class rule(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def rules(self, ctx, *, rulenum : int = None):
        if rulenum == None:
            await ctx.send("Please provide a rule number.")
            return
        msg = ""
        rulestr = """
        
        """
def setup(bot):
    bot.add_cog(rule(bot))