# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

input_string = input("Voer een lijst in van minimaal 5 objecten, gescheiden door komma's: ")

objecten_lijst = [item.strip() for item in input_string.split(",")]

if len(objecten_lijst) < 5:
    print("De lijst moet minimaal 5 objecten bevatten.")
else:

    gesorteerde_lijst = sorted(objecten_lijst, reverse=True)
    print(gesorteerde_lijst)