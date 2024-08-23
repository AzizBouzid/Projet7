action = []
budget = 500
meilleure_action = []


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
        if table[n][w] == table[n - 1][w - action[n - 1][1]]\
                + action[n - 1][3]:
            meilleure_action.append(action[n-1])
            w -= action[n - 1][1]
        n -= 1
    prix = sum([action[1] for action in meilleure_action])
    return table[-1][-1], meilleure_action, prix
