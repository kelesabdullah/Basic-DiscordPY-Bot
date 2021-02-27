import discord
from discord.ext import commands


class kullanıcı(commands.Cog):
    def __init__(self,client):
        self.client=client
    @commands.command()
    async def kullanıcı(self,ctx,member:discord.Member):
            myembed = discord.Embed(title=member.name,color=discord.Color.red())
            myembed.add_field(name="Durum",value=member.status,inline=False)
            myembed.add_field(name="Rol",value=member.top_role,inline=False)
            myembed.add_field(name="ID",value=member.id,inline=False)
            myembed.add_field(name="Oluşturulma Tarihi",value=member.created_at,inline=False)
            myembed.add_field(name="Katılma Tarihi",value=member.joined_at,inline=False)
            myembed.set_thumbnail(url=member.avatar_url)
            myembed.set_image(url="https://cdn.discordapp.com/avatars/795736563174604820/6b504b3e45200810d7d102062bedd1bc.webp?size=1024")
            await ctx.send(embed=myembed)
            await ctx.message.delete()


def setup(client):
    client.add_cog(kullanıcı(client))