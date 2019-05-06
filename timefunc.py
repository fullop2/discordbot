import datetime

def timeCalcHM(hour,min):
    return hour * 3600 + min * 60

def timeCalcHMS(hour,min,sec):
    return hour * 3600 + min * 60 + sec

def timeCalcTime(t):
    return t.hour * 3600 + t.minute * 60 + t.second

def getNow():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)

def getNowWeekday():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).weekday()

def getTime(sec):
    return str(datetime.timedelta(seconds = sec))

def getTimeHM(sec):
    t = (datetime.datetime.min + datetime.timedelta(seconds = sec)).time()
    return str('%02d' % t.hour) + ":" + str('%02d' % t.minute)

