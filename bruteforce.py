from itertools import combinations

budget = 500
profit = 0
combinaisons = []


def force_brute(action):
    global profit
    for i in range(1, len(action) + 1):
        for combinaison in combinations(action, i):
            cout_total = sum(int(ligne[1]) for ligne in combinaison)
            profit_total = sum(float(ligne[3]) for ligne in combinaison)
            if cout_total <= budget and profit_total > profit:
                combinaisons = combinaison
                profit = profit_total
    cout_total = sum(int(ligne[1]) for ligne in combinaisons)
    return combinaisons, profit, cout_total
