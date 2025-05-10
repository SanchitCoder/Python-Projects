# UNIT CONVERTER TOOL IN PYTHON

# Step 1: Define the conversion functions for different unit types

# Length conversion: meters <-> kilometers, miles, centimeters
def convert_length(value, from_unit, to_unit):
    length_units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "mile": 1609.34,
        "inch": 0.0254,
        "foot": 0.3048
    }

    # Convert from source unit to meters
    value_in_meters = value * length_units[from_unit]

    # Convert from meters to target unit
    return value_in_meters / length_units[to_unit]


# Weight conversion: grams <-> kilograms, pounds, ounces
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "gram": 1,
        "kilogram": 1000,
        "pound": 453.592,
        "ounce": 28.3495
    }

    # Convert from source unit to grams
    value_in_grams = value * weight_units[from_unit]

    # Convert from grams to target unit
    return value_in_grams / weight_units[to_unit]


# Temperature conversion: Celsius <-> Fahrenheit, Kelvin
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value

    # Convert to Celsius first
    if from_unit == "fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "kelvin":
        value = value - 273.15

    # Convert from Celsius to desired unit
    if to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "kelvin":
        return value + 273.15
    else:
        return value  # celsius


# Step 2: Build the main user interface logic using a loop
def main():
    print("Welcome to the Python Unit Converter Tool!")

    while True:
        print("\nSelect conversion type:")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            print("\nAvailable units: meter, kilometer, centimeter, mile, inch, foot")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter value: "))
            result = convert_length(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")

        elif choice == "2":
            print("\nAvailable units: gram, kilogram, pound, ounce")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter value: "))
            result = convert_weight(value, from_unit, to_unit)
            print(f"{value} {from_unit} = {result:.4f} {to_unit}")

        elif choice == "3":
            print("\nAvailable units: celsius, fahrenheit, kelvin")
            from_unit = input("Convert from: ").lower()
            to_unit = input("Convert to: ").lower()
            value = float(input("Enter temperature value: "))
            result = convert_temperature(value, from_unit, to_unit)
            print(f"{value}° {from_unit.capitalize()} = {result:.2f}° {to_unit.capitalize()}")

        elif choice == "4":
            print("Thank you for using the Unit Converter Tool. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

# Step 3: Run the app
if __name__ == "__main__":
    main()
