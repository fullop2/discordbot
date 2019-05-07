from doctorMsg import *
from bossAlarmFunc import *
from userFunc import *

import discord
import asyncio
import os

print(discord.__version__)
# discord bot token
token = 'NTU0MjA4NjgyMTI5NDg5OTUx.D2c8mA.IWloQgOx-0UNrE936N17xvM58Eo'#os.environ['BOT_TOKEN']

#discord client ref
app = discord.Client()

flag = False
   
# alram function
async def runAlram(message):
    global flag

    while flag:
        value = list_alramBossWeekdayIndex()
        await asyncio.sleep(value[0])
        userlist = list_getMentionUser()
        if len(userlist) > 0:
            menUser = ''
            for user in userlist:
                menUser += '<@'+str(user.id)+'> '
            await message.channel.send(menUser)
            embed = makeEmbed(str(value[1]) + '알림',\
                              string_fromHM(value[2]) + ' 수술 시작 시간\n' + \
                              string_fromHM(value[3]) +  ' 남았습니다',None,value[4])
            await message.channel.send(embed = embed)
        await asyncio.sleep(value[3]+1)
        
# initialize
@app.event
async def on_ready():
    print("Logged in")
    print(app.user.name)
    print(app.user.id)
    print("------------------")
    await app.change_presence(status=discord.Status.online,activity=discord.Game('백병원'))

def makeEmbed(title,desc,img,color):
    embed = discord.Embed(title=title,description=desc,color=color)
    if img != None:
        embed.setImage(url = img)
    return embed 

def checkPermission(member):
 
    for role in member.roles:
        if role.permissions.value == 104324681:
            return True
    return False
        
@app.event
async def on_message(message):
    global flag
    if message.author.bot or message.content == '' :
        return
    args = str(message.content).split()
    rtMsg = makeEmbed('수술실','',None,0x1010FF)
    
    if args[0].startswith('-'):
        cmd = args[0][1:]
        
        # administrator command
        # 알림 시작
        if 'on' == cmd and checkPermission(message.author):
            flag = True
            rtMsg.description = string_onTimer()
            await message.channel.send(embed = rtMsg)
            await runAlram(message)    
            return
        # 알림 종료
        elif 'off'  == cmd and checkPermission(message.author) :
            flag = False
            rtMsg.description = string_offTimer()
        # 특정 보스 전체 활성화
        elif 'enall' == cmd and checkPermission(message.author):
            if len(args) == 2 and bool_validBossName(args[1]):
                rtMsg.description = string_enableBossAlram(args[1])
            else:
                rtMsg.description = cmdListMsg
        # 특정 보스 전체 비활성화
        elif 'disall' == cmd and checkPermission(message.author) \
              and len(args) == 2  and bool_validBossName(args[1]):
            if len(args) == 2  and bool_validBossName(args[1]):
                rtMsg.description = string_disableBossAlram(args[1])
            else:
                rtMsg.description = cmdListMsg

        # basic user command
        # 다음 보스 시간
        elif 'time'  == cmd:
            if len(args) == 2 :
                if bool_validBossName(args[1]):
                    value = list_bossAllTimeFromName(discord,args[1])
                    rtMsg.title = str(value[1]) + '알림'
                    rtMsg.description = value[2]
                    rtMsg.image = value[3]
                    rtMsg.color = value[4]
                elif 'today' == args[1]:
                    return
                else:
                    rtMsg.description = cmdListMsg
            else:
                value = list_alramBossWeekdayIndex()
                rtMsg.title = str(value[1]) + '알림'
                rtMsg.description =     string_fromHM(value[2]) + ' 수술 시작 시간\n' + \
                                        string_fromHM(value[0]+value[3]) +  ' 남았습니다'
                rtMsg.color = value[4]
        # 개인 보스 알림 활성화
        elif 'en' == cmd :
            if len(args) == 2 and bool_validBossName(args[1]):
                rtMsg.description = string_enableUserBossAlarm(message.author,args[1])
            else:
                rtMsg.description = cmdListMsg
        # 개인 보스 알림 비활성화       
        elif 'dis' == cmd :
            if len(args) == 2  and bool_validBossName(args[1]):
                rtMsg.description = string_disableUserBossAlarm(message.author,args[1])
            else:
                rtMsg.description = cmdListMsg
        # 개인 보스 알림 설정 확인        
        elif 'stat' == cmd :
            rtMsg.description = string_getUserStatus(message.author,discord)
        # 개인 정보 등록
        elif 'reg' == cmd :
            rtMsg.description = string_registerUser(message.author)
        # 개인 정보 삭제
        elif 'rm' == cmd :
            rtMsg.description = string_removeUser(message.author)
        # 전체 보스 설정 확인
        elif 'statall' == cmd :
            rtMsg.description = getBossAllState()
        # 명령어 목록 출력
        else:
            rtMsg.description = string_all()
    else:
        rtMsg.description = identify(str(message.content))
    if rtMsg.description != '':
        await message.channel.send(embed = rtMsg)    

app.run(token)
