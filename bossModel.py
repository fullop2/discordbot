from openpyxl import load_workbook
import os

imgdir = os.environ['IMGDIR']

bossNameList = ['누베르','무라카','카란다','벨','오핀','쿠툼','크자카','가모스','귄트']

#load excel
load_wb = load_workbook('./DataTable.xlsx')

ws_timeTable = load_wb['timeTable']
ws_alarmTable = load_wb['alarmTable']
ws_bossTable = load_wb['bossTable']

timeTable = []
i = 0
for row in ws_timeTable.rows:
       
       timeTable.append([])
       for cell in row:
              timeTable[i].append(cell.value)
       i = i + 1
       
alarmTable = []
i = 0
for row in ws_alarmTable.rows:
       
       alarmTable.append([])
       for cell in row:
              alarmTable[i].append(cell.value)
       i = i + 1

bossTable = []
i = 0
for row in ws_bossTable.rows:
       bossTable.append([])
       for cell in row:
              if(cell.value != None):
                     listCell = cell.value.split(',')
                     bossTable[i].append(listCell)
       i = i + 1

bossImage = {'누베르' : imgdir +'Nouver.png',
       '무라카' : imgdir +'Muraka.png',
       '카란다' : imgdir +'Karanda.png',
       '벨'     : imgdir +'Vell.png',
       '오핀'   : imgdir +'Offin.png',
       '쿠툼'   : imgdir +'Kutum.png',
       '크자카' : imgdir +'Kzarka.png',
       '가모스' : imgdir +'Garmoth.png',
       '귄트'   : imgdir +'Quint.png'}

bossColor = { '누베르' : 0xF3E2A9,
           '무라카' : 0xE6E6E6,
           '카란다' : 0x2EFEF7,
           '벨'     : 0x58FAF4,
           '오핀'   : 0xA9F5D0,
           '쿠툼'   : 0xFE2EC8,
           '가모스' : 0xFE2E2E,
           '크자카' : 0xF78181,
           '귄트'   : 0xFFFFFF}
