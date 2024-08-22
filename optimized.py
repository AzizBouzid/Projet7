from bruteforce import lire_fichier
import time
action = []
budget = 500
meilleure_action = []
fichier = 'action1.csv'
BOLD = '\033[1m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
END = '\033[0m'


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
    action = lire_fichier(fichier)
    start_time = time.time()
    benef, meilleure_action, prix = optimized(action)
    print(f"Les meilleures actions:\n")
    for ligne in meilleure_action:
        print(f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
    print(BOLD + f"\nMontant total: {YELLOW}{prix} €" + END)
    nombre = benef
    print(BOLD + "\nBénéfice total:" + CYAN + "{0:.2f}".format(nombre), "€" + END)
    nombre = time.time()-start_time
    print(BOLD + f"\nTemps d'exécution: {RED}{0:.2f}".format(nombre),
          "secondes\n" + END)
    print(BOLD + f"Nombre d'actions: {len(meilleure_action)}\n" + END)
