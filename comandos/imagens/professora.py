from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member

class professora(commands.Cog):
    """ professora do meu tempo """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def professora(self, ctx, member: discord.Member = None):
        '''teste para saber'''
        if member == None:
            member = ctx.author
        
        professora = Image.open(r"fotos/profruiva.jpg")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((326, 443))

        professora.paste(profilepic, (353,157))

        professora.save("proffruiva.jpg")

        await ctx.send( file = discord.File("proffruiva.jpg"))
    
        os.remove("proffruiva.jpg")


def setup(bot):
    bot.add_cog(professora(bot))