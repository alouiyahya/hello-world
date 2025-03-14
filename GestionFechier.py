import csv

class GestionFichier:
    def lire_fichier(self, nom_fichier):
        file = open(nom_fichier, "r",)
        lecteurCSV = csv.reader(file, delimiter=";")
        for ligne in lecteurCSV:
            print(ligne)
        file.close()

    def ecrire_fichier(self, nom_fichier, contenu):
        file = open(nom_fichier, 'a')
        a = csv.writer(file, delimiter=";")
        a.writerow(contenu)
        file.close()

    def chercher_dans_fichier(self, nom_fichier ,critere):
        file = open(nom_fichier, 'r')
        lecteurCSV = csv.reader(file, delimiter=';')
        for i in lecteurCSV:
            if critere in i:
                print(f'{critere} dans ligne: {i}')

