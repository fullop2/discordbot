import bossdata
import timefunc
import asyncio

async def calcalramtime():
    now = timefunc.getnow()
    wd = timefunc.getnowweekday()
    
    bosstime = bossdata.getBossTime(wd,bossdata.getBossIndex(wd,now))
    alramtime = bossdata.getAlramTime(wd,bossdata.getBossIndex(wd,now))
    nowsec = timefunc.timecalcTime(now.time())
    return [bosstime-alramtime*60-nowsec,alramtime*60]


async def alram(discord, message):

    retlist = []
    now = timefunc.getnow()
    wd = timefunc.getnowweekday()
    
    bosstime = bossdata.getBossTime(wd,bossdata.getBossIndex(wd,now))
    bossname = bossdata.getBossName(wd,bossdata.getBossIndex(wd,now))
    nowsec = timefunc.timecalcTime(now.time())

    for oneboss in bossname :
        emb = discord.Embed(title=str(oneboss),color=bossdata.colors[oneboss])
        emb.set_image(url=bossdata.img[oneboss])
        retlist.append(emb)
    emb = discord.Embed(title='보스 젠 시간', description=str(timefunc.gettimeHM(bosstime)) + '  수술 시작 시간\n' +str(timefunc.gettime(bosstime - nowsec)) + '  남은 시간', color=0x0000FF)
    retlist.append(emb)
    return retlist

async def getbossalltime(discord,name):

    timelist = bossdata.getBossAllTime(name)
    emb = discord.Embed(title=name, color=bossdata.colors[name])
    txt = ""
    for sche in timelist:
        txt += (bossdata.weekdayChar[sche[0]] + '요일 ' + str(timefunc.gettimeHM(sche[1])) + '\n')
    emb.set_image(url=bossdata.img[name])
    emb.description=txt

    return emb

