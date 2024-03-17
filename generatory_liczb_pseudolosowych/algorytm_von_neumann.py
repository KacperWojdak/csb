
def middle_square(seed, iterations):
    if seed <= 0 or iterations <= 0:
        raise ValueError("Seed and iterations must be positive integers")

    num_digits = len(str(seed))
    results = []

    for _ in range(iterations):
        square = seed ** 2
        square_str = str(square).zfill(2 * num_digits)
        middle = int(square_str[(len(square_str) - num_digits) // 2 : (len(square_str) + num_digits) // 2])
        results.append((seed, middle, square))
        seed = middle

    return results

def print_results(results):
    for i, (seed, middle, square) in enumerate(results):
        print(f'x{i+1}\t {square:<20} {middle}')

print_results(middle_square(1211, 10))
# Testing the function with an 8-digit seed
print_results(middle_square(12345678, 10))