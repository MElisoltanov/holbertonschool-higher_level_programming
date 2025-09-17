#!/usr/bin/python3
"""Defines a class Square with a private size attribute."""
# Les trois guillemets (""") ouvrent une chaîne de caractères multilignes,
# appelée docstring. Elle sert à documenter le fichier ou le module.
# Ici, elle explique que ce fichier définit une classe Square avec un attribut privé size.


class Square:
    # Le mot-clé 'class' permet de définir une nouvelle classe en Python.
    # Ici, on crée une classe appelée 'Square'.
    """Class that defines a Square by its size."""
    # Cette docstring décrit la classe Square.
    # Elle explique que la classe définit un carré par sa taille (size).

    def __init__(self, size):
        # 'def' sert à définir une fonction ou une méthode.
        # '__init__' est une méthode spéciale appelée constructeur.
        # Elle est automatiquement appelée lors de la création d'un objet Square.
        # 'self' fait référence à l'instance courante de la classe (l'objet créé).
        # 'size' est un paramètre passé lors de la création de l'objet.
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        """
        # Cette docstring explique le rôle de la méthode __init__ et de ses paramètres.
        # 'Args:' indique les arguments attendus.
        # 'size (int)' précise que size doit être un entier représentant la taille du carré.

        self.__size = size
        # 'self.__size' crée un attribut privé pour l'objet.
        # Les deux underscores '__' devant 'size' signifient que cet attribut est privé,
        # c'est-à-dire qu'il ne doit pas être accédé directement en dehors de la classe.
        # On assigne à 'self.__size' la valeur du paramètre 'size' passé lors de la création de l'objet.
