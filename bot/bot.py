import discord
from discord.ext import commands


from commands.lol_requests import *

DISCORD_TOKEN = 'MTE4NzUxNTY5Njg0NzAxNTk2Ng.GSzjUL.8bkzwJA7cpK458Y1jsKFUI6M6F4d8oPRGXokNw'
RIOT_API_KEY = 'RGAPI-532e655a-680e-440e-a0b2-0e456da5c152'

intents = discord.Intents.all() 

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot está online como {bot.user.name}')

@bot.command()
async def player(ctx, name=None, tag=None):
    if name is None or tag is None:
        await ctx.send('Use /playerStatus \{gameName} \{tag}')
    else:
        summoner = await summonerRequest(name, tag)
        await ctx.send(summoner)
        encryptedSummonerId = await encryptedSummonerIdRequest(summoner)
        await ctx.send(encryptedSummonerId)
        playerSts = await playerStatus(encryptedSummonerId)
        await ctx.send(playerSts)
        #await ctx.send('Status de:', name, '\n', 'Rank:', player['rank'], '\n', 'Wins:', player['wins'], '\n', 'Losses:', player['losses'])
        
bot.run(DISCORD_TOKEN)