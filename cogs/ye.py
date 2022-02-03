import discord
from discord.ext import commands
import requests

class ye(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def yenadzis(self, ctx):
        response = requests.get("https://api.kanye.rest")
        api = response.json()
        await ctx.send(api.get('quote'))

def setup(bot):
    bot.add_cog(ye(bot))