import requests

RIOT_API_KEY = 'RGAPI-c21c1ba4-820d-48dc-b3a4-ddb8cc6a4743'

async def summonerRequest(name=None, tag=None):
  summoner = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/' + name + '/' + tag + '?api_key=' + RIOT_API_KEY
  response = requests.get(summoner)
  return response.json()['puuid']

async def encryptedSummonerIdRequest(puuid):
  encryptedSummonerId = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/' + puuid + '?api_key=' + RIOT_API_KEY
  response = requests.get(encryptedSummonerId)
  return response.json()['id']

async def playerStatus(encryptedSummonerId):
  player = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + RIOT_API_KEY
  response = requests.get(player)

  if len(response.json()) > 1:
    lst = 1
  else:
    lst = 0

  tier = response.json()[lst]['tier']
  wins = int(response.json()[lst]['wins'])
  losses = int(response.json()[lst]['losses'])

  return [tier, wins, losses]

