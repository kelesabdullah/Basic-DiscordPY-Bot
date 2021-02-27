import  discord
from discord.ext import commands
from datetime import datetime
import sys
sys.path.insert(0, "C:\\Users\\Keleş\\Desktop\\DESKTOP\\Verella-BOT\\admins")
import keys
class info(commands.Cog):
    def __init__(self,client):
        self.client=client

    
    @commands.command()
    async def stats(self,ctx):
        if ctx.author.id in keys.sahipler:

            embed=discord.Embed(title="Information",color=discord.Color.green())
            embed.set_author(name="Verella")
            embed.add_field(name=":hourglass: Ping",value=str(round(self.client.latency * 1000)) + ' ms')
            embed.timestamp=datetime.now()
            embed.set_thumbnail(url="https://i.hizliresim.com/ZhAg52.png")
            await ctx.send(embed=embed)
            await ctx.message.delete()
        else:
            embed=discord.Embed(title="Başarısız",description="<a:veria_x:808941361997938759> Bu komutu kullanma yetkin yok tirrek",color=discord.Color.red())
            await ctx.send(embed=embed)
            await ctx.message.delete()



def setup(client):
    client.add_cog(info(client))