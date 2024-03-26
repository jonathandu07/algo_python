TAILLE = 100  # Définit une constante TAILLE qui est la taille maximale du tableau des notes.
STOP = -1     # Définit une constante STOP utilisée pour arrêter la saisie des notes.

def saisir_note():
  """
  Cette fonction permet à l'utilisateur de saisir une note.
  Elle retourne la note saisie sous forme de nombre flottant.
  """

  note = float(input("Notes ? "))  # Demande à l'utilisateur de saisir une note, convertit cette entrée en nombre flottant et l'affecte à la variable 'note'.
  return note                      # Retourne la note saisie.

def calculer_moyenne(notes, nb_val):
  """
  Calcule la moyenne des notes.

  Args:
    notes: Liste des notes.
    nb_val: Nombre de notes valides dans la liste.

  Returns:
    La moyenne calculée des notes.
  """

  total = 0                         # Initialise une variable 'total' à 0 pour cumuler la somme des notes.
  for i in range(nb_val):           # Parcourt les 'nb_val' premiers éléments du tableau 'notes'.
    total += notes[i]               # Ajoute la note à l'index 'i' au total.
  return total / nb_val             # Calcule et retourne la moyenne en divisant le total par le nombre de notes.

def main():
  """
  Fonction principale qui orchestre le processus de saisie des notes, vérifie les conditions et affiche la moyenne.
  """

  notes = [0] * TAILLE              # Initialise un tableau 'notes' avec des zéros, de taille TAILLE.
  nb_val = 0                        # Initialise un compteur pour le nombre de notes valides saisies.
  saisie = saisir_note()            # Appelle la fonction 'saisir_note' et stocke la note saisie dans 'saisie'.

  while saisie != STOP and nb_val < TAILLE:  # Tant que l'utilisateur n'entre pas STOP et que la taille maximale n'est pas atteinte...
    notes[nb_val] = saisie                   # Stocke la note saisie dans le tableau à l'index 'nb_val'.
    nb_val += 1                              # Incrémente le compteur de notes valides.
    saisie = saisir_note()                   # Demande une nouvelle note.

  if saisie == STOP:                    # Si l'utilisateur a saisi STOP...
    if nb_val > 0:                      # ...et s'il y a au moins une note valide...
      print("La moyenne des notes (", end="")
      total = notes[0]                  # Initialise 'total' avec la première note pour l'affichage.
      for i in range(1, nb_val):        # Parcourt et affiche chaque note (sauf la première déjà initialisée).
        total += notes[i]               # Ajoute la note au total pour l'affichage.
        print(", ", end="")
      print(") est de ", calculer_moyenne(notes, nb_val))  # Affiche la moyenne calculée par la fonction 'calculer_moyenne'.
    else:
      print("Aucune note n'a été saisie")  # Si aucune note n'a été saisie.
  else:
    print("La capacité du tableau a été dépassée, désolé")  # Si la taille maximale du tableau est dépassée.

if __name__ == "__main__":
  main()  # Exécute la fonction 'main' si le script est exécuté comme programme principal.
