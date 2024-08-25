# korisnik treba da unese cijenu korpe
# Ako je cijena preko 1000, ispisati ostvarili ste popust (10%)
# Ako je cijena ispod 1000 ispisati vasa korpa iznosi 1000

cart = int(input("Unesite cijenu korpe: "))

if cart >= 1000:
    tax_amount = cart*0.1
    print(f"ostvarili ste popust od 10%, sto iznosi {tax_amount} eura")
else:
    print("Vasa korpa iznosi manje od hiljadu")


