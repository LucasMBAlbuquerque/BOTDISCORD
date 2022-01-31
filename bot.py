from discord.ext import commands
import nest_asyncio
from decouple import config

nest_asyncio.apply()

bot = commands.Bot('!')

bot.load_extension("comandos.cryptocmk")
bot.load_extension("comandos.respostas")

TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)