from discord.ext import commands
from requests import Session
from decouple import config
import discord.embeds
import json
import locale

class Crypto(commands.Cog):
    """ Trabalha com preço de criptos """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def p(self, ctx, coin, base=None):
        '''Comando para preço de cryptos'''
        try:
            local = locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


            if base == 'dolar' or base == 'usd' or base == None:
                base = 'USD'
            elif base == 'real' or base == 'brl':
                base = 'BRL'
            elif base == 'euro':
                base = 'EUR'
            else:
                base = base.upper()
            coin = str(coin)

            parameters = {
                'symbol':f'{coin}',
                'convert':f'{base}'
            }
            if len(coin) == 3:
                parameters = {
                    'symbol':f'{coin.upper()}',
                    'convert':f'{base}'
                }
            else:
                parameters = {
                    'slug':f'{coin.lower()}',
                    'convert':f'{base}'
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
            rank = d['data'][idd[0]]['cmc_rank']
            nome = d['data'][idd[0]]['slug']
            if nome == 'bnb':
                nome = 'binance-coin'
            else:    
                nome = d['data'][idd[0]]['slug']
            
            simbolo = d['data'][idd[0]]['symbol'].lower()
            price = round(f['price'],1)
            hora = round(f['percent_change_1h'],1)
            dia = round(f['percent_change_24h'],1)
            semana = round(f['percent_change_7d'],1)
            #mes = round(f['percent_change_30d'],1)
            moeda = ''
            if hora > 35:
                emojih = ':rofl:'
            elif hora <= 1.5 and hora >= -1.5:
                emojih = ':neutral_face:'
            elif hora >1.5 and hora <= 35:
                emojih = ':laughing:'
            elif hora < -1.5 and hora >= -10:
                emojih = ':cry:'
            elif hora < -10 and hora >= -30:
                emojih = ':sob:'
            elif hora < -30:
                emojih = ':skull'
            if dia > 35:
                emojid = ':rofl:'
            elif dia <= 1.5 and dia >= -1.5:
                emojid = ':neutral_face:'
            elif dia >1.5 and dia <= 35:
                emojid = ':laughing:'
            elif dia <= -1.5 and dia>= -10:
                emojid = ':cry:'
            elif dia < -10 and dia >= -30:
                emojid = ':sob:'
            elif dia < -30:
                emojid = ':skull:'
            if semana > 35:
                emojis = ':rofl:'
            elif semana <= 1.5 and semana >= -1.5:
                emojis = ':neutral_face:'
            elif semana >1.5 and semana <= 35:
                emojis = ':laughing:'
            elif semana <= -1.5 and semana >= -10:
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
            if hora >= 0:
                hora = '+' + f'{hora}'
            if dia >= 0:
                dia = '+' + f'{dia}'
            if semana >= 0:
                semana = '+' + f'{semana}'
            if price and hora and dia and semana and moeda:
                embed_cmk = discord.Embed(
                    title = 'bot price',
                    url = 'https://github.com/LucasMBAlbuquerque',
                    description = f' === **O VALOR DO PAR {coin.upper()}/{base.upper()} É {locale.format_string("%.2f", price, grouping=True)} {moeda}** ===',
                    color=discord.Color.blue()
                )
                embed_cmk.add_field(name = '```MUDANÇA NA ÚTLIMA HORA```', value = f'**{hora}%** {emojih}', inline=False)
                embed_cmk.add_field(name = '```MUDANÇA NAS ÚLTIMAS 24h```', value = f'**{dia}%** {emojid}', inline=False)
                embed_cmk.add_field(name = '```MUDANÇA NA ÚLTIMA SEMANA```', value = f'**{semana}%** {emojis}', inline=False)
                embed_cmk.add_field(name = '```RANKING```', value = f'**{rank}º LUGAR EM MARKETCAP**', inline= False)
                embed_cmk.set_thumbnail(url=f'https://cryptologos.cc/logos/{nome}-{simbolo}-logo.png?')
                await ctx.send(embed=embed_cmk)
            else:
                await ctx.send(f'O par **{coin}/{base}** é inválido')        
        except Exception as error:    
            await ctx.send('Ocorreu um erro')  
            print(error)

def setup(bot):
    bot.add_cog(Crypto(bot))

#f' === O valor do par **{coin}/{base}** é **{price}** **{moeda}** === \n mudança na última hora = **{hora}%** {emojih} \n mudança nas últimas 24h = **{dia}%** {emojid} \n mudança na última semana = **{semana}%** {emojis}'