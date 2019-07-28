import discord
from discord.ext import commands
class apply(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def apply(self, ctx):
        await ctx.send("The application session has started - please check your dms!")
        channel = self.bot.get_channel(604400706778300438)
        def check(msg):
            if msg.guild == None:
                return msg.author.id == ctx.author.id
        try:
            await ctx.author.send(f"Hello *{ctx.author}*\n I heard you would like to apply for staff - lets get started shall we?")
            await ctx.author.send("Just a quick note: You cannot edit your application after it has been sent!")
            await ctx.author.send(f"Please start by giving me your **__IGN__**")
            try:
                ign = await self.bot.wait_for('message', check=check, timeout=200)
                try:
                    await ctx.author.send(f"Alright **__{ign.clean_content}__**, Please tell me how you would benifit the server - *Note: You can use embeds*_\n[~~y/n/~~stop]")
                    benifit = await self.bot.wait_for('message', check=check, timeout=200)
                    if benifit.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...[100%]*")
                        return
                    await ctx.author.send("Alright! Now that we have that out of the way, please give me **all of the alts** you have had on the server - be honest, because we will check.\n[~~y/n/~~stop]")
                    alts_list = await self.bot.wait_for('message', check=check, timeout=200)
                    if alts_list.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("Please give me your age")
                    age = await self.bot.wait_for('message', check=check, timeout=200)
                    if age.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("What device do you play on? \n[~~y/n/~~stop]")
                    device = await self.bot.wait_for('message', check=check, timeout=200)
                    if device.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("What would you do if there was a glitcher on the server? \n[~~y/n/~~stop] __\n\n*Note: You can use embeds*__")
                    glitcher = await self.bot.wait_for('message', check=check, timeout=200)
                    if glitcher.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("What staffing experience do you have? If none just enter ``none``\n\n[~~y/n/~~stop]")
                    staff_exper = await self.bot.wait_for('message', check=check, timeout=200)
                    if staff_exper.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("Do you have screen sharing experience? (Anydesk)\n\n[~~y/n/~~stop]")
                    screenshare = await self.bot.wait_for('message', check=check, timeout=200)
                    if screenshare.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("Final question: What is one mistake you have made as staff (if you haven't been staff on a server before, reply with ``none``)\n\n[~~y/n/~~stop]")
                    mistakes = await self.bot.wait_for('message', check=check, timeout=200)
                    if mistakes.clean_content == "stop":
                        await ctx.author.send("No problem! \n\n*Stopping session...|100%|*")
                        return
                    await ctx.author.send("You are all finished with your staff application! You will be dm'd shortly if you are accepted!")
                    embed = discord.Embed(color=0x0000)
                    embed.add_field(name=f"Staff application by: **{ctx.author}**", value=f"Their IGN: **{ign.clean_content}**\nWhy they want to be staff: **{benifit.clean_content}**\nTheir alts: **{alts_list.clean_content}**\nTheir age: **{age.clean_content}**\nWhat device they play on: **{device.clean_content}**\nWhat they would do if there was a glitcher on the server: **{glitcher.clean_content}**\nStaff experience: **{staff_exper.clean_content}**\nDo they have experience with screenshare? **{screenshare.clean_content}**\nMistakes they've made before: **{mistakes.clean_content}**")
                    await channel.send(embed=embed)
                except:
                    return
            except:
                return
        except Exception:
            return


    # for when we... get removed...
    # rip...
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def goodbye(self, ctx):
        await ctx.send("https://giphy.com/gifs/TBuAgAgXXvPMY")
def setup(bot):
    bot.add_cog(apply(bot))
