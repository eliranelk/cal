import time

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("0, is not devised")
    else:
        return num1 / num2

def modulos(num1, num2):
    return num1 % num2

while True:
    try:
        while True:
            time.sleep(2)
            print("\nwhich number do you choose ? ")
            print("1. add")
            print("2. subtract")
            print("3. multiply")
            print("4. divide")
            print("5. modulos")

            choice = input("\nEnter your choice:")

            if choice == '1' :
                print("you have chosen the add")
            elif choice == '2' :
                print("you have chosen the subtract")
            elif choice == '3':
                print("you have chosen the multiply")
            elif choice == '4':
                print("you have chosen the divide")
            elif choice == '5':
                print("you have chosen the modulos")
            else:
                print("please choose a choice between 1-5")
                break
            try:
                num1 = float(input("\nEnter your first number: "))
                num2 = float(input("Enter your second number: "))
                break
            except ValueError:
                print("please enter a numbers")
                continue

        if choice == '1':
            print(num1, "+",num2 , "=", add, (num1, num2))
        elif choice == '2':
            print(num1, "-",num2 , "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*",num2 , "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/",num2 , "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "%",num2 , "=", modulos(num1, num2))
        else:
            print("choice invalide!!!")
        continue
    except KeyboardInterrupt:
        print("\nbye bye")
        break