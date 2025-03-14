import csv
class Authentification:

    def se_connecter(self,id_utilisateur, mot_de_passe) :
        file = open("login.csv", "r")
        reader = csv.reader(file , delimiter=",")
        for ligne in reader:
            if ligne == [id_utilisateur, mot_de_passe , "administrateur"]:
                enter = "administrateur"
                return enter
            elif ligne == [id_utilisateur, mot_de_passe, "serveur"]:
                enter = "serveur"
                return enter
            elif ligne == [id_utilisateur, mot_de_passe, "chef"]:
                enter = "chef"
                return enter
        if ligne not in file :
            print ("Utilisateur ou mot de passe incorrect")
            return False
            

    def se_deconnecter(self):
        print ("se_deconnecter")


