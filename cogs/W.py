import discord
from discord.ext import commands

currentStatus = {'937667379159248946': 'OFF'
    }

class W(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        słownik = ['Wilusz', 'wilusz', 'Wilusza', "wilusza"]
        for word in słownik:
            if word in message.content:
                await message.add_reaction('\U00002642')

def setup(bot):
    bot.add_cog(W(bot))