# A refactored example of a program in Python to sum user-provided integers.

MAX = 100

def calculate_sum(arr):
    """Calculate the sum of a list of integers."""
    return sum(arr)

def get_number_of_elements():
    """Prompt the user for the number of elements to sum."""
    while True:
        try:
            n = int(input("Enter the number of elements (1-100): "))
            if 1 <= n <= MAX:
                return n
            else:
                print("Invalid input. Please provide a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to input `n` integers."""
    arr = []
    print(f"Enter {n} integers:")
    for _ in range(n):
        while True:
            try:
                arr.append(int(input()))
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return arr

def main():
    try:
        n = get_number_of_elements()
        arr = get_elements(n)
        total = calculate_sum(arr)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()