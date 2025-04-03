import math

def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

def kubus_vol(zijde):
    return zijde ** 3

def bol_vol(straal):
    return (4/3) * math.pi * straal ** 3

def volledige_naam(lijst_met_namen):
    for persoon in lijst_met_namen:
        voornaam = persoon["voornaam"]
        tussen = persoon["tussenvoegsel"]
        achternaam = persoon["achternaam"]
        if tussen:
            naam = f"{voornaam} {tussen} {achternaam}"
        else:
            naam = f"{voornaam} {achternaam}"
        print(naam)

# Conversies
kilometers = 1223
miles = 867
miles_result = kilometers_naar_miles(kilometers)
km_result = miles_naar_kilometers(miles)

print(f"> {kilometers} kilometers = {miles_result} miles")
print(f"> {miles} miles = {km_result} kilometers")

# Volume berekeningen
kubus_volume = kubus_vol(5)
bol_volume = bol_vol(4)

print(f"> De inhoud van deze kubus is: {kubus_volume}")
print(f"> De inhoud van deze bol is: {bol_volume}")

# Volledige namen
namen = [
    {"voornaam": "Willem", "tussenvoegsel": "van", "achternaam": "Dijk"},
    {"voornaam": "Klaas", "tussenvoegsel": "", "achternaam": "Wopstra"},
    {"voornaam": "Miep", "tussenvoegsel": "van der", "achternaam": "Plas"},
    {"voornaam": "Carla", "tussenvoegsel": "", "achternaam": "Hoogvliet"},
]

volledige_naam(namen)
