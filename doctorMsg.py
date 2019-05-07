from bossAlarmFunc import *

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
    return  "의사양반 명령어\n전화, 갖다\n여기가, 어디오\n아래(아랫), 감각\n무슨, 소리\n의사양반\n"+\
            "괄호 안 두 단어를 동시에 사용하면 전화를 받습니다\n\n"

cmdListMsg = '검은사막 알림 명령어 목록\n\
-reg : 등록\n\
-rm : 삭제\n\
-en (보스명) : 해당 보스 알림 설정\n\
-dis (보스명) : 해당 보스 알림 해제\n\
-time : 다음 보스 출현 시간\n\
-time (보스명) : 보스 출현 전체 시간\n\
-stat : 자신의 알람 설정 확인\n\
<관리자 명령어>\n\
-enall (보스명) : 보스 알림 전체 설정\n\
-disall (보스명) : 보스 알림 전체 해제\n\
-statall : 전체 보스 알림 확인'

noPhoneMsg = '전화는 없습니다'
def string_all():
    return doctorMsg() + cmdListMsg + '\n\n' + noPhoneMsg


def string_onTimer():
    return '타이머 작동을 시작합니다'

def string_offTimer():
    return '타이머를 종료합니다'
