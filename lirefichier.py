import csv


def lire_fichier(fichier):
    action = []
    with open(fichier, 'r') as csvfile:
        fichier = csv.reader(csvfile, delimiter=',')
        next(fichier)
        for ligne in fichier:
            if int(float(ligne[1])) > 0 and int(float(ligne[2])) > 0:
                action.append(
                    (ligne[0], int(float(ligne[1])), int(float(ligne[2])),
                     int(float(ligne[1])) * int(float(ligne[2]))/100))
    return action
