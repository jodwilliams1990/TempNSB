import numpy as np
from matplotlib import pyplot as plt
#import seaborn as sns
from scipy.stats import norm
import sys
sys.path.append('../')
sys.path.append('../../')
'''
from CHECLabPy.core.io import TIOReader
import os
import numpy as np
from matplotlib import pyplot as plt
from CHECLabPy.plotting.camera import CameraImage
'''
import time
import shutil
import re

NSB=[0,40,80,125,250,400,1000]
maxtime=60#3600 #seconds, max read in time
every=15 #seconds, period
events=maxtime/every
pri=np.zeros((32,7,int(every))) #EVERY MODULE, EVERY NSB LEVEL, EVERY TIME STAMP
aux=np.zeros((32,7,int(every))) #EVERY MODULE, EVERY NSB LEVEL, EVERY TIME STAMP
psu=np.zeros((32,7,int(every))) #EVERY MODULE, EVERY NSB LEVEL, EVERY TIME STAMP
si=np.zeros((32,7,int(every))) #EVERY Si, EVERY NSB LEVEL, EVERY TIME STAMP
other=np.zeros((15,7,int(every))) #Ambient, Set, Water In, Water Out, Ext2, Ext3, Ext4, Ext5, PSUBP, PSUP,PSU35V1, PSY35V2, DACQ1, DACQ2, EVERY NSB LEVEL, EVERY TIME STAMP
t=np.zeros((7,int(every)))
print('hello')
for k in range (0,len(NSB)):
    #******* PSEUDO-CODE **************#    
    #- SET NSB LEVEL
    start = time.time()
    for eventcount in range (0,int(events)):
        shutil.copyfile('/Users/chec/Desktop/CHECLabPy/Run43461.mon','/Users/chec/Desktop/CHECLabPy/Run43461t.mon')
        file = open('/Users/chec/Desktop/CHECLabPy/Run43461t.mon', 'r') 
        end=time.time()
        t[k,eventcount]=end-start
        a=0
        print(NSB[k],eventcount)
        for row in file:
            b=row
            if a==8+(362*eventcount):#2542:
                #do this    2018-05-14 14:49:56:976 CH T_AMBIENT 18.500000
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                pri[0,k,eventcount]=float(b[hasht[lht-1]:])  
                print(pri[0,k,eventcount])
            if a==8+1+(362*eventcount):#2543:
                #do this    2018-05-14 14:49:56:976 CH T_SET 5.000000
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[1,k,eventcount]=float(b[hasht[lht-1]:])  
            if a==8+2+(362*eventcount):#2544:
                #do this 2018-05-14 14:49:56:976 CH T_WATER_IN 6.800000 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[2,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+3+362*eventcount:#2545:
                #do this 2018-05-14 14:49:56:976 CH T_WATER_OUT 5.300000
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[3,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+18+362*eventcount:#2560:
                #do this 2018-05-14 14:49:56:976 SB TMON_EX2 20.372850 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[4,k,eventcount]=float(b[hasht[lht-1]:]) 
                print(other[4,k,eventcount])
            if a==8+19+362*eventcount:#2561:
                #do this  2018-05-14 14:49:56:976 SB TMON_EX3 24.947031  
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[5,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+20+362*eventcount:#2562:
                #do this  2018-05-14 14:49:56:976 SB TMON_EX4 19.683592
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[6,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+21+362*eventcount:#2563:
                #do this  2018-05-14 14:49:56:976 SB TMON_EX5 21.688692 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[7,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+22+362*eventcount:#2564:
                #do this  2018-05-14 14:49:56:976 SB TMON_FAN1 12.853651
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[8,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+42+362*eventcount:#2584:
                #do this  2018-05-14 14:49:56:976 PSU TEMP_BP_MOD 55.000000 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[9,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+43+362*eventcount:#2585:
                #do this  2018-05-14 14:49:56:976 PSU TEMP_SB_MOD 52.000000 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[10,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+44+362*eventcount:#2586:
                #do this  2586 2018-05-14 14:49:56:976 PSU TEMP_35V1_MOD 47.000000                
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[11,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+45+362*eventcount:#2587:
                #do this    2018-05-14 14:49:56:976 PSU TEMP_35V2_MOD 48.000000 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[12,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+46+362*eventcount:#2588:
                #do this  2586 2018-05-14 14:49:56:976 PSU TEMP_35V1_MOD 47.000000                
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[13,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a==8+47+362*eventcount:#2589:
                #do this    2018-05-14 14:49:56:976 PSU TEMP_35V2_MOD 48.000000 
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                lht=len(hasht)
                other[14,k,eventcount]=float(b[hasht[lht-1]:]) 
            if a>8+2604-2542+362*eventcount and a<8+2604+33-2542+362*eventcount:
                #do this    2605 2018-05-14 14:49:56:976 TM T_PRI 0 36.937500  
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                prino=int(b[hasht[3]:hasht[4]])
                pri[prino,k,eventcount]=float(b[hasht[4]:])          #4          
            #if a>2636 and a<2636+33:
            if a>8+2636-2542+362*eventcount and a<8+2636+33-2542+362*eventcount:
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                prino=int(b[hasht[3]:hasht[4]])
                aux[prino,k,eventcount]=float(b[hasht[4]:])          #4
            #if a>2668 and a<2668+33:
            if a>8+2668-2542+362*eventcount and a<8+2668+33-2542+362*eventcount:
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                prino=int(b[hasht[3]:hasht[4]])
                psu[prino,k,eventcount]=float(b[hasht[4]:])          #4
            if a>8+2700-2542+362*eventcount and a<8+2700+33-2542+362*eventcount:
                hasht=[x.start() for x in re.finditer(' ',b)]
                b=str(b)
                prino=int(b[hasht[3]:hasht[4]])
                si[prino,k,eventcount]=float(b[hasht[4]:])          #4
            #0
            #362
            #724
            #1086
            #1448
            #1810
            #2172 2532
            #2534 2894
            a=a+1
        time.sleep(every)
        print(other[:,0,eventcount])
        