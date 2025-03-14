class resevation:
    def __init__(self,identifiant_unique,nombre_personne,date_reservation,heure_reservation,numero_table):
        self._identifiant_unique = identifiant_unique
        self._nombre_personne = nombre_personne
        self._date_reservation = date_reservation
        self._heure_reservation = heure_reservation
        self._numero_table = numero_table
    
    def afficher_reservation(self):
        return f"IDENTIFIANT UNIQUE: {self._identifiant_unique} \n NOMBRE DE PERSONNE: {self._nombre_personne} \n DATE DE RESERVATION: {self._date_reservation} \n HEURE DE RESERVATION: {self._heure_reservation} \n NUMERO DE TABLE: {self._numero_table}"
    