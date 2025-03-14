class table:
    def __init__(self,numero_table,capacite,est_occupe):
        self._numero_table = numero_table
        self._capacite = capacite
        self._est_occupe = True


    def afficher_info_table(self):
        return f"numero de table : {self._numero_table} \n capacite : {self._capacite}"
    

    def occuper_table(self,etat):
        if self._est_occupe == False:
            self._est_occupe = True
            print ("Table numero",self._numero_table,"est occupee")


    def liberer_table(self):
          if  self._est_occupe == True :
               self._est_occupe = False
               print ("Table numero",self._numero_table,"est libre")
               

