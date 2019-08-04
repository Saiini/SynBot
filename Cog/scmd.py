# run server commands from the bot
import discord
import Cog.mcrcon as mcrcon
import socket
from discord.ext import commands
class scmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.has_permissions(ban_members=True) # just in case something goes **__terribly__** wrong
    async def scmd(self, ctx, *, cmd : str = None):
        if ctx.author.id == 570698736536125481 or ctx.author.id == 593294576026910720 or ctx.author.id == 181174394536722432: # check if we are either cort, erin, or saiini
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(("synhcf.net", 19132))
                mcrcon.login(sock, 'ZxzDqzUUyB')  # Perform initial login
                mcrcon.command(sock, cmd)
            except:
                return
        else:
            await ctx.send("Test failed!")
def setup(bot):
    bot.add_cog(scmd(bot))
