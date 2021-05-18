# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : ia.py
# Description : Ce module contient les variables et fonctions relatives à la gestion de l'IA du jeu.
# ----------------------------------------------------------------------------------------------------------------------
import lettre
import operation
import random

# ----------------------------------------------------------------------------------------------------------------------
# Variables globales du module
# ----------------------------------------------------------------------------------------------------------------------

niveau_actuel = "MOYEN"
niveaux_possibles = {
    "CHIFFRES": {
        'FACILE': {

        },
        'MOYEN': {

        },
        'DIFFICILE': {

        }
    },
    "LETTRES": {
        'FACILE':    [0, 0, 1, 1, 1, 9, 5, 3, 1],
        'MOYEN':     [0, 0, 0, 1, 1, 1, 9, 5, 3],
        'DIFFICILE': [0, 0, 0, 0, 1, 1, 1, 1, 9]
    }
}


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def selectionne_mot(mots: list[str]) -> str:
    """Sélectionne un mot dans la liste de mots fournis."""

    # On conserve un mot par taille (1 mot de 9 lettres, 1 mot de 7 lettres, etc)
    mots_formables: dict[int, str] = {len(mot): mot for mot in mots}

    # On trie les mots selon leur taille
    tailles: list[int] = sorted(mots_formables.keys())
    mots_tries: list[str] = [mots_formables[taille] for taille in tailles]

    # On récupère les poids pour le tirage aléatoire selon le niveau de l'IA
    total_mots: int = len(mots_tries)
    poids_mots: list[int] = niveaux_possibles["LETTRES"][niveau_actuel][-total_mots:]

    # On tire aléatoirement avec les poids du niveau de l'IA
    return random.choices(mots_tries, weights=poids_mots, k=1)[0]


def selectionne_operation(objectif: int, operations: dict[int, any]) -> dict[str, any]:
    """Sélectionne une opération dans la liste d'opérations fournies."""

    return


def trouve_mot(lettres: str, mots_dictionnaire: list[str]) -> str:
    """Trouve un mot qu'il est possible de former à partir des lettres fournies."""
    mots = lettre.forme_mots(lettres, mots_dictionnaire)
    return selectionne_mot(mots)


def trouve_operation(objectif: int, entiers: list[int]) -> dict[str, any]:
    """Trouve une opération à partir des entiers fournis dont le résultat se rapproche de l'objectif."""
    operations = operation.forme_operations(entiers)
    operations = operation.optimise_operations(operations, objectif)
    return selectionne_operation(objectif, operations)
