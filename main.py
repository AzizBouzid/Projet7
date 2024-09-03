from bruteforce import force_brute
from lirefichier import lire_fichier
from optimized import optimized
import questionary
import time

BOLD = '\033[1m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
RED = '\033[91m'
END = '\033[0m'


if __name__ == "__main__":
    reponse = (
        questionary.rawselect(
            "Faites votre choix",
            choices=["Brute force", "Optimized fichier dataset1",
                     "Optimized fichier dataset2", "Quitter"],
        ).ask()
    )
    if reponse == "Quitter":
        exit()
    if reponse == "Brute force":
        start_time = time.time()
        fichier = 'dataset.csv'
        combinaisons, profit, cout_total = force_brute(lire_fichier(fichier))
        print(BOLD + "\nLes meilleures actions:\n" + END)
        for ligne in combinaisons:
            print(
                f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
        print(
            BOLD + f"\nMontant total: {YELLOW}{cout_total} €" + END)
        print(BOLD + f"\nBénéfice total: {CYAN}{profit} €" + END)
        nombre = time.time()-start_time
        print(BOLD + f"\nTemps d'exécution:  {RED}% .2f" % nombre +
              " secondes\n" + END)
        print(BOLD + f"Nombre d'actions: {len(combinaisons)}\n" + END)
    if reponse == "Optimized fichier dataset1" or \
            reponse == "Optimized fichier dataset2":
        if reponse == "Optimized fichier dataset1":
            fichier = 'dataset1.csv'
        if reponse == "Optimized fichier dataset2":
            fichier = 'dataset2.csv'
        action = lire_fichier(fichier)
        start_time = time.time()
        benefice, meilleure_action, prix, portefeuille = optimized(action)
        print(BOLD, "\nNombre d'actions traitées: ", portefeuille)
        print(BOLD + "\nLes meilleures actions:\n" + END)
        for ligne in meilleure_action:
            print(
                f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
        print(BOLD + f"\nMontant total: {YELLOW}{prix} €" + END)
        benef = round(benefice, 2)
        print(BOLD + f"\nBénéfice total: {CYAN}{benef} €" + END)
        nombre = round(time.time()-start_time, 2)
        print(BOLD + f"\nTemps d'exécution: {RED}{nombre} secondes\n" + END)
        print(BOLD + f"Nombre d'actions: {len(meilleure_action)}\n" + END)
