#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
and provides methods for area, perimeter, and string representations.
"""

# Début du code Python. Le shebang (#!) indique au système d'exploitation
# quel interpréteur utiliser pour exécuter ce fichier. Ici, il s'agit de python3.
# Cela permet de lancer le script directement depuis le terminal.

class Rectangle:
    """Defines a rectangle by its width and height."""

    # Déclaration de la classe Rectangle. Une classe est un modèle pour créer
    # des objets (ici, des rectangles). Le mot-clé 'class' sert à définir une classe.
    # Rectangle est le nom de la classe. Les deux-points (:) indiquent le début du bloc.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        # Méthode spéciale appelée lors de la création d'un nouvel objet Rectangle.
        # '__init__' est le constructeur. 'self' fait référence à l'instance créée.
        # 'width' et 'height' sont des paramètres avec une valeur par défaut de 0.
        self.width = width
        # On assigne la valeur du paramètre 'width' à l'attribut 'width' de l'objet.
        self.height = height
        # On assigne la valeur du paramètre 'height' à l'attribut 'height' de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Définition d'une propriété 'width'. Permet d'accéder à la largeur
        # comme un attribut, mais en utilisant une méthode.
        return self.__width
        # Retourne la valeur de l'attribut privé '__width' de l'objet.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        # Définit le setter pour la propriété 'width'. Permet de contrôler
        # la modification de la largeur.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("width must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si tout est correct, assigne la valeur à l'attribut privé '__width'.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Définition d'une propriété 'height'. Permet d'accéder à la hauteur
        # comme un attribut, mais en utilisant une méthode.
        return self.__height
        # Retourne la valeur de l'attribut privé '__height' de l'objet.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        # Définit le setter pour la propriété 'height'. Permet de contrôler
        # la modification de la hauteur.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("height must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si tout est correct, assigne la valeur à l'attribut privé '__height'.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois (largeur + hauteur).

    def __str__(self):
        """Return the string representation of the rectangle using '#'."""
        # Méthode spéciale qui définit la représentation "printable" de l'objet.
        # Utilisée par print() ou str().
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, retourne une chaîne vide.
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # Sinon, crée une chaîne composée de lignes de '#' :
        # - "#" * self.__width crée une ligne de '#' de la largeur du rectangle.
        # - for _ in range(self.__height) répète cette ligne pour chaque hauteur.
        # - "\n".join(...) assemble les lignes avec des retours à la ligne.
        # Les guillemets doubles ("") délimitent les chaînes de caractères.
        # Le caractère spécial '\n' représente un saut de ligne.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet.
        # Utilisée par la fonction repr().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string (f"") pour insérer les valeurs de largeur et hauteur
        # dans la chaîne. Les accolades {} servent à insérer les variables.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple,
        # quand il n'est plus utilisé). Permet d'exécuter du code à la destruction.
        print("Bye rectangle...")
        # Affiche le message "Bye rectangle..." dans la console.
        # La fonction print() sert à afficher du texte à l'écran.
        # Les guillemets délimitent la chaîne à afficher.
