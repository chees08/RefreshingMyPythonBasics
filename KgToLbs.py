while True: 
 choice = input("Choice (Kg, Lbs): ")

 if choice in ('Kg', 'Lbs'):
        weight = input("Weight: " )

        if choice == 'Kg':
            total = float(weight) * 2.20462262
            print(weight , choice , "=" , total, "Lbs")

        elif choice == 'Lbs':
         total = float(weight) / 2.20462262
         print(weight , choice , "=" , total, "Kg")

         next_calculation = input("Let's do next calculation? (yes/no): ")
         if next_calculation == "no":
          break
    
        else:
            print("Invalid Input")
