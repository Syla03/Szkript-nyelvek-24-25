# Ez egy megjegyzés

print("Szia DUE!")
print("Szia", "Due!")
print("Szia", "DUE!", sep=':)')
print("\nSzia", "\n\tDue!", end="")
print('''Ez több
sorba kerül!''')
# Komment

felhasznalo_neve = "Jenő"
print(felhasznalo_neve)
felhasznalo_kora = "20"
print(felhasznalo_neve, felhasznalo_kora)

print("Szia", felhasznalo_neve, "!")

print(f"Szia {felhasznalo_neve}!")

print("\nNeve: \t{0} \nKora: \t{1}".format(felhasznalo_neve, felhasznalo_kora))

print(felhasznalo_neve.rjust(30, ','))
print(felhasznalo_kora.rjust(30, ','))

print(felhasznalo_neve.ljust(30, ','))
print(felhasznalo_kora.ljust(30, ','))

print(felhasznalo_neve.center(30, ','))
print(felhasznalo_kora.center(30, ','))

felhasznalo_neve = input("Hogy hívnak: ")

print("Szia", felhasznalo_neve)

felhasznalo_kora = input("Hány éves vagy: ")
print("Biztosan", felhasznalo_kora, " vagy? Nem", int(felhasznalo_kora)+10, "?")
