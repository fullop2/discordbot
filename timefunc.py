import datetime

def timecalcHM(hour,min):
    return hour * 3600 + min * 60

def timecalcHMS(hour,min,sec):
    return hour * 3600 + min * 60 + sec

def timecalcTime(t):
    return t.hour * 3600 + t.minute * 60 + t.second

def getnow():
    return datetime.datetime.now()

def getnowweekday():
    return datetime.datetime.now().weekday()

def gettime(sec):
    return str(datetime.timedelta(seconds = sec))

def gettimeHM(sec):
    t = (datetime.datetime.min + datetime.timedelta(seconds = sec)).time()
    return str('%02d' % t.hour) + ":" + str('%02d' % t.minute)

