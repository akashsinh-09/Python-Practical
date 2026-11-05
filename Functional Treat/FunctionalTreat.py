
print("Welcome to the Data Analyzer and Transformer Program!")

data = []


def display_menu():
    """Display the main menu of the program."""

    print("\n========== MAIN MENU ==========")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    print("===============================")


def input_data():
    """Accept data from the user as a 1D or 2D list."""

    global data

    print("\nChoose Data Input Type:")
    print("1. One-Dimensional List (1D)")
    print("2. Two-Dimensional List (2D)")
    print("3. Use Sample Data")

    option = input("Enter your choice: ")

    match option:

        case "1":

            values = input("Enter numbers separated by spaces: ")

            data = list(map(int, values.split()))

            print("\n1D Data stored successfully!")
            print("Your Data:", data)

        case "2":

            rows = int(input("Enter number of rows: "))
            columns = int(input("Enter number of columns: "))

            data = []

            for i in range(rows):

                row = []

                for j in range(columns):

                    value = int(input(f"Enter value [{i}][{j}]: "))

                    row.append(value)

                data.append(row)

            print("\n2D Data stored successfully!")

            for row in data:
                print(row)

        case "3":

            data = [34, 12, 56, 78, 43, 21, 90]

            print("\nSample Data Loaded Successfully!")
            print("Your Data:", data)

        case _:
            print("Invalid input type!")

def display_data_summary():
    """Display basic statistics using built-in functions."""

    if not data:
        print("\nPlease input data first!")
        return
    
    numbers = []

    if isinstance(data[0], list):

        for row in data:
            for value in row:
                numbers.append(value)

    else:
        numbers = data

    total_elements = len(numbers)
    total_sum = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total_sum / total_elements

    print("\n========== DATA SUMMARY ==========")
    print("Total Elements:", total_elements)
    print("Sum of Values:", total_sum)
    print("Minimum Value:", minimum)
    print("Maximum Value:", maximum)
    print("Average Value:", round(average, 2))
    print("==================================")

while True:

    display_menu()

    choice = input("Please enter your choice (1-7): ")

    match choice:

        case "1":
            input_data()

        case "2":
            display_data_summary()
