import random

# Opdracht 2 tekstbestanden
# Naam student:
# Groep:



prompt = "Raad het geheime getal: "
aantal_pogingen = 0

while True:
    try:
        gok = int(input(prompt))
        aantal_pogingen += 1
        geheim_getal = random.randint(1, 100)

        while True:
            try:
                gok = int(input(prompt))
                aantal_pogingen += 1
                if gok < geheim_getal:
                    print("hoger")
                elif gok > geheim_getal:
                    print("lager")
                else:
                    print(f"Je hebt het getal geraden het is {geheim_getal}!")
                    print(f"Je hebt het in {aantal_pogingen} keer gedaan")
                    break
            except ValueError:
                print("Voer een geldig getal in.")
    except ValueError:
        print("Voer een geldig getal in.")