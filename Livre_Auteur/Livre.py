from Auteur import *

class Livre :
    """
    Classe Livre
    """
    def __init__(self,p_isbn="",p_titre="",p_maison_edition="",p_Annee=0,p_prix=-10.00) :
        """

        :param p_isbn:
        :param p_titre:
        :param p_auteur:
        :param p_maison_edition:
        :param p_Annee:
        :param p_prix:
        """
        self.ISBN = p_isbn
        self.Titre = p_titre
        self.MaisonEdition = p_maison_edition
        self.__anneeParution = p_Annee
        self.__Prix = p_prix

    def __str__(self):
        chaine = f"{self.ISBN}\n{self.Titre}\n{self.MaisonEdition}\n{self.__Prix}"

        return chaine
