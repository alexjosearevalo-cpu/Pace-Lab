# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:38:25 2026

@author: basir
"""
import math as m
## création d'un parcourt test
class Parcours :
    def __init__ (self, distance, pente, vent):
        self.distance = distance ## longueur de la section
        self.pente = pente ## pente constante de la section
        self.vent = vent ## vent constant soufflant sur la section
##création du cycliste
class Cycliste :
    def __init__ (self, puissance, position, vitesse, resi_mvt,rendement,masse ):
        self.puissance= puissance
        self.position = position
        self.vitesse= vitesse
        self.resi_mvt = resi_mvt ## coefficient de résistance au movement 
        self.rendement = rendement ## coefficient de rendement 
        self.masse= masse
        
        
class Déplacement(Parcours, Cycliste) : ##mouvement du cycliste
    def __intit__ (self):
              super().__init__()
    def F_motrice() : ## quantité de force pour avancer
        force_motrice = (Cycliste.puissance * Cycliste.rendement)/Cycliste.vitesse
    def F_gravite(): ## force généré par la grvité sur le cycliste
        force_gravite = - Cycliste.masse*9,81 * m.sin(Parcours.pente)
    def F_resi_mvt