# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

# Startlijst met pizza's
my_list = ['margharita', 'calzone', 'verdi', 'olivio', 'quattro stagioni']

# Sorteer de lijst op alfabet
my_list.sort()
print("Gesorteerde lijst:", my_list)

# Voeg een nieuwe pizza toe
my_list.append('yo-favorito')
print("Lijst na toevoegen van een pizza:", my_list)

# Verwijder de minst lekkere pizza
my_list.remove('olivio')
print("Lijst na verwijderen van minst lekkere pizza:", my_list)

# Print de eerste 3 pizza's
print("Eerste 3 pizza's:", my_list[:3])

# Print de middelste pizza
middle_index = len(my_list) // 2
print("Middelste pizza:", [my_list[middle_index]])

# Print de laatste 3 pizza's
print("Laatste 3 pizza's:", my_list[-3:])