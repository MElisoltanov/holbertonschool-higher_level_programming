#!/usr/bin/python3
"""Define a class Square with a private size attribute."""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, situé dans /usr/bin/python3.

# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, utilisée pour documenter
# le module ou le fichier. Elle explique brièvement le but du fichier.


class Square:
    """Class that define a Square by its size."""
    # Déclaration d'une nouvelle classe nommée Square.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring de la classe décrit son objectif.

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            Size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # __init__ est une méthode spéciale appelée automatiquement lors de la création
        # d'une nouvelle instance de la classe. Elle sert à initialiser l'objet.
        # self fait référence à l'instance courante de la classe.
        # size est un paramètre optionnel (valeur par défaut : 0).
        # La docstring de la méthode explique son fonctionnement, ses paramètres
        # et les exceptions qu'elle peut lever.

        if not isinstance(size, int):
            # Vérifie si size n'est pas un entier (int).
            # isinstance(obj, type) retourne True si obj est du type indiqué.
            raise TypeError("size must be an integer")
            # Si size n'est pas un entier, lève une exception TypeError
            # avec un message d'erreur explicite.

        if size < 0:
            # Vérifie si size est inférieur à 0.
            raise ValueError("size must be >= 0")
            # Si size est négatif, lève une exception ValueError
            # avec un message d'erreur explicite.

        self.__size = size
        # Attribue la valeur de size à l'attribut privé __size de l'objet.
        # Le double underscore (__) rend l'attribut privé (non accessible directement
        # depuis l'extérieur de la classe).

    def area(self):
        """Return the current square area."""
        # Définition d'une méthode nommée area, qui calcule et retourne l'aire du carré.
        # self permet d'accéder aux attributs et méthodes de l'objet courant.
        # La docstring décrit ce que fait la méthode.

        return self.__size * self.__size
        # Calcule l'aire du carré en multipliant la taille (__size) par elle-même.
        # L'opérateur * sert à faire une multiplication.
        # return permet de renvoyer le résultat à l'appelant de la méthode.
