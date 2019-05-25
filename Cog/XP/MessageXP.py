import discord
from discord.ext import commands
import json
import math
class MessageXP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open("STORE\XPSTORE.json", "r") as store:
            self.users = json.load(store)

    async def _save(self):
        await self.bot.wait_until_ready()
        while not self.bot.closed():
            with open("STORE\XPSTORE.json", 'w') as store:
                json.dump(self.users, indent=5)

    def _levelup(self, author_id):
        present_xp = self.users[author_id]['xp']
        present_lvl = self.users[author_id]['level']
        if math.floor(present_xp / (3600 * max(present_lvl, 1))):
            self.users[author_id]['level'] += 1


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            '''check if im able to get XP. Spoiler: i cant'''
            return
        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['xp'] = 0
        self.users[author_id]['xp'] += 1
        if self._levelup(author_id):
            await message.channel.send(f"Hey {message.author.mention}! You have leveled up to: {self.users['level']}")

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        if not member_id in self.users:
            await ctx.send(f"{member.mention} does not have any lvls yet!")
        else:
            embed = discord.Embed(color=0x0000)
            embed.add_field(name="Stats for this member", value=f"XP: {self.users[member_id]['xp']}\nLevel: {self.users[member_id]['level']}")
            await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(MessageXP(bot))
