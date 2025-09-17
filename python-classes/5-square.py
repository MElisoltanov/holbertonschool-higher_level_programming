#!/usr/bin/python3
"""Define a class Square with a private size attribute and print method."""
# Les guillemets triples (""") permettent d'écrire une docstring,
# c'est-à-dire un commentaire de documentation qui explique le but du fichier ou de la classe.
# Ici, cette docstring décrit brièvement ce que fait le fichier : il définit une classe Square
# avec un attribut privé size et une méthode d'affichage.


class Square:
    """Class that defines a Square by its size and can print it."""
    # Cette docstring décrit la classe Square : elle définit un carré par sa taille
    # et peut l'afficher.

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # La méthode __init__ est le constructeur de la classe.
        # Elle est appelée automatiquement lors de la création d'un nouvel objet Square.
        # Le paramètre size a une valeur par défaut de 0.
        # Les docstrings à l'intérieur des méthodes expliquent leur fonctionnement,
        # les arguments attendus et les erreurs possibles.
        self.size = size
        # self fait référence à l'instance courante de la classe.
        # On utilise self.size pour initialiser l'attribut size de l'objet.
        # Cela passe par le setter (voir plus bas) qui valide la valeur.

    @property
    def size(self):
        """Get the size of the square."""
        # Le décorateur @property transforme cette méthode en "getter" :
        # on peut accéder à la taille du carré comme un attribut (ex : s.size).
        return self.__size
        # On retourne la valeur de l'attribut privé __size.
        # Les deux underscores (__) rendent l'attribut privé (non accessible directement).

    @size.setter
    def size(self, value):
        """Set the size of the square with validation"""
        # Le décorateur @size.setter permet de définir un "setter" pour l'attribut size.
        # Cela permet de contrôler la modification de size (ex : s.size = 5).
        if not isinstance(value, int):
            # On vérifie que la valeur donnée est bien un entier (int).
            raise TypeError("size must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError avec un message explicite.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("size must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__size = value
        # Si toutes les vérifications sont passées, on assigne la valeur à l'attribut privé __size.

    def area(self):
        """Return the current square area."""
        # Cette méthode calcule et retourne l'aire du carré.
        return self.__size * self.__size
        # L'aire d'un carré est la taille au carré (size * size).
        # On utilise l'attribut privé __size.

    def my_print(self):
        """Print the square with the character # to stdout."""
        # Cette méthode affiche le carré à l'écran en utilisant le caractère #.
        # "stdout" signifie "standard output", c'est-à-dire la sortie normale du programme (le terminal).
        if self.__size == 0:
            # Si la taille du carré est 0, on affiche simplement une ligne vide.
            print()
            # print() sans argument affiche une ligne vide (un saut de ligne).
        else:
            # Sinon, on affiche le carré.
            for _ in range(self.__size):
                # On répète l'affichage autant de fois que la taille du carré (une ligne par itération).
                print("#" * self.__size)
                # "#" * self.__size crée une chaîne composée de # répétés size fois.
                # print() affiche cette chaîne à l'écran, suivie d'un saut de ligne.
