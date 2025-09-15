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
