import datetime
import giphy_client
import requests
import pytz
from decouple import config
import random
from giphy_client.rest import ApiException
from discord.ext import commands, tasks
from translate import Translator

class Dates(commands.Cog):
    """Work with dates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()

    @tasks.loop(seconds=1)
    async def current_time(self, tz = pytz.timezone('America/Cayenne')):


        now = datetime.datetime.now(tz)

        now = now.strftime("%H:%M:%S")

        api_giphy = config("api_giphy")
        api_instance = giphy_client.DefaultApi()
        msg = requests.get('https://animechan.vercel.app/api/random').json()
        frase = msg['quote'][0:-1]
        anime = ' Anime: ' + msg['anime']
        personagem1 = f"{msg['anime']} " + msg['character']
        personagem = " - " + msg['character']
        try:
            api_responce = api_instance.gifs_search_get(api_giphy, personagem1, limit=1, rating='r')
            lst =list(api_responce.data)
            giff = random.choice(lst)

            #await ctx.send(giff.embed_url)
            #await ctx.send('\n' + frase + personagem + '\n' + anime)

        except ApiException as e:
            print('Erro ao usar API do ghipy')

        channel = self.bot.get_channel(660320080348839948)
        if now == "04:30:00":
            translator= Translator(to_lang="pt")
            translation = translator.translate(frase)
            await channel.send("Bom dia :sunglasses:")
            await channel.send(giff.embed_url)
            await channel.send('\n' + f'"{translation}"' + personagem + '\n' + anime)


def setup(bot):
    bot.add_cog(Dates(bot))