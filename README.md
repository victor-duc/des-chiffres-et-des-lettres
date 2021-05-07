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


## Modularisation

Pour réaliser le projet, je vais créer plusieurs modules.
Chaque module traitera un sujet donné et sera composé de plusieurs fonctions.


### Module _dictionnaire.py_

Ce module contient les variables et fonctions relatives à la gestion du dictionnaire de mots français.

#### Variables globales

> **mots** : list[str]\
> Cette variable contient la liste des mots du dictionnaire, lorsqu'on fait appel à la fonction **charge**.

#### Fonctions

> **charge**(*chemin_fichier* : str)\
> Cette fonction charge les **mots** d'un fichier qui serviront au jeu.

> **contient**(*mot* : str)\
> Cette fonction indique si le mot existe dans le dictionnaire.

> **filtre**(*max_lettres* : int)\
> Cette fonction filtre les **mots** trop long et les doublons.


### Module _lettres.py_

Ce module contient les variables et fonctions relatives à la gestion des lettres.

#### Variables globales

> **alphabet** : str\
> Cette variable contient toutes les lettres de l'alphabet.

> **poids** : list[int]\
> Cette variable contient le poids des lettres, lorsqu'on fait appel à la fonction **analyse**.

> **voyelles** : str\
> Cette variable contient toutes les voyelles de l'alphabet.

#### Fonctions

> **analyse**(*mots_dictionnaire* : list[str])\
> Cette fonction analyse les mots du dictionnaire pour défnir le **poids** des lettres.\
> Le poids des lettres correspond au nombre d'occurrences des lettres dans le dictionnaire.

> **compte_voyelles**(*mot* : str)\
> Cette fonction compte le nombre de voyelles dans le mot.

> **forme_mots**(*lettres* : str, *mots_dictionnaire* : list[str])\
> Cette fonction forme tous les mots possibles à partir des lettres fournies.\
> Les mots retournés font parties du dictionnaire fourni.

> **tire_aleatoire**(*nombre_lettres* : int, *min_voyelles* : int)\
> Cette fonction tire des lettres aléatoires en se basant sur le **poids** des lettres.


### Module _entiers.py_

Ce module contient les variables et fonctions relatives à la gestion des entiers.

#### Fonctions

> **tire_entiers**(*entiers_disponibles* : list[int], *n* : int)\
> Cette fonction tire aléatoirement les entiers pour le jeu en piochant N entiers dans la liste.

> **tire_objectif**(*valeur_min* : int, *valeur_max* : int)\
> Cette fonction tire aléatoirement l'entier cible du jeu entre la valeur min et max.


### Module _operation.py_

Ce module contient les variables et fonctions relatives à la gestion des opérations.

#### Fonctions

> **cree_addition**(*a* : int, *b* : int)\
> Cette fonction retourne l'addition de a et b.\
> Règle : Le résultat doit être un entier positif, sinon la fonction retourne *None*.

> **cree_division**(*a* : int, *b* : int)\
> Cette fonction retourne la division de a par b.\
> Règle : Le résultat doit être un entier positif, sinon la fonction retourne *None*.

> **cree_multiplication**(*a* : int, *b* : int)\
> Cette fonction retourne la multiplication de a et b.\
> Règle : Le résultat doit être un entier positif, sinon la fonction retourne *None*.

> **cree_soustraction**(*a* : int, *b* : int)\
> Cette fonction retourne la soustraction de a et b\
> Règle : Le résultat doit être un entier positif, sinon la fonction retourne *None*.

> **forme_operations**(*entiers* : list[int])\
> Cette fonction forme les suites d'opérations qu'il est possible de créer à partir des entiers fournis.\
> Elle retourne pour chaque résultat possible, la suite d'opérations la plus courte.

> **optimise_operations**(*operations* : dict[int, any], *objectif* : int)\
> Cette fonction optimise les opérations fournies supprimant les opérations qui s'éloigne de l'objectif. 


### Module _ia.py_

Ce module contient les variables et fonctions relatives à la gestion de l'IA du jeu.

#### Variables globales

> **niveau_actuel** : str\
> Cette variable contient le niveau actuel de l'IA.

> **niveaux_possibles** : dict[str, any]\
> Cette variable contient la configuration des différents niveaux de l'IA. 

#### Fonctions

> **selectionne_mot**(*mots* : list[str])\
> Cette fonction sélectionne un mot dans la liste de mots fournis.\
> Plus le **niveau_actuel** de l'IA est élevé, plus il y a de chance que le mot soit long.

> **selectionne_operation**(*objectif* : int, *operations* : dict[int, any])\
> Cette fonction sélectionne une opération dans la liste d'opérations fournies.\
> Plus le **niveau_actuel** de l'IA est élevé, plus il y a de chance que le résultat de l'opération soit proche
> de l'objectif.

> **trouve_mot**(*lettres* : str, *mots_dictionnaire* : list[str])\
> Cette fonction trouve un mot qu'il est possible de former à partir des lettres fournies.\
> Plus le **niveau_actuel** de l'IA est élevé, plus il y a de chance que le mot soit long.

> **trouve_operation**(*objectif* : int, *entiers* : list[int])\
> Cette fonction trouve une opération à partir des entiers fournis dont le résultat se rapproche de l'objectif.\
> Plus le **niveau_actuel** de l'IA est élevé, plus il y a de chance que le résultat de l'opération soit proche
> de l'objectif.