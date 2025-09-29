#!/usr/bin/python3
"""This module defines the VerboseList class that extends list with notifications."""

# Déclaration de la classe VerboseList qui hérite de la classe intégrée 'list'
class VerboseList(list):
    """A list that prints notifications when modified."""

    # Définition de la méthode 'append' qui ajoute un élément à la fin de la liste
    def append(self, item):
        # Appel de la méthode 'append' de la classe parente 'list' pour ajouter l'élément
        super().append(item)
        # La fonction 'print' affiche un message à l'écran
        # Les crochets [] sont utilisés pour entourer l'élément ajouté
        # Le 'f' devant la chaîne indique une f-string, permettant d'insérer la valeur de 'item'
        print(f"Added [{item}] to the list.")

    # Définition de la méthode 'extend' qui ajoute plusieurs éléments à la liste
    def extend(self, iterable):
        # 'len(iterable)' retourne le nombre d'éléments dans l'objet 'iterable'
        count = len(iterable)
        # Appel de la méthode 'extend' de la classe parente pour ajouter les éléments
        super().extend(iterable)
        # Affiche le nombre d'éléments ajoutés grâce à la f-string
        print(f"Extended the list with [{count}] items.")

    # Définition de la méthode 'remove' qui supprime un élément de la liste
    def remove(self, item):
        # Affiche le message avant de supprimer l'élément
        print(f"Removed [{item}] from the list.")
        # Appel de la méthode 'remove' de la classe parente pour supprimer l'élément
        super().remove(item)

    # Définition de la méthode 'pop' qui retire et retourne un élément de la liste
    # 'index=-1' signifie que par défaut, le dernier élément sera retiré
    def pop(self, index=-1):
        # Récupère l'élément à l'index donné avant de le retirer
        item = self[index]
        # Affiche le message avec l'élément retiré
        print(f"Popped [{item}] from the list.")
        # Appel de la méthode 'pop' de la classe parente pour retirer l'élément
        # et retourne cet élément
        return super().pop(index)
