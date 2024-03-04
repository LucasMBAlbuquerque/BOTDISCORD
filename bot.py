from discord.ext import commands
import nest_asyncio
from decouple import config
import os
nest_asyncio.apply()
#
bot = commands.Bot('!')
#
#bot.load_extension("comandos.coinmarketcap.cryptocmk")
#bot.load_extension("comandos.Imagens.procurado")
#bot.load_extension("comandos.Imagens.nofap")
#bot.load_extension("comandos.Imagens.gremio")
#bot.load_extension("comandos.Imagens.professora")
#bot.load_extension("comandos.Imagens.npc")
#bot.load_extension("comandos.Imagens.odio")
##bot.load_extension("comandos.Animes.gif_anime")
#bot.load_extension("comandos.Imagens.memerandom")
#bot.load_extension("comandos.MensagemDiaria.msg_diaria")
#bot.load_extension("comandos.fazedor_de_pdf.pdf_maker")
#bot.load_extension("comandos.FrasesAnime.FraseAnime")

def carregar_cogs(bot):
    bot.load_extension("comandos.respostas")
    for file in os.listdir("comandos\\coinmarketcap"):
        if file.endswith(".py"):
            cog = file[:-3]
            bot.load_extension(f"comandos.coinmarketcap.{cog}")

carregar_cogs(bot)
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)