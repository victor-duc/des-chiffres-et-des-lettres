# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : moteur_chiffres.py
# Description : Ce module contient les fonctions relatives à la gestion des entiers.
# ----------------------------------------------------------------------------------------------------------------------
import random


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def tire_entiers(entiers_disponibles: list[int], n: int) -> list[int]:
    """
        Tire aléatoirement les entiers pour le jeu en piochant N entiers dans la liste fournies.
        Les valeurs retournées sont triées du plus petit au plus grand.
    """
    return sorted(random.choices(entiers_disponibles, k=n))


def tire_objectif(valeur_min: int, valeur_max: int) -> int:
    """Tire aléatoirement l'entier cible du jeu entre la valeur min et max."""
    return random.randint(valeur_min, valeur_max)
