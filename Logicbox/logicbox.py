print("Welcome to Pattern Generator and Number Analyzer!\n")

while True:
    print("Please select an option:")
    print("1. Generate Pattern")
    print("2. Analyze Number")
    print("3. Exit\n")

    choice = int(input("Enter your choice (1/2/3):"))

    match choice:
        case 1:
            print("1.Square Pattern")
            print("2.Triangle Pattern")
            print("3.Same Number Pattern")
            print("4.Continue Pattern")
            print("5.Pyramid Pattern\n")
            
            choice_pattern = int(input("Enter your choice of pattern (1/2/3/4/5): "))
            rows = int(input("Enter the number of rows for the pattern: "))
            print("Pattern:\n")
            
            match choice_pattern:
                case 1:
                    for i in range(rows):
                        print("* " * rows)  
                case 2:
                    for i in range(1, rows + 1):
                        print("* " * i)
                case 3:
                    for i in range(1, rows + 1):
                        print(str(i) * i)
                case 4:
                    for i in range(1, rows + 1):
                        print(" ".join(str(j) for j in range(1, i + 1)))
                case 5:
                    for i in range(1, rows + 1):
                        print(" " * (rows - i) + "* " * i)
                case _:
                    print("Invalid pattern choice.")
        case 2:
            start = int(input("\nEnter the start of the range: "))
            end = int(input("Enter the end of the range: "))
            for num in range(start, end + 1):
                print(f"{num} is even." if num % 2 == 0 else f"{num} is odd.")
            
        case 3:
            break
        case _:
            print("Invalid choice. Please select a valid option.")
print("Thank you for using the Pattern Generator and Number Analyzer!")
    