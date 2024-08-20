import csv
import time

prix = []
profit = []
action = []
meilleure_action = []
budget = 500
fichier = 'action1.csv'


def lire_fichier(fichier):
    with open(fichier, 'r') as csvfile:
        fichier = csv.reader(csvfile, delimiter=',')
        next(fichier)
        for ligne in fichier:
            if int(float(ligne[1])) > 0 and float(ligne[2]):
                action.append(ligne[0])
                prix.append(int(float(ligne[1])))
                profit.append(float(ligne[2]))
    return prix, profit


def optimized(valeur):
    table = [[0 for x in range(budget + 1)] for x in range(valeur + 1)]
    for i in range(valeur + 1):
        for j in range(budget + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif prix[i-1] <= j:
                table[i][j] = max(profit[i-1]
                                  + table[i-1][j-prix[i-1]],  table[i-1][j])

            else:
                table[i][j] = table[i-1][j]
    prix_total = 0.0
    i = len(prix)
    j = 500
    while (i > 0 and j > 0):
        if table[i][j] == table[i-1][j-prix[i-1]] + profit[i-1]:
            prix_total += prix[i-1]
            j -= prix[i-1]
            meilleure_action.append((action[i], prix[i], profit[i]))
        i -= 1
    meilleur_profit = table[-1][-1]

    return meilleur_profit, prix_total


if __name__ == "__main__":
    start_time = time.time()
    lire_fichier(fichier)
    meilleur_profit, prix_total = optimized(
        len(prix))
    print("\nMeilleures actions : \n")
    somme = 0
    for ligne in meilleure_action:
        benif = ligne[1]*ligne[2]/100
        benif = round(benif, 2)
        somme += benif
        print(f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {benif} €")
    print(f"\nMontant total : {prix_total}")
    print(f"\nMontant profit : {somme}")
    nombre = time.time()-start_time
    print(f"\nTemps d'exécution: {0:.2f}".format(nombre).
          rjust(7), "secondes\n")
