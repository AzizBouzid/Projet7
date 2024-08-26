import csv


def lire_fichier(fichier):
    action = []
    with open(fichier, 'r') as csvfile:
        fichier = csv.reader(csvfile, delimiter=',')
        next(fichier)
        for ligne in fichier:
            name = ligne[0]
            price = int(float(ligne[1]))
            profit = float(ligne[2])
            benefice = round((price * profit) / 100, 2)
            if price > 0 and profit > 0:
                action.append((name, price, profit, benefice))
    return action
