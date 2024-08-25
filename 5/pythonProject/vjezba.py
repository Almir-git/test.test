
# ispisati petlju koja  ispisuje brojeve od 0 do 100

numbers = range(100)

for numbers in numbers: # a moze i samo for numbers in range(100) znaci bez varijable

    if numbers == 10:
        continue

    if numbers == 44:
        break

    if numbers%2 == 0:
        print(f"broj je paran {numbers}")






