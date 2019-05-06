from doctorMsg import *
from bossAlram import *

import discord
import asyncio
import os

print(discord.__version__)
# discord bot token
tokne = os.environ['BOT_TOKEN']

#discord client ref
app = discord.Client()

flag = False
   
# alram function
async def runAlram(message):
    global flag

    while flag:
        delay = calcAlramTime()
        await asyncio.sleep(delay[0])
        bosslist = alram(discord,message)
        await message.channel.send(embed = bosslist) 
        await asyncio.sleep(delay[1]+10)
        
# initialize
@app.event
async def on_ready():
    print("Logged in")
    print(app.user.name)
    print(app.user.id)
    print("------------------")
    await app.change_presence(status=discord.Status.online,activity=discord.Game('백병원'))

@app.event
async def on_message(message):
    global flag
    if message.author.bot or message.content == "" :
        return
    args = str(message.content).split()
    rtMsg = ""

    if args[0].startswith('-'):
        cmd = args[0][1:]
        if 'on' == cmd :
            flag = True
            await message.channel.send('타이머 작동을 시작합니다')
            await runAlram(message)
            return
        elif 'off'  == cmd  :
            flag = False
            await message.channel.send('타이머를 종료합니다')
            return
        elif 'time'  == cmd:
            if len(args) == 2 :
                    if getValidBossName(args[1]):
                        await message.channel.send(embed = getBossAllTimeFromName(discord,args[1]))
                    elif 'today' == args[1]:
                        return
                    else:
                        rtMsg = timeCmdMsg()
            else:
                bosslist = alram(discord,message)
                await message.channel.send(embed = bosslist)
        elif 'en' == cmd :
            if len(args) == 2 and getValidBossName(args[1]):
                enableBossAlram(args[1])
                await message.channel.send(args[1]+'의 알림이 설정되었습니다')
            else:
                await message.channel.send(enableErrorMsg())
        elif 'dis' == cmd :
            if len(args) == 2  and getValidBossName(args[1]):
                disableBossAlram(args[1])
                await message.channel.send(args[1]+'의 알림이 종료되었습니다')
            else:
                await message.channel.send(disableErrorMsg())        
        elif 'status' == cmd :
            await message.channel.send(embed = getBossAllState(discord))                                       
        else:
            rtMsg = allMsg()
    else:
        rtMsg = identify(str(message.content))

    if rtMsg != "":
        await message.channel.send(rtMsg)    

app.run(token)
