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
