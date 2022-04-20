from discord.ext import commands
import giphy_client
import requests
from decouple import config
import random
from giphy_client.rest import ApiException

class animegif(commands.Cog):
    """ gifs e frase anime """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def anime(self, ctx):
        api = config("api_giphy")
        api_instance = giphy_client.DefaultApi()
        msg = requests.get('https://animechan.vercel.app/api/random').json()
        frase = msg['quote']
        frase = f'"{frase[0:-1]}"'
        anime = ' Anime: ' + msg['anime']
        personagem1 = f"{msg['anime']} " + msg['character']
        personagem = " - " + msg['character']
        try:
            api_responce = api_instance.gifs_search_get(api, personagem1, limit=1, rating='r')
            lst =list(api_responce.data)
            giff = random.choice(lst)

            await ctx.send(giff.embed_url)
            await ctx.send('\n' + frase + personagem + '\n' + anime)

        except ApiException as e:
            print('Erro ao usar API do ghipy')



def setup(bot):
    bot.add_cog(animegif(bot))