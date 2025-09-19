#!/usr/bin/python3
"""Defines a Rectangle class with width and height properties,
area and perimeter methods.
"""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.
# Les triples guillemets (""") servent à écrire une chaîne de caractères multilignes,
# ici utilisée pour la docstring du module, qui décrit brièvement le contenu du fichier.

class Rectangle:
    """Class that define a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring de la classe explique son but.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale appelée lors de la création d'une nouvelle instance de Rectangle.
        # Le double underscore (__init__) indique qu'il s'agit d'une méthode spéciale.
        # self fait référence à l'instance créée.
        # width et height sont des paramètres avec une valeur par défaut de 0.
        # La docstring décrit les paramètres attendus.
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        # Cela déclenche le setter @width.setter pour valider la valeur.
        self.height = height
        # Idem pour height, on utilise le setter pour valider la valeur.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        # Permet d'accéder à la largeur via instance.width.
        return self.__width
        # Retourne la valeur de l'attribut privé __width.
        # Le double underscore rend l'attribut privé (non accessible directement).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir la valeur de width
        # tout en effectuant des vérifications.
        if not isinstance(value, int):
            # Vérifie si value est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("width must be >= 0")
            # Si value est négatif, lève une exception ValueError.
        self.__width = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Décorateur @property pour accéder à la hauteur comme un attribut.
        return self.__height
        # Retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Décorateur @height.setter pour définir la hauteur avec validation.
        if not isinstance(value, int):
            # Vérifie si value est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("height must be >= 0")
            # Lève une exception si value est négatif.
        self.__height = value
        # Si tout est correct, assigne value à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode pour calculer l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode pour calculer le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.
