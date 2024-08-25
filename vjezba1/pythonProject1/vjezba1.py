

age = int(input("Koliko imate godina?"))

# ako korisnik unese godine manje od 0, ispisati gresku i zaustaviti program

if age < 0:
    print("Godine ne mogu biti manje od 0")
    quit()

if age <= 12:
    print("Vi ste dijete")
elif age >= 13 and age < 18:
    print("Vi ste tinejdzer")
elif age >= 18 and age < 65:
    print("Vi ste odrasla osoba")
else:
    print("Vi ste penzioner")