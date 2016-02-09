# -*- coding: utf-8 -*-
"""
Created on Tue Feb 09 11:16:47 2016

@author: Who Me
"""

import random
class ApstraktnaIndividua:
    def __init__(self,duzina):
        self.DuzinaHromozoma = duzina;
        self.Hromozom = [random.choice([0,1]) for i in range(duzina)]
        self.Fitness=0.0;
        
    def GetDuzinaHromozoma(self):
        return self.DuzinaHromozoma
    def SetDuzinaHromozoma(self,duzina):
        self.DuzinaHromozoma = duzina
    def GetHromozom(self):
        return self.Hromozom
    def SetHromozom(self,hromo):
        self.Hromozom = hromo
    def GetFitness(self):
        return self.Fitness
    def SetFitness(self,fit):
        self.Fitness = fit
    def Evaluiraj(self):
        pass


   
class Populacija:
    def __init__(self,populacija,maxGeneracija,krizanja,mutacija,elita):
        self.VelicinaPopulacije = populacija;
        self.VjerovatnocaKrizanja = krizanja;
        self.VjerovatnocaMutacije = mutacija;
        self.MaxGeneracija = maxGeneracija;
        self.VelicinaElite = elita;
        
        def GetVelicinaPopulacije(self):
            return self.VelicinaPopulacije
        def SetVelicinaPopulacije(self,populacija):
            self.VelicinaPopulacije = populacija
        
        def GetVjerovatnocaKrizanja(self):
            return self.VjerovatnocaKrizanja
    