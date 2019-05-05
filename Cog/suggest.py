import discord
from discord.ext import commands
import random
class suggest(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def suggest(self, ctx, *, suggestion : str = None):
        # I **know** you wanted to suggest something, what is it?
        if suggestion == None:
            '''see if we are suggesting... nothing?'''''
            NothingArray = [
                "Please input something to suggest!",
                "You cant leave your suggestion empty!",
            ]
            await ctx.send(random.choice(NothingArray))
            return
        channel = ctx.guild.get_channel(574424471163895829) # CHANGE IF CHANNEL WAS DELETED
        author = ctx.message.author
        embed = discord.Embed(color=0x005DF5)
        user_pf = author.avatar_url
        embed.set_thumbnail(url=user_pf)
        embed.add_field(name=f"**{author}** has a suggestion! Here is what they wanted: ", value=f"{suggestion.capitalize()}")
        msg = await channel.send(embed=embed)
        await msg.add_reaction("✅")
        await msg.add_reaction("❌")
        await ctx.send("Suggestion added!")
# adds cog
def setup(bot):
    bot.add_cog(suggest(bot))