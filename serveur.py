from utulisateur import Utulisateur
from user import *


class Serveur(Utulisateur):
    def __init__(self, nom, id, mps):
        super().__init__(nom, id, mps)

    def prendre_reservation(self,reservation):
        reservations.append(reservation)

    def prendre_commande(self,commande):
        commandes.append(commande)

    def generer_facture(self,commande):
        factures.append(commande)

    def consulter_reservation(self):
        return f"Les reservations : {reservations}"
    
    def consulter_commande(self):
        return f"Les commandes : {commandes}"
    