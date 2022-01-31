from discord.ext import commands

class Resposta(commands.Cog):
    """ Reage às mensagens """
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        if "chinelo" in message.content:
            await message.channel.send(
            f'CADE O CHINELOOOOOO :scream: :loudspeaker: :thong_sandal:')
        if "compensou" in message.content:
            await message.channel.send(
            f'UAI COMPENSÔ EM MIGÃO :eyeglasses:')
        if "mina" in message.content:
            await message.channel.send(
            f'ESSA AI EU JÁ PEGUEI :relieved:')
            
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'estou pronto! Estou conectado como {self.bot.user}')

def setup(bot):
    bot.add_cog(Resposta(bot))