import discord
from discord.ext import commands
import json
import requests
import nest_asyncio
from decouple import config
from requests import Request, Session
nest_asyncio.apply()

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'estou pronto! Estou conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
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
    if "comandos" in message.content:
        await message.channel.send(
        f' Lista de comandos \n !p MOEDA MOEDA \n Exemplo: !p BTC USD \n ou \n !p XNO BRL')
        
    await bot.process_commands(message)

@bot.command()
async def preco(ctx, coin, base):
    try:
        response = requests.get(
            f'https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}{base.upper()}')
        data = response.json()
        price = data.get('price')
        price = eval(price)
        if price:
            
            await ctx.send(f'O valor do par {coin}/{base} é {price}$')
            
        else:
            
            await ctx.send(f'O par {coin}/{base} é inválido')
            
    except Exception as error:
        
        await ctx.send('Ocorreu um erro')
        
        print(error)


@bot.command(name='oi')
async def send_hello(ctx):
    name = ctx.author.name
    
    response = 'Olá ' + name
    
    await ctx.send(response)
    
@bot.command(name='risada')
async def riso(ctx):
    
    respond = ':laughing:'
    
    await ctx.send(respond)

@bot.command(name='p')
async def p(ctx, coin, base):
    try:
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
        parameters = {
            'symbol':'{}'.format(coin),
            'convert':'{}'.format(base)
        }
        headers ={
            'Accepts':'application/json',
            'X-CMC_PRO_API_KEY':'a0928e14-2b21-4052-a29a-a3071eb9dde6'
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
        if hora > 35:
            emojih = ':rofl:'
        elif hora <= 0 and hora >= -10:
            emojih = ':cry:'
        elif hora >0 and hora <= 35:
            emojih = ':laughing:'
        elif hora <= -10:
            emojih = ':sob:'
        if dia > 35:
            emojid = ':rofl:'
        elif dia <= 0 and dia >= -10:
            emojid = ':cry:'
        elif dia >0 and dia <= 35:
            emojid = ':laughing:'
        elif dia <= -10:
            emojid = ':sob:'
        if semana > 35:
            emojis = ':rofl:'
        elif semana <= 0 and semana >= -10:
            emojis = ':cry:'
        elif semana >0 and semana <= 35:
            emojis = ':laughing:'
        elif semana <= -10:
            emojis = ':sob:'
        if price and hora and dia and semana:
            
            await ctx.send(f' O valor do par {coin}/{base} é {price}$ \n mudança na última hora = {hora}% {emojih} \n mudança nas últimas 24h = {dia}% {emojid} \n mudança na última semana = {semana}% {emojis}')
            
        else:
            
            await ctx.send(f'O par {coin}/{base} é inválido')
            
    except Exception as error:
        
        await ctx.send('Ocorreu um erro')
        
        print(error)
        
TOKEN = config("TOKEN_SECRETO")
bot.run(TOKEN)