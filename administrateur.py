from utulisateur import Utulisateur
from user import *


class administrateur(Utulisateur):
    def __init__(self,nom,id,mps,role):
        super().__init__(nom,id,mps,role)
    
    def afficher_info(self):
        return f"NOM: {self._nom} \n ID: {self._id_utulisateur} \n MOT DE PASSE: {self._mot_de_passe} \n role : {self._role}"

    def gerer_utulisateur(self,action,utulisateur, i = ""):
        if action == "a":
            users[utulisateur._role].append(utulisateur)
        elif action == "s":
            users[utulisateur._role].remove(utulisateur)    
        elif action == "m":
            users[utulisateur._role].remove(utulisateur)
            users[i._role].append(i)



    def gerrer_le_menu(self,action,article_menu,new_article_menu=''):
        if action == "ajouter":
            Menu.append(article_menu)
            print(Menu)
            return f"menu ajoute"

        elif action == "Supprimer":
            Menu.remove(article_menu)
            print(Menu)
            return f"menu supprime"
        
        
        elif action == "Modifier":
            Menu.remove(article_menu)
            Menu.append(new_article_menu)
            print(Menu)
            return f"menu modifie"

        

# admin = administrateur(1,1,1,"chef")
# print(users)
# admin.gerer_utulisateur("a" , admin)
# print(users)
# admin.gerer_utulisateur("s" , admin)
# print(users)