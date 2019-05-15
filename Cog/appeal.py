import discord
from discord.ext import commands

class appeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def appeal(self, ctx):
        await ctx.send('Dm sent! Please fill your appeal out in dms, if you didnt get a DM from the bot its most likely you have your dms closed\nYour DMs **must** be open in order to appeal for a ban on syn')
        await ctx.author.send(f"Hello *{ctx.author}*\n To appeal for a ban please list your __**IGN**__")
        def check(msg):
            if msg.guild == None:
                return msg.author.id == ctx.author.id
        try:
            _ign = await self.bot.wait_for('message', check=check, timeout=400)
            await ctx.author.send("Alright, now that we have your IGN, please list the main reason you were banned")
            try:
                _reason = await self.bot.wait_for('message', check=check, timeout=400)
                await ctx.author.send(f"Alright! You are all set *{ctx.message.author}*! The staff members will look at your application shortly.")
                channel = self.bot.get_channel(576971106376744960)
                embed = discord.Embed(color=0x000)
                embed.add_field(name=f"Ban appeal for **{_ign.clean_content}**", value=f"Their IGN: {_ign.clean_content}\n\n The reason they were banned: {_reason.clean_content}\n\n Their discord: {ctx.author}")
                await channel.send(embed=embed)
            except:
                return
        except:
            return
def setup(bot):
    bot.add_cog(appeal(bot))