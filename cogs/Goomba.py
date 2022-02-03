import discord
from discord.ext import commands

currentStatus = {'937667379159248946': 'OFF'
    }

class Goomba(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def goomba(self, ctx, input : str):
        global currentStatus
        channel_id = ctx.message.guild.id
        if input == "status":
            if str(channel_id) in currentStatus:
                await ctx.channel.send(f"Aktualny status goomby na tym serwerze to: {currentStatus.get(str(channel_id))}")
            else:
                currentStatus[str(channel_id)] = 'OFF'
                await ctx.channel.send(f"Aktualny status goomby na tym serwerze to: {currentStatus.get(str(channel_id))}")
        elif input == "ON" or input == "OFF":
            currentStatus[str(channel_id)] = input
            await ctx.channel.send(f"Zmieniłeś status goomby na tym serwerze na: {currentStatus.get(str(channel_id))}")
        else:
            await ctx.channel.send("Poprawne użycie komendy to: $goomba status/ON/OFF")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.attachments:
            if currentStatus.get(str(message.guild.id)) == "ON":
                await message.add_reaction('\U0001F1E6')
                await message.add_reaction('\U0001F1E7')
                await message.add_reaction('\U0001F1E8')
                await message.add_reaction('\U0001F1E9')

    @goomba.error
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("W komendzie brakuje argumentu")

def setup(bot):
    bot.add_cog(Goomba(bot))