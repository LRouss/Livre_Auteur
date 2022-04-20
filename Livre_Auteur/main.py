from Livre import *
from Auteur import *

liste_livre=[]
# Instancier deux objets   de la classe Auteur

Auteur1 = Auteur("Coelho","Paulo","Brésil","Portugais","1947")



# Istanciation d'un objet de la classe Livre

L1 = Livre("12345678912345","L'alchimiste","Edition",1988,20)
liste_livre.append(L1)
L2 = Livre("98765432112345","Apprendre à coder avec Python","Eyrolles",2012,100)
liste_livre.append(L2)
Auteur2 = Auteur("Gérard","Swinnen","USA","Anglais",1940,liste_livre)

print(Auteur2.List_livres)

