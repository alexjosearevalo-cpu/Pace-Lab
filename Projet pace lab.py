import math as m
## création d'un parcourt test
g=9.81 
class Parcours :
    def __init__ (self, distance, pente, vent, angle_v,p_air):
        self.distance = distance ## longueur de la section
        self.pente = pente ## pente constante de la section
        self.vent = vent/3.6 ## vent constant soufflant sur la section en km/h
        self.angle_v = angle_v ## angle par rapport au cycliste avec 0 = avant 
        self.p_air= p_air ## densite de l'air 
##création du cycliste
class Cycliste :
    def __init__ (self, puissance, position, vitesse, resi_mvt,rendement,masse,CdA ):
        self.puissance= puissance
        self.position = position
        self.vitesse= vitesse/3.6 ##vitesse donne en km/h
        self.resi_mvt = resi_mvt ## coefficient de résistance au movement 
        self.rendement = rendement ## coefficient de rendement 
        self.masse= masse
        self.CdA= CdA ##coefficient aerodinamique 
        
class Deplacement : ##mouvement du cycliste
    def __init__ (self,Cycliste,Parcours):
              self.Cycliste = Cycliste
              self.Parcours = Parcours
    
    def F_motrice(self) : ## quantité de force pour avancer
        force_motrice = (self.Cycliste.puissance * self.Cycliste.rendement)/self.Cycliste.vitesse
        return force_motrice
    def F_gravite(self): ## force généré par la grvité sur le cycliste
        force_gravite = - self.Cycliste.masse*g * m.sin(m.atan(self.Parcours.pente/100))
        return force_gravite
    def F_resi_mvt(self):##force de la route empéchant d'avancer
        force_resi = - self.Cycliste.resi_mvt * self.Cycliste. masse * g * m.cos(m.atan(self.Parcours.pente/100))
        return force_resi
    def F_air(self):## frottemment de l'air
        force_air = -1/2 * self.Parcours.p_air * self.Cycliste.CdA * (self.Cycliste.vitesse + self.Parcours.vent* m.cos(self.Parcours.angle_v))* abs(self.Cycliste.vitesse + self.Parcours.vent* m.cos(self.Parcours.angle_v))
        
        return force_air
    def acceleration(self): ## acceleration totale
        acceleration = (1/self.Cycliste.masse)*(self.F_motrice() + self.F_gravite() + self.F_resi_mvt()+ self.F_air())
        return acceleration
    def Temps(self,dt=0.01): ##calcul du temps avec Euler
        position = 0
        temps = 0
        while position < self.Parcours.distance :
            self.Cycliste.vitesse = self.Cycliste.vitesse + self.acceleration()*dt
            position = position + self.Cycliste.vitesse*dt
            temps = temps + dt
        print("Force motrice :", self.F_motrice(), "N")
        print("Force gravité :", self.F_gravite(), "N")
        print("Force résistance :", self.F_resi_mvt(), "N")
        print("Force aérodynamique :", self.F_air(), "N")
        print("Accélération :", self.acceleration(), "m/s²")
        print("Le temps pour parcourir",self.Parcours.distance,"m sur une pente de",self.Parcours.pente,"% est de",temps,"s.")
Gui = Cycliste(438,0,40,0.004,0.975,70.8,0.3) ## coefficient sur bitume
Alpe_D_huez = Parcours(13700,8.12,3,0,1.104)
deplacement_1 = Deplacement(Gui,Alpe_D_huez)
deplacement_1.Temps()
