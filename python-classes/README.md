![oop-meme](https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/247/oop-meme.jpg)

## Background Context

It’s VERY important that you read at least all the material that is listed below (and skip what we recommend you to skip, you will see them later in the curriculum).

As usual, make sure you type (never copy and paste), test, understand all examples shown in the following links (including those in the video), test again etc. 
The biggest and most important takeaway of this project is: experiment by yourself OOP, play with it!

Read or watch the below resources in the order presented.

## Resources

**Read or watch**:

- [Object Oriented Programming](https://python.swaroopch.com/oop.html) (_Read everything until the paragraph “Inheritance” excluded. You do NOT have to learn about class attributes, `classmethod` and `staticmethod` yet_)
- [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php) (_Please *be careful*: in most of the following paragraphs, the author shows things the way you should not use or write a class in order to help you better understand some concepts and how everything works in Python 3. Make sure you read everything in the following paragraphs: General Introduction, First-class Everything, A Minimal Class in Python, Attributes (You DON’T have to learn about class attributes), Methods, The `__init__` Method, “Data Abstraction, Data Encapsulation, and Information Hiding,” “Public, Protected, and Private Attributes”_)
- [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
- [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE)
- [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
- [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), **without the help of Google**:

### General

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
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the `__dict__` of a class and/or instance of a class and what does it contain
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
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## More Info

**Documentation is now mandatory!** Each module, class, and method must contain docstring as comments. [Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

---

## Quiz

### Question #0

In this following code, what is `User`?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

- [x] A class
- [ ] A string
- [ ] An attribute
- [ ] A method
- [ ] An instance

---

### Question #1

In this following code, what is `id`?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

- [ ] A public instance attribute
- [x] A public class attribute
- [ ] A public class method
- [ ] A public instance method
- [ ] A private class attribute
- [ ] A protected class attribute

---

### Question #2

In this following code, what is `__password`?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

- [ ] A public class attribute
- [ ] A public instance attribute
- [ ] A protected class attribute
- [ ] A protected instance attribute
- [x] A private class attribute
- [ ] A private instance attribute

---

### Question #3

In this following code, what is `is_new`?

```python
class User:
    id = 89
    name = "no name"
    __password = None

    def __init__(self, new_name=None):
        self.is_new = True
        if new_name is not None:
            self.name = new_name
```

- [ ] A public class attribute
- [x] A public instance attribute
- [ ] A protected class attribute
- [ ] A protected instance attribute
- [ ] A private class attribute
- [ ] A private instance attribute

---

### Question #4

What do these lines print?

```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.is_new
```

- [ ] is_new
- [ ] Nothing
- [ ] False
- [x] True

---

### Question #5

What do these lines print?

```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.id
```

- [x] 89
- [ ] id
- [ ] User.id
- [ ] Nothing

---

### Question #6

What do these lines print?

```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User("John")
>>> u.name
```

- [ ] name
- [ ] None
- [x] John
- [ ] no name

---

### Question #7

What do these lines print?

```python
>>> class User:
>>>     id = 89
>>>     name = "no name"
>>>     __password = None
>>>     
>>>     def __init__(self, new_name=None):
>>>         self.is_new = True
>>>         if new_name is not None:
>>>             self.name = new_name
>>> 
>>> u = User()
>>> u.name
```

- [ ] name
- [ ] None
- [ ] John
- [x] no name

---

## Tasks

### 0. My first square

Write an empty class `Square` that defines a square:

- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/python3
Square = __import__('0-square').Square

my_square = Square()
print(type(my_square))
print(my_square.__dict__)

guillaume@ubuntu:~/$ ./0-main.py
<class '0-square.Square'>
{}
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `0-square.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines an empty class Square."""
# Les trois guillemets doubles (""") servent à écrire une chaîne de caractères
# sur plusieurs lignes. Ici, cette chaîne est un commentaire de documentation
# (appelé "docstring") qui explique le but du fichier ou du module.
# Les docstrings sont utilisées par Python pour générer de la documentation
# automatiquement et pour aider les utilisateurs à comprendre le code.


class Square:
    """Empty class Square."""
    # Ici encore, les trois guillemets doubles (""") servent à écrire une
    # docstring, cette fois pour la classe. Elle explique que la classe
    # Square est vide pour l’instant. Les docstrings de classe sont utiles
    # pour documenter le rôle de la classe auprès des autres développeurs.

    pass
    # Le mot-clé "pass" est une instruction spéciale en Python qui signifie
    # "ne rien faire". On l’utilise ici parce que la classe ne contient
    # aucune méthode ni attribut pour l’instant, mais la syntaxe exige
    # qu’il y ait au moins une instruction à l’intérieur de la classe.
    # "pass" permet donc de créer une classe vide sans erreur de syntaxe.
```
---

### 1. Square with size

Write a class `Square` that defines a square by: (based on `0-square.py`)

- Private instance attribute: `size`
- Instantiation with `size` (no type/value verification)
- You are not allowed to import any module

**Why?**

*Why `size` is private attribute?*

The size of a square is crucial for a square, many things depend of it (area computation, etc.), so you, as class builder, must control the type and value of this attribute. 
One way to have the control is to keep it privately. 
You will see in next tasks how to get, update and validate the size value.

```python
guillaume@ubuntu:~/$ cat 1-main.py
#!/usr/bin/python3
Square = __import__('1-square').Square

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

try:
    print(my_square.__size)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./1-main.py
<class '1-square.Square'>
{'_Square__size': 3}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `1-square.py`

**Code:**
```python
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
```

---

### 2. Size validation

Write a class `Square` that defines a square by: (based on `1-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 2-main.py
#!/usr/bin/python3
Square = __import__('2-square').Square

my_square_1 = Square(3)
print(type(my_square_1))
print(my_square_1.__dict__)

my_square_2 = Square()
print(type(my_square_2))
print(my_square_2.__dict__)

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

try:
    my_square_3 = Square("3")
    print(type(my_square_3))
    print(my_square_3.__dict__)
except Exception as e:
    print(e)

try:
    my_square_4 = Square(-89)
    print(type(my_square_4))
    print(my_square_4.__dict__)
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./2-main.py
<class '2-square.Square'>
{'_Square__size': 3}
<class '2-square.Square'>
{'_Square__size': 0}
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
size must be an integer
size must be >= 0
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `2-square.py`

**Code:**
```python
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
```

---

### 3. Area of a square

Write a class `Square` that defines a square by: (based on `2-square.py`)

- Private instance attribute: `size`
- Instantiation with optional `size`: `def __init__(self, size=0):`
  - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
  - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 3-main.py
#!/usr/bin/python3
Square = __import__('3-square').Square

my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))

guillaume@ubuntu:~/$ ./3-main.py
Area: 9
'Square' object has no attribute 'size'
'Square' object has no attribute '__size'
Area: 25
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `3-square.py`

**Code:**
```python
#!/usr/bin/python3
"""Define a class Square with a private size attribute."""
# Le shebang (#!) indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de python3, situé dans /usr/bin/python3.

# Les triples guillemets (""") permettent d'écrire une chaîne de caractères
# sur plusieurs lignes. Ici, c'est une docstring, utilisée pour documenter
# le module ou le fichier. Elle explique brièvement le but du fichier.


class Square:
    """Class that define a Square by its size."""
    # Déclaration d'une nouvelle classe nommée Square.
    # Les classes servent à créer des objets avec des propriétés et des méthodes.
    # La docstring de la classe décrit son objectif.

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            Size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # __init__ est une méthode spéciale appelée automatiquement lors de la création
        # d'une nouvelle instance de la classe. Elle sert à initialiser l'objet.
        # self fait référence à l'instance courante de la classe.
        # size est un paramètre optionnel (valeur par défaut : 0).
        # La docstring de la méthode explique son fonctionnement, ses paramètres
        # et les exceptions qu'elle peut lever.

        if not isinstance(size, int):
            # Vérifie si size n'est pas un entier (int).
            # isinstance(obj, type) retourne True si obj est du type indiqué.
            raise TypeError("size must be an integer")
            # Si size n'est pas un entier, lève une exception TypeError
            # avec un message d'erreur explicite.

        if size < 0:
            # Vérifie si size est inférieur à 0.
            raise ValueError("size must be >= 0")
            # Si size est négatif, lève une exception ValueError
            # avec un message d'erreur explicite.

        self.__size = size
        # Attribue la valeur de size à l'attribut privé __size de l'objet.
        # Le double underscore (__) rend l'attribut privé (non accessible directement
        # depuis l'extérieur de la classe).

    def area(self):
        """Return the current square area."""
        # Définition d'une méthode nommée area, qui calcule et retourne l'aire du carré.
        # self permet d'accéder aux attributs et méthodes de l'objet courant.
        # La docstring décrit ce que fait la méthode.

        return self.__size * self.__size
        # Calcule l'aire du carré en multipliant la taille (__size) par elle-même.
        # L'opérateur * sert à faire une multiplication.
        # return permet de renvoyer le résultat à l'appelant de la méthode.
```
---

### 4. Access and update private attribute

Write a class `Square` that defines a square by: (based on `3-square.py`)

- Private instance attribute: `size`:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- You are not allowed to import any module

**Why?**

*Why a getter and setter?*

Reminder: `size` is a private attribute. We did that to make sure we control the type and value. 
Getter and setter methods are not 100% Python, but more OOP. 
With them, you will be able to validate the assignment of a private attribute and also define how getting the attribute value will be available from outside - by copy? by assignment? etc.
Also, adding type/value validation in the setter will centralize the logic, since you will do it in only one place.

```python
guillaume@ubuntu:~/$ cat 4-main.py
#!/usr/bin/python3
Square = __import__('4-square').Square

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)

guillaume@ubuntu:~/$ ./4-main.py
Area: 7921 for size: 89
Area: 9 for size: 3
size must be an integer
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `4-square.py`

**Code:**
```python
#!/usr/bin/python3
"""Defines a class Square with a private size attribute and property."""
# Les triples guillemets (""" """) définissent une chaîne de caractères multilignes,
# utilisée ici comme docstring (documentation) pour le module.
# Cette docstring explique brièvement le but du fichier ou du module.


class Square:
    """Class the defines à Square by its size."""
    # Ceci est une docstring pour la classe Square.
    # Elle explique que la classe définit un carré par sa taille.

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        # __init__ est une méthode spéciale appelée constructeur.
        # Elle est appelée automatiquement lors de la création d'un nouvel objet Square.
        # self fait référence à l'instance courante de la classe.
        # size=0 signifie que le paramètre size est optionnel et vaut 0 par défaut.
        self.size = size
        # On utilise la propriété size (définie plus bas) pour initialiser la taille du carré.
        # Cela permet de profiter de la validation faite dans le setter.

    @property
    def size(self):
        """Get the size of the square."""
        # Cette méthode est un getter pour l'attribut privé __size.
        # Le décorateur @property permet d'accéder à cette méthode comme à un attribut.
        return self.__size
        # On retourne la valeur de l'attribut privé __size.
        # Les deux underscores (__) rendent l'attribut privé (non accessible directement de l'extérieur).

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        # Cette méthode est un setter pour l'attribut size.
        # Le décorateur @size.setter permet de définir la valeur de size avec des vérifications.
        if not isinstance(value, int):
            # On vérifie si value n'est pas un entier (int).
            raise TypeError("size must be an integer")
            # Si ce n'est pas un entier, on lève une exception TypeError avec un message explicite.
        if value < 0:
            # On vérifie si value est inférieur à 0.
            raise ValueError("size must be >= 0")
            # Si value est négatif, on lève une exception ValueError avec un message explicite.
        self.__size = value
        # Si toutes les vérifications sont passées, on assigne value à l'attribut privé __size.

    def area(self):
        """Return the current square area."""
        # Cette méthode calcule et retourne l'aire du carré.
        return self.__size * self.__size
        # On multiplie la taille (__size) par elle-même pour obtenir l'aire (côté x côté).
        # Le symbole * est l'opérateur de multiplication en Python.
```
---

### 5. Printing a square

Write a class `Square` that defines a square by: (based on `4-square.py`)

- Private instance attribute: `size`:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Instantiation with optional `size`: `def __init__(self, size=0):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 5-main.py
#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 10
my_square.my_print()

print("--")

my_square.size = 0
my_square.my_print()

print("--")

guillaume@ubuntu:~/$ ./5-main.py
###
###
###
--
##########
##########
##########
##########
##########
##########
##########
##########
##########
##########
--

--
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `5-square.py`

**Code:**
```python
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
```
---

### 6. Coordinates of a square

Write a class `Square` that defines a square by: (based on `5-square.py`)

- Private instance attribute: `size`:
  - property `def size(self):` to retrieve it
  - property setter `def size(self, value):` to set it:
    - `size` must be an integer, otherwise raise a `TypeError` exception with the message `size must be an integer`
    - if `size` is less than `0`, raise a `ValueError` exception with the message `size must be >= 0`
- Private instance attribute: `position`:
  - property `def position(self):` to retrieve it
  - property setter `def position(self, value):` to set it:
    - `position` must be a tuple of 2 positive integers, otherwise raise a `TypeError` exception with the message `position must be a tuple of 2 positive integers`
- Instantiation with optional `size` and optional `position`: `def __init__(self, size=0, position=(0, 0)):`
- Public instance method: `def area(self):` that returns the current square area
- Public instance method: `def my_print(self):` that prints in stdout the square with the character `#`:
  - if `size` is equal to 0, print an empty line
  - `position` should be set using space - **Don’t fill lines by spaces** when `position[1] > 0`
- You are not allowed to import any module

```python
guillaume@ubuntu:~/$ cat 6-main.py
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")

guillaume@ubuntu:~/$ ./6-main.py | tr " " "_" | cat -e
###$
###$
###$
--$
$
_###$
_###$
_###$
--$
___###$
___###$
___###$
--$
guillaume@ubuntu:~/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-classes`
- File: `6-square.py`

**Code:**
```python
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
```