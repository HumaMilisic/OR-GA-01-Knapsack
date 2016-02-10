# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 23:55:43 2016

@author: WorkIt
"""

__name__="modulGA";

import random
from abc import ABCMeta, abstractmethod
import numpy as np

class ApstraktnaIndividua(object):
    __metaclass__ = ABCMeta;
    
    def __cmp__(self,other):
        return cmp(self.Fitness,other.GetFitness);
    
    def __init__(self,duzina):
        self.DuzinaHromozoma = duzina;
        self.Hromozom = [random.choice([0,1]) for i in range(duzina)]
        self.Fitness=0.0;
        self.Evaluiraj();
    
    def __repr__(self):
        temp = ''.join(map(str,self.Hromozom));
#        temp = "("+str(self.priority)+","+str(self.description)+")"
        return temp
        
    def GetDuzinaHromozoma(self):
        return self.DuzinaHromozoma
    def SetDuzinaHromozoma(self,duzina):
        self.DuzinaHromozoma = duzina        
        
    def GetHromozom(self):
        return self.Hromozom
    def SetHromozom(self,hromo):
        self.Hromozom = hromo;
        self.Evaluiraj();
        
    def GetFitness(self):
        return self.Fitness
    def SetFitness(self,fit):
        self.Fitness = fit
    
    @abstractmethod
    def Evaluiraj(self):
        pass

class KnapSackIndividua(ApstraktnaIndividua):
    def Evaluiraj(self):
        suma = 0;
        for i in range(self.DuzinaHromozoma):
            suma = suma + self.Hromozom[i];
        self.Fitness = suma;
    
   
class Populacija(object):
    def __init__(self,populacija,maxGeneracija,krizanja,mutacija,elita):
        self.VelicinaPopulacije = populacija;
        self.VjerovatnocaKrizanja = krizanja;
        self.VjerovatnocaMutacije = mutacija;
        self.MaxGeneracija = maxGeneracija;
        self.VelicinaElite = elita;
        self.populacija =[];
        self.trenutnaGeneracija = 0;
        for i in range(self.VelicinaPopulacije):
            self.populacija.append(KnapSackIndividua(10));
        
        
    def GetVelicinaPopulacije(self):
        return self.VelicinaPopulacije
    def SetVelicinaPopulacije(self,populacija):
        self.VelicinaPopulacije = populacija
        
    def GetVjerovatnocaKrizanja(self):
        return self.VjerovatnocaKrizanja
    def SetVjerovatnocaKrizanja(self,k):
        self.VjerovatnocaKrizanja = k;
            
    def GetVjerovatnocaMutacije(self):
        return self.VjerovatnocaMutacije;
    def SetVjerovatnocaMutacije(self,m):
        self.VjerovatnocaMutacije = m;
            
    def GetMaxGeneracija(self):
        return self.MaxGeneracija;
    def SetMaxGeneracija(self,g):
        self.MaxGeneracija = g;
            
    def GetVelicinaElite(self):
        return self.VelicinaElite;
    def SetVelicinaElite(self,v):
        self.VelicinaElite = v;
            
    def operatorKrizanje1(self,h1,h2,br = -1):
        duzina = h1.GetDuzinaHromozoma()/2;
        r1 = h1.GetHromozom()[:duzina] + h2.GetHromozom()[duzina:];
        r2 = h2.GetHromozom()[:duzina] + h1.GetHromozom()[duzina:];
        return (r1,r2);
    
    def operatorMutacija(self,h1):
        poz = random.randint(0,h1.GetDuzinaHromozoma()-1);
        if h1.Hromozom[poz]:
            h1.Hromozom[poz] = 0;
        else:
            h1.Hromozom[poz] = 1;
