from lirefichier import lire_fichier

action = []
budget = 500
meilleure_action = []


def knapsack(actions, budget):
    n = len(actions)
    # Initialisation de la table avec des zéros
    table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Remplissage de la table
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            prix = int(actions[i - 1][1])  # Prix de l'action
            profit = actions[i - 1][3]     # Bénéfice de l'action

            if prix <= w:
                # On décide de prendre l'action ou non
                table[i][w] = max(profit + table[i-1][w - prix], table[i-1][w])
            else:
                table[i][w] = table[i-1][w]

    # Extraction des actions optimales
    w = budget
    for i in range(n, 0, -1):
        prix = int(actions[i - 1][1])
        if w - prix >= 0 and table[i][w] == table[i-1][w - prix] + actions[i - 1][3]:
            meilleure_action.append(actions[i-1])
            w -= prix

    prix_total = sum(action[1] for action in meilleure_action)
    return table[-1][-1], meilleure_action, prix_total


# Exécution de l'exemple
actions = lire_fichier('dataset2.csv')  # Remplacez par votre fichier CSV
meilleur_profit, meilleure_action, prix_total = knapsack(actions, budget)

print("Profit Maximum:", meilleur_profit)
print("Meilleure Combinaison d'Actions:",
      meilleure_action, len(meilleure_action))
print("Coût Total:", prix_total)
