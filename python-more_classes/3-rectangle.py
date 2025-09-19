#!/usr/bin/python3
"""Define a Rectangle class with width and height,
    area, perimeter and string representation.
"""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Ici, '/usr/bin/python3' est le chemin de l'interpréteur.
# Les triples guillemets (""") permettent d'écrire une chaîne de caractères multilignes,
# appelée docstring. Elle sert à documenter le module ou la classe.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring ici décrit le but de la classe.

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale appelée lors de la création d'une nouvelle instance de la classe.
        # 'self' fait référence à l'objet créé.
        # 'width' et 'height' sont des paramètres avec des valeurs par défaut de 0.
        self.width = width
        # On assigne la valeur du paramètre 'width' à l'attribut 'width' de l'objet.
        self.height = height
        # On assigne la valeur du paramètre 'height' à l'attribut 'height' de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # Retourne la valeur de l'attribut privé '__width'.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir la valeur de 'width'.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("width must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si les vérifications sont passées, assigne la valeur à l'attribut privé '__width'.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Le décorateur @property permet d'accéder à 'height' comme un attribut.
        return self.__height
        # Retourne la valeur de l'attribut privé '__height'.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Le décorateur @height.setter permet de définir la valeur de 'height'.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("height must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si les vérifications sont passées, assigne la valeur à l'attribut privé '__height'.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur pour obtenir l'aire.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation
            of the rectangle with '#' characters.
        """
        # Méthode spéciale qui définit la représentation en chaîne de l'objet.
        # Appelée par la fonction print() ou str().
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        lines = []
        # Crée une liste vide pour stocker chaque ligne du rectangle.
        for _ in range(self.__height):
            # Boucle autant de fois que la hauteur du rectangle.
            lines.append("#" * self.__width)
            # Ajoute une chaîne composée de '#' répétée 'width' fois à la liste.
        return "\n".join(lines)
        # Assemble toutes les lignes avec un saut de ligne '\n' entre chaque,
        # pour former le rectangle en texte.
