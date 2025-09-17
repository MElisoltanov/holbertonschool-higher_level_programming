# Project: Python - Hello, World | Holberton Toulouse, France Intranet

For this project, we expect you to look at this concept:
- [Python programming](https://intranet.hbtn.io/concepts/896 "Python programming")

## Author’s disclaimer

```
Welcome to the Python world!

You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Python has a linter / style guide, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume
```

## Resources

**Read or watch**:

Use this playlist as long as you are learning Python:

- [Learn to Program](https://www.youtube.com/playlist?list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt "Learn to Program")
- [Whetting Your Appetite](https://docs.python.org/3/tutorial/appetite.html "Whetting Your Appetite")
- [Using the Python Interpreter](https://docs.python.org/3/tutorial/interpreter.html "Using the Python Interpreter")
- [An Informal Introduction to Python](https://docs.python.org/3/tutorial/introduction.html "An Informal Introduction to Python") (_Read up until “3.1.2. Strings” included_)
- [How To Use String Formatters in Python 3](https://realpython.com/python-f-strings/ "How To Use String Formatters in Python 3")
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/ "Pycodestyle -- Style Guide for Python Code")

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/ "explain to anyone"), **without the help of Google**:

### General

- How to use the Python interpreter
- How to print text and variables using `print`
- How to use strings
- What are indexing and slicing in Python
- What is the official Python coding style and how to check your code with `pycodestyle`

## Requirements

### Python Scripts

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.*)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repo, containing a description of the repository
- A `README.md` file, at the root of the folder of _this_ project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`

## More Info

### Pycodestyle

`Pycodestyle` is now the [new standard of Python style code](https://github.com/PyCQA/pycodestyle/issues/466 "new standard of Python style code")

---

## Quiz

**Great!**
You've completed the quiz successfully! Keep going!

### Question #0

What does this command line print?

```python
>>> print("Holberton school")
```

- [ ] Holberton
- [ ] “Holberton school”
- [x] Holberton school
- [ ] ‘Holberton school’

---

### Question #1

What does this command line print?

```python
>>> print(f"{98} Battery street")
```

- [x] 98 Battery street
- [ ] f"98 Battery street"
- [ ] 9 Battery street
- [ ] 8 Battery street

---

### Question #2

What does this command line print?

```python
>>> print(f"{98} Battery street, {'San Francisco'}")
```

- [ ] “98 Battery street, San Francisco”
- [ ] 8 Battery street, San
- [x] 98 Battery street, San Francisco
- [ ] San Francisco Battery street, 98

---

### Question #3

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[4])
```

- [ ] P
- [ ] n
- [x] o
- [ ] h

---

### Question #4

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[0:6])
```

- [x] Python
- [ ] Pytho
- [ ] Python is
- [ ] Python is cool

---

### Question #5

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[:6])
```

- [ ] Pytho
- [x] Python
- [ ] Python is
- [ ] is cool

---

### Question #6

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[7:])
```

- [ ] Python i
- [ ] Python is
- [ ] cool
- [x] is cool

---

### Question #7

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[7:-5])
```

- [ ] on
- [ ] nohtyP
- [ ] Python
- [ ] si
- [x] is

---

### Question #8

What does this command line print?

```python
>>> a = "Python is cool"
>>> print(a[-2])
```

- [ ] ol
- [ ] l
- [x] o
- [ ] Nothing

---

# Tasks

## 0. Hello, print

Write a Python script that prints exactly `"Programming is like building a multilingual puzzle`, followed by a new line.

- Use the function `print`

```python
guillaume@ubuntu:~/py/$ ./2-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/$
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `2-print.py`

**Code:**

```python
#!/usr/bin/python3
# Ceci s'appelle un "shebang".
# Il indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier.

print("\"Programming is like building a multilingual puzzle")
# La fonction print() affiche du texte à l'écran.
# Les parenthèses () sont utilisées pour appeler la fonction print
# avec un argument.
# L'argument entre guillemets ("...") est une chaîne de caractères,
# c'est-à-dire du texte.
# Le caractère \ (antislash) avant le guillemet " sert à "échapper"
# le guillemet, pour qu'il soit affiché dans le texte et non interprété
# comme la fin de la chaîne.
# Ainsi, \" affiche un guillemet double dans le texte.
# Le texte affiché sera : "Programming is like building a multilingual puzzle
# Les guillemets autour de la chaîne permettent à Python de savoir
# où commence et où finit le texte à afficher.
```

---

## 1. Print integer

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable `number`, followed by `Battery street`, followed by a new line.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/3-print_number.py)
- The output of the script should be:
    - the number, followed by `Battery street`,
    - followed by a new line
- You are not allowed to cast the variable `number` into a string
- Your code must be 3 lines long
- You have to use f-strings [tips](https://realpython.com/python-f-strings/)

```python
guillaume@ubuntu:~/py/0x00$ ./3-print_number.py
98 Battery street
guillaume@ubuntu:~/py/0x00$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `3-print_number.py`

**Code:**

```python
#!/usr/bin/python3
# Le "shebang" indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce fichier. Ici, il s'agit de Python 3.
# Quand tu lances ce script directement depuis le terminal,
# le système lit cette ligne pour savoir comment l'exécuter.

number = 98
# Ici, on crée une variable appelée "number".
# Une variable sert à stocker une valeur pour la réutiliser plus tard.
# Le signe "=" permet d'assigner une valeur à la variable.
# "98" est un nombre entier (integer) qui est stocké dans "number".

print(f"{number} Battery street")
# La fonction "print" sert à afficher du texte ou des valeurs à l'écran.
# Les parenthèses () entourent ce qu'on veut afficher.
# Le "f" devant les guillemets indique qu'il s'agit d'une "f-string"
# (format string), une façon pratique d'insérer des variables dans du texte.
# Les guillemets doubles "" délimitent la chaîne de caractères à afficher.
# À l'intérieur des guillemets, on peut écrire du texte librement.
# Les accolades {} permettent d'insérer la valeur de la variable "number"
# directement dans la chaîne de caractères.
# Ici, "{number}" sera remplacé par la valeur 98 lors de l'affichage.
# Le texte "Battery street" est affiché juste après la valeur de "number".
# Résultat affiché : 98 Battery street
```

---

## 2. Print float

Complete the source code in order to print the float stored in the variable `number` with a precision of 2 digits.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/4-print_float.py)
- The output of the program should be:
    - `Float:`, followed by the float with only 2 digits
    - followed by a new line
- You are not allowed to cast `number` to string
- You have to use f-strings

```python
guillaume@ubuntu:~/py/0x00$ ./4-print_float.py
Float: 3.14
guillaume@ubuntu:~/py/0x00$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `4-print_float.py`

**Code:**

```python
#!/usr/bin/python3
# Le "shebang" indique au système d'exploitation quel interpréteur utiliser
# pour exécuter ce script Python. Ici, il s'agit de Python 3.

number = 3.14159
# On crée une variable appelée "number".
# On lui attribue la valeur 3.14159, qui est un nombre à virgule flottante
# (float en anglais), c'est-à-dire un nombre décimal.

print(f"Float: {number:.2f}")
# La fonction "print" sert à afficher du texte ou des valeurs à l'écran.
#
# Les parenthèses () sont utilisées pour passer des arguments à la fonction.
#
# Les guillemets doubles " " délimitent une chaîne de caractères.
#
# Le "f" devant les guillemets indique qu'il s'agit d'une "f-string"
# (format string), une façon pratique d'insérer des variables dans une chaîne.
#
# À l'intérieur de la chaîne, les accolades {} permettent d'insérer la valeur
# de la variable "number" directement dans le texte.
#
# ":.2f" est un format spécial :
# - Le ":" indique qu'on va formater la valeur.
# - ".2f" signifie qu'on affiche le nombre avec 2 chiffres après la virgule,
#   sous forme décimale (float).
#
# Le texte affiché sera donc "Float: 3.14", car le nombre est arrondi à deux
# décimales.
```

---

## 3. Print string

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/5-print_string.py)
- The output of the program should be:
    - 3 times the value of `str`
    - followed by a new line
    - followed by the 9 first characters of `str`
    - followed by a new line
- You are not allowed to use any loops or conditional statement
- Your program should be maximum 5 lines long

```python
guillaume@ubuntu:~/py/$ ./5-print_string.py 
Holberton SchoolHolberton SchoolHolberton School
Holberton
guillaume@ubuntu:~/py/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `5-print_string.py`

**Code:**

```python
#!/usr/bin/python3
# La ligne ci-dessus s'appelle un "shebang".
# Elle indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement
# depuis le terminal sans préciser "python3" devant le nom du fichier.

str = "Holberton School"
# Ici, on crée une variable appelée "str".
# Le signe "=" sert à affecter une valeur à la variable.
# La valeur affectée est "Holberton School", qui est une chaîne de caractères.
# Les guillemets doubles " " indiquent le début et la fin de la chaîne.
# Une chaîne de caractères (ou "string") est une suite de caractères
# (lettres, chiffres, symboles, espaces, etc.).
# On peut utiliser des guillemets simples ' ' ou doubles " " pour définir une chaîne.

print(str * 3)
# La fonction "print()" sert à afficher quelque chose à l'écran (dans le terminal).
# Ce qu'on veut afficher est placé entre les parenthèses.
# Ici, on affiche "str * 3".
# L'opérateur "*" permet de répéter la chaîne "str" trois fois.
# Donc, "Holberton School" sera affiché trois fois à la suite.
# Il n'y a pas d'espace ajouté automatiquement entre les répétitions.

print(str[0:9])
# Encore une fois, on utilise la fonction "print()" pour afficher quelque chose.
# Cette fois, on affiche "str[0:9]".
# Les crochets [ ] servent à accéder à une partie de la chaîne, c'est ce qu'on appelle
# le "slicing" (découpage).
# "0:9" signifie qu'on prend les caractères de la position 0 (inclus) à la position 9 (exclue).
# En Python, la première position d'une chaîne est 0.
# Donc, on affiche les 9 premiers caractères de "Holberton School".
# Cela affichera "Holberton".
```

---

## 4. Play with strings

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/6-concat.py)
- You are not allowed to use any loops or conditional statements.
- You have to use the variables `str1` and `str2` in your new line of code
- Your program should be exactly 5 lines long

```python
guillaume@ubuntu:~/py/$ ./6-concat.py
Welcome to Holberton School!
guillaume@ubuntu:~/py/$ wc -l 6-concat.py
5 6-concat.py
guillaume@ubuntu:~/py/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `6-concat.py`

**Code:**

```python
#!/usr/bin/python3
# La ligne ci-dessus s'appelle un "shebang".
# Elle indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement
# depuis le terminal sans préciser "python3" devant.

str1 = "Holberton"
# Ici, on crée une variable appelée "str1".
# Le signe "=" sert à affecter une valeur à la variable.
# La valeur est une chaîne de caractères (string) : "Holberton".
# Les guillemets doubles (" ") indiquent le début et la fin de la chaîne.
# Une chaîne de caractères est une suite de lettres, chiffres ou symboles.

str2 = "School"
# On crée une deuxième variable appelée "str2".
# Elle contient la chaîne de caractères "School".
# Même principe que pour "str1" : on utilise les guillemets
# pour délimiter la chaîne.

str3 = str1 + " " + str2
# On crée une troisième variable appelée "str3".
# On utilise le signe "+" pour concaténer (assembler) des chaînes de caractères.
# "str1" contient "Holberton".
# " " (guillemets avec un espace à l'intérieur) ajoute un espace entre les mots.
# "str2" contient "School".
# Résultat : "str3" contient "Holberton School".

print(f"Welcome to {str3}!")
# La fonction "print()" sert à afficher du texte à l'écran.
# Tout ce qui est entre parenthèses sera affiché.
# Le "f" devant les guillemets indique une "f-string" (format string).
# Cela permet d'insérer la valeur d'une variable dans la chaîne affichée.
# Les accolades {str3} sont remplacées par la valeur de "str3".
# Ici, "Welcome to Holberton School!" sera affiché.
# Le point d'exclamation "!" est un caractère spécial pour ponctuer la phrase.
```

---

## 5. Copy - Cut - Paste

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/7-edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 8 lines long
- `word_first_3` should contain the first 3 letters of the variable `word`
- `word_last_2` should contain the last 2 letters of the variable `word`
- `middle_word` should contain the value of the variable `word` without the first and last letters

```python
guillaume@ubuntu:~/py/$ ./7-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/$ wc -l 7-edges.py
8 7-edges.py
guillaume@ubuntu:~/py/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `7-edges.py`

**Code:**

```python
#!/usr/bin/python3
# La ligne ci-dessus s'appelle un "shebang".
# Elle indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement
# depuis le terminal sans préciser "python3" devant.

word = "Holberton"
# Ici, on crée une variable appelée "word".
# On lui assigne la chaîne de caractères "Holberton".
# Les guillemets doubles (" ") servent à délimiter une chaîne de caractères
# en Python. On peut aussi utiliser des guillemets simples (' ').

word_first_3 = word[0:3]
# Cette ligne crée une nouvelle variable "word_first_3".
# On utilise la syntaxe de "slice" (tranche) : word[0:3].
# Cela signifie qu'on prend les caractères de l'index 0 (inclus)
# jusqu'à l'index 3 (exclu) de la chaîne "word".
# En Python, l'indexation commence à 0.
# Donc, on récupère les 3 premiers caractères : "Hol".

word_last_2 = word[-2:]
# Ici, on crée la variable "word_last_2".
# On utilise encore une "slice" : word[-2:].
# L'index négatif (-2) commence à partir de la fin de la chaîne.
# Donc, on prend les 2 derniers caractères de "word".
# Le ":" sans chiffre après signifie "jusqu'à la fin".

middle_word = word[1:-1]
# Cette ligne crée la variable "middle_word".
# On utilise la "slice" word[1:-1].
# Cela prend les caractères de l'index 1 (deuxième caractère)
# jusqu'à l'index -1 (avant-dernier caractère, exclu).
# On obtient donc tous les caractères sauf le premier et le dernier.

print(f"First 3 letters: {word_first_3}")
# La fonction "print" permet d'afficher du texte à l'écran.
# Le "f" devant les guillemets indique une "f-string" (format string).
# Cela permet d'insérer la valeur de variables directement dans la chaîne
# en utilisant des accolades {}.
# Ici, {word_first_3} sera remplacé par la valeur de la variable.

print(f"Last 2 letters: {word_last_2}")
# Même principe que précédemment.
# On affiche le texte "Last 2 letters:" suivi de la valeur de "word_last_2".

print(f"Middle word: {middle_word}")
# On affiche le texte "Middle word:" suivi de la valeur de "middle_word".
# Les caractères spéciaux comme ":" sont simplement du texte ici.
# Les parenthèses () sont utilisées pour appeler la fonction "print".
```

---

## 6. Create a new sentence

Complete this [source code](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line.

- You can find the source code [here](https://github.com/hs-hq/0x00.py/blob/master/8-concat_edges.py)
- You are not allowed to use any loops or conditional statements
- Your program should be exactly 5 lines long
- You are not allowed to create new variables
- You are not allowed to use string literals

```python
guillaume@ubuntu:~/py/$ ./8-concat_edges.py
object-oriented programming with Python
guillaume@ubuntu:~/py/$ wc -l 8-concat_edges.py
5 8-concat_edges.py
guillaume@ubuntu:~/py/$ 
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `8-concat_edges.py`

**Code:**

```python
#!/usr/bin/python3
# La ligne ci-dessus s'appelle un "shebang".
# Elle indique au système d'exploitation d'utiliser l'interpréteur Python 3
# pour exécuter ce fichier. Cela permet de lancer le script directement
# depuis le terminal sans préciser "python3" devant.

str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
# Ici, on crée une variable appelée "str".
# On lui assigne une chaîne de caractères (string) entre guillemets doubles.
# Les guillemets permettent de définir le début et la fin de la chaîne.
# Le symbole "\" à la fin de la première ligne sert à indiquer que la chaîne
# continue sur la ligne suivante, sans ajouter de saut de ligne.
# Cela permet d'écrire une chaîne très longue sur plusieurs lignes
# pour améliorer la lisibilité du code.

str = str[39:67] + str[-22:-17] + str[:6]
# Cette ligne modifie la variable "str" en utilisant des "slices"
# (tranches) pour extraire et assembler des parties de la chaîne.
# "str[39:67]" extrait les caractères de l'index 39 inclus à 67 exclus.
# "str[-22:-17]" utilise des indices négatifs pour compter depuis la fin
# de la chaîne. Cela extrait les caractères de l'index -22 inclus à -17 exclus.
# "str[:6]" extrait les 6 premiers caractères de la chaîne (de l'index 0 à 5).
# Les "+" servent à concaténer (assembler) les différentes sous-chaînes
# pour former une nouvelle chaîne.

print(str)
# La fonction "print()" affiche le contenu de la variable "str" à l'écran.
# Les parenthèses sont nécessaires pour appeler la fonction.
# Cela permet de voir le résultat final dans le terminal ou la console.
```

---

## 7. Easter Egg

Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

- Your script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`)

```python
guillaume@ubuntu:~/py/$ ./9-easter_egg.py
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
guillaume@ubuntu:~/py/$
```

**Repo:**
- GitHub repository: `holbertonschool-higher_level_programming`
- Directory: `python-hello_world`
- File: `9-easter_egg.py`

**Code:**

```python
#!/usr/bin/python3
# Le "shebang" (#!) indique au système d'exploitation
# quel interpréteur utiliser pour exécuter ce fichier.
# Ici, "/usr/bin/python3" signifie que le script doit être
# exécuté avec Python version 3.

import this
# "import" est un mot-clé de Python qui permet d'ajouter
# des modules externes ou standards à notre programme.
#
# "this" est le nom d'un module standard de Python.
# Ce module est une "easter egg" (fonction cachée ou amusante).
#
# Quand on importe le module "this", il affiche automatiquement
# le "Zen of Python" dans la console.
#
# Le "Zen of Python" est une liste de principes et de bonnes
# pratiques pour écrire du code Python de façon claire et élégante.
#
# Il n'y a pas de fonction "print" ici, car le module "this"
# affiche le texte dès qu'il est importé.
#
# Les guillemets (simples ou doubles) servent à délimiter
# les chaînes de caractères en Python, mais ici ils ne sont
# pas utilisés directement dans le code.
#
# Les caractères spéciaux comme "\n" (saut de ligne) sont
# utilisés dans les chaînes de caractères pour formater le texte,
# mais ils sont gérés à l'intérieur du module "this" et non
# dans ce fichier.
```
