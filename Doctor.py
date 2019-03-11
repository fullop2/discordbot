import LolApi
import DoctorCmd
import discord
import asyncio
import urllib.request
import os

# discord bot token
token = os.environ('BOT_TOKEN")

#discord client ref
app = discord.Client()

# initialize
@app.event
async def on_ready():
    print("Logged in")
    print(app.user.name)
    print(app.user.id)
    print("------------------")

    await app.change_presence(game=discord.Game(name="백병원",type=3))
    



@app.event
async def on_message(message):
    if message.author.bot:
        return
    args = str(message.content).split()
    rtMsg = ""
    if args[0].startswith('-'):
        try:
            if len(args) == 1:
                rtMsg = "알수없는 전화는 받지 않습니다.  \n-----손전화 목록-----\n" + DoctorCmd.GetCmd()
            else:               
                idData = LolApi.GetIdData(args[1])
                rtMsg = str(idData['name']) + ' Level ' + str(idData['summonerLevel']) + '\n'
                
                if 'rank' in args[0]:
                    rtMsg += LolApi.GetRank(idData)
                elif 'mastery' in args[0]:
                    rtMsg += LolApi.GetMastery(idData)
                elif 'info' in args[0]:
                    rtMsg += (str(LolApi.GetRank(idData)) + '\n')
                    rtMsg += str(LolApi.GetInfo(idData))
                elif 'cmd' in args[0]:
                    rtMsg = "\n-----손전화 목록-----\n" + DoctorCmd.GetCmd()
                else:
                    rtMsg = "알수없는 전화는 받지 않습니다.  \n-----손전화 목록-----\n" + DoctorCmd.GetCmd()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                rtMsg = "해당 환자는 중환자실에 존재하지 않습니다"
            else:
                rtMsg = "HTTP Error! Code " + str(e.code)
    else:
        rtMsg = DoctorCmd.identify(str(message.content))

    if rtMsg != "":
        await app.send_message(message.channel,rtMsg)    

app.run(token)
