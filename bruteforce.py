import csv
from itertools import combinations

budget = 500
profit = 0
action = []
combinaisons = []


def lire_fichier(fichier):
    with open(fichier, 'r') as csvfile:
        fichier = csv.reader(csvfile, delimiter=',')
        next(fichier)
        for ligne in fichier:
            if int(float(ligne[1])) > 0 and int(float(ligne[2])) > 0:
                action.append(
                    (ligne[0], int(float(ligne[1])), int(float(ligne[2])),
                     int(float(ligne[1])) * int(float(ligne[2]))/100))
    return action


def force_brute():
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
