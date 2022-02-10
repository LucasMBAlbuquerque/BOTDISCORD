from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member
import random

class gremio(commands.Cog):
    """ fotos meme gremio """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gremio(self, ctx):
        await ctx.send( file = discord.File(r'fotos\gremio'f'{random.randint(1,13)}.jpg'))

def setup(bot):
    bot.add_cog(gremio(bot))