import requests

class RiotAPI():
  def __init__(self, apiKey):
    self.apiKey = apiKey
    self.summonerUrl = 'https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
    self.encryptedSummonerIdUrl = 'https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-puuid/'
    self.summonerStats = 'https://br1.api.riotgames.com/lol/league/v4/entries/by-summoner/'
  
  def summonerRequest(self, name, tag):
    summonerRequest = f'{self.summonerUrl}{name}/{tag}?api_key={self.apiKey}'
    return requests.get(summonerRequest).json()['puuid']

  def encryptedSummonerIdRequest(self, puuid):
    encryptedSummonerId = f'{self.encryptedSummonerIdUrl}{puuid}?api_key={self.apiKey}'
    return requests.get(encryptedSummonerId).json()['id']
  
  def playerStatus(self, encryptedSummonerId):
    summonerSts = f'{self.summonerStats}{encryptedSummonerId}?api_key={self.apiKey}'
    return requests.get(summonerSts).json()


