from utulisateur import Utulisateur
from user import *

class ChefDeCuisine(Utulisateur):
    def __init__(self, nom, id, mps,role):
        super().__init__(nom, id, mps,role)
        
    def consulter_commandes(self):
        return f"les commandes en cours :{commandes}"
    

    def afficher_info(self):
        print("AHAH")

    def mettre_a_jour_statu_commandes(self,statut):
        if statut == "en prep":
            statut == "pret"
            

    