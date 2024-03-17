def generuj_lehmer(seed, a, m, n):
    X = seed
    wyniki_przed_unormowaniem = []
    wyniki_po_unormowaniu = []
    unikalne_wyniki = set()
    okres = 0
    for _ in range(n):
        X = (a * X) % m
        if X in unikalne_wyniki:
            okres = len(wyniki_przed_unormowaniem) + 1
            break
        unikalne_wyniki.add(X)
        wyniki_przed_unormowaniem.append(X)
        wyniki_po_unormowaniu.append(X / m)
    return wyniki_przed_unormowaniem, wyniki_po_unormowaniu, okres

def wyswietl_wyniki_lehmer(seed, a, m, n):
    wyniki_przed_unormowaniem, wyniki_po_unormowaniu, okres = generuj_lehmer(seed, a, m, n)
    print("parametry algorytmu lehmera")
    print("a", a)
    print("m", m)
    print("seed", seed)
    print("# liczby", "przed unormowaniem", "po unormowaniu", sep="\t")
    for i in range(len(wyniki_przed_unormowaniem)):
        print(f"x{i+1}", wyniki_przed_unormowaniem[i], f"{wyniki_po_unormowaniu[i]:.6f}", sep="\t")
    if okres:
        print(f"okres\t{okres}")

seed = 7
a = 16807
m = 2**31 - 1
n = 100

wyswietl_wyniki_lehmer(seed, a, m, n)