import discord
from discord.ext import commands
from classes.Player import Player

DISCORD_TOKEN = 'MTE4NzUxNTY5Njg0NzAxNTk2Ng.GSzjUL.8bkzwJA7cpK458Y1jsKFUI6M6F4d8oPRGXokNw'
intents = discord.Intents.all() 
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}')

@bot.command()
async def soloq(ctx, nameAndTag=None):

    player = Player(nameAndTag)

    try:
        winrate = player.winrate()
        elo = player.elo()
        embed=discord.Embed(title=player.name + ' #' + player.tag.upper(), description='SoloQ status', color=0xFF5733)
        embed.add_field(name="Elo", value=elo, inline=True)
        embed.add_field(name="Winrate:", value=winrate, inline=True)
        embed.add_field(name="Matches:", value=elo, inline=True)
        await ctx.send(embed=embed)
    except:
        embed=discord.Embed(title='Algum erro ocorreu. Verifique se o jogador possui Elo', color=0xFF5733)
        await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)