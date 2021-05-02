# Des chiffres et des lettres

Des chiffres et des lettres est un jeu télévisé français
([page wikipedia](https://fr.wikipedia.org/wiki/Des_chiffres_et_des_lettres))

Ce repository contient un programme en Python recréant le jeu, avec une adaptation : il s'agit d'un jeu *Single Player*
où le joueur joue contre une IA. Hormis ce point, les règles sont les mêmes que le jeu télévisé.

Ce projet a été donné à des étudiants en 1ère année de Prépa. Je me suis dit que j'allais relever le défi pour m'amuser
et apprendre le Python.


## Environnement technique

- OS : Windows 10
- IDE : PyCharm 2021.1 (Community Edition)
- Python : 3.9
- Langue du code : Français
- Convention de nommage : snake_case


## Règles du jeu

Une partie se compose de 12 manches de chiffres et de lettres, avec l'alternance suivante :
chiffres / lettres / lettres, soit au total 4 parties de chiffres et 8 parties de lettres.


### Partie de chiffres

Début de partie :
- Un entier cible est tiré aléatoirement entre 100 et 999
- 6 entiers sont tirés parmi une liste d'entiers prédéfinis, 2 fois les chiffres de 1 à 10 et 1 fois 25, 50, 75 et 100
- Ces 6 entiers ne seront utilisables qu'une fois
- Un timer de 45 secondes démarre

Déroulement de la partie :
- En utilisant les 6 entiers tirés, le joueur doit saisir une suite d'opérations (+ / * -) pour retrouver l'entier cible
- Chaque opération doit respecter le format : `{operande1} {operateur} {operande2}`
- Chaque opération doit renvoyer un entier, sinon elle est considérée invalide
- A tout moment, le joueur peut taper `RAZ` pour effacer ses opérations et repartir avec les 6 entiers de départ
- A tout moment, le joueur peut taper la touche `ENTREE` sans rien saisir d'autre pour terminer la partie.

Fin de partie :
- Si le timer est écoulé, le joueur a perdu et ne marque aucun point
- Si le joueur a trouvé le bon compte, il marque 9 points
- Si le joueur a obtenu le nombre le plus proche, il marque 6 points
- En cas d'égalité, les joueurs marque 6 points


### Une partie de lettres

Début de partie :
- 9 lettres sont tirées aléatoirement (avec au minimum une voyelle)
- Un timer de 30 secondes démarre

Déroulement de la partie :
- En utilisant les 9 lettres tirées, le joueur doit saisir les mots les plus longs
- Chaque mot doit exister dans le dictionnaire du jeu, sinon il est considéré invalide
- A tout moment, le joueur peut taper la touche `ENTREE` sans rien saisir d'autre pour terminer la partie.

Fin de partie :
- Si le timer est écoulé, le joueur a perdu et ne marque aucun point
- Si le joueur a trouvé le mot le plus long, il marque le nombre de lettres en points
- En cas d'égalité, les 2 joueurs marques le nombre de lettres en points