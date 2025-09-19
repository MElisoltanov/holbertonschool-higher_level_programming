#!/usr/bin/python3
"""Defines a Rectangle class with instance counter."""
# Les guillemets triples (""" """) permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, utilisée pour décrire le
# fichier ou le module. Elle peut être lue par des outils de documentation.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Cette docstring décrit la classe Rectangle.
    # Une classe est un plan (ou modèle) pour créer des objets.

    number_of_instances = 0  # Attribut de classe
    # Ceci est un attribut de classe, partagé par toutes les instances
    # de Rectangle. Il compte le nombre d'objets Rectangle créés.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # __init__ est le constructeur de la classe. Il est appelé
        # automatiquement lors de la création d'un nouvel objet.
        # self fait référence à l'objet créé.
        # width et height sont des paramètres avec des valeurs par défaut (0).
        self.width = width
        # On utilise le setter width pour valider et assigner la largeur.
        self.height = height
        # On utilise le setter height pour valider et assigner la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # On retourne la valeur privée __width (avec deux underscores pour
        # indiquer que c'est un attribut interne à la classe).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Cette méthode permet d'assigner une valeur à width tout en
        # effectuant des vérifications.
        if not isinstance(value, int):
            # On vérifie que la valeur est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur est positive ou nulle.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__width = value
        # Si tout est correct, on assigne la valeur à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Même principe que pour width, mais pour la hauteur.
        return self.__height
        # On retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour la hauteur, avec vérifications.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie que la valeur est positive ou nulle.
            raise ValueError("height must be >= 0")
            # Lève une exception si la valeur est négative.
        self.__height = value
        # Assigne la valeur à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode pour calculer l'aire du rectangle.
        return self.__width * self.__height
        # Aire = largeur x hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode pour calculer le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Périmètre = 2 x (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with '#' characters.
        """
        # __str__ permet de définir ce qui s'affiche quand on fait print(objet).
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, on retourne une chaîne vide.
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # On crée une chaîne composée de lignes de '#' :
        # - "#" * self.__width crée une ligne de '#' de la largeur du rectangle.
        # - for _ in range(self.__height) répète cette ligne pour chaque hauteur.
        # - "\n".join(...) assemble toutes les lignes avec un saut de ligne.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # __repr__ retourne une chaîne qui permet de recréer l'objet.
        return f"Rectangle({self.__width}, {self.__height})"
        # f"..." est une f-string (chaîne formatée) qui insère les valeurs
        # de __width et __height dans la chaîne.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement counter.
        """
        # __del__ est appelée automatiquement quand l'objet est détruit
        # (par exemple, avec del ou à la fin du programme).
        print("Bye rectangle...")
        # print affiche un message à l'écran lors de la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # On décrémente le compteur d'instances.
