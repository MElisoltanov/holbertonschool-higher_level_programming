#!/usr/bin/python3
"""Defines a Rectangle class with a class method to create squares."""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.

# Les guillemets triples (""") servent à écrire une docstring, c'est-à-dire un commentaire
# multi-lignes qui décrit le but du fichier ou d'une fonction/classe. Ici, cela explique
# que le fichier définit une classe Rectangle avec une méthode de classe pour créer des carrés.


class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration de la classe Rectangle. Le mot-clé 'class' permet de définir une nouvelle
    # structure de données personnalisée. Tout ce qui est indenté à l'intérieur fait partie
    # de la classe.
    # La docstring de la classe explique son but : définir un rectangle avec une largeur et une hauteur.

    number_of_instances = 0
    # Variable de classe (partagée par toutes les instances) qui compte le nombre d'objets Rectangle créés.

    print_symbol = "#"
    # Variable de classe qui définit le symbole utilisé pour afficher le rectangle
    # lors de l'utilisation de la fonction print.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée automatiquement lors de la création d'une nouvelle instance.
        # 'self' fait référence à l'objet en cours de création.
        # 'width' et 'height' sont des paramètres optionnels (valeur par défaut 0).
        self.width = width
        # On utilise le setter de width pour valider et stocker la largeur.
        self.height = height
        # On utilise le setter de height pour valider et stocker la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'un rectangle, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property permet d'accéder à la méthode comme si c'était un attribut.
        return self.__width
        # Retourne la valeur privée __width (avec deux underscores pour indiquer que c'est privé).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Setter associé à la propriété width. Permet de définir la largeur avec des vérifications.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier. Sinon, lève une exception TypeError.
            raise TypeError("width must be an integer")
        if value < 0:
            # Vérifie que la valeur est positive ou nulle. Sinon, lève une exception ValueError.
            raise ValueError("width must be >= 0")
        self.__width = value
        # Stocke la valeur validée dans l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Propriété pour accéder à la hauteur du rectangle.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour la propriété height, avec vérification du type et de la valeur.
        if not isinstance(value, int):
            # Vérifie que la hauteur est un entier.
            raise TypeError("height must be an integer")
        if value < 0:
            # Vérifie que la hauteur est positive ou nulle.
            raise ValueError("height must be >= 0")
        self.__height = value
        # Stocke la valeur validée dans l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur pour obtenir l'aire.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, le périmètre est 0 (rectangle "vide").
            return 0
        return 2 * (self.__width + self.__height)
        # Calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation of the rectangle
        with print_symbol.
        """
        # Méthode spéciale appelée par print() pour afficher l'objet.
        if self.__width == 0 or self.__height == 0:
            # Si le rectangle est "vide", retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # Convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # Crée une liste de lignes (une par hauteur), chaque ligne contient print_symbol répété
        # 'width' fois. Les lignes sont assemblées avec des retours à la ligne ("\n").
        # Le caractère spécial "\n" permet de passer à la ligne suivante.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet avec eval().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string (chaîne formatée) pour insérer les valeurs de largeur et hauteur.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement counter.
        """
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple avec del).
        print("Bye rectangle...")
        # Affiche un message à la suppression de l'objet. La fonction print affiche du texte
        # dans le terminal. Les guillemets délimitent la chaîne à afficher.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances car un rectangle a été supprimé.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.
        If both have the same area, return rect_1.
        """
        # Méthode statique (n'utilise pas self ni cls) qui compare deux rectangles.
        if not isinstance(rect_1, Rectangle):
            # Vérifie que rect_1 est bien une instance de Rectangle.
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            # Vérifie que rect_2 est bien une instance de Rectangle.
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            # Compare les aires des deux rectangles.
            return rect_1
            # Si rect_1 est plus grand ou égal, retourne rect_1.
        return rect_2
        # Sinon, retourne rect_2.

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        # Méthode de classe (reçoit la classe en premier paramètre, conventionnellement 'cls').
        # Permet de créer un carré (largeur = hauteur = size).
        return cls(size, size)
        # Retourne une nouvelle instance de Rectangle avec largeur et hauteur égales à size.
