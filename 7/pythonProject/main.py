

products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    }
}


option = None
history =[]

allowed_option = [
    "dodaj", "obrisi",
    "izlistaj", "stop",
    "obrisi sve", "prikazi najskuplji proizvod", "pnp"
]

while option not in allowed_option:
    option = input(f"Sta zelite da odradite? {" , ".join(allowed_option)} \n").lower()

    if option == "obrisi":
        product = None

        while product not in products:
            product = input("Unesite ime proizvoda za brisanje: \n ").lower()

        del products[product]

        msg = f"Obrisali ste {product} \n"

        print(msg)
        history.append(msg)
        option = None

    elif option == "dodaj":

        product = None

        while product in products or product is None:
            product = input("Unesite ime proizvoda koje ne postoji: \n").lower()

        product_price = None
        while product_price is None or product_price <= 0:
            product_price = int(input("Unesite cenu proizvoda: \n"))

        product_amount = None
        while product_amount is None or product_amount <0:
            product_amount = int(input("unesite kolicinu proizvoda: \n"))


        products[product] = {
            "cena": product_price,
            "kolicina": product_amount
        }

        mgs = f"Dodali ste novi proizvod {product} \n"

        print(mgs)
        history.append(mgs)
        option = None

    elif option == "izlistaj":
        print(products)
        option = None

    elif option == "istorijat":
        print(history)
        option = None

    elif option == "obrisi sve":
        products = {}
        option = None

    elif option == "prikazi najskuplji proizvod" or "pnp":

        highest_price = 0
        most_expensive_product = None

        for product in products:
            if highest_price < products[product]['cena']:
                highest_price = products[product]['cena']
                most_expensive_product = product

        print(most_expensive_product)


print(products)





