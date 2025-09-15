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
