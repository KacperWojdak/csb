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

results = middle_square(1211, 100)
print_results(results)
plot_results(results)

# Testing the function with an 8-digit seed
results = middle_square(12345678, 200)
print_results(results)
plot_results(results)
