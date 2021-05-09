# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : entier.py
# Description : Ce module contient les fonctions relatives à la gestion des entiers.
# ----------------------------------------------------------------------------------------------------------------------
import random


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def est_positif_non_nul(valeur: any):
    """Indique si la valeur fournie est un entier positif non nul."""
    if valeur is not None:
        if isinstance(valeur, int):
            return valeur > 0
        if isinstance(valeur, float) and valeur.is_integer():
            return valeur > 0
    return False


def tire_entiers(entiers_disponibles: list[int], n: int) -> list[int]:
    """
        Tire aléatoirement les entiers pour le jeu en piochant N entiers dans la liste fournies.
        Les valeurs retournées sont triées du plus petit au plus grand.
    """
    return sorted(random.choices(entiers_disponibles, k=n))


def tire_objectif(valeur_min: int, valeur_max: int) -> int:
    """Tire aléatoirement l'entier cible du jeu entre la valeur min et max."""
    return random.randint(valeur_min, valeur_max)
