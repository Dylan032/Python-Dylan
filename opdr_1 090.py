# Opdracht 1 functies
# Naam student:
# Groep:


def read_from_file(afile):
    try:
        with open(afile, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("Bestand niet gevonden.")
        return ""
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")
        return "" 
def write_to_file(afile, atext):
    try:
        with open(afile, 'a') as file:  
            file.write(atext + '\n')  
    except Exception as e:
        print(f"Er is een fout opgetreden: {e}")

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"
write_to_file(my_file, my_tekst)


print(read_from_file(my_file))
write_to_file(my_file, my_tekst)