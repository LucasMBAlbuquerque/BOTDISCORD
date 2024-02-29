from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member
import random
import ast

class memerandom(commands.Cog):
    """ foto de perfil nofap """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def random(self, ctx, member: discord.Member = None):
        '''meme aleatorio'''
        if member == None:
            member = ctx.author
        
        with open(r'dict/sizes.txt') as f:
            data = f.read()
        
        js = ast.literal_eval(data)

        valor = random.randint(0,4)

        meme = list(js.keys())[valor]
        dimensoes = js[f'meme{valor}']

        foto = Image.open(fr"fotos/meme{valor}.jpg")

        asset = member.avatar_url_as(size = 128)
        data1 = BytesIO(await asset.read())
        profilepic = Image.open(data1)

        profilepic = profilepic.resize((dimensoes[0][0], dimensoes[0][1]))

        foto.paste(profilepic, (dimensoes[1][0],dimensoes[1][1]))

        foto.save("fotorandom.jpg")

        await ctx.send( file = discord.File("fotorandom.jpg"))
    
        os.remove("fotorandom.jpg")


def setup(bot):
    bot.add_cog(memerandom(bot))