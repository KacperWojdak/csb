import numpy as np

def calculate_variance(X, a, b):
    # Oblicz wariancję oryginalnej zmiennej losowej X
    var_X = np.var(X, ddof=1)
    
    # Przekształć zmienną losową X na aX + b
    transformed_X = a * X + b
    
    # Oblicz wariancję przekształconej zmiennej losowej
    var_transformed_X = np.var(transformed_X, ddof=1)
    
    return var_X, var_transformed_X

# Przykładowe dane
X = np.random.normal(0, 1, 1000)  # Próbki z rozkładu normalnego
a = 3
b = 5

var_X, var_transformed_X = calculate_variance(X, a, b)

print(f"Variance of original X: {var_X}")
print(f"Variance of transformed X (aX + b): {var_transformed_X}")
print(f"a^2 * Variance of X: {a**2 * var_X}")