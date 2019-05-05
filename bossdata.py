import timefunc
import os

imgdir = os.environ['IMGDIR']

timeTable =[
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)],
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)],
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,15),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)],
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)],
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)],
 [timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(19,0),timefunc.timecalcHM(24,15)],
 [timefunc.timecalcHM(00,15),timefunc.timecalcHM(2,0),timefunc.timecalcHM(11,0),timefunc.timecalcHM(16,0),timefunc.timecalcHM(17,0),timefunc.timecalcHM(20,0),timefunc.timecalcHM(23,45),timefunc.timecalcHM(26,0)]]

alramTable=[[20,20,20,20,20,20],[20,20,20,20,20,20],[20,20,20,20,20,20],[20,20,20,20,20,20],[20,20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,40,20,20]]

boss =[
 [['크자카'],['크자카','누베르'],['크자카','쿠툼'],['카란다','누베르'],['오핀'],['크자카']],
 [['크자카'],['크자카','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['가모스'],['누베르']],
 [['누베르'],['크자카','누베르'],['카란다','크자카'],['귄트','무라카'],['오핀'],['쿠툼']],
 [['쿠툼'],['크자카','누베르'],['카란다','쿠툼',],['누베르','쿠툼'],['가모스'],['카란다']],
 [['카란다'],['크자카','쿠툼'],['카란다','누베르'],['크자카','쿠툼'],['오핀'],['카란다','누베르']],
 [['카란다','누베르'],['누베르','쿠툼'],['카란다','크자카'],['귄트','무라카'],['가모스']],
 [['가모스'],['카란다','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['벨'],['누베르','쿠툼'],['카란다'],['크자카']]]

img = {'누베르' : imgdir +'Nouver.png',
       '무라카' : imgdir +'Muraka.png',
       '카란다' : imgdir +'Karanda.png',
       '벨'     : imgdir +'Vell.png',
       '오핀'   : imgdir +'Offin.png',
       '쿠툼'   : imgdir +'Kutum.png',
       '크자카' : imgdir +'Kzarka.png',
       '가모스' : imgdir +'Garmoth.png',
       '귄트'   : imgdir +'Quint.png'}

weekdayChar = ['월','화','수','목','금','토','일']

colors = { '누베르' : 0xF3E2A9,
           '무라카' : 0xE6E6E6,
           '카란다' : 0x2EFEF7,
           '벨'     : 0x58FAF4,
           '오핀'   : 0xA9F5D0,
           '쿠툼'   : 0xFE2EC8,
           '가모스' : 0xFE2E2E,
           '크자카' : 0xF78181,
           '귄트'   : 0xFFFFFF}

def getBossIndex(weekday,now) :
    for t in range(0,len(timeTable[weekday])) :
        if timefunc.timecalcTime(now) < timeTable[weekday][t] : 
            return t
        
def getBossTime(weekday, time) :
    return timeTable[weekday][time]

def getAlramTime(weekday,time) :
    return alramTable[weekday][time]

def getBossName(weekday, time) :
    return boss[weekday][time]

def getBossAllTime(name):
    retlist = []
    for weekday in range(0,7):
        for t in range(0,len(timeTable[weekday])) :
            for bo in boss[weekday][t] :
                if name == bo :
                    retlist.append([weekday,timeTable[weekday][t]])
    return retlist
