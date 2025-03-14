class menu:
    def __init__(self,id_article,nom,description,prix,categorie):
        self._id_article = id_article
        self._nom = nom
        self._description = description
        self._prix = prix
        self._categorie = categorie
    def afficher_articles(self):
        return f"ARTICLES : id_articles:{self._id_article} \n nom :{self._nom} \n description :{self._description} \n prix: {self._prix} \n categorie :{self._categorie}"
    