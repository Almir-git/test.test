

def hello_world():
    print("hello world")




def calculate_delivery(city):
    if city == "beograd" or city == "zagreb":
        print("Dostava je 500 din")
    elif city == "subotica":
        print("Dostava je 1200 din")
    elif city == "novi sad":
        print("Dostava je 700 din")
    elif city == "split":
        print("Dostava je 1300 din")
    else:
        print("Grad ne postoji")



calculate_delivery("Beograd")


def calculate(number1, number2):
    return number1+number2







