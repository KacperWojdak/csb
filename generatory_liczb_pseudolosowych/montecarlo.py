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
            break
        else:
            seen_seeds.add(seed)

        results.append((seed, middle, square))
        seed = middle

    return results

def monte_carlo_pi(results, num_points):
    points_inside_circle = 0
    
    for _ in range(num_points):
        _, middle, _ = results[_ % len(results)]  # Using modulo to loop through the results
        x = (middle % 10000) / 10000  # Normalize to range [0, 1]
        y = (middle // 10000) / 10000  # Normalize to range [0, 1]
        
        distance = x**2 + y**2
        if distance <= 1:
            points_inside_circle += 1
    
    pi_approx = 4 * points_inside_circle / num_points
    return pi_approx

# Run middle square algorithm to generate random numbers
results = middle_square(1211, 1000)

# Approximate π using generated random numbers
num_points = 100000
pi_approx = monte_carlo_pi(results, num_points)
print("Approximated value of π using Monte Carlo method with Middle Square algorithm:", pi_approx)
