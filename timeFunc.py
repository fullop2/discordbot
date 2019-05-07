import datetime

def second_calcSecondFromHM(hour,min):
    return hour * 3600 + min * 60

def second_calcSecondFromHMS(hour,min,sec):
    return hour * 3600 + min * 60 + sec

def second_calcSecondFromDateTime(datetime):
    return datetime.hour * 3600 + datetime.minute * 60 + datetime.second

def datetime_now():
    return datetime.datetime.utcnow() + datetime.timedelta(hours=9)

def int_nowWeekday():
    return (datetime.datetime.utcnow() + datetime.timedelta(hours=9)).weekday()

def datetime_fromSecond(sec):
    return str(datetime.timedelta(seconds = sec))

def string_fromHM(sec):
    t = (datetime.datetime.min + datetime.timedelta(seconds = sec)).time()
    return str('%02d' % t.hour) + ":" + str('%02d' % t.minute)

