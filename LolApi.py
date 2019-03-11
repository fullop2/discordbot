import Common
import json

# lol api url
lolApiGet = {'IdData' : "lol/summoner/v4/summoners/by-name/"#{summonerName}
             ,'RankData' : "/lol/league/v4/positions/by-summoner/"#{encryptedSummonerId}
             ,'ChampMastery' : "/lol/champion-mastery/v4/champion-masteries/by-summoner/"#{encryptedSummonerId}
             ,'MatchInfo' : "/lol/match/v4/matchlists/by-account/"#{encryptedAccountId}
             }

def GetIdData(data):
    idEncode = str(data.encode('UTF-8')).replace('\\x','%')
    idEncode = idEncode[2:len(idEncode)-1]
    rt = json.loads(Common.UrlRequest(lolApiGet['IdData'],idEncode))
    return rt

# print Functions
def GetRank(idData):
    rankData = json.loads(Common.UrlRequest(lolApiGet['RankData'],idData['id']))
    rt = ""
    for line in rankData:
        rt = rt + line['position'] + " : " + line['tier'] + " " + line['rank'] + " " + str(line['leaguePoints']) + '\n' \
             + "Wins : " +  str(line['wins']) + " Losses : " +  str(line['losses']) + '\n'
                                                                                       
    if len(rankData) == 0:
        rt = "이번 시즌 환자의 협곡 투쟁 성과가 없습니다"
                                                                                       
    return rt


def GetMastery(idData):
    champData = json.loads(Common.UrlRequest(lolApiGet['ChampMastery'],idData['id']))
    dataSize = 10;
    if len(champData) < 10:
        dataSize = len(champData)
    elif len(champData) > 10:
        dataSize = 10;
    rt = ""
    for i in range(dataSize):
        rt = rt + str(champData[i]['championId']) + " " + str(champData[i]['championPoints'])+"\n"
    return rt
        
def GetInfo(idData):
    infoData = json.loads(Common.UrlRequest(lolApiGet['MatchInfo'],idData['accountId']))

    rt = ""

    if len(infoData) == 0:
        rt = "중환자실에 없는 전화입니다"
    else:
        rt = infoData['matches'][0]
    return rt


