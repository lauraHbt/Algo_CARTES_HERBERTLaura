from Mage import *
import random

class Cartes:
    def __init__(self, nom, mana, description):
        self.nom = nom
        self.mana = mana
        self.desc = description
        self.main = []
    def creaMain(self):
        choixC = random.randint(1,3)
        if (choixC == 1):
            valeur = random.randint(0,2)
            self.main.append(Cristal(valeur))
        if (choixC == 2):
            valeur = random.randint(5,10)
            score = random.randint(10,15)
            self.main.append(Creature(10,valeur,score))  
        if (choixC == 3):
            valeur = random.randint(15,20)
            self.main.append(Blast(valeur))        

    def afficheCarte(self):
        if (len(self.main)<3):
            self.creaMain()
            print(self.main)

    def passeTour(self,num):
        if (num == 0):
            joueurs[0].mana = joueurs[0].mana + 5
        if (num == 1):
            joueurs[1].mana = joueurs[1].mana + 5 

class Mage:
    def __init__(self, nom, PdV, Mana):
        self.nom = nom
        self.pdV = PdV
        self.mana = Mana
        self.jeu = []
        self.defo = []
#    def attaque(self):   
            
class Cristal(Cartes):
    def __init__(self, valeur):
        Cartes.__init__(self,"Cristal", valeur, "Augmente Mana")
        self.valeur = valeur
    def capCristal(self,mana):
        mana = mana + self.valeur
        return mana

class Creature(Cartes):
    def __init__(self, PdV, valeur, ScoreAtt):
        Cartes.__init__(self,"Creature", valeur, "Pour défendre")
        self.pdV = PdV
        self.scoreAtt = ScoreAtt
        self.mort = False
    def verifVie(self):
        if (self.pdV == 0):
            self.mort = True
            return self.mort

class Blast(Cartes):
    def __init__(self, valeur):
        Cartes.__init__(self,"Blast", valeur, "Attaque")

#Code
tour = 0
joueurs = []
print("\n ---Bienvenue au Jeu de Cartes Fantastique---")
nbrJ = int(input("\nCombien de joueurs? 1 ou 2 :"))
if nbrJ == 2 :
    uno = str(input("Nom du Premier Joueur : "))
    joueurs.append(Mage(uno,60,40))
    secon = str(input("Nom du Deuxième Joueur : "))
    joueurs.append(Mage(secon,60,40))
    print("Les joueurs sont " + joueurs[0].nom + " et " + joueurs[1].nom)
else :
    print("\nFait-toi des AMIS !")
while (joueurs[0].pdV !=0 and joueurs[0].pdV !=0):
    for i in range(10):
        tour+=1
