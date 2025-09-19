#!/usr/bin/python3
"""Defines a Rectangle class with comparison static method."""
# Ceci est une chaîne de caractères spéciale appelée "docstring".
# Elle sert à documenter le fichier ou le module.
# Les triples guillemets (""") permettent d'écrire sur plusieurs lignes.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Cette docstring décrit la classe Rectangle.
    # Une classe est un plan pour créer des objets (ici, des rectangles).

    number_of_instances = 0
    # Variable de classe : elle compte combien d'instances (objets)
    # Rectangle ont été créées. Elle est partagée par tous les objets.

    print_symbol = "#"
    # Variable de classe : définit le symbole utilisé pour afficher
    # le rectangle avec la méthode __str__. Par défaut, c'est "#".

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée automatiquement lors de la création
        # d'un nouvel objet Rectangle. Elle initialise la largeur et la hauteur.
        # Les paramètres width et height ont des valeurs par défaut de 0.
        self.width = width
        # Attribut d'instance : la largeur du rectangle.
        # On utilise le setter (voir plus bas) pour valider la valeur.
        self.height = height
        # Attribut d'instance : la hauteur du rectangle.
        # On utilise aussi le setter pour valider la valeur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Cette méthode permet d'accéder à la largeur (width)
        # comme s'il s'agissait d'un attribut simple.
        return self.__width
        # On retourne la valeur privée __width (avec deux underscores),
        # qui stocke la largeur réelle.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Cette méthode permet d'attribuer une valeur à width
        # tout en vérifiant qu'elle est correcte.
        if not isinstance(value, int):
            # On vérifie que la valeur est un entier (int).
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__width = value
        # Si tout est correct, on stocke la valeur dans l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Permet d'accéder à la hauteur (height) comme un attribut simple.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Permet d'attribuer une valeur à height avec validation.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie que la valeur n'est pas négative.
            raise ValueError("height must be >= 0")
            # Lève une exception si la valeur est négative.
        self.__height = value
        # Stocke la valeur dans l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Aire = largeur * hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, périmètre = 2 * (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with print_symbol.
        """
        # Méthode spéciale appelée par print() ou str().
        # Retourne une chaîne qui représente le rectangle avec le symbole choisi.
        if self.__width == 0 or self.__height == 0:
            # Si largeur ou hauteur est 0, retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # On convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # On crée une liste de lignes (une par hauteur), chaque ligne contient
        # le symbole répété largeur fois. On assemble les lignes avec "\n" (saut de ligne).

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer
        # l'objet avec eval(). Utile pour le débogage.
        return f"Rectangle({self.__width}, {self.__height})"
        # f-string : permet d'insérer les valeurs de __width et __height dans la chaîne.

    def __del__(self):
        """Print a message when a Rectangle instance is
        deleted and decrement counter.
        """
        # Méthode spéciale appelée quand l'objet est détruit (par exemple, avec del).
        print("Bye rectangle...")
        # Affiche un message à la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.
        If both have the same area, return rect_1.
        """
        # Méthode statique : ne dépend pas d'une instance particulière.
        # Compare deux rectangles et retourne celui qui a la plus grande aire.
        if not isinstance(rect_1, Rectangle):
            # Vérifie que rect_1 est bien une instance de Rectangle.
            raise TypeError("rect_1 must be an instance of Rectangle")
            # Lève une exception si ce n'est pas le cas.
        if not isinstance(rect_2, Rectangle):
            # Vérifie que rect_2 est bien une instance de Rectangle.
            raise TypeError("rect_2 must be an instance of Rectangle")
            # Lève une exception si ce n'est pas le cas.
        if rect_1.area() >= rect_2.area():
            # Compare les aires des deux rectangles.
            # Si rect_1 a une aire supérieure ou égale, on le retourne.
            return rect_1
        return rect_2
        # Sinon, on retourne rect_2.

