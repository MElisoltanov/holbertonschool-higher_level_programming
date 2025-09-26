#!/usr/bin/python3
"""
This module defines an abstract Animal class
and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class, subclass of Animal."""

    def sound(self):
        """Return the sound made by a dog."""
        return "Bark"


class Cat(Animal):
    """Cat class, subclass of Animal."""

    def sound(self):
        """Return the sound made by a cat."""
        return "Meow"
