from abc import ABC, abstractmethod
class Utulisateur(ABC):
    def __init__(self,nom,id,mps,role):
        self._nom = nom
        self._id_utulisateur = id
        self._mot_de_passe = mps
        self._role = role

    @abstractmethod
    def afficher_info(self):
        pass
    
    
    def modifier_mot_de_passe(self,nouveau_mot_de_passe):
        return self._mot_de_passe == nouveau_mot_de_passe
    