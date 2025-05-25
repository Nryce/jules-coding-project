# main.py
def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit.

    Args:
        celsius: Temperature in Celsius.

    Returns:
        Temperature in Fahrenheit.
    """
    return (celsius * 9/5) + 32

import argparse

def main():
    parser = argparse.ArgumentParser(description="Convert Celsius to Fahrenheit.")
    parser.add_argument("--celsius", type=float, help="Celsius temperature to convert")
    args = parser.parse_args()

    if args.celsius is not None:
        fahrenheit = celsius_to_fahrenheit(args.celsius)
        print(f"{args.celsius}°C is {fahrenheit}°F")
    else:
        print("Unit Converter - Ready to convert!")

if __name__ == "__main__":
    main()
