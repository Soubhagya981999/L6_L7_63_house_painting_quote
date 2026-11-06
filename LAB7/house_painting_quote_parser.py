def clean_colour_name(name):
    """Convert a valid colour name into a lowercase code."""
    if not isinstance(name, str):
        raise ValueError("Colour name must be text.")

    name = name.strip()

    if not name:
        raise ValueError("Colour name cannot be empty.")

    return name.lower().replace(' ', '_')


def room_area(text):
    """Calculate room area using LENGTHxWIDTH."""
    if not isinstance(text, str):
        raise ValueError("Room dimensions must be text.")

    parts = text.lower().strip().split('x')

    if len(parts) != 2:
        raise ValueError("Enter dimensions in LENGTHxWIDTH format.")

    try:
        length = int(parts[0].strip())
        width = int(parts[1].strip())
    except ValueError:
        raise ValueError("Dimensions must be whole numbers.")

    if length <= 0 or width <= 0:
        raise ValueError("Dimensions must be positive numbers.")

    return length * width


def total_wall_area(text):
    """Calculate total wall area from semicolon-separated values."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Wall areas cannot be empty.")

    parts = text.split(';')

    try:
        areas = [int(area.strip()) for area in parts]
    except ValueError:
        raise ValueError("All wall areas must be whole numbers.")

    if any(area <= 0 for area in areas):
        raise ValueError("Wall areas must be positive numbers.")

    return sum(areas)


def main():
    print("==== Running clean_colour_name ====")
    value = input("Enter a paint colour name (e.g. Ocean Blue): ")
    print("Colour code:", clean_colour_name(value))

    print("\n==== Running room_area ====")
    value = input("Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): ")
    print("Room area (sq ft):", room_area(value))

    print("\n==== Running total_wall_area ====")
    value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
    print("Total wall area (sq ft):", total_wall_area(value))


if __name__ == "__main__":
    main()