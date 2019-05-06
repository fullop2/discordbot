from iBossData import *
from timeFunc import *

personList = {}

def registerUser(name):
    if name in personList:
        return str(name) + '에 대한 알림 정보가 이미 존재합니다'
    else:
        personList[name] = enableDict.copy()
        return str(name) + '\n'+ str(personList[name])+'에 대한 알림 정보를 생성했습니다'

def removeUser(name):
    if name in personList:
        del personList[name]
        return str(name) + '에 대한 알림 정보를 삭제했습니다'
    else:
        return str(name) + '에 대한 알림 정보가 없습니다'

def enableUserBossAlram(user,name):
    if user in personList:
        personList[user][name] = True
        return '당신의 ' + name + ' 알림을 설정했습니다'
    else:
        return '존재하지 않는 사용자입니다'

def disableUserBossAlram(user,name):
    if user in personList:
        personList[user][name] = False
        return '당신의 ' + name + ' 알림을 해제했습니다'
    else:
        return '존재하지 않는 사용자입니다'

def getMentionUser():
    
    now = getNow()
    wd = getNowWeekday()
    info = getAlramIndex(wd,now)
    
    if len(info) == 0:
        return '보스 알림 설정을 모두 꺼뒀는지 확인하십시오'

    bossName = getAlramName(info[0],info[1])
    mentionlist = []
    for user in personList:
        for bos in bossName:
            if personList[user][bos]:
               mentionlist.append(user.name)
               break
    return mentionlist

def getUserStatus(name,discord):

    if not(name in personList):
        return '존재하지 않는 사용자입니다'
        
    txt = str(name) + '\n'
    for bos in bossName:
        txt += (bos + ' : ')
        if personList[name][bos]:
            txt += '활성화\n'
        else:
            txt += '비활성화\n' 
    return txt
