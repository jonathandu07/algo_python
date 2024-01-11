# Affiche une matrice remplie de caractères aléatoires

HAUTEUR = 20  # Définit une constante pour la hauteur de la matrice (nombre de lignes).
LARGEUR = 30  # Définit une constante pour la largeur de la matrice (nombre de colonnes).

def afficher_matrice(matrice):
    """
    Affiche une matrice de caractères.

    Args:
      matrice: La matrice à afficher.
    """
    # Boucle sur chaque ligne de la matrice.
    for i in range(HAUTEUR):
        # Boucle sur chaque colonne de la ligne actuelle.
        for j in range(LARGEUR):
            # Affiche le caractère situé à la position [i][j] sans retour à la ligne.
            print(matrice[i][j], end="")
        # Une fois la ligne terminée, passe à la ligne suivante.
        print()

def generer_matrice(hauteur, largeur):
    """
    Génère une matrice de caractères aléatoires.

    Args:
      hauteur: La hauteur de la matrice.
      largeur: La largeur de la matrice.

    Returns:
      La matrice générée.
    """
    matrice = []  # Initialise une liste vide pour la matrice.
    # Boucle sur chaque ligne de la matrice à créer.
    for i in range(hauteur):
        matrice.append([])  # Ajoute une nouvelle ligne sous forme de liste vide.
        # Boucle sur chaque colonne de la ligne actuelle.
        for j in range(largeur):
            # Ajoute un caractère aléatoire dans la ligne.
            matrice[i].append(chr(random.randint(ord(' '), ord('²'))))
    return matrice  # Renvoie la matrice remplie.

if __name__ == "__main__":
    # Vérifie si le script est le programme principal.
    matrice = generer_matrice(HAUTEUR, LARGEUR)  # Génère une matrice avec les dimensions spécifiées.
    afficher_matrice(matrice)  # Affiche la matrice générée.
