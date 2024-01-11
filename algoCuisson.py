# Indique le temps de cuisson d'une viande

# Variables
viande = None
cuisson = None
poids = None
coefficient = None

# Constantes
BOEUF = 1
AGNEAU = 2
BLEU = 1
A_POINT = 2
BIEN_CUIT = 3
UNE_MINUTE = 60

# Choix du type de viande
print("Viande ?")
print("1 - Boeuf")
print("2 - Agneau")
viande = int(input())

# Choix du type de cuisson
print("Cuisson ?")
print("1 - Bleu")
print("2 - A point")
print("3 - Bien cuit")
cuisson = int(input())

# Choix du poids de la viande
poids = int(input("Poids en gramme ? "))

# Calcul du coefficient de cuisson
if viande == BOEUF:
    if cuisson == BLEU:
        coefficient = 10 / 500
    elif cuisson == A_POINT:
        coefficient = 17 / 500
    else:
        coefficient = 25 / 500
else:
    if cuisson == BLEU:
        coefficient = 15 / 400
    elif cuisson == A_POINT:
        coefficient = 25 / 400
    else:
        coefficient = 40 / 400

# Calcul du temps de cuisson
temps_de_cuisson = poids * coefficient * UNE_MINUTE

# Affichage du résultat
print("Le temps de cuisson est de", temps_de_cuisson, "secondes.")
