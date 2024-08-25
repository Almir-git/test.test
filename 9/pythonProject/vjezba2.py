def calculate_delivery(city):
    if city == "beograd" or city == "zagreb":
        return 500
    elif city == "subotica":
        return 1200
    elif city == "novi sad":
        return 700
    elif city == "split":
        return 1300
    else:
        return -1


belgrade_delivery = calculate_delivery("beograd")
product_price = 200
total_cart_price = belgrade_delivery+product_price


print(f"Vasa narudzina kosta {product_price}, dostava je {belgrade_delivery}, a ukupno korpa je {total_cart_price}")