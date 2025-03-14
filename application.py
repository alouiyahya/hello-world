import csv
from utulisateur import *
from administrateur import *
from serveur import *
from chefDeCuisine import *
from menu import *
from Reservation import *
from Commande import *
from facture import *
from table import *
from GestionFechier import *
from Authentification import *
from CalculateurFinancier import *



authentification = Authentification()
gestionFichier = GestionFichier()
calculateurFinancier = CalculateurFinancier()
admin = administrateur("yahya","1111","0000","administrateur")
chef = ChefDeCuisine("yahya","1111","0000","chef")


#run the program from this page


def login():
    print("++++++++++++++++++++++++ < WELCOME TO OUR APP> ++++++++++++++++++++++++")
    username = input("  Enter your user     : ")
    password = input("  Enter your password : ")

    if authentification.se_connecter(username, password) == "administrateur":
        print("Login successfuly!")
        admin_menu()
    elif authentification.se_connecter(username, password) == "serveur":
        print("Login successfuly!")
        serveur_menu()
    elif authentification.se_connecter(username, password) == "chef":
        print("Login successfuly!")
        chef_menu()
    


    
def admin_menu():
     i = 1
     while i != 0:
        print("+++++++++++++++++++++++++++++++++ WELCOME ADMIN +++++++++++++++++++++++++++++++++")
        print(" <1> ajouter un utulisateur  :")
        print(" <2> modifier un utulisateur :")
        print(" <3> supprimer un utulisateur:")
        print(" <4> Ajouter un menu         :")
        print(" <5> supprimer un Menu       :")
        print(" <6> Modifier un Menu        :")
        print(" <7> Se deconnecter          :")
        i = int(input("Saisir votre choix: "))
        if i == 1:
            nom = input("saisir votre nom: ")
            id = input(" saisir votre id : ")
            mdp = input("saisir votre mot de passe : ")
            role = input("Saisir votre role (administrateur / serveur / chef): ")
            user = administrateur(nom, id, mdp,role)
            user.gerer_utulisateur("a", user)
            gestionFichier.ecrire_fichier("login.csv", [nom,id,mdp,role])
            print(users)


        elif i == 2:
            u_type = input('Modifier admin (a), serveur (s) ou chef (c): ')
            if u_type == 'a' or u_type == 'Administrateur':

                for i in users['administrateur']:
                    print(i._nom)
                mod_user = input('Entrer le nom d\'utilisateur: ')
                for i in users['administrateur']:
                    if mod_user == i._nom :
                        nom = str(input('Nom: '))
                        id_u = str(input('Id: '))
                        mdp = str(input('Mot de passe: '))
                        role = str(input('Role (administrateur, serveur ou chef): '))
                        user = administrateur(nom, id_u, mdp, role)
                        admin.gerer_utulisateur('m', i, user)
                        print(users)
            
            elif u_type == 's' or u_type == 'Serveur':
                for i in users['serveur']:
                    print(i._nom)
                mod_user = input('Entrer le nom d\'utilisateur: ')
                for i in users['serveur']:
                    if mod_user == i._nom :
                        nom = str(input('Nom: '))
                        id_u = str(input('Id: '))
                        mdp = str(input('Mot de passe: '))
                        role = str(input('Role (administrateur, serveur ou chef): '))
                        user = administrateur(nom, id_u, mdp, role)
                        admin.gerer_utulisateur('m', i, user)
                        print(users)
   
            
            elif u_type == 'C' or u_type == 'Chef':
                for i in users['chef']:
                    print(i._nom)
                mod_user = input('Entrer le nom d\'utilisateur: ')
                for i in users['chef']:
                    if mod_user == i._nom :
                        nom = str(input('Nom: '))
                        id_u = str(input('Id: '))
                        mdp = str(input('Mot de passe: '))
                        role = str(input('Role (administrateur, serveur ou chef): '))
                        user = administrateur(nom, id_u, mdp, role)
                        admin.gerer_utulisateur('m', i, user)
                        print(users)
            else:
                print('Il  y a aucun utilisateur avec ce nom.')




        elif i == 3:
            for ad in users['administrateur']:
                print(ad._id_utulisateur)
            for ser in users['serveur']:
                print(ser._id_utulisateur)
            for che in users['chef']:
                print(che._id_utulisateur)
            user = input('Entrez l\'id d\'utilisateur: ')
            if users['administrateur'] != [] and user == ad._id_utulisateur:
                admin.gerer_utulisateur('s', ad)
                print(users)
            elif users['serveur'] != [] and user == ser._id_utulisateur:
                admin.gerer_utulisateur('s', ser)
                print(users)
            elif users['chef'] != [] and user == che._id_utulisateur:
                admin.gerer_utulisateur('s', che)
                print(users)
            else:
                print('L\'identifiant saisi est incorrect')


        elif i == 4:
            id_article =input("id article: ")
            nom = input("nom:")
            description = input("description:")
            prix = int(input("prix: "))
            categorie = input("categorie: ")
            menu1 = menu(id_article,nom,description,prix,categorie)
            gestionFichier.ecrire_fichier("menu.csv", [nom,description,prix,categorie])
            print(admin.gerrer_le_menu("ajouter",menu1,new_article_menu=''))



        elif i == 5:
            for j in Menu:
                print(j._nom)
                x = input("choisir nom: ")
                if x == j._nom:
                    print(admin.gerrer_le_menu("Supprimer",j))

        elif i == 6:
            for j in Menu:
                print(j._nom)
                x = input("choisir nom: ")
                if x == j._nom:
                    id_article = input("id article: ")
                    nom = input("nom:")
                    description = input("description:")
                    prix = int(input("prix: "))
                    categorie = input("categorie: ")
                    menu1 = menu(id_article,nom,description,prix,categorie)
                    print(admin.gerrer_le_menu("Modifier",j,menu1))




        elif i == 7:
            se_deconnecter()


def se_deconnecter():
        i = 1
        while i != 0:
            print('\n1- Connecter')
            print('0- Quitter')
            i = int(input("Saisir votre choix: "))
            if i == 1:
                login()
            elif i == 0:
                print('Au Revoir!')
                return
            else:
                print('Choix est incorrecte.')

def serveur_menu():
    i = 1
    while i != 0:
        print("+++++++++++++++++++++++++++++++++ WELCOME SERVEUR +++++++++++++++++++++++++++++++++")
        print(" <1> prendre_reservation  :  ")
        print(" <2> prendre_commande     :  ")
        print(" <3> generer_facture      :  ")
        print(" <4> consulter_reservation:  ")
        print(" <5> consulter_commande   :  ")
        i = int(input("Saisir votre choix: "))
        if i == 1:
            identifiant_unique = input("saisir votre reservation: ")
            nombre_personne = input("nombre de personne: ")
            date_reservation = input("date de reservation: ")
            heure_reservation = input("heure de reservation: ")
            numero_table = input("numero de table: ")
            reserv = resevation(identifiant_unique,nombre_personne,date_reservation,heure_reservation,numero_table)
            reservations.append(reserv)
            print(reservations)


        if i == 2:
            _id_commannde = input("saisir votre commande: ")
            _reservation = input("reservation: ")
            _article = input("articlete: ")
            _statu = input("statu: ")
            cmd = commande(_id_commannde,_reservation,_article,_statu)
            commandes.append(cmd)
            print(commandes)



        elif i == 3:
            for cmd in commandes:
                print(cmd._id_commannde)
                print(facture)

               
        
        elif i == 4:
            cmd.consulter_reservation
        elif i == 5:
            cmd.consulter_commande
        elif i == 0:
            se_deconnecter
            





def chef_menu():
    i = 1
    while i != 0:
        print("+++++++++++++++++++++++++++++++++ WELCOME CHEF +++++++++++++++++++++++++++++++++")
        print(" <1> consulter_commandes               :  ")
        print(" <2> mettre_a_jour_statu_commandes     :  ")
        i = int(input("Saisir votre choix: "))
        if i == 1:
          while i != 0:
              print(f'\n{"#"*15} Bienvenue Chef! {"#"*15}')
              print('1- Consulter commande')
              print('2- Mettre a jour statut de commande')
              print('{0- Decconecter')
              i = int(input('\n- Saisir votre choix: '))
              print(f'{"#" * 47}\n')


              if i == 1:
                  print('=== Commandes en cours ===')
                  chef.consulter_commandes()
                  print('='*26)

        elif i == 2:
            print('=== Commandes en cours ===')
            chef.consulter_commandes()
            print('='*26)
            com_id = input('Choisir commande avec son Id: ')
            N_statut = input('Choisir la nouvelle statut (en preparation ou pret): ')
            for commande in commandes:
                if com_id == commande._id_commande:
                    print(chef.mettre_a_jour_statut_commande(commande, N_statut))

        elif i == 0:
            se_deconnecter()




#chef_menu()
#serveur_menu()
#admin_menu()
login()




