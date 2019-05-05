import DoctorCmd
import discord
import asyncio
import urllib.request
import os
import time
import datetime
from datetime import timedelta

print(discord.__version__)
# discord bot token
token = 'NTU0MjA4NjgyMTI5NDg5OTUx.XM5Xpg.toENs0OM-Z-QVx4iNlCQe6XVdNo'#os.environ['BOT_TOKEN']

#discord client ref
app = discord.Client()

# initialize
@app.event
async def on_ready():
    print("Logged in")
    print(app.user.name)
    print(app.user.id)
    print("------------------")

    await app.change_presence(status=discord.Status.online,activity=discord.Game('백병원'))
    


timeTable =[
 [datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(20,0),datetime.time(23,45)],
 [datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(20,0),datetime.time(23,45)],
 [datetime.time(2,0),datetime.time(16,0),datetime.time(20,0),datetime.time(23,15),datetime.time(23,45)],
 [datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(20,0),datetime.time(23,45)],
 [datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(20,0),datetime.time(23,45),datetime.time(00,15)],
 [datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(19,0)],
 [datetime.time(00,15),datetime.time(2,0),datetime.time(11,0),datetime.time(16,0),datetime.time(17,0),datetime.time(20,0),datetime.time(23,45)]]

boss =[
 [['크자카'],['크자카','누베르'],['크자카','쿠툼'],['카란다','누베르'],['오핀']],
 [['크자카'],['크자카','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['가모스']],
 [['누베르'],['크자카','누베르'],['카란다','크자카'],['귄트','무라카'],['오핀']],
 [['쿠툼'],['크자카','누베르'],['카란다','쿠툼',],['누베르','쿠툼'],['가모스']],
 [['카란다'],['크자카','쿠툼'],['카란다','누베르'],['크자카','쿠툼'],['오핀']],
 [['카란다','누베르'],['누베르','쿠툼'],['카란다','크자카'],['귄트','무라카'],['가모스']],
 [['가모스'],['카란다','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['벨'],['누베르','쿠툼'],['카란다']]]

img = {'누베르' : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EB%88%84%EB%B2%A0%EB%A5%B4.png',
       '무라카' : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EB%AC%B4%EB%9D%BC%EC%B9%B4.png',
       '카란다' : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EC%B9%B4%EB%9E%80%EB%8B%A4.png',
       '벨'     : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EB%B2%A8.png',
       '오핀'   : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EC%98%A4%ED%95%80.png',
       '쿠툼'   : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EC%BF%A0%ED%88%BC.png',
       '크자카' : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%ED%81%AC%EC%9E%90%EC%B9%B4.png',
       '가모스' : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EA%B0%80%EB%AA%A8%EC%8A%A4.png',
       '귄트'   : 'https://raw.githubusercontent.com/fullop2/discordbot/master/pic/%EA%B7%84%ED%8A%B8.png'}

def getBossIndex(weekday,now) :
    for t in range(0,len(timeTable[weekday])) :
        if(now.time() < timeTable[weekday][t]) : 
            return t
        
def getBossTime(weekday, time) :
    return timeTable[weekday][time]

def getBossName(weekday, time) :
    return boss[weekday][time]

async def alram(message):
    now = datetime.datetime.now()
    wd = now.weekday()
    bosstime = getBossTime(wd,getBossIndex(wd,now))
    bossname = getBossName(wd,getBossIndex(wd,now))

    bosssec = bosstime.hour * 3600 + bosstime.minute * 60 + bosstime.second
    nowsec = now.time().hour * 3600 + now.time().minute * 60 + now.time().second

    for oneboss in bossname :
        emb = discord.Embed(title=str(oneboss),color=0x00ff00)
        emb.set_image(url=img[oneboss])
        await message.channel.send(embed = emb)
    emb = discord.Embed(title='보스 젠 시간', description=str(bosstime) + '\n' +str(datetime.timedelta(seconds=bosssec - nowsec)), color=0x00ff00)
    await message.channel.send(embed = emb)  
    return

flag = False

@app.event
async def on_message(message):
    global flag
    if message.author.bot or message.content == "" :
        return
    args = str(message.content).split()
    rtMsg = ""

    if args[0].startswith('-'):
        if flag == True and 'off' in args[0] :
            flag = False
            return
        if 'time' in args[0]:
            await alram(message)
        else:
            rtMsg = "알수없는 전화는 받지 않습니다.  \n-----손전화 목록-----\n" + DoctorCmd.GetDocTalk()
    else:
        rtMsg = DoctorCmd.identify(str(message.content))

    if rtMsg != "":
        await message.channel.send(rtMsg)    



app.run(token)
