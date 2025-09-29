#!/usr/bin/python3
"""
This module defines an abstract Animal class
and its subclasses Dog and Cat.
"""

# On importe la classe ABC (Abstract Base Class) et le décorateur abstractmethod
# depuis le module abc de Python. Ces outils permettent de créer des classes abstraites,
# c'est-à-dire des modèles que d'autres classes vont devoir suivre.
from abc import ABC, abstractmethod

# On définit une classe appelée Animal qui hérite de la classe ABC.
# Cela signifie qu'Animal est une classe abstraite et ne peut pas être instanciée directement.
class Animal(ABC):
    """Abstract base class representing an animal."""

    # On utilise le décorateur @abstractmethod pour indiquer que la méthode sound
    # doit obligatoirement être définie dans les sous-classes.
    # Une méthode abstraite n'a pas d'implémentation ici, elle sert juste de modèle.
    @abstractmethod
    def sound(self):
        # Cette méthode doit être redéfinie dans chaque sous-classe.
        # Le mot-clé pass indique que la fonction ne fait rien ici.
        # On utilise pass pour créer une fonction vide, en attendant qu'elle soit
        # implémentée dans les classes filles.
        pass

# On définit une classe Dog qui hérite de la classe Animal.
# Cela signifie que Dog est un type d'Animal et doit respecter le modèle imposé
# par la classe Animal (donc définir la méthode sound).
class Dog(Animal):
    """Dog class, subclass of Animal."""

    # On redéfinit la méthode sound pour la classe Dog.
    # Ici, la méthode retourne la chaîne de caractères "Bark".
    # Les guillemets (" ") servent à délimiter une chaîne de caractères en Python.
    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"

# On définit une classe Cat qui hérite aussi de la classe Animal.
# Cat doit également définir la méthode sound.
class Cat(Animal):
    """Cat class, subclass of Animal."""

    # On redéfinit la méthode sound pour la classe Cat.
    # Cette méthode retourne la chaîne de caractères "Meow".
    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
