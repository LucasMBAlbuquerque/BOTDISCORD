import asyncio
import zipfile
import os
from PIL import Image
#from os import system
from discord.ext import commands
import discord

class Baixar(commands.Cog):
    '''Transforma fotos em pdf'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def pdf(self, ctx):
        #files = []
        for attachment in ctx.message.attachments:
            # fp = BytesIO()
            await attachment.save(fr'arquivos/{attachment.filename}')
    
    #@commands.command()
    #async def pdfdm(self, ctx):
    #    await ctx.author.send("Envie seu pdf Aqui")
    
    @commands.command()
    async def dm_command(self, ctx):
        '''transforma fotos em zip em pdf'''
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.author.send("testando")
            def check(m):
                arquivo = ctx.message.attachments
                return m.channel == ctx.channel and bool(m.attachments)

            
            try:
                msg = await self.bot.wait_for('message', check=check)
                msg = msg.attachments[0]
                await msg.save(fr'arquivos/{msg.filename}')

                with zipfile.ZipFile(fr'arquivos/{msg.filename}', 'r') as zip_ref:
                    zip_ref.extractall(fr'arquivos/unzipeds')
                
                initial_count = 1
                dir = 'arquivos/unzipeds'

                for path in os.listdir(dir):
                    if os.path.isfile(os.path.join(dir, path)):
                        initial_count += 1

                lst = list(range(initial_count))[1:initial_count]
                lst = [fr'arquivos/unzipeds/{str(x)}.jpg' for x in lst]

                images = [
                    Image.open(f) for f in lst
                ]

                pdf_path = "seu_pdf.pdf"

                images[0].save(
                    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
                    )

                await ctx.send( file = discord.File("seu_pdf.pdf"))

                os.remove(fr"arquivos/{msg.filename}")
                for fotos in lst:
                    os.remove(fr"{fotos}")
                os.remove("seu_pdf.pdf")
                #await ctx.author.send(msg)
                #Note: This waits for all types of files, json, py, jpg, png... 
                # If you want only specific types of files you can do it with message.attachments[0].filename.endswith('extension_here')

            except asyncio.exceptions.TimeoutError:
                # usuário não responder em 1 minuto
                pass

def setup(bot):
    bot.add_cog(Baixar(bot))