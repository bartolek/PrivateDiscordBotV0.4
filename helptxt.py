import discord
from discord.ext import commands

client = commands.Bot(command_prefix="$")
client.remove_command("help")

@client.command()
async def help(ctx):
    embed=discord.Embed(title="===== help ====", description="Dostępne komendy:", color=0xc41c1c)
    embed.add_field(name="Włączenie bota goomba", value="$goomba", inline=False)
    await ctx.author.send(embed=embed)