from collections import Counter
from colorama import init, Fore

init(autoreset=True)

with open('log.txt', 'r') as file:
    lines = file.readlines()

types = [line.split(' - ')[0].strip() for line in lines]
count = Counter(types)

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
