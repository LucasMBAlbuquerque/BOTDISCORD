from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member

class nofap(commands.Cog):
    """ foto de perfil nofap """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def nofap(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        
        fapeiro = Image.open(r"fotos\nofap.jpg")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((1080, 864))

        fapeiro.paste(profilepic, (0,211))

        fapeiro.save("nofappic.jpg")

        await ctx.send( file = discord.File("nofappic.jpg"))
    
        os.remove("nofappic.jpg")


def setup(bot):
    bot.add_cog(nofap(bot))