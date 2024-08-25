# Napraviti sledece variables: program_name, version, is_new_program
# Tipovi koje moram koristiti: string, decimal, boolean

Program_name = "Bookstore"
Version = 13.1
Is_new_program = True

#list
books = ["Pepeljuga", "Crvenkapa"]
print(books)

print(books[1])

print(Program_name, Version, Is_new_program)

# DA promijenim prvu stavku iz liste i stavim ime "Pragmatic programmer"
# da izbrisem drugu

books[0] = "Pragmatic programmer"
print(books)

books.remove("Crvenkapa")
print(books)

