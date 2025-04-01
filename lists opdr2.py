# Opdracht 2 lists
# Naam student:
# Groep:


rivier_info = {
    "rijn": ["nederland", "duitsland", "Frankrijk"],
    "maas": ["nederland", "belgië", "duitsland"],
    "nijl": ["egypte", "soedan", "oeganda"]
}

rivieren = list(rivier_info.keys())
# rivieren is nu een list met alleen de riviernamen: ['rijn', 'maas', 'nijl']

# Hier jouw code.....# Opdracht 1 berekeningen
# Naam student:
# Groep:

# Print de namen van de rivieren
print("De rivieren zijn:")
for rivier in rivieren:
    print(f"- {rivier}")

# Print de landen waar de rivieren doorheen stromen
print("\nDe rivieren stromen door de volgende landen:")
for rivier, landen in rivier_info.items():
    landen_str = ", ".join(landen)
    print(f"De {rivier.capitalize()} stroomt door: {landen_str}")

# Print een samenvatting
print("\nSamenvatting:")
for rivier, landen in rivier_info.items():
    print(f"De {rivier.capitalize()} stroomt door {len(landen)} landen.")