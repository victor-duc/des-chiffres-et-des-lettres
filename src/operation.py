# coding:utf-8

# ----------------------------------------------------------------------------------------------------------------------
# Projet      : Des chiffres et des lettres
# Module      : operation.py
# Description : Ce module contient les fonctions relatives à la gestion des opérations.
# ----------------------------------------------------------------------------------------------------------------------
import entier


# ----------------------------------------------------------------------------------------------------------------------
# Fonctions triées par ordre alphabétique
# ----------------------------------------------------------------------------------------------------------------------

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
    if entier.est_positif_non_nul(c):
        if isinstance(c, float):
            c = int(c)  # On s'assure que c est un entier car le résultat d'une division est un float
        return {"a": a, "operateur": operateur, "b": b, "c": c}

    return None


def cree_operations(a: int, b: int) -> dict[int, any]:
    """Crée les opérations entre `a` et `b` dont le résultat est un entier positif non nul."""
    if a < b:
        a, b = b, a  # Si a inférieur à b, on inverse les valeurs

    if b == 0:
        return {}  # Les opérations avec b à zéro sont inutiles ou impossible

    operations: list[any] = [
        cree_operation(a, "-", b, a - b),
        cree_operation(a, "/", b, a / b),
        cree_operation(a, "*", b, a * b),
        cree_operation(a, "+", b, a + b),
    ]

    # Indexation par résultat
    return {operation["c"]: operation for operation in operations if operation is not None}


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
                operations_bc: list[any] = []
                if isinstance(operations_b[b], list):
                    operations_bc = operations_b[b] + [operations_c[c]]
                else:
                    operations_bc = [operations_b[b], operations_c[c]]
                if c not in operations or len(operations[c]) > len(operations_bc):
                    operations[c] = operations_bc

    return operations


def optimise_operations(operations: dict[int, any], objectif: int) -> dict[int, any]:
    """Optimise les opérations fournies supprimant les opérations qui s'éloigne de l'objectif."""
    operations_optimisees: dict[int, any] = {}

    for c in operations:
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
