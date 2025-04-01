# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = ["Dylan", "Paul", "Kees", "Marie", "Hilda"]

#
print(gasten)

gasten.remove("Marie")
print(gasten)

index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")
gasten.append("Dylan")
if "Jij" in gasten:
    gasten[gasten.index("Jij")] = "Dylan"
while "Jij" in gasten:
    gasten[gasten.index("Jij")] = "Dylan"
print(gasten)