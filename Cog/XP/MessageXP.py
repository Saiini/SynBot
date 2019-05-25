import discord
from discord.ext import commands
import json
import asyncio


class MessageXP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        with open(r"STORE\user.json", "r") as store:
            self.users = json.load(store)
        self.bot.loop.create_task(self._save())

    async def _save(self):
        await self.bot.wait_until_ready()
        while not self.bot.is_closed():
            with open(r"STORE\user.json", 'w') as store:
                json.dump(self.users, store, indent=5)
            await asyncio.sleep(2)

    def _levelup(self, author_id, message):
        present_xp = self.users[author_id]['xp']
        present_lvl = self.users[author_id]['level']
        if present_xp >= round((4 * (present_lvl ** 3)) / 5):
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

    @commands.command()
    async def level(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)
        if not member_id in self.users:
            await ctx.send(f"{member.mention} does not have any lvls yet!")
        else:
            embed = discord.Embed(color=0x0000)
            embed.add_field(name="Stats for this member", value=f"XP: {self.users[member_id]['xp']}\nLevel: {self.users[member_id]['level']}", inline=True)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(MessageXP(bot))
