import discord
from discord.ext import commands
class apply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def apply(self, ctx):
        await ctx.send("The application session has started - please check your dms!")
        channel = self.bot.get_channel(579527082296475679)
        def check(msg):
            if msg.guild == None:
                return msg.author.id == ctx.author.id
        try:
            await ctx.author.send(f"Hello *{ctx.author}*\n I heard you would like to apply for staff - lets get started shall we?")
            await ctx.author.send(f"Please start by giving me your **__IGN__**")
            try:
                ign = await self.bot.wait_for('message', check=check, timeout=200)
                try:
                    await ctx.author.send(
                        f"Alright **__{ign.clean_content}__**, Please tell me how you would benifit the server - Note: You can use embeds")
                    benifit = await self.bot.wait_for('message', check=check, timeout=200)
                    await ctx.author.send("Alright! Now that we have that out of the way, please give me **all of the alts** you have had on the server - be honest, because we will check.")
                    alts_list = await self.bot.wait_for('message', check=check, timeout=200)
                    await ctx.author.send("Final step: Please give me your age")
                    age = await self.bot.wait_for('message', check=check, timeout=200)
                    await ctx.author.send("You are all finished with your staff application! You will be dm'd shortly if you are accepted!")
                    embed = discord.Embed(color=0x0000)
                    embed.add_field(name=f"Staff application by: **{ctx.author}**", value=f"Their IGN: **{ign.clean_content}**\nWhy they want to be staff: **{benifit.clean_content}**\nTheir alts: **{alts_list.clean_content}**\nTheir age: **{age.clean_content}**")
                    await channel.send(embed=embed)
                except:
                    return
            except:
                return
        except Exception:
            return
def setup(bot):
    bot.add_cog(apply(bot))