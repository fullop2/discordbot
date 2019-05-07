from bossModel import *
from alarmModel import *
from timeFunc import *

def string_getBossImage(bossName):
    return bossImage[bossName]

def hex_getBossColor(bossName):
    return bossColor[bossName]

def list_getBossColors():
    return bossColor

def bool_getValidBoss(bossName):
    return enableBossList[bossName]

def second_getAlarmTime(weekday, index) :
    return timeTable[weekday][index]

def second_getAlarmBeforeTime(weekday,index) :
    return alarmTable[weekday][index]*60

def list_getAllBossNames() :
    return bossNameList

def list_getBossListWeekday(weekday):
    return bossTable[weekday]

def list_getBossListDay(weekday,index):
    return bossTable[weekday][index]

def size_getTableLengthOnWeekday(weekday):
    return len(bossTable[weekday])
