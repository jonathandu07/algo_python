# Affiche une forme géométrique choisie par l'utilisateur

# Variables
taille = None        # Variable pour stocker la taille de la forme.
car = None           # Variable pour stocker le caractère utilisé pour dessiner.
choixDessin = None   # Variable pour stocker le choix de la forme.
i = None             # Variable de boucle pour les colonnes.
j = None             # Variable de boucle pour les lignes.

# Initialisation
taille = int(input("taille ? "))         # Demande à l'utilisateur la taille de la forme.
car = input("caractère ? ")              # Demande le caractère à utiliser pour dessiner.

# Saisie de la forme
while True: 
    try:
        choixDessin = int(input("forme ?\n1 - rectangle plein\n2 - rectangle creux\n3 - croix\n4 - triangle rectangle\n5 - losange\n6 - damier\n"))
        # Demande le type de forme à dessiner.
        if choixDessin < 1 or choixDessin > 6:
            raise ValueError("Choix incorrect")   # Vérifie si le choix est entre 1 et 6.
        break
    except ValueError:
        print("Veuillez saisir un nombre compris entre 1 et 6")
        # En cas de choix invalide, affiche un message d'erreur.

# Affichage de la forme
for j in range(taille):       # Boucle sur les lignes.
    for i in range(taille):   # Boucle sur les colonnes.
        # Dessine un rectangle plein.
        if choixDessin == 1:
            print(car, end="") 
        # Dessine un rectangle creux.
        elif choixDessin == 2:
            if i == 0 or i == taille - 1 or j == 0 or j == taille - 1:
                print(car, end="") 
            else:
                print(" ", end="")
        # Dessine une croix.
        elif choixDessin == 3:
            if i == j or i + j - 1 == taille:
                print(car, end="")
            else:
                print(" ", end="")
        # Dessine un triangle rectangle.
        elif choixDessin == 4:
            if j == taille - 1 or i == 0 or i == j:
                print(car, end="")
            else:
                print(" ", end="")
        # Dessine un losange.
        elif choixDessin == 5:
            if i + j - 1 == (taille + 1) // 2 or i + j - 1 == taille + (taille // 2) or i - j == taille // 2 or j - i == taille // 2:
                print(car, end="")
            else:
                print(" ", end="")
        # Dessine un damier.
        elif choixDessin == 6:
            if (i + j) % 2 == 0:
                print(car, end="")
            else:
                print(" ", end="")
    print()  # Passe à la ligne suivante après chaque ligne de la forme.
