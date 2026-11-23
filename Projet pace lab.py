# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:38:25 2026

@author: basir
"""
import math as m
## création d'un parcourt test
class Parcours :
    def __init__ (self, distance, pente, vent, angle_v):
        self.distance = distance ## longueur de la section
        self.pente = pente ## pente constante de la section
        self.vent = vent ## vent constant soufflant sur la section
        self.angle_v = angle_v ## angle par rapport au cycliste avec 0 = arrière 
##création du cycliste

class Cycliste :
    def __init__ (self, puissance, position, vitesse, resi_mvt,rendement,masse,watts_kilo):
        self.puissance= puissance
        self.position = position
        self.vitesse= vitesse
        self.resi_mvt = resi_mvt ## coefficient de résistance au movement 
        self.rendement = rendement ## coefficient de rendement 
        self.masse= masse 
        self.watts_kilo= self.puissance/self.masse
        
        
class Déplacement(Parcours, Cycliste) : ##mouvement du cycliste
    def __intit__ (self):
              super().__init__()
    
    def F_motrice(self) : ## quantité de force pour avancer
        force_motrice = (Cycliste.puissance * Cycliste.rendement)/Cycliste.vitesse
    
    def F_gravite(self): ## force généré par la grvité sur le cycliste
        force_gravite = - Cycliste.masse*9,81 * m.sin(Parcours.pente)
    
    def F_resi_mvt(self):##force de la route empéchant d'avancer
        force_resi = - Cycliste.resi_mvt * Cycliste. masse * 9,81 * m.cos(Parcours.pente)
     
    def F_air(self):## frottemment de l'air
        force_air = -1/2 * 1.204 * 0.3 * (Cycliste.vitesse - Parcours.vent* m.cos(Parcours.angle_v))* m.norm(Cycliste.vitesse - Parcours.vent* m.cos(Parcours.angle_v))
        ## 1.204 est la densité de l'air à 20°C, 0.3 est la moyenne de la trainée 
    def acceleration(self):
        acceleration = (1/Cycliste.masse)*(self.F_motrice() + self.F_gravite() + self.F_resi_mvt()+ self.F_air())
Gui = Cycliste(438,23.2,0.05,97.5,70.8) ## coefficient sur bitume
parcours_1= Parcours(13700,8.12,10,0)
