#!/usr/bin/python3
"""Defines a Rectangle class with customizable print symbol."""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.

# Les guillemets triples (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, c'est-à-dire un commentaire
# de documentation qui explique le but du fichier ou du module.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring ici décrit le rôle de la classe.

    number_of_instances = 0
    # Variable de classe (partagée par toutes les instances).
    # Elle compte le nombre d'objets Rectangle créés.

    print_symbol = "#"
    # Variable de classe utilisée pour afficher le rectangle.
    # Par défaut, le symbole utilisé est le dièse (#).

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée lors de la création d'un nouvel objet Rectangle.
        # Elle initialise les attributs width (largeur) et height (hauteur).
        # Les paramètres width et height ont une valeur par défaut de 0.
        self.width = width
        # On utilise le setter de width pour valider et assigner la largeur.
        self.height = height
        # On utilise le setter de height pour valider et assigner la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        # Permet d'accéder à la largeur avec obj.width.
        return self.__width
        # Retourne la valeur privée __width (attribut d'instance).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Setter associé à la propriété width.
        # Permet d'assigner une valeur à width tout en validant la donnée.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie que la valeur est positive ou nulle.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, lève une exception ValueError.
        self.__width = value
        # Si tout est correct, assigne la valeur à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Propriété pour accéder à la hauteur de l'objet.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour valider et assigner la hauteur.
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
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 × (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with print_symbol.
        """
        # Méthode spéciale appelée par str(obj) ou print(obj).
        # Retourne une chaîne représentant le rectangle avec le symbole choisi.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # Convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # Crée une liste de lignes (une par hauteur), chaque ligne contient le symbole répété largeur fois.
        # "\n".join(...) assemble toutes les lignes avec un saut de ligne entre chaque.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale appelée par repr(obj).
        # Retourne une chaîne qui permet de recréer l'objet avec eval().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string pour insérer les valeurs de largeur et hauteur.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted and
        decrement counter.
        """
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple avec del).
        print("Bye rectangle...")
        # Affiche un message d'adieu à la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances de la classe.
