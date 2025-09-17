#!/usr/bin/python3
"""Define a class Square with a private size attribute."""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, situé dans /usr/bin/python3.

# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, ils servent à écrire une docstring, c'est-à-dire
# un commentaire de documentation qui décrit le but du module ou du fichier.


class Square:
    # Le mot-clé 'class' permet de définir une nouvelle classe en Python.
    # Ici, on crée une classe appelée 'Square' (carré en anglais).
    # Une classe est un plan qui permet de créer des objets ayant des
    # propriétés (attributs) et des comportements (méthodes).

    """Class that defines a Square by its size."""
    # Cette docstring décrit la classe. Elle explique que la classe définit
    # un carré à partir de sa taille (size).

    def __init__(self, size=0):
        # La méthode __init__ est une méthode spéciale appelée constructeur.
        # Elle est automatiquement appelée lors de la création d'un nouvel
        # objet de la classe. Elle sert à initialiser les attributs de l'objet.
        #
        # Le double underscore (__) avant et après 'init' indique qu'il s'agit
        # d'une méthode spéciale (aussi appelée "méthode magique").
        #
        # Le paramètre 'self' fait référence à l'instance de la classe en cours
        # de création. Il permet d'accéder aux attributs et méthodes de l'objet.
        #
        # Le paramètre 'size' permet de donner une taille au carré lors de sa
        # création. Il a une valeur par défaut de 0 si aucun argument n'est donné.

        """Initialize a new Square.
        Args:
            Size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # Cette docstring explique le rôle de la méthode __init__.
        # Elle décrit les paramètres attendus (ici, size), et les exceptions
        # qui peuvent être levées si les conditions ne sont pas respectées.

        if not isinstance(size, int):
            # La fonction isinstance() vérifie si 'size' est bien un entier (int).
            # Si ce n'est pas le cas, le bloc suivant (raise) sera exécuté.

            raise TypeError("size must be an integer")
            # Le mot-clé 'raise' permet de lever une exception.
            # Ici, on lève une exception de type TypeError avec un message
            # d'erreur personnalisé si 'size' n'est pas un entier.

        if size < 0:
            # Cette condition vérifie si la valeur de 'size' est inférieure à 0.
            # Si c'est le cas, on lève une exception pour signaler une erreur.

            raise ValueError("size must be >= 0")
            # On lève une exception de type ValueError si 'size' est négatif,
            # avec un message d'erreur explicite.

        self.__size = size
        # On crée un attribut privé '__size' pour l'objet en cours.
        # Le double underscore (__) devant 'size' indique que cet attribut
        # est privé : il ne doit pas être accédé directement en dehors de la classe.
        # On assigne à cet attribut la valeur de 'size' passée lors de la création
        # de l'objet.
