class commande:
    def __init__(self,id_commannde,reservation,article,statu):
        self._id_commannde = id_commannde
        self._reservation = reservation
        self._article = []
        self._statu = statu


    def ajouter_article(self,article_menu):
        self._article.append(article_menu)


    def afficher_commande(self):
        return f"Commande : id_commannde :{self._id_commannde} \n reservation :{self._reservation} \n article :{self._article} \n statu :{self._statu}"
    def calculer_total(self,total,tva,prix,ps):
        tva = 0.2
        ps = 0.05
        total == (prix * tva) + (prix * ps)
        return f"total = {total}"
        
        



