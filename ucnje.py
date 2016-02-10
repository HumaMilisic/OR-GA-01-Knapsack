# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 23:46:46 2016

@author: WorkIt
"""

from abc import ABCMeta, abstractmethod
import numpy as np
import random
import modulGA as ga
try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q
import operator;

#import mTest;

class Ab(object):
    __metaclass__ = ABCMeta;
    
    @abstractmethod
    def foo(self):
        pass
    
class B(Ab):
    def foo(self):
        print "a";

B();

#mTest.fib(100);

#for l in range(10):
#    print l
    
#a = np.array([1]);
#print a
#np.resize(a,5)
#print a
    
#print [random.choice([0,1]) for i in range(10)]

q = ga.KnapSackIndividua(10);
q2 = ga.KnapSackIndividua(10);
q.Evaluiraj();
print q.GetHromozom()
print q.GetFitness()
#q.SetHromozom([random.choice([0,1]) for i in range(10)])
print q2.GetHromozom()
print q2.GetFitness()

t = [1000,2,3,4,5,6,7,8,9,10]
tt =  ''.join(map(str,t))
print tt
w = ga.Populacija(5,2,2,2,2); #(self,populacija,maxGeneracija,krizanja,mutacija,elita)

qr = w.operatorKrizanje1(q,q2);
#print qr[1];
#print qr[0];
qr1 = ga.KnapSackIndividua(10);
qr1.SetHromozom(qr[1]);

qr0 = ga.KnapSackIndividua(10);
qr0.SetHromozom(qr[0]);

print qr1
print qr1.GetFitness()
print qr0
print qr0.GetFitness()


pp = ga.Populacija(10,10,0.9,0.1,2);
for i in range(pp.GetVelicinaPopulacije()):
    print i
    print pp.populacija[i]    
    pp.operatorMutacija(pp.populacija[i])
    print pp.populacija[i]
    
red = Q.PriorityQueue()
red.put(0);
red.put(10);
red.put(0);
red.put(0);

while not red.empty():
    cv1 = red.get()
    print cv1
#pp.populacija