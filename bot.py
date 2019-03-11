import discord
import asyncio
import urllib.request
import json

#discord client ref
#app = discord.Client()

# discord bot token
token = "NTU0MjA4NjgyMTI5NDg5OTUx.D2c8mA.IWloQgOx-0UNrE936N17xvM58Eo"

# lol api url
lolApiKey = "?api_key=RGAPI-e37fe8bf-60ec-4661-a787-8a00593628d3"
lolApiUrl = "https://kr.api.riotgames.com/"
lolApiGetIdData = "lol/summoner/v4/summoners/by-name/"#{summonerName}
lolApiGetRankData = "/lol/league/v4/positions/by-summoner/"#{encryptedSummonerId}
lolApiGetChampMastery = "/lol/champion-mastery/v4/champion-masteries/by-summoner/"#{encryptedSummonerId}

# request URL
def UrlRequest(type, key):
    byte_data = urllib.request.urlopen(lolApiUrl + type + key + lolApiKey).read()
    text_data = byte_data.decode('utf-8')
    return text_data

# translate Korean to Unicode
def Translation(name):
    print("unimplemented")
    
# print command
def PrintCmd():
    print("!rank")

# initialize
#@app.event
#async def on_ready():
#    print("Logged in")
#    print(app.user.name)
#    print(app.user.id)
#    print("------------------")

#    await app.change_presence(game=discord.Game(name="Hello",type=3))
    
#
#@app.event
#async
def on_message(msg):

    args = msg.split()


    if args[0].startswith('-'):
        if 'rank' in args[0]:
            try:
                idData = json.loads(UrlRequest(lolApiGetIdData,args[1]))
                print(idData['name'] + ' Level ' + str(idData['summonerLevel']))
                rankData = json.loads(UrlRequest(lolApiGetRankData,idData['id']))
                for line in rankData:
                    print(line['position'] + " : " + line['tier'] + " " + line['rank'] + " " + str(line['leaguePoints']))
                    print("Wins : " +  str(line['wins']) + " Losses : " +  str(line['losses']) + '\n')
                if len(rankData) == 0:
                    print("이번 시즌 랭크 전적(배치)가 없습니다")
                    
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print("이번 시즌 랭크 전적(배치)가 없습니다")
                else:
                    print("HTTP Error! Code " + str(e.code))
        elif 'mastery' in args[0]:
            try:  
                idData = json.loads(UrlRequest(lolApiGetIdData,args[1]))
                champData = json.loads(UrlRequest(lolApiGetChampMastery,idData['id']))
                dataSize = 10;
                if len(champData) < 10:
                    dataSize = len(champData)
                elif len(champData) > 10:
                    dataSize = 10;
                    
                for i in range(dataSize):
                    print(champData[i]+'\n')    
                    
            except urllib.error.HTTPError as e:
                if e.code == 404:
                    print("숙련도 정보가 없습니다")
                else:
                    print("HTTP Error! Code " + str(e.code))
            
        else:
            print("Undefined Command!")
    else:
         return
         
            

#app.run(token)
