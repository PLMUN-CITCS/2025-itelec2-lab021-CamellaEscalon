def get_non_negative_integer() -> int:
    """
    Prompts the user to input a non-negative integer and ensures the input is valid.
    
    Returns:
        int: A non-negative integer entered by the user.
    """
    while True:
        try:
            # Prompt the user to input a non-negative integer
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Please enter a non-negative integer.")
            else:
                return number  # Return the valid input
        except ValueError:
            # Handle the case where input is not a valid integer
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.
    
    Args:
        n (int): The non-negative integer for which the factorial is calculated.
    
    Returns:
        int: The factorial of the given number.
    """
    # Base case: factorial of 0 is 1
    if n == 0:
        return 1
    
    factorial = 1
    # Calculate factorial using an iterative approach
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial

def main():
    """
    Main function that orchestrates the flow of the program.
    Gets the user input, calculates the factorial, and displays the result.
    """
    # Get valid non-negative integer input from the user
    number = get_non_negative_integer()
    
    # Calculate the factorial of the input number
    result = calculate_factorial(number)
    
    # Display the result
    print(f"The factorial of {number} is: {result}")

# Ensure the script runs when executed directly
if __name__ == "__main__":
    main()