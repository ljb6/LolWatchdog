import requests

class RiotAPI():
  def __init__(self, api_key):
    self.api_key = api_key
    self.summoner_url = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
    self.encryptedSummonerId_url = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'
    self.summoner_stats = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
  
  def summoner_request(self, name, tag):
    summoner_request = f'{self.summoner_url}{name}/{tag}?api_key={self.api_key}'
    return requests.get(summoner_request).json()['puuid']

  def encryptedSummonerId_request(self, puuid):
    encryptedSummonerId = f'{self.encryptedSummonerId_url}{puuid}?api_key={self.api_key}'
    return requests.get(encryptedSummonerId).json()['id']
  
  def playerStatus(self, encryptedSummonerId):
    summoner_sts = f'{self.summoner_stats}{encryptedSummonerId}?api_key={self.api_key}'
    return requests.get(summoner_sts).json()


