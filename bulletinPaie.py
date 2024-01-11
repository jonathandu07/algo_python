# Déclaration des variables et constantes
nom = None                 # Variable pour stocker le nom de l'employé
prenom = None              # Variable pour stocker le prénom de l'employé
statut = None              # Variable pour stocker le statut de l'employé
nb_heures = None           # Variable pour stocker le nombre d'heures travaillées
nb_enfants = None          # Variable pour stocker le nombre d'enfants de l'employé
saisie = None              # Variable pour stocker la saisie temporaire de l'utilisateur
prime_enfants = None       # Variable pour stocker le montant de la prime pour enfants
salaire_hors_prime = None  # Variable pour stocker le salaire hors prime
salaire_a_verser = None    # Variable pour stocker le salaire total à verser
majoration = None          # Variable pour stocker le taux de majoration des heures supplémentaires
taux_horaire = 11.07       # Constante représentant le taux horaire

# Récupération des données nécessaires par une saisie
nom = input("Saisir le nom de famille \n")
prenom = input("Saisir le prénom \n")

# Affichage du menu et saisie du statut
print("Statut ? \n")
print("1 - Agent de service \n")
print("2 - Employé de bureau \n")
print("3 - Cadre \n")
saisie = input()
statut = ""
while statut not in ["1", "2", "3"]:
    print("Veuillez saisir un statut valide (1, 2 ou 3) \n")
    saisie = input()
    statut = saisie

# Saisie du nombre d'heures travaillées
nb_heures = int(input("Saisir le nombre d'heures travaillées \n"))

# Saisie du nombre d'enfants
nb_enfants = int(input("Saisir le nombre d'enfant \n"))

# Traitement et Calcul des données pour établir la fiche de paie simplifiée
# 1. Calcul de la prime selon le nombre d'enfants
if nb_enfants == 0:
    prime_enfants = 0
elif nb_enfants == 1:
    prime_enfants = 20
elif nb_enfants == 2:
    prime_enfants = 50
else:
    prime_enfants = 70 + 20 * (nb_enfants - 2)

# 2. Calcul du salaire hors prime selon le nombre d'heures travaillées
# et en tenant compte de la majoration si besoin
if nb_heures < 169:
    salaire_hors_prime = nb_heures * taux_horaire
elif nb_heures > 180:
    majoration = 1.5
    salaire_hors_prime = taux_horaire * 169 + taux_horaire * majoration * 12 + taux_horaire * 1.6 * (nb_heures - 180)
else:
    majoration = 1.5
    salaire_hors_prime = taux_horaire * 169 + taux_horaire * majoration * (nb_heures - 168)

# 3. Calcul du salaire total à verser
salaire_a_verser = salaire_hors_prime + prime_enfants

# Affichage de la fiche de paie
print("BULLETIN DE PAIE")
print("Nom :", nom)
print("Prénom :", prenom)
print("Statut :", statut)
print("Nombre d'heures travaillées :", nb_heures)
print("Salaire hors prime :", salaire_hors_prime)
print("Nombre d'enfants :", nb_enfants)
print("Prime enfants :", prime_enfants)
print("Salaire :", salaire_a_verser)
