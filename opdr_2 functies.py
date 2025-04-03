# Opdracht 1 functies
# Naam student:
# Groep


def kilometers_naar_miles(kilometers):
    return kilometers / 1.609344

def miles_naar_kilometers(miles):
    return miles * 1.609344

# Gegeven waarden
kilometers = 1223
miles = 867

# Conversies
miles_result = kilometers_naar_miles(kilometers)
km_result = miles_naar_kilometers(miles)

# Output
print(f"> {kilometers} kilometers = {miles_result} miles")
print(f"> {miles} miles = {km_result} kilometers")