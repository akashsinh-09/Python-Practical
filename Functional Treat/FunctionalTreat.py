
print("Welcome to the Data Analyzer and Transformer Program!")

data = []
dataset_summary = {}


def display_menu():
    """Display the main menu and function documentation."""

    print("\n========== MAIN MENU ==========")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda)")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. User Defined Functions")
    print("8. Exit Program")
    print("===============================")

    # print("\nFunction Documentation:")
    # for function in [
    #     input_data,
    #     flatten_data,
    #     display_data_summary,
    #     calculate_average,
    #     find_unique,
    #     factorial,
    #     lambda_operations,
    #     sort_data,
    #     calculate_statistics
    # ]:
    #     print(function.__name__, ":", function.__doc__)


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
            display_data_grid()

        case "3":
            data = [34, 12, 56, 78, 43, 21, 90]

            print("\nSample Data Loaded Successfully!")
            print("Your Data:", data)

        case _:
            print("Invalid input type!")


def flatten_data():
    """Convert a 2D list into a 1D list."""

    if not data:
        return []

    if isinstance(data[0], list):
        numbers = []

        for row in data:
            for value in row:
                numbers.append(value)

        return numbers

    return data


def display_data_summary():
    """Display basic statistics using built-in functions."""

    numbers = flatten_data()

    if not numbers:
        print("\nPlease input data first!")
        return

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

    display_args(*numbers)

    display_kwargs(
        total_elements=total_elements,
        total_sum=total_sum,
        minimum=minimum,
        maximum=maximum,
        average=round(average, 2)
    )


def calculate_average(numbers):
    """Calculate the average of given numbers."""

    return sum(numbers) / len(numbers)


def find_unique(numbers):
    """Find unique numbers from the dataset."""

    unique = []

    for number in numbers:
        if number not in unique:
            unique.append(number)

    return unique


def udf_operations():
    """Perform operations using user-defined functions."""

    numbers = flatten_data()

    if not numbers:
        print("\nPlease input data first!")
        return

    print("\n========== UDF OPERATIONS ==========")
    print("1. Calculate Average")
    print("2. Find Unique Numbers")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            average = calculate_average(numbers)
            print("\nAverage:", round(average, 2))

        case "2":
            unique = find_unique(numbers)
            print("\nUnique Numbers:", unique)

        case _:
            print("Invalid choice!")


def factorial(number):
    """Calculate factorial using recursion."""

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


def factorial_operation():
    """Take user input and display factorial."""

    number = int(input("Enter a number: "))

    if number < 0:
        print("Factorial is not defined for negative numbers!")
    else:
        result = factorial(number)
        print(f"Factorial of {number} is: {result}")


def lambda_operations():
    """Perform data transformations using lambda, map and filter."""

    numbers = flatten_data()

    if not numbers:
        print("Please input data first!")
        return

    print("\n========== LAMBDA OPERATIONS ==========")
    print("1. Filter Values Above Threshold")
    print("2. Filter Values Below Threshold")
    print("3. Square All Values using map()")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            threshold = int(input("Enter threshold value: "))

            result = list(filter(
                lambda x: x >= threshold, numbers
            ))

            print("Values above or equal to threshold:", result)

        case "2":
            threshold = int(input("Enter threshold value: "))

            result = list(filter(
                lambda x: x <= threshold, numbers
            ))

            print("Values below or equal to threshold:", result)

        case "3":
            result = list(map(
                lambda x: x ** 2, numbers
            ))

            print("Squared Values:", result)

        case _:
            print("Invalid choice!")


def display_args(*numbers):
    """Accept and display multiple values using *args."""

    print("\nValues received using *args:")

    for number in numbers:
        print(number)


def display_kwargs(**details):
    """Display dataset information using **kwargs."""

    print("\nDataset Summary using **kwargs:")

    for key, value in details.items():
        print(key, ":", value)


def calculate_statistics(numbers):
    """Return minimum, maximum, sum and average."""

    minimum = min(numbers)
    maximum = max(numbers)
    total = sum(numbers)
    average = total / len(numbers)

    return minimum, maximum, total, average


def display_dataset_statistics():
    """Calculate and display dataset statistics using global keyword."""

    global dataset_summary

    numbers = flatten_data()

    if not numbers:
        print("Please input data first!")
        return

    minimum, maximum, total, average = calculate_statistics(numbers)

    dataset_summary = {
        "Total Elements": len(numbers),
        "Minimum": minimum,
        "Maximum": maximum,
        "Sum": total,
        "Average": round(average, 2)
    }

    print("\n========== DATASET STATISTICS ==========")

    for key, value in dataset_summary.items():
        print(key, ":", value)


def sort_data():
    """Sort 1D and 2D list data."""

    if not data:
        print("Please input data first!")
        return

    print("\n========== SORT DATA ==========")
    print("1. Sort in Ascending Order")
    print("2. Sort in Descending Order")
    print("3. Sort 2D Rows using sorted()")

    choice = input("Enter your choice: ")

    match choice:

        case "1":
            if isinstance(data[0], list):
                print("This option is for 1D data.")
                return

            data.sort()
            print("Ascending Order:", data)

        case "2":
            if isinstance(data[0], list):
                print("This option is for 1D data.")
                return

            data.sort(reverse=True)
            print("Descending Order:", data)

        case "3":
            if not isinstance(data[0], list):
                print("Please enter 2D data first!")
                return

            sorted_data = sorted(data, key=sum)

            print("\nOriginal 2D Data:")

            for row in data:
                print(row)

            print("\nSorted 2D Data (by row sum):")

            for row in sorted_data:
                print(row)

            print("\nOriginal data remains unchanged!")

        case _:
            print("Invalid choice!")


def display_data_grid():
    """Display 2D list in a formatted grid."""

    if not data:
        print("No data available!")
        return

    if not isinstance(data[0], list):
        print("Current data is a 1D list:")
        print(data)
        return

    print("\n========== 2D DATA GRID ==========")

    for row in data:
        for value in row:
            print(f"{value:8}", end="")

        print()


while True:

    display_menu()

    choice = input("\nPlease enter your choice (1-8): ")

    match choice:

        case "1":
            input_data()

        case "2":
            display_data_summary()

        case "3":
            factorial_operation()

        case "4":
            lambda_operations()

        case "5":
            sort_data()

        case "6":
            display_dataset_statistics()

        case "7":
            udf_operations()

        case "8":
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("Invalid choice! Please enter a number between 1 and 8.")
