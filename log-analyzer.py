from collections import Counter
from colorama import init, Fore

# Initialiser colorama
init(autoreset=True)

# Lire le fichier log
with open('log.txt', 'r') as file:
    lines = file.readlines()

# Compter les types de messages (ERROR, WARNING, INFO)
types = [line.split(' - ')[0].strip() for line in lines]
count = Counter(types)

# Affichage coloré dans le terminal
print(Fore.CYAN + "\n📊 Résumé de l'analyse du fichier log.txt :\n")
for level in ['ERROR', 'WARNING', 'INFO']:
    couleur = {
        'ERROR': Fore.RED,
        'WARNING': Fore.YELLOW,
        'INFO': Fore.GREEN
    }.get(level, Fore.WHITE)
    print(couleur + f"{level}: {count.get(level, 0)}")

# Générer un rapport texte
with open('rapport.txt', 'w') as report:
    report.write("Rapport d'analyse des logs\n")
    report.write("===========================\n")
    for level in ['ERROR', 'WARNING', 'INFO']:
        report.write(f"{level}: {count.get(level, 0)}\n")

print(Fore.MAGENTA + "\n Rapport généré dans 'rapport.txt'")
