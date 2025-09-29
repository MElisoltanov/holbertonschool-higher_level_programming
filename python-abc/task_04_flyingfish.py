#!/usr/bin/python3
"""This module defines Fish, Bird, and FlyingFish classes for multiple inheritance."""

# Définition de la classe Fish.
class Fish:
    # Définition de la docstring de la classe Fish.
    """Fish class with swim and habitat methods."""

    # Définition de la méthode swim de la classe Fish.
    def swim(self):
        # La fonction print affiche du texte à l'écran.
        # Les guillemets entourent la chaîne de caractères à afficher.
        print("The fish is swimming")

    # Définition de la méthode habitat de la classe Fish.
    def habitat(self):
        # Affiche où vit le poisson.
        print("The fish lives in water")

# Définition de la classe Bird.
class Bird:
    # Docstring de la classe Bird.
    """Bird class with fly and habitat methods."""

    # Définition de la méthode fly de la classe Bird.
    def fly(self):
        # Affiche que l'oiseau vole.
        print("The bird is flying")

    # Définition de la méthode habitat de la classe Bird.
    def habitat(self):
        # Affiche où vit l'oiseau.
        print("The bird lives in the sky")

# Définition de la classe FlyingFish qui hérite de Fish et Bird.
class FlyingFish(Fish, Bird):
    # Docstring de la classe FlyingFish.
    """FlyingFish class that inherits from Fish and Bird."""

    # Redéfinition de la méthode swim pour FlyingFish.
    def swim(self):
        # Affiche que le poisson volant nage.
        print("The flying fish is swimming!")

    # Redéfinition de la méthode fly pour FlyingFish.
    def fly(self):
        # Affiche que le poisson volant vole.
        print("The flying fish is soaring!")

    # Redéfinition de la méthode habitat pour FlyingFish.
    def habitat(self):
        # Affiche où vit le poisson volant.
        print("The flying fish lives both in water and the sky!")
