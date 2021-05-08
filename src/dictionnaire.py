# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : dictionnaire.py
# Description : Ce module contient les variables et fonctions relatives à la gestion du dictionnaire de mots français.
# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Variables globales du module
# ----------------------------------------------------------------------------------------------------------------------

mots: list[str] = []   # Liste contenant les mots du dictionnaire


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def charge(chemin_fichier: str) -> None:
    """Charge les mots du fichier."""
    global mots

    # Ouvre le fichier en mode lecture (r = read)
    with open(chemin_fichier, mode='r') as fichier:
        mots = [ligne.strip() for ligne in fichier.readlines()]
    return


def contient(mot: str) -> bool:
    """Indique si le mot fait partie des mots du dictionnaire."""
    return mot in mots


def filtre(max_lettres: int) -> None:
    """Filtre les mots trop long, ayant plus de max_lettres."""
    global mots

    mots = [mot for mot in mots if len(mots) <= max_lettres]
    return
