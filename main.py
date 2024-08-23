import questionary
import time
from bruteforce import force_brute, lire_fichier
from optimized import optimized

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
                     "Optimized fichier dataset2"],
        ).ask()
    )
    if reponse == "Brute force":
        fichier = 'dataset.csv'
        start_time = time.time()
        lire_fichier(fichier)
        combinaisons, profit, cout_total = force_brute()
        print(BOLD + "\nLes meilleures actions:\n" + END)
        for ligne in combinaisons:
            print(
                f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
        print(
            BOLD + f"\nMontant total: {YELLOW}{cout_total} €" + END)
        print(BOLD + f"\nBénéfice total: {CYAN}{profit} €" + END)
        nombre = time.time()-start_time
        print(BOLD + f"\nTemps d'exécution: {RED}{0:.2f}".format(nombre),
              "secondes\n" + END)
        print(BOLD + f"Nombre d'actions: {len(combinaisons)}\n" + END)
    if reponse == "Optimized fichier dataset1" or \
            reponse == "Optimized fichier dataset2":
        if reponse == "Optimized fichier dataset1":
            fichier = 'dataset1.csv'
        if reponse == "Optimized fichier dataset2":
            fichier = 'dataset2.csv'
        action = lire_fichier(fichier)
        start_time = time.time()
        benef, meilleure_action, prix = optimized(action)
        print(BOLD + "\nLes meilleures actions:\n" + END)
        for ligne in meilleure_action:
            print(
                f"\t{ligne[0]}:\tCoût = {ligne[1]} €\tBénéfice = {ligne[3]} €")
        print(BOLD + f"\nMontant total: {YELLOW}{prix} €" + END)
        nombre = benef
        print(BOLD + "\nBénéfice total: " + CYAN + "{0:.2f}".format(nombre),
              "€" + END)
        nombre = time.time()-start_time
        print(BOLD + f"\nTemps d'exécution: {RED}{0:.2f}".format(nombre),
              "secondes\n" + END)
        print(BOLD + f"Nombre d'actions: {len(meilleure_action)}\n" + END)
