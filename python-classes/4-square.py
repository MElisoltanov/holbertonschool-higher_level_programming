#!/usr/bin/python3
"""Defines a class Square with a private size attribute and property."""
# Les triples guillemets (""" """) définissent une chaîne de caractères multilignes,
# utilisée ici comme docstring (documentation) pour le module.
# Cette docstring explique brièvement le but du fichier ou du module.


class Square:
    """Class the defines à Square by its size."""
    # Ceci est une docstring pour la classe Square.
    # Elle explique que la classe définit un carré par sa taille.

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # __init__ est une méthode spéciale appelée constructeur.
        # Elle est appelée automatiquement lors de la création d'un nouvel objet Square.
        # self fait référence à l'instance courante de la classe.
        # size=0 signifie que le paramètre size est optionnel et vaut 0 par défaut.
        self.size = size
        # On utilise la propriété size (définie plus bas) pour initialiser la taille du carré.
        # Cela permet de profiter de la validation faite dans le setter.

    @property
    def size(self):
        """Get the size of the square."""
        # Cette méthode est un getter pour l'attribut privé __size.
        # Le décorateur @property permet d'accéder à cette méthode comme à un attribut.
        return self.__size
        # On retourne la valeur de l'attribut privé __size.
        # Les deux underscores (__) rendent l'attribut privé (non accessible directement de l'extérieur).

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        # Cette méthode est un setter pour l'attribut size.
        # Le décorateur @size.setter permet de définir la valeur de size avec des vérifications.
        if not isinstance(value, int):
            # On vérifie si value n'est pas un entier (int).
            raise TypeError("size must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError avec un message explicite.
        if value < 0:
            # On vérifie si value est inférieur à 0.
            raise ValueError("size must be >= 0")
            # Si value est négatif, on lève une exception ValueError avec un message explicite.
        self.__size = value
        # Si toutes les vérifications sont passées, on assigne value à l'attribut privé __size.

    def area(self):
        """Return the current square area."""
        # Cette méthode calcule et retourne l'aire du carré.
        return self.__size * self.__size
        # On multiplie la taille (__size) par elle-même pour obtenir l'aire (côté x côté).
        # Le symbole * est l'opérateur de multiplication en Python.
