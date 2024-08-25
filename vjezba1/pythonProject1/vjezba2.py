# Napisi program koji trazi od korisnika da unese ime proizvoda a zatim ispisuje cijenu tog proizvoda
# Ako proizvod ne postoji, ispisi poruku "Proizvod nije pronadjen"

products = {"brasno": 1.55, "ulje": 3.33, "jaja": 3.22}

search_product = input("Unesite ime proizvoda: ").lower()

if search_product in products:
    print(products[search_product])
else:
    print("Nije pronadjen proizvod")



