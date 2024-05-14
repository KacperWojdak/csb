import numpy as np

# Definiujemy funkcję, która oblicza wariancję przekształconej zmiennej losowej
def variance_transformed(a, b, X):
    # Wartość oczekiwana X
    E_X = np.mean(X)
    
    # Wariancja X
    var_X = np.var(X, ddof=1)
    
    # Przekształcona zmienna losowa Y = aX + b
    Y = a * X + b
    
    # Wartość oczekiwana Y
    E_Y = np.mean(Y)
    
    # Wariancja Y
    var_Y = np.var(Y, ddof=1)
    
    # Wariancja przekształconej zmiennej losowej zgodnie z teoretycznym wzorem
    theoretical_var_Y = a**2 * var_X
    
    return var_Y, theoretical_var_Y

# Przykładowe dane
X = np.random.normal(0, 1, 1000)  # Losowe dane z rozkładu normalnego
a = 2
b = 5

# Obliczanie wariancji przekształconej zmiennej losowej
empirical_var_Y, theoretical_var_Y = variance_transformed(a, b, X)

print(f"Empiryczna wariancja Y: {empirical_var_Y}")
print(f"Teoretyczna wariancja Y: {theoretical_var_Y}")

# Sprawdzenie, czy wartości są zbliżone
np.isclose(empirical_var_Y, theoretical_var_Y)