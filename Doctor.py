import DoctorCmd
import bossalram

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
async def runalram(message):
    global flag

    while flag:
        delay = await bossalram.calcalramtime()
        await asyncio.sleep(delay[0])
        bosslist = await bossalram.alram(discord,message)
        for emb in alram(dis,message):
            await message.channel.send(embed = emb) 
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
        if 'on' in args[0] :
            flag = True
            await runalram(message)
            return
        if 'off' in args[0] :
            flag = False
            return
        if 'time' in args[0]:
            if len(args) == 2 :
                await message.channel.send(embed = await bossalram.getbossalltime(discord,args[1]))
            else:
                bosslist = await bossalram.alram(discord,message)
                for bos in bosslist:
                    await message.channel.send(embed = bos)                
        else:
            rtMsg = "알수없는 전화는 받지 않습니다.  \n-----손전화 목록-----\n" + DoctorCmd.GetDocTalk()
    else:
        rtMsg = DoctorCmd.identify(str(message.content))

    if rtMsg != "":
        await message.channel.send(rtMsg)    

app.run(token)
