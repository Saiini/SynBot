import discord
from discord.ext import commands
class appeal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        '''
        This really ugly code works for some strange reason...
        '''
    @commands.command()
    @commands.cooldown(rate=1, per=16)
    async def appeal(self, ctx):
        author = ctx.author
        channel = self.bot.get_channel(576971106376744960)
        try:
            await ctx.message.add_reaction("📬")
            await ctx.send("*Sent you a dm!*")
            await ctx.author.send(f"Hey **{author}**!\nIt appears you would like to appeal for a ban, Lets get started shall we?\nPlease list your __**IGN**__ for me")
            ign = await self.bot.wait_for('message', timeout=200)
            try:
                await ctx.author.send(f'Alright *{ign.clean_content}*, please tell me the __**main reason**__ you were banned')
                reason = await self.bot.wait_for('message', timeout=200)
                try:
                    await ctx.author.send(f"Okay, so you were banned for: **{reason.clean_content}**, is this correct? [y/stop]")
                    option = await self.bot.wait_for('message', timeout=200)
                    try:
                        if option.clean_content == 'y':
                            await ctx.author.send("Okay! Now that we have that out of the way, what type of ban did you recieve? [Perm/Temp]")
                            ban_type = await self.bot.wait_for('message', timeout=200)
                            try:
                                await ctx.author.send("Oki-Doki! We have everything set! The staff members will look at your ban appeal shortly.\n Thank you for your time!")
                                embed = discord.Embed(color=0x7C0A02)
                                embed.add_field(name="Ban Appeal", value=f"IGN: *{ign.clean_content}*\n Reason for ban: *{reason.clean_content}*\n Ban type: *{ban_type.clean_content}*\n Discord: *{author}*")
                                await channel.send(embed=embed)
                            except Exception:
                                return
                        if option.clean_content == 'stop':
                            await ctx.author.send("*Stopping...*")
                            await ctx.author.send("*Stopped!*")
                            return
                    finally:
                        return
                finally:
                    return
            finally:
                return
        finally:
            return
def setup(bot):
    bot.add_cog(appeal(bot))