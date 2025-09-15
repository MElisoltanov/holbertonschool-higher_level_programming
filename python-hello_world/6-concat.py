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
