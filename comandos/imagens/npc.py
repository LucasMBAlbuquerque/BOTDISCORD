from io import BytesIO
from discord.ext import commands
from PIL import Image
import os
import discord.member

class npc(commands.Cog):
    """ quando você vira um npc """

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def npc(self, ctx, member: discord.Member = None):
        '''teste para saber'''
        if member == None:
            member = ctx.author
        
        npceiro = Image.open(r"fotos/npc.jpg")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        profilepic = Image.open(data)

        profilepic = profilepic.resize((228, 215))

        npceiro.paste(profilepic, (10,76))

        npceiro.save("npcpic.jpg")

        await ctx.send( file = discord.File("npcpic.jpg"))
    
        os.remove("npcpic.jpg")


def setup(bot):
    bot.add_cog(npc(bot))