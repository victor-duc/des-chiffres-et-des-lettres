# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : moteur_chiffres.py
# Description : Ce module contient les fonctions relatives à la gestion des opérations.
# ----------------------------------------------------------------------------------------------------------------------
import entiers


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

def cree_addition(a: int, b: int) -> dict[str, any]:
    """Crée l'addition de a et b."""
    return cree_operation(a, "+", b, a + b)


def cree_division(a: int, b: int) -> dict[str, any]:
    """Crée la division de a par b, ou b par a (la plus petite valeur sera le diviseur)"""
    if a < b:
        a, b = b, a  # Si a inférieur à b, on inverse les valeurs
    if b == 0:
        return None  # On évite la division par zéro

    return cree_operation(a, "/", b, a / b)


def cree_multiplication(a: int, b: int) -> dict[str, any]:
    """Crée la multiplication de a et b."""
    return cree_operation(a, "*", b, a * b)


def cree_operation(a: int, operateur: str, b: int, c: int) -> dict[str, any]:
    """
        Crée un dictionnaire correspondant à l'opération.

        Le dictionnaire aura les clés suivantes :
          - a: opérande de l'opération
          - b: opérande de l'opération
          - c: résultat de l'opération
          - operateur: opérateur de l'opération

        Le résultat doit être un entier positif, sinon la fonction retourne None.
    """
    if entiers.est_positif_non_nul(c):
        if isinstance(c, float):
            c = int(c)  # On s'assure que c est un entier car le résultat d'une division est un float
        return {"a": a, "operateur": operateur, "b": b, "c": c}

    return None


def cree_operations(a: int, b: int) -> dict[int, any]:
    """Crée les opérations entre `a` et `b` dont le résultat est un entier positif non nul."""
    operations: dict[int, any] = {}
    fonctions: list[any] = [
        cree_addition,
        cree_division,
        cree_multiplication,
        cree_soustraction
    ]
    for fonction in fonctions:
        operation = fonction(a, b)
        if operation is None:
            continue

        c = operation["c"]
        if c not in operations:
            operations[c] = operation
    return operations


def cree_soustraction(a: int, b: int) -> dict[str, any]:
    """Crée la soustraction de a et b."""
    if a < b:
        a, b = b, a  # Si a inférieur à b, on inverse les valeurs

    return cree_operation(a, "-", b, a - b)


def forme_operations(entiers: list[int]) -> dict[int, any]:
    """
        Forme les suites d'opérations qu'il est possible de créer à partir des entiers fournis.
        Elle retourne pour chaque résultat possible, la suite d'opérations la plus courte.
    """
    operations: dict[int, any] = {}

    if len(entiers) <= 1:
        return operations

    if len(entiers) == 2:
        a, b = entiers
        return cree_operations(a, b)

    for a in entiers:
        sous_liste = list(entiers)
        sous_liste.remove(a)

        operations_b = forme_operations(sous_liste)  # Appel récursif, avec une liste plus petite
        for b in operations_b:
            operations_c = cree_operations(a, b)
            for c in operations_c:
                operations_bc = []
                if isinstance(operations_b[b], list):
                    operations_bc = operations_b[b] + [operations_c[c]]
                else:
                    operations_bc = [operations_b[b], operations_c[c]]
                if c not in operations or len(operations[c]) > len(operations_bc):
                    operations[c] = operations_bc

        for b in operations_b:
            if b not in operations or len(operations[b]) > len(operations_b[b]):
                if isinstance(operations_b[b], list):
                    operations[b] = operations_b[b]
                else:
                    operations[b] = [operations_b[b]]

    return operations


def optimise_operations(operations: dict[int, any], objectif: int) -> None:
    """Optimise les opérations fournies supprimant les opérations qui s'éloigne de l'objectif."""
    operations_optimisees = {}

    for c in operations:
        if c > (objectif * 2):
            continue

        operations_c = operations[c]
        nombre_operations = len(operations_c)
        min_distance = abs(objectif - c)
        index = nombre_operations - 1

        for i in range(nombre_operations):
            distance = abs(objectif - operations_c[i]["c"])
            if distance < min_distance:
                min_distance = distance
                index = i

        c = operations_c[index]["c"]
        operations_optimisees[c] = operations_c[0:index + 1]

    return operations_optimisees

