#!/usr/bin/env python3
# Le shebang indique au système d'exploitation quel interpréteur utiliser pour exécuter ce fichier.
# Ici, il utilise l'interpréteur Python 3 trouvé dans le PATH de l'environnement.

from abc import ABC, abstractmethod
# Importe le module abc (Abstract Base Classes) qui permet de créer des classes abstraites.
# ABC est la classe de base pour définir une classe abstraite.
# abstractmethod est un décorateur pour indiquer qu'une méthode doit être implémentée dans les sous-classes.

import math
# Importe le module math qui fournit des fonctions mathématiques comme pi.

class Shape(ABC):
    # Définit une nouvelle classe appelée Shape qui hérite de ABC.
    # Cela signifie que Shape est une classe abstraite.

    """
    Abstract base class for shapes.
    """
    # La docstring décrit le but de la classe.
    # Les docstrings sont entourées de triples guillemets (""" ... """).
    # Elles servent à documenter le code.

    @abstractmethod
    # Le décorateur @abstractmethod indique que la méthode qui suit doit être
    # obligatoirement définie dans les sous-classes.

    def area(self):
        # Définit une méthode nommée area.
        # Les méthodes sont des fonctions définies à l'intérieur d'une classe.
        # self est le premier paramètre de chaque méthode de classe et fait référence à l'instance courante.

        """
        Abstract method to return the area of the shape.
        """
        # Docstring qui explique le but de la méthode.

        pass
        # pass est une instruction qui ne fait rien.
        # Elle sert ici à indiquer que la méthode n'a pas d'implémentation.

    @abstractmethod
    # Indique que la méthode perimeter doit aussi être définie dans les sous-classes.

    def perimeter(self):
        # Définit une méthode nommée perimeter.

        """
        Abstract method to return the perimeter of the shape.
        """
        # Docstring pour la méthode perimeter.

        pass
        # pass indique que la méthode n'a pas d'implémentation ici.

class Circle(Shape):
    # Définit une classe Circle qui hérite de Shape.
    # Circle doit donc implémenter les méthodes abstraites area et perimeter.

    """
    Circle shape.
    """
    # Docstring qui décrit la classe Circle.

    def __init__(self, radius):
        # Méthode spéciale __init__ appelée lors de la création d'une instance.
        # radius est un paramètre qui représente le rayon du cercle.

        self.radius = radius
        # self.radius crée un attribut d'instance appelé radius et lui assigne la valeur passée en paramètre.

    def area(self):
        # Implémente la méthode area pour la classe Circle.

        return math.pi * (self.radius ** 2)
        # Calcule l'aire du cercle.
        # math.pi donne la valeur de π.
        # self.radius ** 2 élève le rayon au carré.
        # Les parenthèses sont utilisées pour regrouper les opérations.

    def perimeter(self):
        # Implémente la méthode perimeter pour la classe Circle.

        return 2 * math.pi * self.radius
        # Calcule le périmètre du cercle.
        # 2 * π * rayon.

class Rectangle(Shape):
    # Définit une classe Rectangle qui hérite de Shape.

    """
    Rectangle shape.
    """
    # Docstring qui décrit la classe Rectangle.

    def __init__(self, width, height):
        # Méthode spéciale __init__ appelée lors de la création d'une instance.
        # width est la largeur du rectangle.
        # height est la hauteur du rectangle.

        self.width = width
        # self.width crée un attribut d'instance width.

        self.height = height
        # self.height crée un attribut d'instance height.

    def area(self):
        # Implémente la méthode area pour la classe Rectangle.

        return self.width * self.height
        # Calcule l'aire du rectangle.
        # Multiplie la largeur par la hauteur.

    def perimeter(self):
        # Implémente la méthode perimeter pour la classe Rectangle.

        return 2 * (self.width + self.height)
        # Calcule le périmètre du rectangle.
        # Additionne la largeur et la hauteur, puis multiplie par 2.

def shape_info(shape):
    # Définit une fonction nommée shape_info.
    # shape est un paramètre qui doit être un objet ayant les méthodes area et perimeter.

    """
    Prints the area and perimeter of a shape.
    """
    # Docstring qui explique le but de la fonction.

    print(f"Area: {shape.area()}")
    # print est une fonction intégrée qui affiche du texte à l'écran.
    # f"..." est une f-string, une chaîne de caractères formatée.
    # {shape.area()} exécute la méthode area de l'objet shape et insère le résultat dans la chaîne.

    print(f"Perimeter: {shape.perimeter()}")
    # Affiche le périmètre du shape.
    # Utilise aussi une f-string pour insérer le résultat de shape.perimeter().
