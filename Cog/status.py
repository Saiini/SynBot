import discord
from discord.ext import commands
import os
class status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def status(self, ctx):
        '''checks if the server is online or offline'''
        await ctx.send("Please wait...")
        ip = "synpvp.xyz"
        stat = os.system(f'ping {ip}')
        if stat == 0:
            await ctx.send("Server is online!")
        else:
            await ctx.send("Server if offline!")
def setup(bot):
    bot.add_cog(status(bot))