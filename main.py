def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the correct dispatch stack for a package based on its size and mass.
    
    Args:
        width (float): Width of the package in cm.
        height (float): Height of the package in cm.
        length (float): Length of the package in cm.
        mass (float): Mass of the package in kg.
    
    Returns:
        str: One of "STANDARD", "SPECIAL", or "REJECTED".
    """
    if any(x <= 0 for x in (width, height, length, mass)):
        raise ValueError("All values must be positive numbers.")
    
    volume = width * height * length

    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def main():
    while True:
        try:
            user_input = input("Enter width, height, length, and mass separated by commas: ").strip()
            width, height, length, mass = map(float, user_input.split(","))
            category = sort(width, height, length, mass)
            print(f"Package category: {category}")
            break

        except ValueError as e:
            print(f"Invalid input ({e}). Please enter four positive numbers separated by commas.")
        except Exception as e:
            print(f"Unexpected error: {e}")
            break


if __name__ == "__main__":
    main()
