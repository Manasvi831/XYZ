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
