import discord
from discord.ext import commands

class report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @commands.cooldown(10, 2.5)
    async def report(self, ctx, *, ignprompt : str = None):
        author = ctx.message.author
        def check(msg):
            if msg.guild == None:
                return msg.author.id == ctx.author.id
        if ignprompt == None:
            await ctx.send("You must provide an IGN in order to report!")
            return
        await ctx.author.send(f"Hey! i heard you wanted to report *{ignprompt}*! Please tell me the **reason** you are reporting them")
        try:
            reasonreport = await self.bot.wait_for('message', check=check, timeout=120)
            await ctx.author.send(f"You have successfully reported __**{ignprompt}**__ for __**{reasonreport.clean_content}**__!")
            channel = self.bot.get_channel(553964384590757898)
            embed = discord.Embed(color=0x0000)
            embed.add_field(name="User Report", value=f"Their IGN: {ignprompt}\n Reported for: {reasonreport.clean_content}")
            await channel.send(embed=embed)
        except Exception as error:
            return print(error)
def setup(bot):
    bot.add_cog(report(bot))