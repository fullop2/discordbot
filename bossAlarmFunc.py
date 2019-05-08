from bossInterface import *
from userFunc import *
from timeFunc import *
from alarmModel import *

# 다음 보스 정보 검색
def list_alramBossWeekdayIndex():

    timer = list_getAlarmIndex()
    bossTime = second_getAlarmTime(timer[0],timer[1])
    alarmTime = second_getAlarmBeforeTime(timer[0],timer[1])
    nowTime = second_calcSecondFromDateTime(datetime_now())

    deltaTime = bossTime - alarmTime - nowTime
    if timer[0] != int_nowWeekday():
        deltaTime += (86400 * abs(timer[0] - int_nowWeekday()))
    
    bossNames = ''
    for bossName in list_getBossListDay(timer[0],timer[1]) :
        bossNames += (bossName + ' ')

    mixColor = 0xFFFFFF
    for color in list_getBossColors():
        mixColor = mixColor & hex_getBossColor(color)
        
    return [deltaTime,bossNames,bossTime,alarmTime,mixColor]

# 지정된 시간의 보스 정보
def list_getAlarmBossName(weekday, index):
    retList = []
    for bossName in list_getBossListDay(weekday,index):
        if bool_getValidBoss(bossName):
            retList.append(bossName)
    return retList


# 모든 보스 이름
def string_getBossName():
    txt = ""
    for bossName in list_getAllBossNames():
        txt += (bossName + ' ')
    return txt

# 보스 설정 표시
def string_getState():

    txt = '보스 목록'
    for bossName in list_getAllBossNames():
        txt += (bossName + ' : ')
        if bool_getValidBoss(bossName):
            txt += '활성화\n'
        else:
            txt += '비활성화\n'
    return txt

# 멘션할 멤버 검색            
def list_getMentionUser():
    
    info = list_getAlarmIndex()
    
    if len(info) == 0:
        return string_disableAllBossAlarm()

    bossList = list_getBossListDay(info[0],info[1])
    mentionlist = []
    for userName in userList:
        for bossName in bossList:
            if userList[userName][bossName]:
               mentionlist.append(userName)
               break
    return mentionlist

# 보스 상태 
def list_bossAllState():
    return ['보스 알림 설정 상태', string_getState(), 0x0F00FF]

weekday = ['월','화','수','목','금','토','일']

# 해당 보스의 전체 일정
def list_bossAllTimeFromName(bossName):

    if bool_validBossName(bossName):      
        timelist = list_getAllBossTime(bossName)
        txt = ""
        for sche in timelist:
            txt += (weekday[sche[0]] + '요일 ' + str(string_fromHM(sche[1])) + '\n')
        embedList = [name, txt,string_getBossImage(name),hex_getBossColor(name)]
    else:
        embedList = ['설정 오류','잘못된 이름을 입력했거나 보스 알림 설정을 모두 꺼뒀는지 확인하십시오\n' + name,null,0xFF0000]
    return embedList

# 보스 설정 상태 확인
def bool_validBossName(bossName):
    return bossName in enableBossList

# 보스 알람 설정       
def string_enableBossAlram(name):
    enableBossList[name] = True
    return name +'의 알림이 설정되었습니다'

# 보스 알람 해제
def string_disableBossAlram(name):
    enableBossList[name] = False
    return name + '의 알림이 해제되었습니다'


####################################################
# private

# 해당 보스의 전체 정보
def list_getAllBossTime(bossName):
    retlist = []    
    for weekday in range(0,7):
        for index in range(0,size_getTableLengthOnWeekday(weekday)) :
            for elementBossName in list_getBossListDay(weekday,index) :
                if bossName == elementBossName :
                    retlist.append([weekday,getAlarmTime(weekday, index)])
    return retlist

# 바로 다음 보스 일정 검색
def index_getStartIndex() :

    now = datetime_now()
    weekday = int_nowWeekday()
    
    for index in range(0,size_getTableLengthOnWeekday(weekday)) :
        if second_calcSecondFromDateTime(now) < second_getAlarmTime(weekday, index):
            return index
    return -1

# 출력할 보스 일정 검색
def list_getAlarmIndex():
    
    index = index_getStartIndex()
    weekday = int_nowWeekday()
    i = 0;
    if index < 0 :
        index = 0
        i = 1

    while True:
        while index < size_getTableLengthOnWeekday( (weekday+i)%7 ):
            for bossName in list_getBossListDay(weekday,index):
                if bool_getValidBoss(bossName):
                    return [(weekday+i)%7, index];
            index = index + 1 
        i = i + 1
        index = 0          
    return []   

