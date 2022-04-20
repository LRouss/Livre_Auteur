class Auteur:
    """
        Classe Auteur
    """

    def __init__(self, p_nom="", p_prenom="", p_pays_origine="", p_langue_ecriture="", p_annee_naissance="", p_list = []):
        """
        Constructeur de la classe Livre
        :param p_nom:
        :param p_prenom:
        :param p_pays_origine:
        :param p_langue_ecriture:
        :param p_annee_naissance:
        """
        self.NomAuteur = p_nom
        self.PrenomAuteur = p_prenom
        self.PaysOrigine = p_pays_origine
        self.LangueEcriture = p_langue_ecriture
        self.__AnneeNaiss = p_annee_naissance
        self.List_livres = p_list

    def __str__(self):
        chaine = f""
        return chaine