import discord
from discord.ext import commands
from commands.lol_requests import *

DISCORD_TOKEN = 'MTE4NzUxNTY5Njg0NzAxNTk2Ng.GSzjUL.8bkzwJA7cpK458Y1jsKFUI6M6F4d8oPRGXokNw'

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
        encryptedSummonerId = await encryptedSummonerIdRequest(summoner)
        playerSts = await playerStatus(encryptedSummonerId)

        winrate = (playerSts[1] / (playerSts[1] + playerSts[2])) * 100
        
        embed=discord.Embed(title=name + ' #' + tag.upper() +' status', description='SoloQ status', color=0xFF5733)
        embed.add_field(name="Elo:", value=playerSts[0], inline=True)
        embed.add_field(name="Winrate:", value="{:.2f}".format(winrate) + '%', inline=True)
        await ctx.send(embed=embed)

bot.run(DISCORD_TOKEN)