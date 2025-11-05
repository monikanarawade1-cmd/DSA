

Maximize Profit by Shipping Partial Orders (Fractional Knapsack) Problem Statement: You run a shipping company and need to load a truck with parcels of different weights and profits. The truck has a limited weight capacity. Write a program to choose parcels (even partially) to maximize profit using the Fractional Knapsack strategy.



# Function to calculate maximum profit using Fractional Knapsack
def fractional_knapsack(weights, profits, capacity):
    n = len(weights)
    # Create list of (profit/weight ratio, weight, profit)
    items = [(profits[i]/weights[i], weights[i], profits[i]) for i in range(n)]
    # Sort items by profit/weight ratio in descending order
    items.sort(key=lambda x: x[0], reverse=True)

    total_profit = 0
    fractions = [0]*n  # Track fraction of each parcel taken

    for i, (ratio, w, p) in enumerate(items):
        if capacity == 0:
            break
        if w <= capacity:
            capacity -= w
            total_profit += p
            fractions[i] = 1  # Take full parcel
        else:
            frac = capacity / w
            total_profit += p * frac
            fractions[i] = frac
            capacity = 0

    return total_profit, fractions, items

# ------------------- Main Program -------------------
n = int(input("Enter number of parcels: "))
weights = []
profits = []
for i in range(n):
    w = float(input(f"Enter weight of parcel {i+1}: "))
    p = float(input(f"Enter profit of parcel {i+1}: "))
    weights.append(w)
    profits.append(p)

capacity = float(input("Enter truck capacity: "))

max_profit, fractions, items = fractional_knapsack(weights, profits, capacity)

print(f"\nMaximum Profit: {max_profit:.2f}")
print("Parcels taken (fraction of each):")
for i, frac in enumerate(fractions):
    ratio, w, p = items[i]
    print(f"Parcel with weight {w} and profit {p}: {frac*100:.1f}%")

OUTPUT:
Enter number of parcels: 3
Enter weight of parcel 1: 10
Enter profit of parcel 1: 60
Enter weight of parcel 2: 20
Enter profit of parcel 2: 100
Enter weight of parcel 3: 30
Enter profit of parcel 3: 120
Enter truck capacity: 50

Maximum Profit: 240.00
Parcels taken (fraction of each):
Parcel with weight 10.0 and profit 60.0: 100.0%
Parcel with weight 20.0 and profit 100.0: 100.0%
Parcel with weight 30.0 and profit 120.0: 66.7%






