from doctorMsg import *
from bossAlram import *
from userFunc import *

import discord
import asyncio
import os

print(discord.__version__)
# discord bot token
token = os.environ['BOT_TOKEN']

#discord client ref
app = discord.Client()

flag = False
   
# alram function
async def runAlram(message):
    global flag

    while flag:
        delay = calcAlramTime()
        await asyncio.sleep(delay[0])
        userlist = getMentionUser()
        print(userlist)
        if len(userlist) > 0:
            await message.channel.send(str(userlist))
            bosslist = alram(discord)
            await message.channel.send(embed = bosslist)
            print('out sleep')
        await asyncio.sleep(delay[1]+1)
        
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
                bosslist = alram(discord)
                await message.channel.send(embed = bosslist)
        elif 'en' == cmd :
            if len(args) == 2 and getValidBossName(args[1]):
                rtMsg = enableBossAlram(args[1])
            else:
                rtMsg = enableErrorMsg()
        elif 'dis' == cmd :
            if len(args) == 2  and getValidBossName(args[1]):
                rtMsg = disableBossAlram(args[1])
            else:
                rtMsg = disableErrorMsg()
                
        elif 'enur' == cmd :
            if len(args) == 2 and getValidBossName(args[1]):
                rtMsg = enableUserBossAlram(message.author,args[1])
            else:
                await message.channel.send(enableCmdMsg())
        elif 'disur' == cmd :
            if len(args) == 2  and getValidBossName(args[1]):
                rtMsg = disableUserBossAlram(message.author,args[1])
            else:
                await message.channel.send(disableCmdMsg())
        elif 'statur' == cmd :
            rtMsg = getUserStatus(message.author,discord)                
        elif 'reg' == cmd :
            rtMsg = registerUser(message.author)
        elif 'rm' == cmd :
            rtMsg = removeUser(message.author)              
        elif 'status' == cmd :
            await message.channel.send(embed = getBossAllState(discord))                                       
        else:
            rtMsg = allMsg()
    else:
        rtMsg = identify(str(message.content))

    if rtMsg != "":
        await message.channel.send(rtMsg)    

app.run(token)
