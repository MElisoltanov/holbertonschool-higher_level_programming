#!/usr/bin/python3
"""Define a class Square with size and position attributes,
    and advanced print.
"""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, donc le script sera
# exécuté avec Python 3.
#
# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, c'est-à-dire un commentaire
# qui décrit le module ou la classe. Elle peut être lue par des outils ou
# affichée avec help().


class Square:
    """Define a new square by its size and position."""
    # Déclaration d'une nouvelle classe appelée Square.
    # Les classes servent à créer des objets qui regroupent des données
    # (attributs) et des fonctions (méthodes).
    # La docstring ici décrit brièvement la classe.

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
            position (tuple): The position (spaces right, lines down).
        Raises:
            TyperError: If size is not an integer
                        or position is not a tuple of 2 positives integers.
            ValueError: If size is less than 0.
        """
        # __init__ est le constructeur de la classe. Il est appelé
        # automatiquement lors de la création d'un nouvel objet Square.
        # self fait référence à l'objet lui-même.
        # size est un paramètre optionnel (valeur par défaut 0).
        # position est aussi optionnel (par défaut (0, 0)).
        # Les docstrings expliquent les paramètres et les erreurs possibles.

        self.size = size
        # On utilise le setter size pour valider et stocker la taille.
        self.position = position
        # On utilise le setter position pour valider et stocker la position.

    @property
    def size(self):
        """Get the size of the square."""
        # @property transforme cette méthode en attribut en lecture seule.
        # On peut donc faire square.size pour obtenir la taille.
        return self.__size
        # On retourne la valeur privée __size (avec deux underscores pour
        # indiquer que c'est un attribut interne à la classe).

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        # Ce setter permet d'attribuer une valeur à size tout en vérifiant
        # qu'elle est correcte.
        if not isinstance(value, int):
            # On vérifie que value est un entier (int).
            raise TypeError("size must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError
            # avec un message explicite.
        if value < 0:
            # On vérifie que value est positif ou nul.
            raise ValueError("size must be >= 0")
            # Si value est négatif, on lève une exception ValueError.
        self.__size = value
        # Si tout est correct, on stocke value dans l'attribut privé __size.

    @property
    def position(self):
        """Get the position of the square."""
        # Cette propriété permet de lire la position du carré.
        return self.__position
        # On retourne la valeur privée __position.

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        # Ce setter permet de modifier la position tout en vérifiant
        # que la valeur est correcte.
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            # On vérifie que value est un tuple,
            # que sa longueur est 2,
            # que chaque élément est un entier,
            # et que chaque entier est positif ou nul.
            raise TypeError("position must be a tuple of 2 positive integers")
            # Si ce n'est pas le cas, on lève une exception TypeError.
        self.__position = value
        # Si tout est correct, on stocke value dans __position.

    def area(self):
        """Return the current square area."""
        # Cette méthode calcule et retourne l'aire du carré.
        return self.__size * self.__size
        # On multiplie la taille par elle-même (côté x côté).

    def my_print(self):
        """Print the square with the character #, considering position."""
        # Cette méthode affiche le carré à l'écran avec le caractère #,
        # en tenant compte de la position (décalage horizontal et vertical).
        if self.__size == 0:
            # Si la taille est 0, on affiche juste une ligne vide.
            print()
            # print() affiche une chaîne de caractères à l'écran.
            # Sans argument, il affiche juste un saut de ligne (\n).
            return
            # On quitte la fonction.

        for _ in range(self.__position[1]):
            # On affiche autant de lignes vides que le décalage vertical
            # (position[1]).
            print()
            # Chaque print() ajoute un saut de ligne.

        for _ in range(self.__size):
            # Pour chaque ligne du carré (autant que la taille) :
            print(" " * self.__position[0] + "#" * self.__size)
            # " " * self.__position[0] crée une chaîne d'espaces pour le
            # décalage horizontal (position[0]).
            # "#" * self.__size crée une ligne de dièses de la longueur du carré.
            # On concatène les deux chaînes et on les affiche avec print().
            # print() ajoute automatiquement un saut de ligne à la fin.
