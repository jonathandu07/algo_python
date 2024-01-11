# Jeu de questions-réponses "Deux erreurs de moins"

# Déclaration des variables et constantes
nb_tentatives = 1           # Compteur pour le nombre de tentatives de l'utilisateur.
saisie = None               # Variable pour stocker la réponse de l'utilisateur.
MAX_TENTATIVES = 5          # Constante pour le nombre maximal de tentatives autorisées.

# Demander la première réponse
saisie = input("Quelle est la capitale de la France ?")  # Pose la question à l'utilisateur.

# Boucle principale
while saisie != "Paris" and MAX_TENTATIVES - nb_tentatives != 0:
    # Affichage du message d'erreur
    print("Mauvaise réponse !")
    # Informe l'utilisateur du nombre de tentatives restantes.
    print("Plus que {} tentative(s)".format(MAX_TENTATIVES - nb_tentatives))
    # Demande d'une nouvelle réponse
    saisie = input("Quelle est la capitale de la France ?")
    # Incrémente le compteur de tentatives.
    nb_tentatives += 1

# Affichage du résultat
if MAX_TENTATIVES - nb_tentatives != 0:
    # Si l'utilisateur trouve la bonne réponse avant d'atteindre le nombre maximal de tentatives.
    print("Bravo !")
else:
    # Si l'utilisateur épuise toutes ses tentatives sans trouver la bonne réponse.
    print("Revoyez votre géographie !")
