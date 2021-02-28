import discord
from discord.ext import commands

class komutlar(commands.Cog):
    def __init__(self,client):
        self.client=client



    @commands.command()
    async def komutlar(self,ctx):
        embed = discord.Embed(title="Komut Listesi")
        
        embed.add_field(name="Avatar",value=":white_circle: !avatar <kullanıcı> komutu ile kullanıcıların avatarlarının büyütülmüş halini görebilirsinz.")
        embed.add_field(name="Döviz",value=":white_circle: Bazı döviz kurları ve kripto paraların güncel değerlerini gösterir. Komutu => '!döviz'")
        embed.add_field(name="Kullanıcı Bilgi",value=":white_circle: '!kullanıcı' komutu etiketlediğiniz kişinin bilgilerini yazdırır")
        embed.add_field(name="Sustur",value=":white_circle: Etiketlediğiniz kişi metin kanallarına mesaj gönderemez. Komutu => '!sustur'")
        embed.add_field(name="Mesaj Silme",value=":white_circle: '!sil <mesaj miktarı>' yazarak sohbeti temizleyebilirsiniz")


        await ctx.send(embed=embed)
        await ctx.message.delete()



def setup(client):
    client.add_cog(komutlar(client))