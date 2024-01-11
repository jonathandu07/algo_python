# Indique le temps de cuisson d'une viande

# Variables
viande = None         # Initialisation de la variable 'viande' pour stocker le choix de la viande.
cuisson = None        # Initialisation de la variable 'cuisson' pour stocker le choix du type de cuisson.
poids = None          # Initialisation de la variable 'poids' pour stocker le poids de la viande en grammes.
coefficient = None    # Initialisation de la variable 'coefficient' pour calculer le temps de cuisson.

# Constantes
BOEUF = 1             # Constante représentant le choix du boeuf.
AGNEAU = 2            # Constante représentant le choix de l'agneau.
BLEU = 1              # Constante pour le type de cuisson 'Bleu'.
A_POINT = 2           # Constante pour le type de cuisson 'A point'.
BIEN_CUIT = 3         # Constante pour le type de cuisson 'Bien cuit'.
UNE_MINUTE = 60       # Constante pour convertir le temps en secondes.

# Choix du type de viande
print("Viande ?")
print("1 - Boeuf")
print("2 - Agneau")
viande = int(input()) # Demande à l'utilisateur de choisir le type de viande.

# Choix du type de cuisson
print("Cuisson ?")
print("1 - Bleu")
print("2 - A point")
print("3 - Bien cuit")
cuisson = int(input()) # Demande à l'utilisateur de choisir le type de cuisson.

# Choix du poids de la viande
poids = int(input("Poids en gramme ? ")) # Demande à l'utilisateur de saisir le poids de la viande en grammes.

# Calcul du coefficient de cuisson
if viande == BOEUF:     # Condition pour le choix du boeuf.
    if cuisson == BLEU: # Condition pour la cuisson bleu du boeuf.
        coefficient = 10 / 500
    elif cuisson == A_POINT: # Condition pour la cuisson à point du boeuf.
        coefficient = 17 / 500
    else:              # Condition pour la cuisson bien cuite du boeuf.
        coefficient = 25 / 500
else:                   # Condition pour le choix de l'agneau.
    if cuisson == BLEU: # Condition pour la cuisson bleu de l'agneau.
        coefficient = 15 / 400
    elif cuisson == A_POINT: # Condition pour la cuisson à point de l'agneau.
        coefficient = 25 / 400
    else:              # Condition pour la cuisson bien cuite de l'agneau.
        coefficient = 40 / 400

# Calcul du temps de cuisson
temps_de_cuisson = poids * coefficient * UNE_MINUTE # Calcul du temps de cuisson en secondes.

# Affichage du résultat
print("Le temps de cuisson est de", temps_de_cuisson, "secondes.") # Affiche le temps de cuisson calculé.
