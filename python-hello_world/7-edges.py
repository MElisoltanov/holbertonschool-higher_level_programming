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
