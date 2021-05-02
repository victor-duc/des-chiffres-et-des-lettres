# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : moteur_chiffres.py
# Description : Ce module contient les fonctions "moteur" permettant de réaliser une partie de chiffres.
# ----------------------------------------------------------------------------------------------------------------------
import random


# ----------------------------------------------------------------------------------------------------------------------
# Variables globales du module
# ----------------------------------------------------------------------------------------------------------------------

max_entiers = 6             # Nombre d'entiers qu'il faut tirer
min_objectif = 100          # Nombre min de l'objectif à tirer
max_objectif = 999          # Nombre max de l'objectif à tirer

# Entiers disponibles pour le tirage au sort
entiers_disponibles = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    25, 50, 75, 100
]

# Niveaux de l'IA pour trouver des mots
niveaux_ia = {
    'FACILE':    100,
    'MOYEN':     50,
    'DIFFICILE': 5
}


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def cree_operations(a: int, b: int) -> dict[int, any]:
    """
    Crée toutes les opérations possibles entre a et b.
    Chaque résultat est un entier positif supérieur à zéro.
    """
    if a < b:
        a, b = b, a  # Inverse les valeurs pour que a >= b

    operations: dict[int, any] = {
        a + b: [a, '+', b, '=', a + b],
        a * b: [a, '*', b, '=', a * b]
    }

    c = a - b
    if c > 0:
        operations[c] = [a, '-', b, '=', c]

    if (a % b) == 0:
        c = int(a / b)
        operations[c] = [a, '/', b, '=', c]

    return operations


def filtre_operations(operations: dict[int, any], objectif: int) -> dict[int, any]:
    """Exclus les opérations qui s'éloigne de l'objectif au lieu de s'en approcher"""
    operations_filtrees = {}

    for resultat in operations:
        formules = operations[resultat]
        min_distance = abs(objectif - resultat)
        index = len(formules) - 1

        for i in range(len(formules) - 1, 0, -5):
            distance = abs(objectif - formules[i])
            if distance < min_distance:
                min_distance = distance
                index = i

        if index < (len(formules) - 1):
            operations_filtrees[formules[index]] = formules[0:index + 1]

    return operations_filtrees


def interprete_formule(formule: str, entiers: list[int], erreurs: list[str] = []) -> list[any]:
    """Intreprete une formule et renvoie un tableau correspondant à l'opération."""
    if not formule:
        erreurs.append("Formule vide !")
        return None

    operateurs = [operateur for operateur in "+-/*" if operateur in formule]
    if len(operateurs) != 1:
        erreurs.append("Formule invalide ! (problème d'opérateur)")
        return None

    segments = [segment.strip() for segment in formule.split(operateurs[0])]
    if len(segments) != 2:
        erreurs.append("Formule invalide ! (problème sur les segments)")
        return None

    if not segments[0].isnumeric() or not segments[1].isnumeric():
        erreurs.append("Formule invalide ! (nombres invalides)")
        return None

    a = int(segments[0])
    b = int(segments[1])
    if a not in entiers or b not in entiers:
        erreurs.append("Formule invalide ! (nombres non autorisés)")
        return None
    elif a == b and entiers.count(a) < 2:
        erreurs.append("Formule invalide ! (nombres utilisés plusieurs fois)")
        return None

    operateur = operateurs[0]
    if operateur == '+':
        return [a, operateur, b, '=', a + b]

    if operateur == '*':
        return [a, operateur, b, '=', a * b]

    if operateur == '-':
        c = a - b
        if c <= 0:
            erreurs.append("Formule invalide ! (résultat nul ou négatif)")
            return None
        return [a, operateur, b, '=', c]

    # Division '/'
    if (a % b) != 0:
        erreurs.append("Formule invalide ! (résultat non entier)")
        return None
    return [a, operateur, b, '=', int(a / b)]


def tire_entiers() -> list[int]:
    """Tire les entiers à utiliser pour atteindre l'objectif de la partie de chiffres."""
    return sorted(random.choices(entiers_disponibles, k=max_entiers))


def tire_objectif() -> int:
    """Tire l'objectif d'une partie de chiffre."""
    return random.randint(min_objectif, max_objectif)


def trouve_operation(entiers_tries: list[int], objectif: int, niveau: str) -> list[any]:
    """Trouve les operations pour atteindre l'objectif à partir des entiers fournis."""

    if niveau not in niveaux_ia:
        raise ValueError("Niveau d'IA inconnu ! ({})".format(niveau))

    # Trouves toutes les operations possibles
    operations = trouve_operations(entiers_tries)
    operations = filtre_operations(operations, objectif)

    # Sélectionne une distance aléatoire par rapport à l'objectif selon le niveau de l'IA
    max_distance = niveaux_ia[niveau]
    distances = sorted([abs(objectif - resultat) for resultat in operations.keys()])
    if len(distances) > max_distance:
        distances = distances[0:max_distance]
    distance = random.choice(distances)

    # Sélectionne l'opération correspondant à la distance sélectionnée
    operations = [operations[resultat] for resultat in operations.keys() if abs(objectif - resultat) == distance]
    return operations[0]


def trouve_operations(entiers_tries: list[int]) -> dict[str, any]:
    """Trouves toutes les opérations possibles à partir des entiers"""
    if len(entiers_tries) <= 1:
        return {}

    if len(entiers_tries) == 2:
        a, b = entiers_tries
        return cree_operations(a, b)

    operations = {}
    for entier in entiers_tries:
        sous_liste = list(entiers_tries)
        sous_liste.remove(entier)
        sous_operations = trouve_operations(sous_liste)
        for sous_resultat in sous_operations:
            operations_courantes = cree_operations(entier, sous_resultat)
            for resultat_courant in operations_courantes:
                nouvelles_operations = sous_operations[sous_resultat] + operations_courantes[resultat_courant]
                if resultat_courant not in operations or len(operations[resultat_courant]) > len(nouvelles_operations):
                    operations[resultat_courant] = nouvelles_operations

        for sous_resultat in sous_operations:
            if sous_resultat not in operations or len(operations[sous_resultat]) > len(sous_operations[sous_resultat]):
                operations[sous_resultat] = sous_operations[sous_resultat]

    return operations
