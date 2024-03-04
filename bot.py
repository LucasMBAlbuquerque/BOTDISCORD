from discord.ext import commands
import nest_asyncio
from decouple import config
import os
nest_asyncio.apply()

bot = commands.Bot('!')

def carregar_cogs(bot):
    bot.load_extension("comandos.respostas")
    for file in os.listdir("comandos\\coinmarketcap"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"comandos.coinmarketcap.{cog}")

carregar_cogs(bot)
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)