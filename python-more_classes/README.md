## Resources

**Read or watch**:

- [Object Oriented Programming](/rltoken/NxSyny_ojf0m2yY1FxhvsA) (_Read everything until the paragraph “Inheritance” (excluded)_)
- [Object-Oriented Programming](/rltoken/PgSxX0FFvkpyAjNyoU0qcg) (_Please be careful: in most of the following paragraphs, the author shows the way you should not use or write a class, in order to help you better understand some concepts and how everything works in Python 3. Make sure you read only the following paragraphs: “General Introduction,” “First-class Everything,” “A Minimal Class in Python,” “Attributes,” “Methods,” “The `__init__` Method,”  “Data Abstraction, Data Encapsulation, and Information Hiding,” “`__str__`- and `__repr__`-Methods,” “Public- Protected- and Private Attributes,” & “Destructor”_)
- [Class and Instance Attributes](/rltoken/2Lv-3qPSpQfC1VI52d9LZA)
- [classmethods and staticmethods](/rltoken/18KAvV_Ife9t5o3HYXj9DQ)
- [Properties vs. Getters and Setters](/rltoken/uHYbs5bXkYo6KvTtT6K5Sg) (_Mainly the last part “Public instead of Private Attributes”_)
- [str vs repr](/rltoken/I0LZ2eMDlX6Fc-vrJvY5fA)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](/rltoken/TUamWq6RTFPs75ESaJtOcg), **without the help of Google**:

### General

- Why Python programming is awesome
- What is OOP
- “first-class everything”
- What is a class
- What is an object and an instance
- What is the difference between a class and an object or instance
- What is an attribute
- What are and how to use public, protected and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- What are the special `__str__` and `__repr__` methods and how to use them
- What is the difference between `__str__` and `__repr__`
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain `__dict__` of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

## Requirements

### General

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

---

## Quiz

**Question #0**

What is `__init__`?

- [ ] A class attribute
- [ ] A class method
- [x] The instance method called when a new object is created
- [ ] The instance method called when a class is called for the first time

---

**Question #1**

What is `__str__`?

- [x] Instance method that returns an “informal” and nicely printable string representation of an instance
- [ ] Instance method that returns the dictionary representation of an instance
- [ ] Instance method that prints an “informal” and nicely printable string representation of an instance

---

**Question #2**

What is `__repr__`?

- [ ] Instance method that prints an “official” string representation of an instance
- [x] Instance method that returns an “official” string representation of an instance
- [ ] Instance method that returns the dictionary representation of an instance

---

**Question #3**

What is `__del__`?

- [ ] Instance method that removes the last character of an instance
- [ ] Instance method that prints the memory address of an instance
- [x] Instance method called when an instance is deleted

---

**Question #4**

What is `__doc__`?

- [x] The string documentation of an object (based on docstring)
- [ ] Prints the documentation of an object
- [ ] Creates man file

---

**Question #5**

What do these lines print?

```python
class User:
    id = 1

print(User.id)
```

- [ ] None
- [x] 1
- [ ] 89
- [ ] 98

---

**Question #6**

What do these lines print?

```python
class User:
    id = 1

u = User()
print(u.id)
```

- [ ] None
- [x] 1
- [ ] 89
- [ ] 98

---

**Question #7**

What do these lines print?

```python
class User:
    id = 1

u = User()
u.id = 89
print(u.id)
```

- [ ] None
- [ ] 1
- [x] 89
- [ ] 98

---

**Question #8**

What do these lines print?

```python
class User:
    id = 1

User.id = 98
u = User()
print(u.id)
```

- [ ] None
- [ ] 1
- [ ] 89
- [x] 98

---

**Question #9**

What do these lines print?

```python
class User:
    id = 1

u = User()
User.id = 98
print(u.id)
```

- [ ] None
- [ ] 1
- [ ] 89
- [x] 98

---

**Question #10**

What do these lines print?

```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(u.id)
```

- [ ] None
- [ ] 1
- [x] 89
- [ ] 98

---

**Question #11**

What do these lines print?

```python
class User:
    id = 1

User.id = 98
u = User()
u.id = 89
print(User.id)
```

- [ ] None
- [ ] 1
- [ ] 89
- [x] 98

---

**Question #12**

What do these lines print?

```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(User.id)
```

- [ ] None
- [ ] 1
- [ ] 89
- [x] 98

---

**Question #13**

What do these lines print?

```python
class User:
    id = 1

u = User()
u.id = 89
User.id = 98
print(u.id)
```

- [ ] None
- [ ] 1
- [x] 89
- [ ] 98

---

## Tasks

### 0. Simple rectangle

Write an empty class `Rectangle` that defines a rectangle:

- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-rectangle.Rectangle'>
{}
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `0-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with a class method to create squares."""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.

# Les guillemets triples (""") servent à écrire une docstring, c'est-à-dire un commentaire
# multi-lignes qui décrit le but du fichier ou d'une fonction/classe. Ici, cela explique
# que le fichier définit une classe Rectangle avec une méthode de classe pour créer des carrés.


class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration de la classe Rectangle. Le mot-clé 'class' permet de définir une nouvelle
    # structure de données personnalisée. Tout ce qui est indenté à l'intérieur fait partie
    # de la classe.
    # La docstring de la classe explique son but : définir un rectangle avec une largeur et une hauteur.

    number_of_instances = 0
    # Variable de classe (partagée par toutes les instances) qui compte le nombre d'objets Rectangle créés.

    print_symbol = "#"
    # Variable de classe qui définit le symbole utilisé pour afficher le rectangle
    # lors de l'utilisation de la fonction print.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée automatiquement lors de la création d'une nouvelle instance.
        # 'self' fait référence à l'objet en cours de création.
        # 'width' et 'height' sont des paramètres optionnels (valeur par défaut 0).
        self.width = width
        # On utilise le setter de width pour valider et stocker la largeur.
        self.height = height
        # On utilise le setter de height pour valider et stocker la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'un rectangle, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property permet d'accéder à la méthode comme si c'était un attribut.
        return self.__width
        # Retourne la valeur privée __width (avec deux underscores pour indiquer que c'est privé).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Setter associé à la propriété width. Permet de définir la largeur avec des vérifications.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier. Sinon, lève une exception TypeError.
            raise TypeError("width must be an integer")
        if value < 0:
            # Vérifie que la valeur est positive ou nulle. Sinon, lève une exception ValueError.
            raise ValueError("width must be >= 0")
        self.__width = value
        # Stocke la valeur validée dans l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Propriété pour accéder à la hauteur du rectangle.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour la propriété height, avec vérification du type et de la valeur.
        if not isinstance(value, int):
            # Vérifie que la hauteur est un entier.
            raise TypeError("height must be an integer")
        if value < 0:
            # Vérifie que la hauteur est positive ou nulle.
            raise ValueError("height must be >= 0")
        self.__height = value
        # Stocke la valeur validée dans l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur pour obtenir l'aire.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, le périmètre est 0 (rectangle "vide").
            return 0
        return 2 * (self.__width + self.__height)
        # Calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation of the rectangle
        with print_symbol.
        """
        # Méthode spéciale appelée par print() pour afficher l'objet.
        if self.__width == 0 or self.__height == 0:
            # Si le rectangle est "vide", retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # Convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # Crée une liste de lignes (une par hauteur), chaque ligne contient print_symbol répété
        # 'width' fois. Les lignes sont assemblées avec des retours à la ligne ("\n").
        # Le caractère spécial "\n" permet de passer à la ligne suivante.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet avec eval().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string (chaîne formatée) pour insérer les valeurs de largeur et hauteur.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement counter.
        """
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple avec del).
        print("Bye rectangle...")
        # Affiche un message à la suppression de l'objet. La fonction print affiche du texte
        # dans le terminal. Les guillemets délimitent la chaîne à afficher.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances car un rectangle a été supprimé.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.
        If both have the same area, return rect_1.
        """
        # Méthode statique (n'utilise pas self ni cls) qui compare deux rectangles.
        if not isinstance(rect_1, Rectangle):
            # Vérifie que rect_1 est bien une instance de Rectangle.
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            # Vérifie que rect_2 est bien une instance de Rectangle.
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            # Compare les aires des deux rectangles.
            return rect_1
            # Si rect_1 est plus grand ou égal, retourne rect_1.
        return rect_2
        # Sinon, retourne rect_2.

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        # Méthode de classe (reçoit la classe en premier paramètre, conventionnellement 'cls').
        # Permet de créer un carré (largeur = hauteur = size).
        return cls(size, size)
        # Retourne une nouvelle instance de Rectangle avec largeur et hauteur égales à size.
```

---

### 1. Real definition of a rectangle

Write a class `Rectangle` that defines a rectangle by: (based on `0-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

guillaume@ubuntu:~/$ ./1-main.py
{'_Rectangle__width': 2, '_Rectangle__height': 4}
{'_Rectangle__width': 10, '_Rectangle__height': 3}
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `1-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
""" Defines a Rectangle class with width and height properties."""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, donc le script sera
# exécuté avec Python 3.
#
# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, c'est-à-dire un commentaire
# spécial utilisé pour décrire le module ou la classe. Cette docstring explique
# que le fichier définit une classe Rectangle avec des propriétés de largeur
# (width) et de hauteur (height).

class Rectangle:
    """Class thart defines a rectangle by its width and height."""
    # Déclaration de la classe Rectangle. Le mot-clé 'class' permet de définir
    # un nouveau type d'objet. Ici, on crée une classe nommée Rectangle.
    #
    # La docstring de la classe décrit brièvement ce que fait la classe :
    # elle définit un rectangle à partir de sa largeur et de sa hauteur.

    def __init__(self, width=0, height=0):
        """ Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale __init__ appelée automatiquement lors de la création
        # d'une nouvelle instance de la classe Rectangle.
        #
        # Les paramètres width et height sont optionnels et valent 0 par défaut.
        # Cela signifie que si on ne précise rien, le rectangle aura une largeur
        # et une hauteur de 0.
        #
        # La docstring de la méthode explique son rôle et décrit les arguments.
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        # Cela déclenche le setter (défini plus bas) qui valide la valeur.
        self.height = height
        # On assigne la valeur du paramètre height à l'attribut height de l'objet.
        # Cela déclenche aussi le setter qui valide la valeur.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en propriété.
        # Cela permet d'accéder à la largeur de l'objet comme un attribut
        # (ex: mon_rectangle.width) au lieu d'appeler une méthode.
        return self.__width
        # On retourne la valeur de l'attribut privé __width.
        # Les deux underscores (__) devant width signifient que cet attribut
        # est privé : il ne doit pas être accédé directement en dehors de la classe.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir le comportement lors de
        # l'affectation d'une nouvelle valeur à la propriété width.
        # Cela permet de valider la valeur avant de la stocker.
        if not isinstance(value, int):
            # On vérifie que la valeur donnée est bien un entier (int).
            # isinstance(value, int) retourne True si value est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError
            # avec un message explicite.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError
            # avec un message explicite.
        self.__width = value
        # Si toutes les vérifications sont passées, on assigne la valeur à
        # l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Comme pour width, ce décorateur permet d'accéder à la hauteur
        # comme une propriété (ex: mon_rectangle.height).
        return self.__height
        # On retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Le décorateur @height.setter permet de définir le comportement lors
        # de l'affectation d'une nouvelle valeur à la propriété height.
        if not isinstance(value, int):
            # On vérifie que la valeur donnée est bien un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("height must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__height = value
        # Si toutes les vérifications sont passées, on assigne la valeur à
        # l'attribut privé __height.
```

---

### 2. Area and Perimeter

Write a class `Rectangle` that defines a rectangle by: (based on `1-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter is equal to `0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Rectangle = __import__('2-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

guillaume@ubuntu:~/$ ./2-main.py
Area: 8 - Perimeter: 12
--
Area: 30 - Perimeter: 26
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `2-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with width and height properties,
area and perimeter methods.
"""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.
# Les triples guillemets (""") servent à écrire une chaîne de caractères multilignes,
# ici utilisée pour la docstring du module, qui décrit brièvement le contenu du fichier.

class Rectangle:
    """Class that define a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring de la classe explique son but.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale appelée lors de la création d'une nouvelle instance de Rectangle.
        # Le double underscore (__init__) indique qu'il s'agit d'une méthode spéciale.
        # self fait référence à l'instance créée.
        # width et height sont des paramètres avec une valeur par défaut de 0.
        # La docstring décrit les paramètres attendus.
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        # Cela déclenche le setter @width.setter pour valider la valeur.
        self.height = height
        # Idem pour height, on utilise le setter pour valider la valeur.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        # Permet d'accéder à la largeur via instance.width.
        return self.__width
        # Retourne la valeur de l'attribut privé __width.
        # Le double underscore rend l'attribut privé (non accessible directement).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir la valeur de width
        # tout en effectuant des vérifications.
        if not isinstance(value, int):
            # Vérifie si value est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("width must be >= 0")
            # Si value est négatif, lève une exception ValueError.
        self.__width = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Décorateur @property pour accéder à la hauteur comme un attribut.
        return self.__height
        # Retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Décorateur @height.setter pour définir la hauteur avec validation.
        if not isinstance(value, int):
            # Vérifie si value est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("height must be >= 0")
            # Lève une exception si value est négatif.
        self.__height = value
        # Si tout est correct, assigne value à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode pour calculer l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode pour calculer le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.
```

---

### 3. String representation

Write a class `Rectangle` that defines a rectangle by: (based on `2-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Rectangle = __import__('3-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

guillaume@ubuntu:~/$ ./3-main.py
Area: 8 - Perimeter: 12
##
##
##
##
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
--
##########
##########
##########
<3-rectangle.Rectangle object at 0x7f92a75a2eb8>
guillaume@ubuntu:~/$ 
```

_Object address can be different_

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `3-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Define a Rectangle class with width and height,
    area, perimeter and string representation.
"""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Ici, '/usr/bin/python3' est le chemin de l'interpréteur.
# Les triples guillemets (""") permettent d'écrire une chaîne de caractères multilignes,
# appelée docstring. Elle sert à documenter le module ou la classe.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring ici décrit le but de la classe.

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle.
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        # Méthode spéciale appelée lors de la création d'une nouvelle instance de la classe.
        # 'self' fait référence à l'objet créé.
        # 'width' et 'height' sont des paramètres avec des valeurs par défaut de 0.
        self.width = width
        # On assigne la valeur du paramètre 'width' à l'attribut 'width' de l'objet.
        self.height = height
        # On assigne la valeur du paramètre 'height' à l'attribut 'height' de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # Retourne la valeur de l'attribut privé '__width'.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Le décorateur @width.setter permet de définir la valeur de 'width'.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("width must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si les vérifications sont passées, assigne la valeur à l'attribut privé '__width'.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Le décorateur @property permet d'accéder à 'height' comme un attribut.
        return self.__height
        # Retourne la valeur de l'attribut privé '__height'.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Le décorateur @height.setter permet de définir la valeur de 'height'.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("height must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si les vérifications sont passées, assigne la valeur à l'attribut privé '__height'.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur pour obtenir l'aire.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation
            of the rectangle with '#' characters.
        """
        # Méthode spéciale qui définit la représentation en chaîne de l'objet.
        # Appelée par la fonction print() ou str().
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        lines = []
        # Crée une liste vide pour stocker chaque ligne du rectangle.
        for _ in range(self.__height):
            # Boucle autant de fois que la hauteur du rectangle.
            lines.append("#" * self.__width)
            # Ajoute une chaîne composée de '#' répétée 'width' fois à la liste.
        return "\n".join(lines)
        # Assemble toutes les lignes avec un saut de ligne '\n' entre chaque,
        # pour former le rectangle en texte.
```

---

### 4. Eval is magic

Write a class `Rectangle` that defines a rectangle by: (based on `3-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`: (see example below)
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()` (see example below)
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

guillaume@ubuntu:~/$ ./4-main.py
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7cc88
--
##
##
##
##
--
##
##
##
##
--
Rectangle(2, 4)
--
0x7f09ebf7ccc0
--
False
True
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `4-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
and provides methods for area, perimeter, and string representation.
"""

# Le shebang (#!/usr/bin/python3) indique au système d'exploitation
# d'utiliser l'interpréteur Python 3 pour exécuter ce fichier.
# Il doit toujours être placé en première ligne du fichier.

# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, ils servent à écrire une docstring,
# c'est-à-dire un commentaire qui décrit le module.
# Les docstrings sont utilisées par la documentation automatique de Python.

class Rectangle:
    """Represents a rectangle."""

    # Déclaration d'une classe nommée Rectangle.
    # Une classe est un modèle pour créer des objets (ici, des rectangles).
    # Les classes commencent toujours par une majuscule par convention.

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        # Méthode spéciale __init__ appelée automatiquement lors de la création
        # d'un nouvel objet Rectangle. Elle initialise les attributs de l'objet.
        # self fait référence à l'instance courante de la classe.
        # width et height sont des paramètres avec des valeurs par défaut (0).
        self.width = width
        # On assigne la valeur du paramètre width à l'attribut width de l'objet.
        self.height = height
        # On assigne la valeur du paramètre height à l'attribut height de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Méthode spéciale appelée lorsqu'on accède à l'attribut width.
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # Retourne la valeur de l'attribut privé __width.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        # Méthode spéciale appelée lorsqu'on modifie l'attribut width.
        # Le décorateur @width.setter permet de définir la valeur de width.
        if not isinstance(value, int):
            # Vérifie si value n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("width must be >= 0")
            # Si value est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Méthode spéciale appelée lorsqu'on accède à l'attribut height.
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        return self.__height
        # Retourne la valeur de l'attribut privé __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        # Méthode spéciale appelée lorsqu'on modifie l'attribut height.
        # Le décorateur @height.setter permet de définir la valeur de height.
        if not isinstance(value, int):
            # Vérifie si value n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si value est négatif.
            raise ValueError("height must be >= 0")
            # Si value est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si les vérifications sont passées, assigne value à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur (__width) par la hauteur (__height) et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation of the
        rectangle with '#' characters.
        """
        # Méthode spéciale appelée par print() ou str().
        # Retourne une chaîne de caractères représentant le rectangle avec des '#'.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        lines = []
        # Crée une liste vide pour stocker chaque ligne du rectangle.
        for _ in range(self.__height):
            # Boucle autant de fois que la hauteur du rectangle.
            lines.append("#" * self.__width)
            # Ajoute une ligne composée de '#' répété largeur fois.
        return "\n".join(lines)
        # Assemble toutes les lignes avec un saut de ligne (\n) entre chaque.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet.
        # Utilisée par la fonction repr().
        return f"Rectangle({self.__width}, {self.__height})"
        # f-string : permet d'insérer les valeurs de __width et __height dans la chaîne.
        # La chaîne retournée peut être utilisée avec eval() pour recréer l'objet.
```

---

### 5. Detect instance deletion

Write a class `Rectangle` that defines a rectangle by: (based on `4-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Rectangle = __import__('5-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

guillaume@ubuntu:~/$ ./5-main.py
Area: 8 - Perimeter: 12
Bye rectangle...
[NameError] name 'my_rectangle' is not defined
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `5-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height,
and provides methods for area, perimeter, and string representations.
"""

# Début du code Python. Le shebang (#!) indique au système d'exploitation
# quel interpréteur utiliser pour exécuter ce fichier. Ici, il s'agit de python3.
# Cela permet de lancer le script directement depuis le terminal.

class Rectangle:
    """Defines a rectangle by its width and height."""

    # Déclaration de la classe Rectangle. Une classe est un modèle pour créer
    # des objets (ici, des rectangles). Le mot-clé 'class' sert à définir une classe.
    # Rectangle est le nom de la classe. Les deux-points (:) indiquent le début du bloc.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        # Méthode spéciale appelée lors de la création d'un nouvel objet Rectangle.
        # '__init__' est le constructeur. 'self' fait référence à l'instance créée.
        # 'width' et 'height' sont des paramètres avec une valeur par défaut de 0.
        self.width = width
        # On assigne la valeur du paramètre 'width' à l'attribut 'width' de l'objet.
        self.height = height
        # On assigne la valeur du paramètre 'height' à l'attribut 'height' de l'objet.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Définition d'une propriété 'width'. Permet d'accéder à la largeur
        # comme un attribut, mais en utilisant une méthode.
        return self.__width
        # Retourne la valeur de l'attribut privé '__width' de l'objet.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is negative.
        """
        # Définit le setter pour la propriété 'width'. Permet de contrôler
        # la modification de la largeur.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("width must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__width = value
        # Si tout est correct, assigne la valeur à l'attribut privé '__width'.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Définition d'une propriété 'height'. Permet d'accéder à la hauteur
        # comme un attribut, mais en utilisant une méthode.
        return self.__height
        # Retourne la valeur de l'attribut privé '__height' de l'objet.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is negative.
        """
        # Définit le setter pour la propriété 'height'. Permet de contrôler
        # la modification de la hauteur.
        if not isinstance(value, int):
            # Vérifie si 'value' n'est pas un entier.
            raise TypeError("height must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie si 'value' est négatif.
            raise ValueError("height must be >= 0")
            # Si c'est négatif, lève une exception ValueError avec un message.
        self.__height = value
        # Si tout est correct, assigne la valeur à l'attribut privé '__height'.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur et retourne le résultat.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 fois (largeur + hauteur).

    def __str__(self):
        """Return the string representation of the rectangle using '#'."""
        # Méthode spéciale qui définit la représentation "printable" de l'objet.
        # Utilisée par print() ou str().
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, retourne une chaîne vide.
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # Sinon, crée une chaîne composée de lignes de '#' :
        # - "#" * self.__width crée une ligne de '#' de la largeur du rectangle.
        # - for _ in range(self.__height) répète cette ligne pour chaque hauteur.
        # - "\n".join(...) assemble les lignes avec des retours à la ligne.
        # Les guillemets doubles ("") délimitent les chaînes de caractères.
        # Le caractère spécial '\n' représente un saut de ligne.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet.
        # Utilisée par la fonction repr().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string (f"") pour insérer les valeurs de largeur et hauteur
        # dans la chaîne. Les accolades {} servent à insérer les variables.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted."""
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple,
        # quand il n'est plus utilisé). Permet d'exécuter du code à la destruction.
        print("Bye rectangle...")
        # Affiche le message "Bye rectangle..." dans la console.
        # La fonction print() sert à afficher du texte à l'écran.
        # Les guillemets délimitent la chaîne à afficher.
```

---

### 6. How many instances

Write a class `Rectangle` that defines a rectangle by: (based on `5-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Rectangle = __import__('6-rectangle').Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))

guillaume@ubuntu:~/$ ./6-main.py
2 instances of Rectangle
Bye rectangle...
1 instances of Rectangle
Bye rectangle...
0 instances of Rectangle
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `6-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with instance counter."""
# Les guillemets triples (""" """) permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, utilisée pour décrire le
# fichier ou le module. Elle peut être lue par des outils de documentation.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Cette docstring décrit la classe Rectangle.
    # Une classe est un plan (ou modèle) pour créer des objets.

    number_of_instances = 0  # Attribut de classe
    # Ceci est un attribut de classe, partagé par toutes les instances
    # de Rectangle. Il compte le nombre d'objets Rectangle créés.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # __init__ est le constructeur de la classe. Il est appelé
        # automatiquement lors de la création d'un nouvel objet.
        # self fait référence à l'objet créé.
        # width et height sont des paramètres avec des valeurs par défaut (0).
        self.width = width
        # On utilise le setter width pour valider et assigner la largeur.
        self.height = height
        # On utilise le setter height pour valider et assigner la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # @property transforme cette méthode en attribut en lecture seule.
        return self.__width
        # On retourne la valeur privée __width (avec deux underscores pour
        # indiquer que c'est un attribut interne à la classe).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Cette méthode permet d'assigner une valeur à width tout en
        # effectuant des vérifications.
        if not isinstance(value, int):
            # On vérifie que la valeur est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur est positive ou nulle.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__width = value
        # Si tout est correct, on assigne la valeur à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Même principe que pour width, mais pour la hauteur.
        return self.__height
        # On retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour la hauteur, avec vérifications.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie que la valeur est positive ou nulle.
            raise ValueError("height must be >= 0")
            # Lève une exception si la valeur est négative.
        self.__height = value
        # Assigne la valeur à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode pour calculer l'aire du rectangle.
        return self.__width * self.__height
        # Aire = largeur x hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode pour calculer le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Périmètre = 2 x (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with '#' characters.
        """
        # __str__ permet de définir ce qui s'affiche quand on fait print(objet).
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, on retourne une chaîne vide.
            return ""
        return "\n".join("#" * self.__width for _ in range(self.__height))
        # On crée une chaîne composée de lignes de '#' :
        # - "#" * self.__width crée une ligne de '#' de la largeur du rectangle.
        # - for _ in range(self.__height) répète cette ligne pour chaque hauteur.
        # - "\n".join(...) assemble toutes les lignes avec un saut de ligne.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # __repr__ retourne une chaîne qui permet de recréer l'objet.
        return f"Rectangle({self.__width}, {self.__height})"
        # f"..." est une f-string (chaîne formatée) qui insère les valeurs
        # de __width et __height dans la chaîne.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement counter.
        """
        # __del__ est appelée automatiquement quand l'objet est détruit
        # (par exemple, avec del ou à la fin du programme).
        print("Bye rectangle...")
        # print affiche un message à l'écran lors de la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # On décrémente le compteur d'instances.
```

---

### 7. Change representation

Write a class `Rectangle` that defines a rectangle by: (based on `6-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character(s) stored in  `print_symbol`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 7-main.py
#!/usr/bin/python3
Rectangle = __import__('7-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
print(my_rectangle_1)
print("--")
my_rectangle_1.print_symbol = "&"
print(my_rectangle_1)
print("--")

my_rectangle_2 = Rectangle(2, 1)
print(my_rectangle_2)
print("--")
Rectangle.print_symbol = "C"
print(my_rectangle_2)
print("--")

my_rectangle_3 = Rectangle(7, 3)
print(my_rectangle_3)

print("--")

my_rectangle_3.print_symbol = ["C", "is", "fun!"]
print(my_rectangle_3)

print("--")

guillaume@ubuntu:~/$ ./7-main.py
########
########
########
########
--
&&&&&&&&
&&&&&&&&
&&&&&&&&
&&&&&&&&
--
##
--
CC
--
CCCCCCC
CCCCCCC
CCCCCCC
--
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']['C', 'is', 'fun!']
--
Bye rectangle...
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `7-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with customizable print symbol."""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.

# Les guillemets triples (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, c'est-à-dire un commentaire
# de documentation qui explique le but du fichier ou du module.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration d'une classe nommée Rectangle.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring ici décrit le rôle de la classe.

    number_of_instances = 0
    # Variable de classe (partagée par toutes les instances).
    # Elle compte le nombre d'objets Rectangle créés.

    print_symbol = "#"
    # Variable de classe utilisée pour afficher le rectangle.
    # Par défaut, le symbole utilisé est le dièse (#).

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée lors de la création d'un nouvel objet Rectangle.
        # Elle initialise les attributs width (largeur) et height (hauteur).
        # Les paramètres width et height ont une valeur par défaut de 0.
        self.width = width
        # On utilise le setter de width pour valider et assigner la largeur.
        self.height = height
        # On utilise le setter de height pour valider et assigner la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property transforme cette méthode en attribut en lecture seule.
        # Permet d'accéder à la largeur avec obj.width.
        return self.__width
        # Retourne la valeur privée __width (attribut d'instance).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Setter associé à la propriété width.
        # Permet d'assigner une valeur à width tout en validant la donnée.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, lève une exception TypeError avec un message.
        if value < 0:
            # Vérifie que la valeur est positive ou nulle.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, lève une exception ValueError.
        self.__width = value
        # Si tout est correct, assigne la valeur à l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Propriété pour accéder à la hauteur de l'objet.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour valider et assigner la hauteur.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie que la valeur est positive ou nulle.
            raise ValueError("height must be >= 0")
            # Lève une exception si la valeur est négative.
        self.__height = value
        # Assigne la valeur à l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, calcule le périmètre : 2 × (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with print_symbol.
        """
        # Méthode spéciale appelée par str(obj) ou print(obj).
        # Retourne une chaîne représentant le rectangle avec le symbole choisi.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est nulle, retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # Convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # Crée une liste de lignes (une par hauteur), chaque ligne contient le symbole répété largeur fois.
        # "\n".join(...) assemble toutes les lignes avec un saut de ligne entre chaque.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale appelée par repr(obj).
        # Retourne une chaîne qui permet de recréer l'objet avec eval().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string pour insérer les valeurs de largeur et hauteur.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted and
        decrement counter.
        """
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple avec del).
        print("Bye rectangle...")
        # Affiche un message d'adieu à la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances de la classe.
```

---

### 8. Compare rectangles

Write a class `Rectangle` that defines a rectangle by: (based on `7-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 8-main.py
#!/usr/bin/python3
Rectangle = __import__('8-rectangle').Rectangle

my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")

guillaume@ubuntu:~/$ ./8-main.py
my_rectangle_1 is bigger or equal to my_rectangle_2
my_rectangle_2 is bigger than my_rectangle_1
Bye rectangle...
Bye rectangle...
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `8-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with comparison static method."""
# Ceci est une chaîne de caractères spéciale appelée "docstring".
# Elle sert à documenter le fichier ou le module.
# Les triples guillemets (""") permettent d'écrire sur plusieurs lignes.

class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Cette docstring décrit la classe Rectangle.
    # Une classe est un plan pour créer des objets (ici, des rectangles).

    number_of_instances = 0
    # Variable de classe : elle compte combien d'instances (objets)
    # Rectangle ont été créées. Elle est partagée par tous les objets.

    print_symbol = "#"
    # Variable de classe : définit le symbole utilisé pour afficher
    # le rectangle avec la méthode __str__. Par défaut, c'est "#".

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée automatiquement lors de la création
        # d'un nouvel objet Rectangle. Elle initialise la largeur et la hauteur.
        # Les paramètres width et height ont des valeurs par défaut de 0.
        self.width = width
        # Attribut d'instance : la largeur du rectangle.
        # On utilise le setter (voir plus bas) pour valider la valeur.
        self.height = height
        # Attribut d'instance : la hauteur du rectangle.
        # On utilise aussi le setter pour valider la valeur.
        Rectangle.number_of_instances += 1
        # À chaque création d'objet, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Cette méthode permet d'accéder à la largeur (width)
        # comme s'il s'agissait d'un attribut simple.
        return self.__width
        # On retourne la valeur privée __width (avec deux underscores),
        # qui stocke la largeur réelle.

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Cette méthode permet d'attribuer une valeur à width
        # tout en vérifiant qu'elle est correcte.
        if not isinstance(value, int):
            # On vérifie que la valeur est un entier (int).
            raise TypeError("width must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError.
        if value < 0:
            # On vérifie que la valeur n'est pas négative.
            raise ValueError("width must be >= 0")
            # Si la valeur est négative, on lève une exception ValueError.
        self.__width = value
        # Si tout est correct, on stocke la valeur dans l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Permet d'accéder à la hauteur (height) comme un attribut simple.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Permet d'attribuer une valeur à height avec validation.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier.
            raise TypeError("height must be an integer")
            # Lève une exception si ce n'est pas un entier.
        if value < 0:
            # Vérifie que la valeur n'est pas négative.
            raise ValueError("height must be >= 0")
            # Lève une exception si la valeur est négative.
        self.__height = value
        # Stocke la valeur dans l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Aire = largeur * hauteur.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si la largeur ou la hauteur est 0, le périmètre est 0.
            return 0
        return 2 * (self.__width + self.__height)
        # Sinon, périmètre = 2 * (largeur + hauteur).

    def __str__(self):
        """Return the string representation of
        the rectangle with print_symbol.
        """
        # Méthode spéciale appelée par print() ou str().
        # Retourne une chaîne qui représente le rectangle avec le symbole choisi.
        if self.__width == 0 or self.__height == 0:
            # Si largeur ou hauteur est 0, retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # On convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # On crée une liste de lignes (une par hauteur), chaque ligne contient
        # le symbole répété largeur fois. On assemble les lignes avec "\n" (saut de ligne).

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer
        # l'objet avec eval(). Utile pour le débogage.
        return f"Rectangle({self.__width}, {self.__height})"
        # f-string : permet d'insérer les valeurs de __width et __height dans la chaîne.

    def __del__(self):
        """Print a message when a Rectangle instance is
        deleted and decrement counter.
        """
        # Méthode spéciale appelée quand l'objet est détruit (par exemple, avec del).
        print("Bye rectangle...")
        # Affiche un message à la suppression de l'objet.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.
        If both have the same area, return rect_1.
        """
        # Méthode statique : ne dépend pas d'une instance particulière.
        # Compare deux rectangles et retourne celui qui a la plus grande aire.
        if not isinstance(rect_1, Rectangle):
            # Vérifie que rect_1 est bien une instance de Rectangle.
            raise TypeError("rect_1 must be an instance of Rectangle")
            # Lève une exception si ce n'est pas le cas.
        if not isinstance(rect_2, Rectangle):
            # Vérifie que rect_2 est bien une instance de Rectangle.
            raise TypeError("rect_2 must be an instance of Rectangle")
            # Lève une exception si ce n'est pas le cas.
        if rect_1.area() >= rect_2.area():
            # Compare les aires des deux rectangles.
            # Si rect_1 a une aire supérieure ou égale, on le retourne.
            return rect_1
        return rect_2
        # Sinon, on retourne rect_2.
```

---

### 9. A square is a rectangle

Write a class `Rectangle` that defines a rectangle by: (based on `8-rectangle.py`)

- Private instance attribute: `width`:
  - property `def width(self):` to retrieve it
  - property setter `def width(self, value):` to set it:
    - `width` must be an integer, otherwise raise a `TypeError` exception with the message `width must be an integer`
    - if `width` is less than `0`, raise a `ValueError` exception with the message `width must be >= 0`
- Private instance attribute: `height`:
  - property `def height(self):` to retrieve it
  - property setter `def height(self, value):` to set it:
    - `height` must be an integer, otherwise raise a `TypeError` exception with the message `height must be an integer`
    - if `height` is less than `0`, raise a `ValueError` exception with the message `height must be >= 0`
- Public class attribute `number_of_instances`:
  - Initialized to `0`
  - Incremented during each new instance instantiation
  - Decremented during each instance deletion
- Public class attribute `print_symbol`:
  - Initialized to `#`
  - Used as symbol for string representation
  - Can be any type
- Instantiation with optional `width` and `height`: `def __init__(self, width=0, height=0):`
- Public instance method: `def area(self):` that returns the rectangle area
- Public instance method: `def perimeter(self):` that returns the rectangle perimeter:
  - if `width` or `height` is equal to `0`, perimeter has to be equal to `0`
- `print()` and `str()` should print the rectangle with the character `#`:
  - if `width` or `height` is equal to 0, return an empty string
- `repr()` should return a string representation of the rectangle to be able to recreate a new instance by using `eval()`
- Print the message `Bye rectangle...` (`...` being 3 dots not ellipsis) when an instance of `Rectangle` is deleted
- Static method `def bigger_or_equal(rect_1, rect_2):` that returns the biggest rectangle based on the area
  - `rect_1` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_1 must be an instance of Rectangle`
  - `rect_2` must be an instance of `Rectangle`, otherwise raise a `TypeError` exception with the message `rect_2 must be an instance of Rectangle`
  - Returns `rect_1` if both have the same area value
- Class method `def square(cls, size=0):` that returns a new Rectangle instance with `width == height == size`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 9-main.py
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)

guillaume@ubuntu:~/$ ./9-main.py
Area: 25 - Perimeter: 20
#####
#####
#####
#####
#####
Bye rectangle...
guillaume@ubuntu:~/$ 
```

**No test cases needed**

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-more_classes`
- File: `9-rectangle.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a Rectangle class with a class method to create squares."""
# Le shebang (#!) indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement depuis le terminal.

# Les guillemets triples (""") servent à écrire une docstring, c'est-à-dire un commentaire
# multi-lignes qui décrit le but du fichier ou d'une fonction/classe. Ici, cela explique
# que le fichier définit une classe Rectangle avec une méthode de classe pour créer des carrés.


class Rectangle:
    """Class that defines a rectangle by its width and height."""
    # Déclaration de la classe Rectangle. Le mot-clé 'class' permet de définir une nouvelle
    # structure de données personnalisée. Tout ce qui est indenté à l'intérieur fait partie
    # de la classe.
    # La docstring de la classe explique son but : définir un rectangle avec une largeur et une hauteur.

    number_of_instances = 0
    # Variable de classe (partagée par toutes les instances) qui compte le nombre d'objets Rectangle créés.

    print_symbol = "#"
    # Variable de classe qui définit le symbole utilisé pour afficher le rectangle
    # lors de l'utilisation de la fonction print.

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle and increment instance counter."""
        # Méthode spéciale appelée automatiquement lors de la création d'une nouvelle instance.
        # 'self' fait référence à l'objet en cours de création.
        # 'width' et 'height' sont des paramètres optionnels (valeur par défaut 0).
        self.width = width
        # On utilise le setter de width pour valider et stocker la largeur.
        self.height = height
        # On utilise le setter de height pour valider et stocker la hauteur.
        Rectangle.number_of_instances += 1
        # À chaque création d'un rectangle, on incrémente le compteur d'instances.

    @property
    def width(self):
        """Get the width of the rectangle."""
        # Le décorateur @property permet d'accéder à la méthode comme si c'était un attribut.
        return self.__width
        # Retourne la valeur privée __width (avec deux underscores pour indiquer que c'est privé).

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        # Setter associé à la propriété width. Permet de définir la largeur avec des vérifications.
        if not isinstance(value, int):
            # Vérifie que la valeur est un entier. Sinon, lève une exception TypeError.
            raise TypeError("width must be an integer")
        if value < 0:
            # Vérifie que la valeur est positive ou nulle. Sinon, lève une exception ValueError.
            raise ValueError("width must be >= 0")
        self.__width = value
        # Stocke la valeur validée dans l'attribut privé __width.

    @property
    def height(self):
        """Get the height of the rectangle."""
        # Propriété pour accéder à la hauteur du rectangle.
        return self.__height
        # Retourne la valeur privée __height.

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        # Setter pour la propriété height, avec vérification du type et de la valeur.
        if not isinstance(value, int):
            # Vérifie que la hauteur est un entier.
            raise TypeError("height must be an integer")
        if value < 0:
            # Vérifie que la hauteur est positive ou nulle.
            raise ValueError("height must be >= 0")
        self.__height = value
        # Stocke la valeur validée dans l'attribut privé __height.

    def area(self):
        """Return the area of the rectangle."""
        # Méthode qui calcule et retourne l'aire du rectangle.
        return self.__width * self.__height
        # Multiplie la largeur par la hauteur pour obtenir l'aire.

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        # Méthode qui calcule et retourne le périmètre du rectangle.
        if self.__width == 0 or self.__height == 0:
            # Si l'un des côtés est nul, le périmètre est 0 (rectangle "vide").
            return 0
        return 2 * (self.__width + self.__height)
        # Calcule le périmètre : 2 fois la somme de la largeur et de la hauteur.

    def __str__(self):
        """Return the string representation of the rectangle
        with print_symbol.
        """
        # Méthode spéciale appelée par print() pour afficher l'objet.
        if self.__width == 0 or self.__height == 0:
            # Si le rectangle est "vide", retourne une chaîne vide.
            return ""
        symbol = str(self.print_symbol)
        # Convertit print_symbol en chaîne de caractères (au cas où ce serait un autre type).
        return "\n".join(symbol * self.__width for _ in range(self.__height))
        # Crée une liste de lignes (une par hauteur), chaque ligne contient print_symbol répété
        # 'width' fois. Les lignes sont assemblées avec des retours à la ligne ("\n").
        # Le caractère spécial "\n" permet de passer à la ligne suivante.

    def __repr__(self):
        """Return a string that can recreate the rectangle."""
        # Méthode spéciale qui retourne une chaîne permettant de recréer l'objet avec eval().
        return f"Rectangle({self.__width}, {self.__height})"
        # Utilise une f-string (chaîne formatée) pour insérer les valeurs de largeur et hauteur.

    def __del__(self):
        """Print a message when a Rectangle instance is deleted
        and decrement counter.
        """
        # Méthode spéciale appelée lors de la suppression de l'objet (par exemple avec del).
        print("Bye rectangle...")
        # Affiche un message à la suppression de l'objet. La fonction print affiche du texte
        # dans le terminal. Les guillemets délimitent la chaîne à afficher.
        Rectangle.number_of_instances -= 1
        # Décrémente le compteur d'instances car un rectangle a été supprimé.

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on the area.
        If both have the same area, return rect_1.
        """
        # Méthode statique (n'utilise pas self ni cls) qui compare deux rectangles.
        if not isinstance(rect_1, Rectangle):
            # Vérifie que rect_1 est bien une instance de Rectangle.
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            # Vérifie que rect_2 est bien une instance de Rectangle.
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            # Compare les aires des deux rectangles.
            return rect_1
            # Si rect_1 est plus grand ou égal, retourne rect_1.
        return rect_2
        # Sinon, retourne rect_2.

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle instance with width == height == size."""
        # Méthode de classe (reçoit la classe en premier paramètre, conventionnellement 'cls').
        # Permet de créer un carré (largeur = hauteur = size).
        return cls(size, size)
        # Retourne une nouvelle instance de Rectangle avec largeur et hauteur égales à size.
```
