
# Napraviti listu proizvoda  i ubaciti 3 proizvoda Iphone 14. Iphone 15 i Samsung S23
# Napisati provjeru koja provjerava da li postoji Iphone 14 u nasoj listi
# Za Iphone 14 napraviti varijablu


products = ["Iphone 14", "Iphone 15", "Samsung S23"]

Phone_new = input("Unesite ime telefona koji trazite")
print("KORISNIK JE UNEO "+Phone_new)

if Phone_new in products:
    print("Pronasli smo Iphone 14")
else:
    print("Nismo pronasli trazeni proizvod")



