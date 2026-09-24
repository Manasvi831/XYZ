"""A simple script to display a motivational 'Keep Calm' message."""

def create_calm_message(action_text: str) -> str:
    """Format and return a clear motivational message."""
    return f"KEEP CALM AND {action_text.upper()}"


def main() -> None:
    """Run the main program logic."""
    target_action = "CLEAR"
    message = create_calm_message(target_action)
    print(message)


if __name__ == "__main__":
    main()
    
    #xyz# Take input from the user and convert it to integers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Calculate the sum
result = num1 + num2

# Print the result using an f-string
print(f"The sum of {num1} and {num2} is: {result}")

