from iBossData import *

def identify(msg):
    rtMsg = ""
    if '전화' in msg and '갖다' in msg:
        rtMsg = '이보세요! 여긴 지금 중환자실입니다. 전화는 없어요. 당신은 다른 병원에서 안 돼 가지고 이리로 왔어요.'\
                + ' 조금만 늦었어도 큰일날 뻔했습니다. 아… 전화는 몸에 해로우니까, 그냥 푹 쉬세요.'
    elif '여기가' in msg and '어디오' in msg:
        rtMsg = '아, 병원이오. 안심하세요. 어… 지혈제를 썼고 응급 수술을 했어요. 피를 너무 많이 흘려서, 이거 하마터면 큰일날 뻔했습니다.'
    elif ('아래' in msg or '아랫' in msg) and '감각' in msg:
        rtMsg = '어… 하필이면… 총알이 영 좋지 않은 곳에 맞았어요.'
    elif '무슨' in msg and '소리' in msg:
        rtMsg = '어… 어느 정도 완쾌된 뒤에 말해 주려고 했는데… 잘 알아 두세요.'\
                +'아… 선생은 앞으로 아이를… 가질 수가 없습니다. 다시 말해서 성관계를 할 수가 없다는 것이오.'\
                +'에, 총알이 가장 중요한 곳을 지나갔다 이말입니다.'
    elif '의사양반' in msg:
        rtMsg = '안정을 취하세요. 흥분하면 다시 출혈을 할 수가 있어요. 그렇게 되면 걷잡지 못합니다.'
    return rtMsg

# print command
def doctorMsg():
    return  "의사양반 명령어 : (전화 갖다), (여기가 어디오), (아래 감각), (무슨 소리), (의사양반)\n"+\
            "괄호 안 두 단어를 동시에 사용하면 전화를 받습니다\n\n"

timeMsg = '-time 다음 보스 출현 시간을 알려줍니다\n -time (보스명) 보스의 모든 출현 시간을 알려줍니다\n보스 목록\n'
enMsg = '-en (보스명) : 보스 알을 설정합니다\n보스 목록\n'
disMsg = '-dis (보스명) : 보스 알림을 해제합니다\n보스 목록\n'

def timeCmdMsg():
    return timeMsg +getBossNameString()

def enableCmdMsg():
    return enMsg + getStateString()

def disableCmdMsg():
    return disMsg + getStateString()

def blackDesertCmdMsg():
    return '명령어 목록\n'+timeMsg+enMsg+disMsg+getStateString()

def allMsg():
    return doctorMsg() + blackDesertCmdMsg()
