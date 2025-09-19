#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
and provides methods for area, perimeter, and string representation.
"""

# Le shebang (#!/usr/bin/python3) indique au système d'exploitation
# d'utiliser l'interpréteur Python 3 pour exécuter ce fichier.
# Il doit toujours être placé en première ligne du fichier.

# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, ils servent à écrire une docstring,
# c'est-à-dire un commentaire qui décrit le module.
# Les docstrings sont utilisées par la documentation automatique de Python.

class Rectangle:
    """Represents a rectangle."""

    # Déclaration d'une classe nommée Rectangle.
    # Une classe est un modèle pour créer des objets (ici, des rectangles).
    # Les classes commencent toujours par une majuscule par convention.

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        # Méthode spéciale __init__ appelée automatiquement lors de la création
        # d'un nouvel objet Rectangle. Elle initialise les attributs de l'objet.
        # self fait référence à l'instance courante de la classe.
        # width et height sont des paramètres avec des valeurs par défaut (0).
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        self.height = height
        # On assigne la valeur du paramètre height à l'attribut height de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Méthode spéciale appelée lorsqu'on accède à l'attribut width.
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # Retourne la valeur de l'attribut privé __width.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        # Méthode spéciale appelée lorsqu'on modifie l'attribut width.
        # Le décorateur @width.setter permet de définir la valeur de width.
        if not isinstance(value, int):
            # Vérifie si value n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("width must be >= 0")
            # Si value est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Méthode spéciale appelée lorsqu'on accède à l'attribut height.
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__height
        # Retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        # Méthode spéciale appelée lorsqu'on modifie l'attribut height.
        # Le décorateur @height.setter permet de définir la valeur de height.
        if not isinstance(value, int):
            # Vérifie si value n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("height must be >= 0")
            # Si value est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur (__width) par la hauteur (__height) et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation of the
        rectangle with '#' characters.
        """
        # Méthode spéciale appelée par print() ou str().
        # Retourne une chaîne de caractères représentant le rectangle avec des '#'.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        lines = []
        # Crée une liste vide pour stocker chaque ligne du rectangle.
        for _ in range(self.__height):
            # Boucle autant de fois que la hauteur du rectangle.
            lines.append("#" * self.__width)
            # Ajoute une ligne composée de '#' répété largeur fois.
        return "\n".join(lines)
        # Assemble toutes les lignes avec un saut de ligne (\n) entre chaque.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet.
        # Utilisée par la fonction repr().
        return f"Rectangle({self.__width}, {self.__height})"
        # f-string : permet d'insérer les valeurs de __width et __height dans la chaîne.
        # La chaîne retournée peut être utilisée avec eval() pour recréer l'objet.
