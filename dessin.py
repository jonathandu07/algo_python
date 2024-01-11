# Affiche un rectangle rempli avec un même caractère

# Déclaration des variables et constantes
largeur = None   # Variable pour stocker la largeur du rectangle.
hauteur = None   # Variable pour stocker la hauteur du rectangle.
i = None         # Variable de boucle pour les colonnes.
j = None         # Variable de boucle pour les lignes.
car = None       # Variable pour stocker le caractère à utiliser pour le dessin.

# Demander les informations à l'utilisateur
# 1 - La largeur
largeur = int(input("Largeur ?"))  # Demande à l'utilisateur d'entrer la largeur du rectangle.
# 2 - La hauteur
hauteur = int(input("Hauteur ?"))  # Demande à l'utilisateur d'entrer la hauteur du rectangle.
# 3 - Le caractère à utiliser
car = input("Caractère ?")         # Demande à l'utilisateur d'entrer le caractère à utiliser pour le dessin.

# Boucle principale
for j in range(hauteur):            # Boucle sur les lignes du rectangle.
    # Boucle pour afficher une ligne
    for i in range(largeur):        # Boucle sur les colonnes de chaque ligne.
        print(car, end="")          # Affiche le caractère sans passer à la ligne.
    print()                         # Passe à la ligne suivante après avoir terminé une ligne du dessin.
