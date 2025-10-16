def sort(width, height, length, mass):
    volume = width * height * length
    
    bulky = volume >= 1000000 or max(width, height, length) >= 150
    heavy = mass >= 20
    
    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"
    else:
        return "STANDARD"


def main():
    done = False

    while not done:
        try:
            width, height, length, mass = map(int, input("Enter width, height, length, and mass separated by spaces: ").split())
            if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
                raise ValueError
            category = sort(width, height, length, mass)
            print(category)
            done = True
        except ValueError:
            print("Invalid input. Please enter four positive integers separated by spaces.")

if __name__ == "__main__":
    main()