class facture:
    def __init__(self,id_facture,commande,total_ht,tvA,frais_service,total_ttc):
        self._id_facture = id_facture
        self._commande = commande
        self._hortax = total_ht
        self._tvA = tvA
        self._frais_service = frais_service
        self._total_ttc = total_ttc
    def afficher_facture(self):
        return f"Facture : id_facture :{self._id_facture} \n commande :{self._commande} \n total_ht :{self._total_ht} \n tvA :{self._tvA} \n frais_service :{self._frais_service} \n total_ttc :{self._total_ttc}"
    def calculer_total(self):
        self._hortax = self._total_ttc / 1.2
        self._tvA = self._total_ttc * 0.2
        self._frais_service = self._total_ttc * 0.05
        self._total_ttc = self._hortax + self._tvA + self._frais_service 
        return f" hortax : {self._hortax} \ntvA : {self._tvA} \nfrais service  : {self._frais_service} \ntotal : {self._total_ttc}"
    
        