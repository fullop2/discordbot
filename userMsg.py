def string_userAlreadyExist(userName):
        return str(userName) + '에 대한 알림 정보가 이미 존재합니다'

def string_userRegisterSuccess(userName):
        return str(userName) + ' 유저에 대한 알림 정보를 생성했습니다'

def string_removeUserSuccess(userName):
        return str(userName) + '에 대한 알림 정보를 삭제했습니다'
    
def string_accessUnavailableUser():
        return '존재하지 않는 사용자입니다'

def string_msgEnableUserBossAlarm(bossName):
        return '당신의 ' + bossName + ' 알림을 설정했습니다'

def string_msgDisableUserBossAlarm(bossName):
        return '당신의 ' + bossName + ' 알림을 해제했습니다'

def string_disableAllBossAlarm():
        return '보스 알림 설정을 모두 꺼뒀는지 확인하십시오'
