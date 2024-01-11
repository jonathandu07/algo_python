# Déclaration des variables et constantes (sans jamais utiliser de fonctions)
largeur = 0                # Variable pour contrôler la largeur actuelle du dessin.
hauteur = 0                # Variable pour contrôler la hauteur actuelle du dessin.
largeurVoulue = None       # Variable pour stocker la largeur souhaitée pour le dessin.
hauteurVoulue = None       # Variable pour stocker la hauteur souhaitée pour le dessin.
caractere = None           # Variable pour stocker le caractère à utiliser pour le dessin.

# Demander les informations à l'utilisateur
# 1 - La largeur
largeurVoulue = int(input("Saisir la largeur du dessin SVP"))  # Demande de saisir la largeur.
# 2 - La hauteur
hauteurVoulue = int(input("Saisir la hauteur du dessin SVP"))  # Demande de saisir la hauteur.
# 3 - Le caractère à utiliser
caractere = input("Saisir le caractère à utiliser pour le dessin SVP")  # Demande de saisir le caractère.

# Initialisation des variables
largeur = 0  # Réinitialisation de la largeur pour le processus de dessin.
hauteur = 0  # Réinitialisation de la hauteur pour le processus de dessin.

# Boucle principale
while hauteur < hauteurVoulue:  # Tant que la hauteur actuelle est inférieure à la hauteur souhaitée.
    # Boucle pour afficher une ligne
    while largeur < largeurVoulue:  # Tant que la largeur actuelle est inférieure à la largeur souhaitée.
        print(caractere, end="")    # Affiche le caractère sans passer à la ligne.
        largeur += 1                # Incrémente la largeur.
    print()                         # Passe à la ligne suivante après avoir terminé une ligne du dessin.
    hauteur += 1                    # Incrémente la hauteur.
    largeur = 0                     # Réinitialise la largeur pour la prochaine ligne.
