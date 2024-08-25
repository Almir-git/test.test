

shops = {
    "Maxi": {
        "hleb": 100,
        "jaja": 33,
    },
    "Idea":  {
        "hleb": 90,
        "jaja": 35,
    },
    "HML":  {
        "hleb": 92,
        "jaja": 32,
    },
    "HML":  {
        "jaja": 32,
    }
}

# da ispisem cijene hleba, pa ispisati prosjecnu cijenu

total_bread_price = 0
total_bread_shop = 0

for shop_name, items in shops.items():
    if "hleb" in items:
        total_bread_price += items["hleb"]
        total_bread_shop += 1


averge_bread_price = total_bread_price / total_bread_shop

print(averge_bread_price)





