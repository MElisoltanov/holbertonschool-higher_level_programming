# Project: Python - Abstract Classes and Interfaces | Holberton Toulouse, France Intranet

## Python OOP - Abtract Class, Interface, Subclassing

### Introduction:

Welcome to this set of exercises aimed at honing your understanding and application of Object-Oriented Programming (OOP) concepts in Python. Through these exercises, you will delve into abstract classes, interfaces, duck typing, and subclassing standard base classes among other crucial OOP concepts. By the end of these exercises, you should be proficient in employing OOP principles to design, implement, and test Python programs.

### Learning Objectives:

1. **Abstract Classes:** Understand and apply abstract classes to define common interfaces while enforcing certain levels of class completeness.
2. **Interfaces and Duck Typing:** Grasp the concept of interfaces and duck typing to ensure that objects adhere to a specific contract or protocol.
3. **Subclassing Standard Base Classes:** Learn to extend standard base classes like lists, dictionaries, and iterators to create custom data structures with specialized behavior.
4. **Method Overriding:** Employ method overriding to alter or enhance the behavior of base class methods.
5. **Multiple Inheritance:** Understand and apply multiple inheritance to form complex relationships between classes.
6. **Mixins:** Utilize mixins to compose behavior across unrelated classes.

### Resources:

- [Python 3 Object-Oriented Programming](/rltoken/oV5Tf8bq_jN2kEhm3kA1dA)
- [ABC — Abstract Base Classes](/rltoken/_0PgSum1lebIia7sFQmIbA)
- [Real Python - Object-Oriented Programming (OOP) in Python 3](/rltoken/9VEEisWUdD72t7ZZOIw0Aw)
- [Corey Schafer - OOP Playlist](/rltoken/2aZrJyZm6ld8Uprg_Q9KMQ)
- [sentdex - Python OOP Tutorial](/rltoken/YExxID954JR9aCTgBIZb0A)

The above resources provide a mix of reading material, interactive exercises, and video tutorials to cater to different learning styles. It’s recommended to go through these resources to build a solid understanding of OOP concepts in Python before attempting the exercises.

## Tasks

---

### 0. Abstract Animal Class and its Subclasses

#### Background:

In object-oriented programming, Abstract Base Classes (ABCs) ensure that derived classes implement specific methods from the base class. This provides a blueprint for creating and structuring derived classes. Python’s `ABC` package facilitates the creation of abstract base classes.

#### Objective:

1. Create an abstract class named `Animal` using the `ABC` package. This class should have an abstract method called `sound`.
2. Create two subclasses of `Animal`: `Dog` and `Cat`. Implement the `sound` method in each subclass to return the strings “Bark” and “Meow” respectively.

#### Resources:

- Python `ABC` documentation: [https://docs.python.org/3/library/abc.html](/rltoken/_0PgSum1lebIia7sFQmIbA)

#### Instructions:

1. **Setting up the Abstract Class**:
    - Import the necessary components from the `abc` module.
    - Define the `Animal` class, ensuring it inherits from `ABC` to mark it as abstract.
    - Inside the `Animal` class, declare an abstract method named `sound` using the `@abstractmethod` decorator.
2. **Implementing the Subclasses**:
    - Create a subclass named `Dog` that inherits from the `Animal` class.
        - Implement the `sound` method in the `Dog` class to return the string “Bark”.
    - Similarly, create a subclass named `Cat` that also inherits from the `Animal` class.
        - Implement the `sound` method in the `Cat` class to return the string “Meow”.

**Hints**:

- The abstract method in the base class doesn’t have a body. You need to provide the implementation in the subclasses.
- If you try to instantiate a class that hasn’t implemented all of its abstract methods, Python will raise a `TypeError`.

```python
$ cat main_00_abc.py 
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())

animal = Animal()
print(animal.sound())

$ ./main_00_abc.py 
Bark
Meow
Traceback (most recent call last):
  File "main_00_abc.py", line 10, in <module>
    animal = Animal()
TypeError: Can't instantiate abstract class Animal with abstract method sound
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_00_abc.py`

**Code:**
```python
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
```
---

### 1. Shapes, Interfaces, and Duck Typing

#### Background:

Python employs a concept called “duck typing,” which is concerned with the semantics of objects rather than their inheritance hierarchy. If an object behaves like a duck (i.e., has all the methods and properties of a duck), then it’s considered a duck, regardless of its actual class. This concept allows for flexible and dynamic polymorphism.

In this exercise, we’ll use abstract base classes to design a blueprint for shapes and use duck typing to handle objects of different shapes uniformly.

#### Objective:

1. Create an abstract class named `Shape` with two abstract methods: `area` and `perimeter`.
2. Implement two concrete classes: `Circle` and `Rectangle`, both inheriting from `Shape`. Each class should provide implementations for the `area` and `perimeter` methods.
3. Write a standalone function named `shape_info` that accepts an object of type `Shape` (by duck typing) and prints its area and perimeter.
4. Test the `shape_info` function with instances of both `Circle` and `Rectangle`.

#### Resources:

- Python `ABC` documentation: [https://docs.python.org/3/library/abc.html](/rltoken/_0PgSum1lebIia7sFQmIbA)
- Concept of Duck Typing: [https://realpython.com/lessons/duck-typing/](/rltoken/i3FBxu-VBtDf3LuXcT_82g)

#### Instructions:

1. **Shape Abstract Class**:
    - Define an abstract class `Shape` using the `ABC` package.
    - Within `Shape`, declare two abstract methods: `area` and `perimeter`.
2. **Circle and Rectangle Classes**:
    - Create a `Circle` class that inherits from `Shape`. The constructor (`__init__`) should accept a radius. Implement the `area` and `perimeter` methods.
    - Create a `Rectangle` class, also inheriting from `Shape`. Its constructor should accept the width and height. Implement the `area` and `perimeter` methods.
3. **shape_info Function**:
    - Define a function named `shape_info` that takes a single argument.
    - Without explicitly checking the type of the argument, call its `area` and `perimeter` methods (relying on duck typing).
    - Print the area and perimeter of the shape passed to the function.
4. **Testing**:
    - Instantiate a `Circle` and a `Rectangle`.
    - Pass each object to the `shape_info` function and observe the output.

**Hints**:

- While Python doesn’t enforce interfaces in the same way as statically-typed languages, abstract base classes provide a mechanism to ensure certain methods are implemented in subclasses.
- Duck typing in the `shape_info` function implies that you shouldn’t use `isinstance` checks. Instead, trust that the passed object adheres to the `Shape` interface.

```python
$ cat main_01_duck_typing.py 
#!/usr/bin/env python3
from task_01_duck_typing import Circle, Rectangle, shape_info

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

shape_info(circle)
shape_info(rectangle)

$ ./main_01_duck_typing.py 
Area: 78.53981633974483
Perimeter: 31.41592653589793
Area: 28
Perimeter: 22
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_01_duck_typing.py`

**Code:**
```python
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
```
---

### 2. Extending the Python List with Notifications

#### Background:

In Python, you can extend built-in classes to add or modify behavior. The `list` class provides a collection of methods and functionalities that handle list operations. By extending the `list` class, you can provide custom behaviors while retaining the original functionalities.

#### Objective:

Create a class named `VerboseList` that extends the Python `list` class. This custom class should print a notification message every time an item is added (using the `append` or `extend` methods) or removed (using the `remove` or `pop` methods).

#### Instructions:

1. **Setting up the VerboseList Class**:
    - Define a class `VerboseList` that inherits from the built-in `list` class.
    - Within `VerboseList`, override the methods that modify the list: `append`, `extend`, `remove`, and `pop`.
2. **Implementing Notifications**:
    - For the `append` method: After adding the item to the list, print a message like “Added [item] to the list.”
    - For the `extend` method: After extending the list, print a message like “Extended the list with [x] items.” where [x] is the number of items added.
    - For the `remove` method: Before removing the item from the list, print a message like “Removed [item] from the list.”
    - For the `pop` method: Before popping the item from the list, print a message like “Popped [item] from the list.” If the index is not specified, default behavior is to pop the last item.
3. **Testing**:
    - Instantiate a `VerboseList` object.
    - Test all the overridden methods (`append`, `extend`, `remove`, and `pop`) and ensure that the appropriate messages are printed for each operation.

**Hints**:

- Remember to call the original method of the `list` class using the `super()` function to ensure that the original functionality is retained. For example, for `append`: `super().append(item)`.
- Think about edge cases, such as trying to remove an item that doesn’t exist in the list.

```python
$ cat main_02_verboselist.py 
#!/usr/bin/env python3
from task_02_verboselist import VerboseList

vl = VerboseList([1, 2, 3])
vl.append(4)
vl.extend([5, 6])
vl.remove(2)
vl.pop()
vl.pop(0)

$ ./main_02_verboselist.py 
Added [4] to the list.
Extended the list with [2] items.
Removed [2] from the list.
Popped [6] from the list.
Popped [1] from the list.
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_02_verboselist.py`

**Code:**
```python
#!/usr/bin/python3
"""This module defines the VerboseList class that extends list with notifications."""

# Déclaration de la classe VerboseList qui hérite de la classe intégrée 'list'
class VerboseList(list):
    """A list that prints notifications when modified."""

    # Définition de la méthode 'append' qui ajoute un élément à la fin de la liste
    def append(self, item):
        # Appel de la méthode 'append' de la classe parente 'list' pour ajouter l'élément
        super().append(item)
        # La fonction 'print' affiche un message à l'écran
        # Les crochets [] sont utilisés pour entourer l'élément ajouté
        # Le 'f' devant la chaîne indique une f-string, permettant d'insérer la valeur de 'item'
        print(f"Added [{item}] to the list.")

    # Définition de la méthode 'extend' qui ajoute plusieurs éléments à la liste
    def extend(self, iterable):
        # 'len(iterable)' retourne le nombre d'éléments dans l'objet 'iterable'
        count = len(iterable)
        # Appel de la méthode 'extend' de la classe parente pour ajouter les éléments
        super().extend(iterable)
        # Affiche le nombre d'éléments ajoutés grâce à la f-string
        print(f"Extended the list with [{count}] items.")

    # Définition de la méthode 'remove' qui supprime un élément de la liste
    def remove(self, item):
        # Affiche le message avant de supprimer l'élément
        print(f"Removed [{item}] from the list.")
        # Appel de la méthode 'remove' de la classe parente pour supprimer l'élément
        super().remove(item)

    # Définition de la méthode 'pop' qui retire et retourne un élément de la liste
    # 'index=-1' signifie que par défaut, le dernier élément sera retiré
    def pop(self, index=-1):
        # Récupère l'élément à l'index donné avant de le retirer
        item = self[index]
        # Affiche le message avec l'élément retiré
        print(f"Popped [{item}] from the list.")
        # Appel de la méthode 'pop' de la classe parente pour retirer l'élément
        # et retourne cet élément
        return super().pop(index)
```
---

### 3. CountedIterator - Keeping Track of Iteration

#### Background:

Subclassing allows a new class to inherit properties and methods from an existing class. In Python, many built-in classes can be extended to customize or enhance their behavior. The `iter` function, which returns an iterator object, provides the `__next__` method to fetch the next item in the sequence. This exercise focuses on extending the functionality of this iterator object.

#### Objective:

Create a class named `CountedIterator` that extends the built-in iterator obtained from the `iter` function. The `CountedIterator` should keep track of the number of items that have been iterated over. Specifically, you will need to override the `__next__` method to increment a counter each time an item is fetched.

#### Instructions:

1. **Setting up the CountedIterator Class**:
    - Define a class `CountedIterator`.
    - In the constructor (`__init__`), initialize two attributes: the iterator object (using the `iter` function) and a counter to track the number of items iterated.
    - Provide a method `get_count` to return the current value of the counter.
2. **Overriding the next Method**:
    - Within the `CountedIterator` class, override the `__next__` method.
    - In this method, increment the counter each time the `__next__` method is called.
    - Fetch the next item from the original iterator and return it. If there are no items left to iterate, the method should raise the `StopIteration` exception.
3. **Testing**:
    - Instantiate a `CountedIterator` object using a list or another iterable.
    - Iterate over items using a loop or manual calls to the `__next__` method.
    - Use the `get_count` method to retrieve and print the number of items that have been fetched.

**Hints**:

- Remember that the `__next__` method should raise a `StopIteration` exception when there are no more items to iterate, so ensure this behavior is retained in your overridden method.
- You can initialize the iterator object in the `CountedIterator` constructor using: `self.iterator = iter(some_iterable)`.

```python
$ cat main_03_countediterator.py 
#!/usr/bin/env python3
from task_03_countediterator import CountedIterator

data = [1, 2, 3, 4]
counted_iter = CountedIterator(data)

try:
    while True:
        item = next(counted_iter)
        print(f"Got {item}, total {counted_iter.get_count()} items iterated.")
except StopIteration:
    print("No more items.")

$ ./main_03_countediterator.py 
Got 1, total 1 items iterated.
Got 2, total 2 items iterated.
Got 3, total 3 items iterated.
Got 4, total 4 items iterated.
No more items.
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_03_countediterator.py`

**Code:**
```python
#!/usr/bin/python3
"""This module defines the CountedIterator
class that tracks iteration count."""

# Définition de la classe CountedIterator.
# Une classe est un modèle pour créer des objets en Python.
class CountedIterator:
    """Iterator that counts the number of items iterated."""

    # La méthode __init__ est le constructeur de la classe.
    # Elle est appelée automatiquement lors de la création
    # d'une nouvelle instance de la classe.
    def __init__(self, iterable):
        # 'self' fait référence à l'objet courant.
        # 'iterable' est un objet sur lequel on peut itérer
        # (par exemple une liste, un tuple, une chaîne de caractères).
        # La fonction 'iter()' transforme l'objet 'iterable'
        # en un itérateur, qui permet d'obtenir les éléments
        # un par un.
        self.iterator = iter(iterable)
        # On initialise l'attribut 'count' à 0.
        # Cet attribut va compter le nombre d'éléments
        # déjà parcourus.
        self.count = 0

    # La méthode __next__ permet d'obtenir l'élément suivant
    # de l'itérateur. Elle est appelée à chaque itération
    # (par exemple dans une boucle for ou avec la fonction next()).
    def __next__(self):
        # On récupère l'élément suivant de l'itérateur
        # avec la fonction 'next()'.
        item = next(self.iterator)
        # On incrémente le compteur 'count' de 1
        # à chaque fois qu'on récupère un élément.
        self.count += 1
        # On retourne l'élément récupéré.
        return item

    # La méthode 'get_count' permet d'obtenir la valeur
    # actuelle du compteur, c'est-à-dire le nombre
    # d'éléments déjà parcourus.
    def get_count(self):
        """Return the number of items iterated so far."""
        # On retourne la valeur de l'attribut 'count'.
        return self.count
```
---

### 4. The Enigmatic FlyingFish - Exploring Multiple Inheritance

#### Background:

In some object-oriented languages, a class can inherit attributes and behaviors from more than one parent class. This is known as multiple inheritance. Python is one of the languages that supports multiple inheritance, which can be a powerful tool, but it also comes with complexities, particularly regarding method resolution order (MRO).

#### Objective:

Construct a `FlyingFish` class that inherits from both a `Fish` class and a `Bird` class. Within `FlyingFish`, override methods from both parents. The goal is to comprehend multiple inheritance and how Python determines method resolution order.

#### Instructions:

1. **Parent Classes Setup**:
    - Create a `Fish` class with methods `swim` (which prints “The fish is swimming”) and `habitat` (which prints “The fish lives in water”).
    - Create a `Bird` class with methods `fly` (which prints “The bird is flying”) and `habitat` (which prints “The bird lives in the sky”).
2. **Implementing FlyingFish**:
    - Construct a `FlyingFish` class that inherits from both `Fish` and `Bird`.
    - Override the `fly` method to print “The flying fish is soaring!”.
    - Override the `swim` method to print “The flying fish is swimming!”.
    - Override the `habitat` method to print “The flying fish lives both in water and the sky!”.
3. **Testing and MRO Exploration**:
    - Instantiate an object of the `FlyingFish` class.
    - Call the `fly`, `swim`, and `habitat` methods and observe the outputs.
    - Use the `mro()` method or the `.__mro__` attribute on the `FlyingFish` class to investigate the method resolution order. For instance, `print(FlyingFish.mro())`.

**Hints**:

- Consider the order in which you list the parent classes when defining `FlyingFish`. It affects the method resolution order.
- While multiple inheritance can be a powerful tool, it should be used judiciously, as it can make the code more complex and harder to read.

```python
$ cat main_04_flyingfish.py 
#!/usr/bin/env python3
from task_04_flyingfish import Fish, FlyingFish

flying_fish = FlyingFish()
flying_fish.swim()
flying_fish.fly()
flying_fish.habitat()

$ ./main_04_flyingfish.py 
The flying fish is swimming!
The flying fish is soaring!
The flying fish lives both in water and the sky!
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_04_flyingfish.py`

**Code:**
```python
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
```
---

### 5. The Mystical Dragon - Mastering Mixins

#### Background:

Mixins are a way to add functionality to classes in a modular fashion. They’re not meant to stand alone but are meant to be combined with other classes to add behaviors. By using mixins, you can compose behaviors in classes without the need for deep or rigid inheritance hierarchies.

#### Objective:

Design two mixin classes, `SwimMixin` and `FlyMixin`, each equipped with methods `swim` and `fly` respectively. Next, construct a class `Dragon` that inherits from both these mixins. Your aim is to show that a `Dragon` instance can both swim and fly.

#### Instructions:

1. **Creating Mixins**:
    - Design a mixin called `SwimMixin` with a method `swim` that prints “The creature swims!”.
    - Design another mixin called `FlyMixin` with a method `fly` that prints “The creature flies!”.
2. **Implementing Dragon**:
    - Construct a class named `Dragon` that inherits from both `SwimMixin` and `FlyMixin`.
    - Within the `Dragon` class, you can add additional methods or attributes if desired, such as `roar`, which could print “The dragon roars!”.
3. **Testing the Dragon’s Abilities**:
    - Instantiate an object of the `Dragon` class named `draco`.
    - Demonstrate `draco`‘s abilities by calling the `swim`, `fly`, and (if implemented) `roar` methods.

**Hints**:

- While designing mixins, remember that they should be focused, providing a single piece of functionality. They shouldn’t be overly broad or try to manage too much behavior.
- Mixins allow for code reusability and can be combined in various ways to give objects different capabilities without setting up complex inheritance hierarchies.

```python
$ cat main_05_dragon.py 
#!/usr/bin/env python3
from task_05_dragon import Dragon

dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!

$ ./main_05_dragon.py 
The creature swims!
The creature flies!
The dragon roars!
```

**Repo:**

- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-abc`
- File: `task_05_dragon.py`

**Code:**
```python
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
```