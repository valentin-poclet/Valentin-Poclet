"""
primes.py - Vérification des nombres premiers

Ce script contient une fonction secondaire `isprime()` 
qui permet de vérifier si un entier est un nombre premier,
et une fonction principale `main()` qui effectue des 
appels à `isprime()` pour afficher les nombres premiers jusqu'à 100.

Fonctions :
-----------
- isprime(p):
    Vérifie si un nombre entier `p` est un nombre premier.
    
    Arguments :
    - p (int) : un entier à tester.
    
    Retourne :
    - bool : `True` si `p` est un nombre premier, sinon `False`.

    Exemple d'utilisation :
    >>> isprime(7)
    True
    >>> isprime(10)
    False

- main():
    Fonction principale qui effectue des appels à 
    `isprime()` et affiche les nombres premiers jusqu'à 100.
    
    Exemple de sortie :
    2, 3, 5, 7, 11, 13, ..., 97
"""

#### Fonction secondaire
def isprime(p):
    """
    Vérifie si un nombre entier `p` est un nombre premier.

    Args:
    p (int): L'entier à vérifier.

    Returns:
    bool: True si `p` est un nombre premier, sinon False.

    """

    # votre code ici
    if p <= 1:
        return False
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            return False
    return True

#### Fonction principale
def main():
    """
    Affiche les nombres premiers entre 0 et 99 en appelant la fonction `isprime()`.
    """
    # vos appels à la fonction secondaire ici
    isprime(1)
    isprime(4)
    isprime(10)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
