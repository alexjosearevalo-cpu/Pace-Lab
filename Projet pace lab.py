import math as m
## création d'un parcourt test
class Parcours :
    def __init__ (self, distance, pente, vent, angle_v):
        self.distance = distance ## longueur de la section
        self.pente = pente ## pente constante de la section
        self.vent = vent ## vent constant soufflant sur la section
        self.angle_v = angle_v ## angle par rapport au cycliste avec 0 = avant 
##création du cycliste
class Cycliste :
    def __init__ (self, puissance, position, vitesse, resi_mvt,rendement,masse ):
        self.puissance= puissance
        self.position = position
        self.vitesse= vitesse
        self.resi_mvt = resi_mvt ## coefficient de résistance au movement 
        self.rendement = rendement ## coefficient de rendement 
        self.masse= masse
        
        
class Deplacement : ##mouvement du cycliste
    def __init__ (self,Cycliste,Parcours):
              self.Cycliste = Cycliste
              self.Parcours = Parcours
    
    def F_motrice(self) : ## quantité de force pour avancer
        force_motrice = (self.Cycliste.puissance * self.Cycliste.rendement)/self.Cycliste.vitesse
        return force_motrice
    def F_gravite(self): ## force généré par la grvité sur le cycliste
        force_gravite = - self.Cycliste.masse*9.81 * m.sin(self.Parcours.pente)
        return force_gravite
    def F_resi_mvt(self):##force de la route empéchant d'avancer
        force_resi = - self.Cycliste.resi_mvt * self.Cycliste. masse * 9.81 * m.cos(self.Parcours.pente)
        return force_resi
    def F_air(self):## frottemment de l'air
        force_air = -1/2 * 1.204 * 0.3 * (self.Cycliste.vitesse - self.Parcours.vent* m.cos(self.Parcours.angle_v))* abs(self.Cycliste.vitesse - self.Parcours.vent* m.cos(self.Parcours.angle_v))
        ## 1.204 est la densité de l'air à 20°C, 0.3 est la moyenne de la trainée
        return force_air
    def acceleration(self):
        acceleration = (1/self.Cycliste.masse)*(self.F_motrice() + self.F_gravite() + self.F_resi_mvt()+ self.F_air())
        print("Force motrice :", self.F_motrice(), "N")
        print("Force gravité :", self.F_gravite(), "N")
        print("Force résistance :", self.F_resi_mvt(), "N")
        print("Force aérodynamique :", self.F_air(), "N")
        print("Accélération :", acceleration, "m/s²")

        return acceleration
        
        
        
Gui = Cycliste(438,0,23.2,0.05,97.5,70.8,) ## coefficient sur bitume
parcours_1= Parcours(13700,8.12,10,0)
deplacement_1 = Deplacement(Gui,parcours_1)
deplacement_1.acceleration()
