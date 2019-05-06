from timeFunc import *
import os

imgdir = os.environ['IMGDIR']


bossName = ['누베르','무라카','카란다','벨','오핀','쿠툼','크자카','가모스','귄트']

timeTable =[
 [timeCalcHM(22,55),timeCalcHM(22,57),timeCalcHM(22,59),timeCalcHM(23,1),timeCalcHM(23,30)],
 [timeCalcHM(2,0),timeCalcHM(11,0),timeCalcHM(16,0),timeCalcHM(20,0),timeCalcHM(23,45)],
 [timeCalcHM(2,0),timeCalcHM(16,0),timeCalcHM(20,0),timeCalcHM(23,15),timeCalcHM(23,45)],
 [timeCalcHM(2,0),timeCalcHM(11,0),timeCalcHM(16,0),timeCalcHM(20,0),timeCalcHM(23,45)],
 [timeCalcHM(2,0),timeCalcHM(11,0),timeCalcHM(16,0),timeCalcHM(20,0),timeCalcHM(23,45)],
 [timeCalcHM(2,0),timeCalcHM(11,0),timeCalcHM(16,0),timeCalcHM(19,0)],
 [timeCalcHM(0,15),timeCalcHM(2,0),timeCalcHM(11,0),timeCalcHM(16,0),timeCalcHM(17,0),timeCalcHM(20,0),timeCalcHM(23,45)]]

alramTable=[[1,1,1,1,1],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,20],[20,20,20,20,40,20]]

boss =[
 [['크자카'],['크자카','누베르'],['크자카','쿠툼'],['카란다','누베르'],['오핀']],
 [['크자카'],['크자카','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['가모스']],
 [['누베르'],['크자카','누베르'],['카란다','크자카'],['귄트','무라카'],['오핀']],
 [['쿠툼'],['크자카','누베르'],['카란다','쿠툼',],['누베르','쿠툼'],['가모스']],
 [['카란다'],['크자카','쿠툼'],['카란다','누베르'],['크자카','쿠툼'],['오핀']],
 [['카란다','누베르'],['누베르','쿠툼'],['카란다','크자카'],['귄트','무라카']],
 [['가모스'],['카란다','쿠툼'],['크자카','누베르'],['카란다','쿠툼'],['벨'],['누베르','쿠툼'],['카란다']]]

img = {'누베르' : imgdir +'Nouver.png',
       '무라카' : imgdir +'Muraka.png',
       '카란다' : imgdir +'Karanda.png',
       '벨'     : imgdir +'Vell.png',
       '오핀'   : imgdir +'Offin.png',
       '쿠툼'   : imgdir +'Kutum.png',
       '크자카' : imgdir +'Kzarka.png',
       '가모스' : imgdir +'Garmoth.png',
       '귄트'   : imgdir +'Quint.png'}

colors = { '누베르' : 0xF3E2A9,
           '무라카' : 0xE6E6E6,
           '카란다' : 0x2EFEF7,
           '벨'     : 0x58FAF4,
           '오핀'   : 0xA9F5D0,
           '쿠툼'   : 0xFE2EC8,
           '가모스' : 0xFE2E2E,
           '크자카' : 0xF78181,
           '귄트'   : 0xFFFFFF}
