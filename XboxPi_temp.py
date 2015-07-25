from os import popen
from sys import stdin
import re

s = re.compile('[ :]')

class Event:
    def __init__(self,key,value,old_value):
        self.key = key
        self.value = value
        self.old_value = old_value
    #def is_press(self):
    #    return self.value==1 and self.old_value==0
    def __str__(self):
        return 'Event(%s,%d,%d)' % (self.key,self.value,self.old_value)

    #subprocess = popen('nohup xboxdrv --silent','r',65536)
i = 1
#def event_stream(deadzone=0, scale=32000):
while (i == 1):
        line = 'X1:   712 Y1: -2608  X2: -5768 Y2:  3046  du:0 dd:0 dl:0 dr:0  back:0 guide:0 start:0  TL:0 TR:0  A:0 B:0 X:0 Y:0  LB:0 RB:0  LT:205 RT:  0'
        data = list(filter(bool,s.split(line[:-1])))
        print(data,'s')
        if len(data)==41:
            # Break input string into a data dict
            data = { data[x]:int(data[x+1]) for x in range(0,len(data)-2,2) }
            print(data)
            for key in data:
                event = Event(key,data[key],data[key])
                #yield event
                print(event)
        i = i + 1




