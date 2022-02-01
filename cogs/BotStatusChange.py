import discord
from discord.ext import commands

class BotStatusChange(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def play(self, ctx, gamename):
        await self.bot.change_presence(activity=discord.Game(name=gamename))

    @commands.command()
    async def listen(self, ctx, songname):
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=songname))

def setup(bot):
    bot.add_cog(BotStatusChange(bot))