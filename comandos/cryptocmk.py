from discord.ext import commands
from requests import Session
from decouple import config
import json

class Crypto(commands.Cog):
    """ Trabalha com preço de criptos """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def p(self, ctx, coin, base):
        try:
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            if coin == coin.upper():
                parameters = {
                    'symbol':'{}'.format(coin),
                    'convert':'{}'.format(base.upper())
                }
            else:
                parameters = {
                    'slug':'{}'.format(coin),
                    'convert':'{}'.format(base.upper())
                }
            
            TOKENCMK = config("X-CMC_PRO_API_KEY")
            headers ={
                'Accepts':'application/json',
                'X-CMC_PRO_API_KEY':TOKENCMK
            }
            session = Session()
            session.headers.update(headers)
            response = session.get(url, params=parameters)
            d = json.loads(response.text)
            idd = list(d['data'])
            f = d['data'][idd[0]]['quote']['{}'.format(base)]
            price = round(f['price'],3)
            hora = round(f['percent_change_1h'],3)
            dia = round(f['percent_change_24h'],3)
            semana = round(f['percent_change_7d'],3)
            moeda = ''
            if hora > 35:
                emojih = ':rofl:'
            elif hora <= 1 and hora >= -1:
                emojih = ':neutral_face:'
            elif hora >1 and hora <= 35:
                emojih = ':laughing:'
            elif hora < -1 and hora >= -10:
                emojih = ':cry:'
            elif hora < -10 and hora >= -30:
                emojih = ':sob:'
            elif hora < -30:
                emojih = ':skull'
            if dia > 35:
                emojid = ':rofl:'
            elif dia <= 1 and dia >= -1:
                emojid = ':neutral_face:'
            elif dia >1 and dia <= 35:
                emojid = ':laughing:'
            elif dia <= -1 and dia>= -10:
                emojid = ':cry:'
            elif dia < -10 and dia >= -30:
                emojid = ':sob:'
            elif dia < -30:
                emojid = ':skull:'
            if semana > 35:
                emojis = ':rofl:'
            elif semana <= 1 and semana >= -1:
                emojis = ':neutral_face:'
            elif semana >1 and semana <= 35:
                emojis = ':laughing:'
            elif semana <= -1 and semana >= -10:
                emojis = ':cry:'
            elif semana < -10 and semana >= -30:
                emojis = ':sob:'
            elif semana < -30:
                emojis = ':skull:'
            if parameters['convert'] == 'BRL':
                moeda = 'R$'
            elif parameters['convert'] == 'USD':
                moeda = '$'
            if parameters['convert'] != 'BRL' and parameters['convert'] != 'USD':
                moeda = base
            if price and hora and dia and semana and moeda:
                await ctx.send(f' === O valor do par {coin}/{base} é **{price}** **{moeda}** === \n mudança na última hora = {hora}% {emojih} \n mudança nas últimas 24h = {dia}% {emojid} \n mudança na última semana = {semana}% {emojis}')
            else:
                await ctx.send(f'O par {coin}/{base} é inválido')        
        except Exception as error:    
            await ctx.send('Ocorreu um erro')  
            print(error)

def setup(bot):
    bot.add_cog(Crypto(bot))