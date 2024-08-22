import csv
from itertools import combinations
import time

fichier = 'action.csv'
budget = 500
profit = 0
action = []
combinaisons = []
BOLD = '\033[1m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
END = '\033[0m'


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


if __name__ == '__main__':
    start_time = time.time()
    lire_fichier(fichier)
    combinaisons, profit, cout_total = force_brute()
    print(BOLD + "\nLes meilleures actions:\n" + END)
    for ligne in combinaisons:
        print(f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
    print(
        BOLD + f"\nMontant total: {YELLOW}{str(cout_total).rjust(10)} €" + END)
    print(BOLD + f"\nBénéfice total: {CYAN}{str(profit).rjust(11)} €" + END)
    nombre = time.time()-start_time
    print(BOLD + f"\nTemps d'exécution: {RED}{0:.2f}".format(nombre).
          rjust(7), "secondes\n" + END)
