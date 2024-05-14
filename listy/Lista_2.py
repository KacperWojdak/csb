import numpy as np

def simulate_insurance(annual_days, lambda_claims, claim_mean, daily_revenue, initial_capital, num_simulations):
    successful_simulations = 0

    for _ in range(num_simulations):
        capital = initial_capital
        positive_capital = True

        for day in range(annual_days):
            # Dodajemy dzienny dochód
            capital += daily_revenue

            # Liczba roszczeń tego dnia (proces Poissona)
            num_claims = np.random.poisson(lambda_claims)

            # Suma roszczeń tego dnia (kwoty roszczeń mają rozkład wykładniczy)
            total_claim_amount = np.sum(np.random.exponential(claim_mean, num_claims))

            # Odejmujemy kwotę roszczeń od kapitału
            capital -= total_claim_amount

            # Sprawdzamy, czy kapitał jest nadal dodatni
            if capital < 0:
                positive_capital = False
                break

        if positive_capital:
            successful_simulations += 1

    # Prawdopodobieństwo, że kapitał będzie zawsze dodatni przez 365 dni
    probability_positive_capital = successful_simulations / num_simulations
    return probability_positive_capital

# Parametry symulacji
annual_days = 365
lambda_claims = 10
claim_mean = 1000
daily_revenue = 11000
initial_capital = 25000
num_simulations = 10000

# Uruchomienie symulacji
probability_positive = simulate_insurance(annual_days, lambda_claims, claim_mean, daily_revenue, initial_capital, num_simulations)

print(f"Prawdopodobieństwo, że kapitał będzie zawsze dodatni przez pierwszych 365 dni: {probability_positive:.4f}")
