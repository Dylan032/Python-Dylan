# Opdracht 1 while-loops
# Naam student:
# Groep:

vragen = [
    "Wat vind je van de huidige regering?",
    "Wat vind je van de Python-lessen tot nu toe?",
    "Wat vind jij de mooiste stad van Nederland?"
]
antwoorden = []
for vraag in vragen:
    antwoord = input(vraag + " ")
    antwoorden.append(antwoord)

# Resultaten opslaan in een tekstbestand
with open("enquete_resultaten.txt", "w", encoding="utf-8") as bestand:
    for i, vraag in enumerate(vragen):
        bestand.write(f"{vraag}\nAntwoord: {antwoorden[i]}\n\n")

print("De resultaten zijn opgeslagen in 'enquete_resultaten.txt'.")