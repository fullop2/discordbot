from iBossData import *
from timeFunc import *

def calcAlramTime():
    now = getNow()
    wd = getNowWeekday()

    info = getAlramIndex(wd,now)

    if len(info) == 0 :
        print(info)
        return -1

    bosstime = getAlramTime(info[0],info[1])
    alramtime = getAlramBeforeTime(info[0],info[1])
    nowsec = timeCalcTime(now.time())
    if info[0] != wd:
        bosstime  =  bosstime+ (86400 * abs(info[0] - wd))
    return [bosstime-alramtime*60-nowsec,alramtime*60]

def getBossAllState(discord):
    emb = discord.Embed(title='보스 상태', description=getStateString(), color=0x0F00FF)
    return emb

def alram(discord):

    now = getNow()
    wd = getNowWeekday()
    info = getAlramIndex(wd,now)

    if len(info) == 0 :
        emb = discord.Embed(title='오류', description='잘못된 이름을 입력했거나 보스 알림 설정을 모두 꺼뒀는지 확인하십시오\n', color=0xFF0000)
    else :
        bossTime = getAlramTime(info[0],info[1])
        bossName = getAlramName(info[0],info[1])
        nowSec = timeCalcTime(now.time())

        if info[0] != wd:
            bossTime  =  bossTime + (86400 * abs(info[0] - wd))
        leftTime = ((bossTime - nowSec) - ((bossTime - nowSec) % 60) + 60)
        bossNames = ""
        for oneboss in bossName :
                bossNames += (oneboss + ' ')
        emb = discord.Embed(title=bossNames + ' 젠 시간', description=str(getTimeHM(bossTime)) + '  수술 시작 시간\n' +str(getTimeHM(leftTime)) + '분 전', color=0x0000FF)
    return emb

weekday = ['월','화','수','목','금','토','일']

def getBossAllTimeFromName(discord,name):

    if getValidBossName(name):      
        timelist = getBossAllTime(name)
        emb = discord.Embed(title=name, color=getColor(name))
        txt = ""
        for sche in timelist:
            txt += (weekday[sche[0]] + '요일 ' + str(getTimeHM(sche[1])) + '\n')
        emb.set_image(url=getImage(name))
        emb.description=txt
    else:
        emb = discord.Embed(title='설정 오류',description='잘못된 이름을 입력했거나 보스 알림 설정을 모두 꺼뒀는지 확인하십시오\n' + name, color=0xFF0000)
    return emb

def getValidBossName(name):
    for boss in bossName :
        if boss == name :
            return True
    return False

        
def enableBossAlram(name):
    enableBoss[name] = True
    return name +'의 알림이 설정되었습니다'

def disableBossAlram(name):
    enableBoss[name] = False
    return name + '의 알림이 종료되었습니다'

personList = {}
