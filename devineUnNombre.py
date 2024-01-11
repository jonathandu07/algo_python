# Jeu de devinette du nombre

# Déclaration des variables et constantes
min = 1                # Limite inférieure pour le nombre aléatoire.
max = 100              # Limite supérieure pour le nombre aléatoire.
reponse = None         # Variable pour stocker la réponse de l'utilisateur.
nb_tentatives = 0      # Compteur pour le nombre de tentatives.
valeur = None          # Variable pour stocker le nombre deviné par le programme.
saisie_ok = False      # Flag pour vérifier si la saisie de l'utilisateur est valide.

# Le caractère saisi n'a pas d'importance. C'est pour attendre que l'utilisateur ait choisi son nombre
reponse = input("Choisissez un nombre compris entre {} et {}, puis appuyez sur une touche".format(min, max))

# Boucle principale
while reponse != "=":
    # Génération d'un nombre aléatoire
    valeur = random.randint(min, max)  # Génère un nombre aléatoire entre les limites min et max.

    # Affichage de la proposition
    print("Je tente {}. Est-ce plus, moins ou est-ce le nombre (+/-/=) ?".format(valeur))
    nb_tentatives += 1  # Incrémente le compteur de tentatives.

    # Boucle de saisie de la réponse
    while not saisie_ok:
        saisie_ok = True
        reponse = input()  # Demande à l'utilisateur de répondre par "+", "-" ou "=".

        # Traitement de la réponse
        if reponse == "+":
            min = valeur + 1  # Ajuste la limite inférieure pour la prochaine tentative.
        elif reponse == "-":
            max = valeur - 1  # Ajuste la limite supérieure pour la prochaine tentative.
        elif reponse == "=":
            print("Super ! J'ai réussi en {} tentatives".format(nb_tentatives))  # Affiche le succès.
        else:
            saisie_ok = False  # Indique une saisie invalide.
            print("Erreur de saisie. Saisissez +, - ou =")  # Demande de saisir une réponse valide.
