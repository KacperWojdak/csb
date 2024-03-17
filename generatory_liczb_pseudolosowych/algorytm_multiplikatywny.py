def generuj_liczby_pseudolosowe(a, m, seed, ilosc_liczb):
    X = int(seed * m)
    wyniki_przed_unormowaniem = []
    wyniki_po_unormowaniu = []
    unikalne_wyniki = set()
    okres = 0
    for i in range(ilosc_liczb):
        X = (a * X) % m
        if X in unikalne_wyniki:
            okres = i + 1
            break
        unikalne_wyniki.add(X)
        wyniki_przed_unormowaniem.append(X)
        wyniki_po_unormowaniu.append(X / m)
    return wyniki_przed_unormowaniem, wyniki_po_unormowaniu, okres

def wyswietl_wyniki(a, m, seed, ilosc_liczb):
    wyniki_przed_unormowaniem, wyniki_po_unormowaniu, okres = generuj_liczby_pseudolosowe(a, m, seed, ilosc_liczb)
    print("parametry algorytmu multiplikatywnego")
    print("a", a)
    print("m", m)
    print("seed", seed)
    print("# liczby", "przed unormowaniem", "po unormowaniu", sep="\t")
    for i in range(len(wyniki_przed_unormowaniem)):
        print(f"x{i+1}", wyniki_przed_unormowaniem[i], f"{wyniki_po_unormowaniu[i]:.6f}", sep="\t")
    if okres:
        print(f"okres\t{okres}")

a = 32345
m = 121
seed = 0.2
ilosc_liczb = 60

wyswietl_wyniki(a, m, seed, ilosc_liczb)