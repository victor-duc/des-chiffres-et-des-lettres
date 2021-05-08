# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : lettres.py
# Description : Ce module contient les variables et fonctions relatives à la gestion des lettres.
# ----------------------------------------------------------------------------------------------------------------------
import random


# ----------------------------------------------------------------------------------------------------------------------
# Variables globales du module
# ----------------------------------------------------------------------------------------------------------------------

alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
poids: list[int] = []
voyelles: str = "AEIOUY"


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def analyse(mots_dictionnaire: list[str]) -> None:
    """
        Analyse les mots du dictionnaire pour définir les poids des lettres.
        Le poids des lettres correspond au nombre d'occurrences des lettres dans le dictionnaire.
    """
    totales = {lettre: 0 for lettre in alphabet}
    for mot in mots_dictionnaire:
        for lettre in mot:
            totales[lettre] += 1

    global poids
    poids = totales.values()
    return


def compte_voyelles(mot: str) -> int:
    """Compte le nombre de voyelles dans le mot."""
    total: int = 0
    for lettre in mot:
        if lettre in "AEIOUY":
            total += 1
    return total


def forme_mots(lettres: str, mots_dictionnaire: list[str]) -> list[str]:
    """
        Forme tous les mots possibles à partir des lettres fournies.
        Les mots retournés font parties du dictionnaire.
    """
    mots_formables: list[str] = []
    for mot in mots_dictionnaire:
        est_formable: bool = True
        for lettre in mot:
            if mot.count(lettre) > lettres.count(lettre):
                est_formable = False
                break
        if est_formable:
            mots_formables.append(mot)
    return mots_formables


def tire_lettres(nombre_lettres: int, min_voyelles: int) -> list[int]:
    """Tire des lettres aléatoires en se basant sur le poids des lettres du dictionnaire."""
    tirage: list[str] = []
    max_boucle: int = 10
    i: int = 0  # Ce compteur évite de boucler trop longtemps sans qu'on ait de voyelles
    while (not tirage or compte_voyelles(tirage) < min_voyelles) and i < max_boucle:
        tirage = random.choices(alphabet, weights=poids, k=nombre_lettres)
        i += 1
    return tirage

