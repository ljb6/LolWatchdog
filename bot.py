import discord
from discord.ext import commands
from classes.Player import Player
import json

DISCORD_TOKEN = ''
intents = discord.Intents.all() 
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}')

@bot.command()
async def comandos(ctx):
    with open('commands/commands.json', 'r') as arquivo_json:
        dados = json.load(arquivo_json)
        embed=discord.Embed(title='Comandos', color=0xFF5733)
        embed.set_footer(text='LolWatchdog - gh: @ljb6', icon_url='https://avatars.githubusercontent.com/u/81322668?s=400&v=4')

        for command in dados['commands']:
            embed.add_field(name=command['command'], value=command['description'], inline=False)
        await ctx.send(embed=embed)
        
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
