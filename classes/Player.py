from .RiotAPI import RiotAPI

riotRequests = RiotAPI('RGAPI-0cadcd4f-a1c3-4af1-bc93-c9a0fba9aec1')

class Player():

  def __init__(self, nameAndTag):
    splited = nameAndTag.split('#')

    self.name = splited[0] #name
    self.tag = splited[1] #tag
    self.puuid = riotRequests.summonerRequest(self.name, self.tag)
    self.encryptedSummonerId = riotRequests.encryptedSummonerIdRequest(self.puuid)
    self.summoner = riotRequests.playerStatus(self.encryptedSummonerId)

  def infos(self):
    print([self.name, self.tag, self.puuid, self.encryptedSummonerId, self.summoner])

  def elo(self):
    elo = self.summoner[0]['tier']
    rank = self.summoner[0]['rank']
    return f'{elo} {rank}'
  
  def winrate(self):
    wins = int(self.summoner[0]['wins'])
    losses = int(self.summoner[0]['losses'])
    return wins / (wins + losses) * 100


