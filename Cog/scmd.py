# run server commands from the bot
import discord
from discord.ext import commands
from mcrcon import MCRcon
class scmd(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def scmd(self, ctx, *, cmd : str = None):
        if cmd == None:
            # no command was provided
            return
        conn = MCRcon("", "")
        conn.connect()
        resp = conn.command(f"/{cmd}")
        print(f"SENT: {cmd}")

def setup(bot):
    bot.add_cog(scmd(bot))
