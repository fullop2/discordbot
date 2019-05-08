from bossInterface import *
from timeFunc import *
from userMsg import *
from alarmModel import *

userList = {}

def string_registerUser(userName):
    if userName in userList:
        return string_userAlreadyExist(userName)
    else:
        userList[userName] = enableDict.copy()
        return string_userRegisterSuccess(userName)

def string_removeUser(userName):
    if userName in userList:
        del userList[userName]
        return string_removeUserSuccess(userName)
    else:
        return string_accessUnavailableUser()

def string_enableUserBossAlarm(userName,bossName):
    if userName in userList:
        userList[userName][bossName] = True
        return string_msgEnableUserBossAlarm(bossName)
    else:
        return string_accessUnavailableUser()

def string_disableUserBossAlarm(userName,bossName):
    if userName in userList:
        userList[userName][bossName] = False
        return string_msgDisableUserBossAlarm(bossName)
    else:
        return string_accessUnavailableUser()


def string_getUserStatus(userName):

    if not(userName in userList):
        return string_accessUnavailableUser()

    userInfo = userList[userName]
    txt = str(userName) + ' 설정 정보\n'
    for bossName in userInfo:
        txt += (bossName + ' : ')
        if userInfo[bossName]:
            txt += '활성화\n'
        else:
            txt += '비활성화\n' 
    return txt

def list_userList():
    txt = ''
    i = 0
    for userName in userList:
        txt += (userName.name + ' ')     
        i = i + 1
        if i > 3:
            i = 0
            txt += '\n'
    if txt == '':
        txt = '유저 목록이 없습니다'
    return ['유저 목록',txt]
        
