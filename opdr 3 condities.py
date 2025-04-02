# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}

# Hier komt je code...
leeftijd_input = int(input("Geef uw leeftijd in aantal jaar\n"))

groep = None
for key, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        groep = key
        break

if groep:
    korting_percentage = kortings_percentages[groep]
    korting = normale_toegangsprijs * (korting_percentage / 100)
    te_betalen_prijs = normale_toegangsprijs - korting

    print(f"U behoort tot de groep {groep}")
    print(f"U krijgt {korting_percentage}% korting")
    print(f"U betaalt daarom {te_betalen_prijs:.2f}")
else:
    print("Uw leeftijd valt buiten de toegestane groepen.")