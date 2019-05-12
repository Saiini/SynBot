import discord
from discord.ext import commands
class appeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    #@commands.cooldown()
    async def appeal(self, ctx):
        channel = self.bot.get_channel(576971106376744960)
        await ctx.message.add_reaction("📬")
        await ctx.author.send("To appeal, please specify your __**IGN**__")
        try:
            ign = await self.bot.wait_for('message', timeout=210)
        except Exception:
            ign = None
            await ctx.author.send("Something went wrong...\nStopping...")
        if not ign:
            return None
        else:
            await ctx.author.send(f"Alright, so i got **{ign.clean_content}**... Is that correct? [Y/stop]")
            try:
                option = await self.bot.wait_for('message', timeout=210)
            except Exception:
                option = None
            if option.clean_content.lower().startswith('y' or 'Y') == False:
                # automatically stop
                return await ctx.author.send("Something went wrong: **You were suppsed to reply with Y or Stop, please try again...\nStopping...\nStopped**")
            if option.clean_content.lower().startswith('y' or 'Y'):
                await ctx.author.send("Perfect! Now that we have that out of the way, please give me the __**Main Reason**__ you were banned\n")
                try:
                    reason = await self.bot.wait_for('message', timeout=210)
                except Exception:
                    reason = None
                await ctx.author.send("Okay! Now for the final step: __**Why should we unban you?**__")
                try:
                    user_reason = await self.bot.wait_for('message', timeout=70)
                except Exception:
                    user_reason = None
                await ctx.author.send("Alright! You are all set! The staff members at Syn will dm you shortly about your ban appeal. Thank you ~")
                embed = discord.Embed(color=0xDC143C)
                footer = f"\n\nDiscord: {ctx.message.author}"
                embed.add_field(name="Ban appeal ~", value=f"IGN: **{ign.clean_content}**\nReason For Ban: **{reason.clean_content}**\nWhy this user should be unbanned: {user_reason.clean_content}\n" + footer)
                await channel.send(embed=embed)
            elif ign.content.lower().startswith('stop'):
                await ctx.author.send("*Stopping...*\nStopped!")
                return
def setup(bot):
    bot.add_cog(appeal(bot))