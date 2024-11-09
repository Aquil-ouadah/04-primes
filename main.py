"""Ce code permet de vérifier si un nombre entier est premier"""
from math import sqrt
#### Fonction secondaire


def isprime(p):

    """Fonction qui vérifie si un nombre entier p est premier."""
    if p < 2:
        return False
    if p == 2:
        return True
    for d in range(2, int(sqrt(p)) + 1):
        if p % d == 0:
            return False
    return True
# votre code ici


#### Fonction principale


def main():
    """Cette fonction est la fonction principale"""
# Parcourir une plage de nombres avec un for in range
    for t in range(1, 57):
        if isprime(t):
            print(isprime)
        else:
            print(isprime)

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
