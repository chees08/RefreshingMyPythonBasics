
while True: 
    choice = input("Choice (add, sub): ")

    if choice in ('add', 'sub'):
        number1 = float(input("First number: " ))
        number2 = float(input("Second Number: " ))

        if choice == 'add':
            total = number1 + number2
            print(number1 , choice , number2, "=" , total)

        elif choice == 'sub':
            total = number1 - number2
            print(total)

    if total == 69.0:
        print("what are u smiling to?")
    else:
     print("")

    next_calculation = input("Let's do next calculation? (yes/no): ")
    if next_calculation == "no":
      break
    
    else:
     print("Invalid Input")