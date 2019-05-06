from bossData import *
from timeFunc import *

enableBoss = {
       '누베르' : True,
       '무라카' : True,
       '카란다' : True,
       '벨'     : True,
       '오핀'   : True,
       '쿠툼'   : True,
       '크자카' : True,
       '가모스' : True,
       '귄트'   : True}

enableDict = enableBoss.copy()

def getImage(name):
    return img[name]

def getColor(name):
    return colors[name]

def getAlramIndex(weekday,now):
    
    index = getStartIndex(weekday,now)
    i = 0;
    if index < 0 :
        index = 0
        i = 1

    while True:
        while index < len(boss[(weekday+i)%7]):
            for bos in boss[(weekday+i)%7][index]:
                if enableBoss[bos]:
                    return [(weekday+i)%7, index];
            index = index + 1 
        i = i + 1
        index = 0
            
    return []
               
        

def getStartIndex(weekday,now) :
    for index in range(0,len(timeTable[weekday])) :
        if timeCalcTime(now) < timeTable[weekday][index] :
            return index
    return -1
        
def getAlramTime(weekday, index) :
    return timeTable[weekday][index]

def getAlramName(weekday, index):
    retList = []
    for bos in boss[weekday][index]:
        if enableBoss[bos]:
            retList.append(bos)
    return retList

def getAlramBeforeTime(weekday,index) :
    return alramTable[weekday][index]

def getAllBossNames() :
    return bossName

def getBossAllTime(name):
    retlist = []
    
    for weekday in range(0,7):
        for index in range(0,len(timeTable[weekday])-1) :
            for bossName in boss[weekday][index] :
                if name == bossName :
                    retlist.append([weekday,timeTable[weekday][index]])
    return retlist

def getValidBoss(name):
    return enableBoss[name]

def getBossNameString():
    txt = ""
    for bos in bossName:
        txt += (bos + ' ')
    return txt

def getStateString():

    txt = ""
    for bos in bossName:
        txt += (bos + ' : ')
        if enableBoss[bos]:
            txt += '활성화\n'
        else:
            txt += '비활성화\n'
    return txt


            
