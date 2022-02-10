from discord.ext import commands
import nest_asyncio
from decouple import config

nest_asyncio.apply()

bot = commands.Bot('!')

bot.load_extension("comandos.coinmarketcap.cryptocmk")
bot.load_extension("comandos.respostas")
bot.load_extension("comandos.imagens.procurado")
bot.load_extension("comandos.imagens.nofap")
bot.load_extension("comandos.imagens.gremio")
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)