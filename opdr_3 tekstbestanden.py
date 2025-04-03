def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Controleer of het een letter is
            base = ord('A') if char.isupper() else ord('a')
            # Verschuif de letter en zorg dat het binnen het alfabet blijft
            encrypted_char = chr((ord(char) - base + shift) % 26 + base)
            encrypted_text += encrypted_char
        else:
            # Niet-letters blijven ongewijzigd
            encrypted_text += char
    return encrypted_text


def main():
    text = input("Tekst om te encrypten: ")
    print("Geëncrypte tekst:", encrypt(text, 5))


if __name__ == "__main__":
    main()