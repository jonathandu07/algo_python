# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 16:18:23 2024

@author: alpha
"""
import random
# Jeu de la bataille navale avec un seul bateau d'une case

HAUTEUR = 4
LARGEUR = 4
PLOUF = "~"
BATEAU = "b"
EAU = "e"

def afficher_plateau(plateau):
  """
  Affiche un plateau de bataille navale.

  Args:
    plateau: Le plateau à afficher.
  """

  for i in range(HAUTEUR):
    for j in range(LARGEUR):
      print(plateau[i][j], end="")
    print()

def placer_bateau(plateau):
  """
  Place un bateau d'une case sur une case choisie aléatoirement.

  Args:
    plateau: Le plateau sur lequel placer le bateau.
  """

  i = random.randint(0, HAUTEUR - 1)
  j = random.randint(0, LARGEUR - 1)
  plateau[i][j] = BATEAU

def jouer(plateau):
  """
  Joue une partie de bataille navale.

  Args:
    plateau: Le plateau de jeu.

  Returns:
    True si le joueur a gagné, False sinon.
  """

  # Initialisation du plateau de jeu
  for i in range(HAUTEUR):
    for j in range(LARGEUR):
      plateau[i][j] = EAU

  # Placement du bateau
  placer_bateau(plateau)

  # Affichage du plateau du jeu
  afficher_plateau(plateau)

  # Boucle de jeu
  while True:
    # Saisie des coordonnées de tir
    i = int(input("Quelle colonne (entre 1 et {} ) : ".format(LARGEUR))) - 1
    j = int(input("Quelle ligne (entre 1 et {} ) : ".format(HAUTEUR))) - 1

    # Test du tir
    if plateau[j][i] != BATEAU:
      plateau[j][i] = PLOUF
      print("Plouf !")
    else:
      return True

  print("Touché coulé ! Bravo, vous avez gagné !")
  return False

if __name__ == "__main__":
  plateau = [[EAU for i in range(LARGEUR)] for j in range(HAUTEUR)]
  jouer(plateau)
