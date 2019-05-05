from discord.ext import commands
# https://discordapp.com/oauth2/authorize/?permissions=402653227&scope=bot&client_id=574420286166794250
cogs = [
    "Cog.suggest",
    "Cog.Admin"
]
bot = commands.Bot(command_prefix=">")
bot.remove_command('help')
#loads the cogs list
if __name__ == '__main__':
    for cog in cogs:
        try:
            bot.load_extension(cog)
            print(f"loaded {cog}")
        except Exception as error:
            print(f"ERROR: {error}\n IN COG {cog}")
bot.run("NTc0NDIwMjg2MTY2Nzk0MjUw.XM80Uw.16Ibkl5dfLTn3qGw3XCzlkK2VCA")
