import csv
import time
action = []
budget = 500
meilleure_action = []
fichier = 'action1.csv'


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


def optimized(action):
    n = len(action)
    w = budget
    table = [[0 for x in range(w + 1)] for x in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, w + 1):
            if action[i - 1][1] <= w:
                table[i][w] = max((action[i-1][3]) + table[i-1]
                                  [w - action[i - 1][1]], table[i - 1][w])
            else:
                table[i][w] = table[i-1][w]
    while w >= 0 and n >= 0:
        if table[n][w] == table[n - 1][w - action[n - 1][1]] + action[n - 1][3]:
            meilleure_action.append(action[n-1])
            w -= action[n - 1][1]
        n -= 1
    prix = sum([action[1] for action in meilleure_action])
    return table[-1][-1], meilleure_action, prix


if __name__ == '__main__':
    list_actions = lire_fichier(fichier)
    start_time = time.time()
    benef, meilleure_action, prix = optimized(action)
    print(f"Les meilleures actions:\n")
    for ligne in meilleure_action:
        print(f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
    print(f"\nMontant total du bénéfice: {int(benef)} €")
    print(f"\nMontant total: {prix} €")
    nombre = time.time()-start_time
    print(f"\nTemps d'exécution: {0:.2f}".format(nombre).
          rjust(7), "secondes\n")
    print(f"Nombre d'actions: {len(meilleure_action)}")
