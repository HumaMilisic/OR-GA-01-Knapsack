# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 01:14:17 2016

@author: WorkIt
"""

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
import operator;
#import math;
#q = Q.PriorityQueue()
#q.put(10)
#q.put(1)
#q.put(5)
#while not q.empty():
#    print q.get()
    
testString =  "Algoritam Shannon - Fanovog kodiranja je jednostavan za implementirati"

mapaFrekvencija = {};

for i in range(len(testString)):
    slovo =  testString[i]
    temp = mapaFrekvencija.get(slovo,-1)
    if(temp==-1):
        mapaFrekvencija[slovo] = 1
    else:
        mapaFrekvencija[slovo] = temp+1 
        
sorted_x = sorted(mapaFrekvencija.items(), key = operator.itemgetter(1),reverse=True)
red = Q.PriorityQueue()

class priority(object):
    def __init__(self,priority,desc):
        self.priority = priority
        self.description = desc
        return
    def __cmp__(self,other):
        return cmp(self.priority,other.priority)
    def __repr__(self):
        temp = "";
        temp = "("+str(self.priority)+","+str(self.description)+")"
        return temp
        
        
for i in range(len(sorted_x)):
    par = sorted_x[i]
    temp = priority(par[1],par[0])
    red.put(temp)

#red.put(priority(12,("qwe","qwe")))        
stablo = Q.PriorityQueue()
while not red.empty():
    cv1 = red.get()
    #print cv1
    if not red.empty():
        cv2 = red.get()
        #print cv2
        prio = cv1.priority + cv2.priority
        desc = (cv1.description,cv2.description)
        #print prio
        #print desc
        red.put(priority(prio,desc))
    else:
        stablo.put(cv1)
root = stablo.get()
#print root

kodiranje = {}

def funk(root,kod):
    if(type(root) is tuple):
        prvi = root[0]
        drugi = root[1]
    else:
        prvi = root.description[0]
        drugi = root.description[1]
    if len(prvi)==1:        
        kodiranje[prvi] = kod
    else:
        if(kod != "-1"):
            funk(prvi,"0"+kod)
        else:
            funk(prvi,"0")
    if len(drugi)==1:
        kodiranje[drugi] = kod
    else:
        if(kod != "-1"):
            funk(drugi,"1"+kod)
        else:
            funk(drugi,"1")
    
funk(root,"-1")
print kodiranje    