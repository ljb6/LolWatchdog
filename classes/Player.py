from .RiotAPI import RiotAPI

riot_requests = RiotAPI('RGAPI-0cadcd4f-a1c3-4af1-bc93-c9a0fba9aec1')

class Player():
  
  riot_requests = RiotAPI('RGAPI-0cadcd4f-a1c3-4af1-bc93-c9a0fba9aec1')

  def __init__(self, nameAndTag):
    splited = nameAndTag.split('#')

    self.name = splited[0] #name
    self.tag = splited[1] #tag
    self.puuid = riot_requests.summoner_request(self.name, self.tag)
    self.encryptedSummonerId = riot_requests.encryptedSummonerId_request(self.puuid)
    self.summoner = riot_requests.playerStatus(self.encryptedSummonerId)

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

lucca = Player('bckrz#pjl')
lucca.elo()

