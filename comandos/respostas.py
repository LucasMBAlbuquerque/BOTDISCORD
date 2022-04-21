from xmlrpc import client
from discord.ext import commands
import requests
import json
class Resposta(commands.Cog):
    """ Reage às mensagens """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.content == "opa":
            msg = "OPA EAE VEI BLZ. G2AAAAA"
            await message.channel.send(msg)
            
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou pronto! Estou conectado como {self.bot.user}')

def setup(bot):
    bot.add_cog(Resposta(bot))