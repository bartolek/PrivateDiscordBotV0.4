import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="$")
bot.remove_command("help")

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="HELME", description="Dostępne komendy:", color=0xca2b2b)
    embed.add_field(name="$goomba {Argument}", value="Argumenty: status/ON/OFF", inline=False)
    embed.add_field(name="$play {Nazwa}", value="Zmiana statusu bota, W grze:", inline=True)
    embed.add_field(name="$listen {Nazwa}", value="Zmiana statusu bota, Słucha:", inline=True)
    embed.add_field(name="$randomizer {Arg} {Arg}", value="Losuje liczbę z przedziału ", inline=False)
    embed.add_field(name="$kanyenadzis", value="Cytate Kanye na dzis", inline=False)
    await ctx.author.send(embed=embed)