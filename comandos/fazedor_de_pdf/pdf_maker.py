import asyncio
import zipfile
import os
from PIL import Image
from discord.ext import commands
import discord

class Baixar(commands.Cog):
    '''Transforma fotos em pdf'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def pdf(self, ctx):
        '''transforma fotos em pdf (Este comando só funciona no chat privado do bot)'''
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.author.send(
                "Caso for enviar as imagens dentro de um arquivo .zip, deixe-as em ordem alfabética \n"
                "No caso de enviar as imagens separadamente, sem estarem em um arquivo .zip, envie todas na mesma mensagem. "
                "Para que as imagens fiquem na ordem certa no discord, também precisam estar em ordem alfabética."
                "A vantagem de enviar o as imagens dentro de um .zip é que podem ser usadas ilimitadas imagens, diferente de enviá-las separadamente,"
                "pois o discord só suporta enviar 10 arquivos na mesma mensagem.")
            await ctx.author.send("Envie seus arquivos dentro de 1 minuto")
            def check(m):
                arquivo = ctx.message.attachments
                return m.channel == ctx.channel and bool(m.attachments)

            
            try:
                msg = await self.bot.wait_for('message', check=check)
                if msg.attachments[0].filename[-4:] == '.zip':
                    msg = msg.attachments[0]
                    #msg = list(msg.attachments)
                    await msg.save(fr'arquivos/{msg.filename}')

                    with zipfile.ZipFile(fr'arquivos/{msg.filename}', 'r') as zip_ref:
                        zip_ref.extractall(fr'arquivos/unzipeds')
                
                    initial_count = 1
                    dir = 'arquivos/unzipeds'

                    for path in os.listdir(dir):

                        if os.path.isfile(os.path.join(dir, path)):
                            initial_count += 1

                    lst = list(range(initial_count))[1:initial_count]
                    lista = []
                    for root, dirs, files in os.walk(r"arquivos/unzipeds"):
                        for filename in files:
                            lista.append(filename)

                    nome_novo = 1
                    for arquive in lista:
                        os.rename(fr'arquivos/unzipeds/{arquive}',fr'arquivos/unzipeds/{str(nome_novo)}.jpg')
                        nome_novo +=1

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
                elif msg.attachments[0].filename[-4:] == '.jpg':
                    for arquivos in msg.attachments:
                        await arquivos.save(fr'arquivos\unzipeds\{arquivos.filename}')
                    initial_count = 1
                    dir = r'arquivos\unzipeds'

                    for path in os.listdir(dir):

                        if os.path.isfile(os.path.join(dir, path)):
                            initial_count += 1

                    lst = list(range(initial_count))[1:initial_count]
                    lista = []
                    for root, dirs, files in os.walk(r"arquivos\unzipeds"):
                        for filename in files:
                            lista.append(filename)

                    nome_novo = 1
                    for arquive in lista:
                        os.rename(fr'arquivos\unzipeds\{arquive}',fr'arquivos\unzipeds\{str(nome_novo)}.jpg')
                        nome_novo +=1

                    lst = [fr'arquivos\unzipeds\{str(x)}.jpg' for x in lst]

                    images = [
                        Image.open(f) for f in lst
                    ]

                    pdf_path = "seu_pdf.pdf"

                    images[0].save(
                        pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
                        )

                    await ctx.send( file = discord.File("seu_pdf.pdf"))

                    for fotos in lst:
                        os.remove(fr"{fotos}")
                    os.remove("seu_pdf.pdf")                    


            except asyncio.exceptions.TimeoutError:
                # usuário não responder em 1 minuto
                pass

def setup(bot):
    bot.add_cog(Baixar(bot))