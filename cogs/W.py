import discord
from discord.ext import commands

class W(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        słownik = ['Witam']
        for word in słownik:
            if word in message.content:
                await message.add_reaction('\U00002642')

def setup(bot):
    bot.add_cog(W(bot))