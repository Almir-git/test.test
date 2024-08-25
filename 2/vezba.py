Cars = ["Mercedes", "BMW", "Yugo"]
print (Cars)

Cars [1] = "Audi"
print(Cars)

# Da dodam jos jednu marku listi .append dodajem
Cars.append("Skoda")
print(Cars)

Cars.sort()
print(Cars)
# ako bi mi trebalo unazad da sortiram onda u zagradi dodajem reverse = True

# Trenutno na stanju ima X automobila
print(f"Trenutno na stanju imamo {len(Cars)} automobila")
