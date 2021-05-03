# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : moteur_lettres.py
# Description : Ce module contient les fonctions "moteur" permettant de réaliser une partie de lettres.
# ----------------------------------------------------------------------------------------------------------------------
import random


# ----------------------------------------------------------------------------------------------------------------------
# Variables globales du module
# ----------------------------------------------------------------------------------------------------------------------

dictionnaire = []       # Liste contenant les mots du dictionnaire
max_lettres = 9         # Nombre max de lettres dans les mots du dictionnaire
min_voyelles = 1        # Nombre min de voyelles dans les mots du dictionnaire
poids_lettres = {}      # Poids des lettres du dictionnaire

# Niveaux de l'IA pour trouver des mots. Il s'agit de poids (voir fonction trouve_mot)
niveaux_ia = {
    'FACILE':    [0, 0, 1, 1, 1, 9, 5, 3, 1],
    'MOYEN':     [0, 0, 0, 1, 1, 1, 9, 5, 3],
    'DIFFICILE': [0, 0, 0, 0, 1, 1, 1, 1, 9]
}


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def charge_dictionnaire(chemin: str) -> None:
    """Charge les mots du fichier.

    :param chemin: Chemin vers le fichier contenant les mots du dictionnaire.
    """
    global dictionnaire
    global poids_lettres

    mots: set[str] = {}
    with open(chemin, mode='r') as fichier:
        for ligne in fichier.readlines():
            ligne = ligne.strip()
            if ligne and len(ligne) <= max_lettres:
                mots.add(ligne)

    dictionnaire = mots.keys()
    poids_lettres = compte_lettres()
    return


def compte_lettres() -> dict[str, int]:
    """Compte les lettres du dictionnaire."""
    poids = {lettre: 0 for lettre in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    if dictionnaire:
        for mot in dictionnaire:
            for lettre in mot:
                poids[lettre] += 1
    return poids


def compte_voyelles(mot: str) -> int:
    """Compte le nombre de voyelles dans le mot."""
    total: int = 0
    for lettre in mot:
        if lettre in "AEIOUY":
            total += 1
    return total


def tire_lettres() -> list[str]:
    """Tire des lettres aléatoires en se basant sur le poids des lettres du dictionnaire."""
    tirage: list[str] = []
    if poids_lettres:
        alphabet = list(poids_lettres.keys())
        poids = list(poids_lettres.values())
        while not tirage or compte_voyelles(tirage) < min_voyelles:
            tirage = random.choices(alphabet, weights=poids, k=max_lettres)
    return tirage


def trouve_mot(lettres: list[str], niveau: str) -> str:
    """Trouve un mot dans le dictionnaire à partir des lettres fournies."""

    if niveau not in niveaux_ia:
        raise ValueError("Niveau d'IA inconnu ! ({})".format(niveau))

    # On conserve un mot par taille (1 mot de 9 lettres, 1 mot de 7 lettres, etc)
    mots_formables: dict[int, str] = {len(mot): mot for mot in trouve_mots(lettres)}
    if not mots_formables:
        return ''

    # On trie les mots selon leur taille
    tailles: list[int] = sorted(mots_formables.keys())
    mots_tries: list[str] = [mots_formables[taille] for taille in tailles]

    # On récupère les poids pour le tirage aléatoire selon le niveau de l'IA
    total_mots: int = len(mots_tries)
    poids_mots: list[int] = niveaux_ia[niveau][-total_mots:]

    # On tire aléatoirement avec les poids du niveau de l'IA
    return random.choices(mots_tries, weights=poids_mots, k=1)[0]


def trouve_mots(lettres) -> list[str]:
    """Trouve tous les mots qu'il est possible de former avec les lettres fournies."""
    resultat: list[str] = []
    if dictionnaire:
        for mot in dictionnaire:
            est_formable: bool = True
            for lettre in mot:
                if mot.count(lettre) > lettres.count(lettre):
                    est_formable = False
                    break
            if est_formable:
                resultat.append(mot)
    return resultat

