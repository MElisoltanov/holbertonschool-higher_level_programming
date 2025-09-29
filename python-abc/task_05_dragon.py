#!/usr/bin/python3
"""This module defines SwimMixin, FlyMixin, and Dragon classes for mixin demonstration."""

# Définition de la classe SwimMixin.
class SwimMixin:
    # Définition d'une docstring pour la classe SwimMixin.
    """Mixin providing swim ability."""
    # Définition de la méthode swim de la classe SwimMixin.
    def swim(self):
        # Utilisation de la fonction print pour afficher un message à l'écran.
        # Les guillemets entourent la chaîne de caractères à afficher.
        # Le point d'exclamation est un caractère spécial pour marquer l'enthousiasme.
        print("The creature swims!")

# Définition de la classe FlyMixin.
class FlyMixin:
    # Définition d'une docstring pour la classe FlyMixin.
    """Mixin providing fly ability."""
    # Définition de la méthode fly de la classe FlyMixin.
    def fly(self):
        # Utilisation de la fonction print pour afficher un message à l'écran.
        # Les guillemets entourent la chaîne de caractères à afficher.
        # Le point d'exclamation est un caractère spécial pour marquer l'enthousiasme.
        print("The creature flies!")

# Définition de la classe Dragon qui hérite de SwimMixin et FlyMixin.
class Dragon(SwimMixin, FlyMixin):
    # Définition d'une docstring pour la classe Dragon.
    """Dragon class with swim, fly, and roar abilities."""
    # Définition de la méthode roar de la classe Dragon.
    def roar(self):
        # Utilisation de la fonction print pour afficher un message à l'écran.
        # Les guillemets entourent la chaîne de caractères à afficher.
        # Le point d'exclamation est un caractère spécial pour marquer l'enthousiasme.
        print("The dragon roars!")
