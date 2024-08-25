
name =  "admin"
password = "mojaSifra"

# ako je ime admin i ako je sifra mojaSifra
# Ako je ime "toma" i ako je sifra "123456"
# mozemo elif dodavati koliko hocemo

if name == "admin" and password == "mojaSifra":
    print("Dobro dosao admine!")
elif name == "toma" and password == "123456":
    print("Dobrodosao Tomo!")
elif name == "Mare" and password == "222222":
    print("Dobrodosao Mare!")
else:
    print("Niste administrator! Pogresna sifra ili ime")
