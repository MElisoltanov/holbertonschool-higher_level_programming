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
