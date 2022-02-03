import discord
from discord.ext import commands
import random

class Randomizer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def randomizer(self, ctx, min : int, max : int):
        if min < max:
            numer = random.randrange(min, max + 1)
            await ctx.channel.send(numer)
        else:
            await ctx.channel.send("Pierwsza podana liczba musi być mniejsza od drugiej!")

    @randomizer.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.BadArgument) or isinstance(error, commands.CommandNotFound) or isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Poprawne użycie komendy to: $randomizer int int")


def setup(bot):
    bot.add_cog(Randomizer(bot))