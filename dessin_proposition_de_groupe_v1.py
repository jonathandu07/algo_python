# Déclaration des variables et constantes (sans jamais utiliser de fonctions)
largeur = None         # Variable pour stocker la largeur du dessin.
hauteur = None         # Variable pour stocker la hauteur du dessin.
i = None               # Variable de boucle pour les colonnes.
j = None               # Variable de boucle pour les lignes.
caractere = None       # Variable pour stocker le caractère à utiliser pour le dessin.

# Demander les informations à l'utilisateur
# 1 - La largeur
largeur = int(input("Saisir la largeur du dessin SVP \n"))
# 2 - La hauteur
hauteur = int(input("Saisir la hauteur du dessin SVP \n"))
# 3 - Le caractère à utiliser
caractere = input("Saisir le caractère à utiliser pour le dessin SVP \n")

# Cette boucle ci-dessous représente la hauteur totale
# Répéter Y (= la hauteur saisie) fois la boucle avec l'indice j
for j in range(hauteur):
    # Cette boucle ci-dessous représente une ligne complète
    # Répéter X (= la largeur saisie) fois le caractère sur une même ligne
    for i in range(largeur):
        print(caractere, end="")
    print()  # Passe à la ligne suivante après chaque ligne du dessin.
