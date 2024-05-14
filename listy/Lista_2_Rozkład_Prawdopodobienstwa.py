import random
import matplotlib.pyplot as plt
import numpy as np

def middle_square(seed, iterations):
    if seed <= 0 or iterations <= 0:
        raise ValueError("Seed and iterations must be positive integers")

    num_digits = len(str(seed))
    results = []

    # Set to store seen seeds
    seen_seeds = set()

    for _ in range(iterations):
        square = seed ** 2
        square_str = str(square).zfill(2 * num_digits)
        middle = int(square_str[(len(square_str) - num_digits) // 2 : (len(square_str) + num_digits) // 2])

        # If the seed repeats, break the loop
        if seed in seen_seeds:
            print(f"Seed {seed} is repeated. The following results may be repeated.")
            break
        else:
            seen_seeds.add(seed)

        results.append((seed, middle, square))
        seed = middle

    return results

def print_results(results):
    for i, (seed, middle, square) in enumerate(results):
        print(f'x{i+1}\t {square:<20} {middle}')

def plot_results(results):
    x_values = [i for i in range(len(results) - 1)]
    normalized_results = [middle / 10000 for _, middle, _ in results[:-1]]

    # Plotting the points with normalized values
    plt.scatter(x_values, normalized_results, c='blue', label='Punkty (xi, xi+1)')
    plt.xlabel('Iteracja')
    plt.ylabel('Znormalizowana wartość środkowa')
    plt.title('Wykres punktowy wyników algorytmu middle square')

    # Obliczamy całkę od 0 do 1 z e^-x^2
    x = np.linspace(0, 1, 1000)  # Zakres od 0 do 1
    y = np.exp(-x**2)  # Funkcja e^-x^2
    integral = np.trapz(y, x)  # Obliczamy całkę numerycznie

    print("Wartość całki od 0 do 1 z e^-x^2:", integral)

    plt.legend()
    plt.show()

# Funkcja generująca punkty na podstawie middle_square
def generate_points_from_middle_square(seed, iterations):
    results = middle_square(seed, iterations)
    points = [(seed, middle) for seed, middle, square in results]
    return points

# Funkcja wykonująca operacje na wygenerowanych punktach
def process_points(points):
    suma = 0
    all = 0
    max_value = 0
    lib = []
    table = 0

    # Znajdowanie maksymalnej wartości w tablicy punktów
    for point in points:
        if point[1] > max_value:
            max_value = point[1]

    # Normalizacja tablicy punktów i zapisanie jej w 'lib'
    for point in points:
        lib.append(point[1] / max_value)

    length = len(lib)
    przebieg = 0

    # Pętla while, która trwa, dopóki 'table' nie zostanie ustawione
    while table == 0:
        ax = random.randint(0, length - 1)
        bx = random.randint(0, length - 1)
        a = lib[ax]
        b = lib[bx]
        operation = (1 - a)**3 * ((256 / 27) * a)
        
        print(f"{a} {b} {operation}")
        
        przebieg += 1
        
        # Sprawdzenie, czy 'b' jest mniejsze lub równe wynikowi operacji
        if b <= operation:
            table = a

    print(f"{table} przy {przebieg} próbach")
"""
# Generowanie punktów przy użyciu algorytmu middle_square
seed = 1211
iterations = 100
points = generate_points_from_middle_square(seed, iterations)

# Przykład użycia punktów w dalszej analizie
print("Generated Points:")
for point in points:
    print(point)

# Wykonanie operacji na wygenerowanych punktach
process_points(points)

# Wizualizacja wyników
results = middle_square(seed, iterations)
print_results(results)
plot_results(results)
"""
# Testowanie funkcji z 8-cyfrowym seedem
seed = 12345678
iterations = 200
points = generate_points_from_middle_square(seed, iterations)

# Przykład użycia punktów w dalszej analizie
print("Generated Points with 8-digit seed:")
for point in points:
    print(point)

# Wykonanie operacji na wygenerowanych punktach
process_points(points)

# Wizualizacja wyników
results = middle_square(seed, iterations)
print_results(results)
plot_results(results)
