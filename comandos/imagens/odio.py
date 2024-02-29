from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member

class odeia(commands.Cog):
    """ O mais odiado do pedaço """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def odio(self, ctx, member: discord.Member = None):
        '''teste para saber'''
        if member == None:
            member = ctx.author
        
        odiado = Image.open(r"fotos/odeia.jpg")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((288, 158))

        odiado.paste(profilepic, (321,63))

        odiado.save("odiadopic.jpg")

        await ctx.send( file = discord.File("odiadopic.jpg"))
    
        os.remove("odiadopic.jpg")


def setup(bot):
    bot.add_cog(odeia(bot))