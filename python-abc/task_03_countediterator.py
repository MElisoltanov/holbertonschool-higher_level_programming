#!/usr/bin/python3
"""This module defines the CountedIterator
class that tracks iteration count."""

# Définition de la classe CountedIterator.
# Une classe est un modèle pour créer des objets en Python.
class CountedIterator:
    """Iterator that counts the number of items iterated."""

    # La méthode __init__ est le constructeur de la classe.
    # Elle est appelée automatiquement lors de la création
    # d'une nouvelle instance de la classe.
    def __init__(self, iterable):
        # 'self' fait référence à l'objet courant.
        # 'iterable' est un objet sur lequel on peut itérer
        # (par exemple une liste, un tuple, une chaîne de caractères).
        # La fonction 'iter()' transforme l'objet 'iterable'
        # en un itérateur, qui permet d'obtenir les éléments
        # un par un.
        self.iterator = iter(iterable)
        # On initialise l'attribut 'count' à 0.
        # Cet attribut va compter le nombre d'éléments
        # déjà parcourus.
        self.count = 0

    # La méthode __next__ permet d'obtenir l'élément suivant
    # de l'itérateur. Elle est appelée à chaque itération
    # (par exemple dans une boucle for ou avec la fonction next()).
    def __next__(self):
        # On récupère l'élément suivant de l'itérateur
        # avec la fonction 'next()'.
        item = next(self.iterator)
        # On incrémente le compteur 'count' de 1
        # à chaque fois qu'on récupère un élément.
        self.count += 1
        # On retourne l'élément récupéré.
        return item

    # La méthode 'get_count' permet d'obtenir la valeur
    # actuelle du compteur, c'est-à-dire le nombre
    # d'éléments déjà parcourus.
    def get_count(self):
        """Return the number of items iterated so far."""
        # On retourne la valeur de l'attribut 'count'.
        return self.count
