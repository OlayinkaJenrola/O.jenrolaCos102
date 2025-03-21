def simple_interest(P, R, T):
    return P * (1 + (R / 100) * T)

def compound_interest(P, R, n, T):
    return P * (1 + (R / (100 * n)))**(n * T)

def annuity_plan(PMT, R, n, T):
    R = R / (100 * n)
    return PMT * ((1 + R)**(n * T) - 1) / R

# Input values
P = float(input("Enter principal amount: "))
R = float(input("Enter annual interest rate (%): "))
T = float(input("Enter time (years): "))
n = int(input("Enter compounding periods per year: "))
PMT = float(input("Enter annuity payment: "))

# Calculate and display results
print(f"Simple Interest: {simple_interest(P, R, T):.2f}")
print(f"Compound Interest: {compound_interest(P, R, n, T):.2f}")
print(f"Annuity Plan: {annuity_plan(PMT, R, n, T):.2f}")

