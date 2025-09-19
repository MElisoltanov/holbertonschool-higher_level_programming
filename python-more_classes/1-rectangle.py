#!/usr/bin/python3
""" Defines a Rectangle class with width and height properties."""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, donc le script sera
# exécuté avec Python 3.
#
# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, c'est-à-dire un commentaire
# spécial utilisé pour décrire le module ou la classe. Cette docstring explique
# que le fichier définit une classe Rectangle avec des propriétés de largeur
# (width) et de hauteur (height).

class Rectangle:
    """Class thart defines a rectangle by its width and height."""
    # Déclaration de la classe Rectangle. Le mot-clé 'class' permet de définir
    # un nouveau type d'objet. Ici, on crée une classe nommée Rectangle.
    #
    # La docstring de la classe décrit brièvement ce que fait la classe :
    # elle définit un rectangle à partir de sa largeur et de sa hauteur.

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale __init__ appelée automatiquement lors de la création
        # d'une nouvelle instance de la classe Rectangle.
        #
        # Les paramètres width et height sont optionnels et valent 0 par défaut.
        # Cela signifie que si on ne précise rien, le rectangle aura une largeur
        # et une hauteur de 0.
        #
        # La docstring de la méthode explique son rôle et décrit les arguments.
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        # Cela déclenche le setter (défini plus bas) qui valide la valeur.
        self.height = height
        # On assigne la valeur du paramètre height à l'attribut height de l'objet.
        # Cela déclenche aussi le setter qui valide la valeur.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en propriété.
        # Cela permet d'accéder à la largeur de l'objet comme un attribut
        # (ex: mon_rectangle.width) au lieu d'appeler une méthode.
        return self.__width
        # On retourne la valeur de l'attribut privé __width.
        # Les deux underscores (__) devant width signifient que cet attribut
        # est privé : il ne doit pas être accédé directement en dehors de la classe.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir le comportement lors de
        # l'affectation d'une nouvelle valeur à la propriété width.
        # Cela permet de valider la valeur avant de la stocker.
        if not isinstance(value, int):
            # On vérifie que la valeur donnée est bien un entier (int).
            # isinstance(value, int) retourne True si value est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError
            # avec un message explicite.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError
            # avec un message explicite.
        self.__width = value
        # Si toutes les vérifications sont passées, on assigne la valeur à
        # l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Comme pour width, ce décorateur permet d'accéder à la hauteur
        # comme une propriété (ex: mon_rectangle.height).
        return self.__height
        # On retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Le décorateur @height.setter permet de définir le comportement lors
        # de l'affectation d'une nouvelle valeur à la propriété height.
        if not isinstance(value, int):
            # On vérifie que la valeur donnée est bien un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("height must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__height = value
        # Si toutes les vérifications sont passées, on assigne la valeur à
        # l'attribut privé __height.
