import discord
from discord.ext import commands 

client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
    print("Bot uruchomił się poprawnie.")

client.remove_command("help")

@client.command()
async def help(ctx):
    await ctx.channel.send("test")

client.run("OTM3MDg4NTQ5NDQ1MDYyNzQ3.YfWpuA.87Lo-nPE0dKYyTGN7S6V4W58YU0")