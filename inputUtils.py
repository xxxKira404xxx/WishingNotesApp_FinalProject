def getItemName():
    """Gets and validates item name input (alphanumeric only)."""
    # Validate that name is not empty and contains only alphanumeric characters
    while True:
        rawName = input("Item name       : ").strip()
        if not rawName:
            print("\nItem name cannot be empty.")
            continue
        if not rawName.replace(" ", "").isalnum():
            print("Invalid characters in item name.")
            continue
        return rawName.title()
    

def getItemLink():
    """Gets and validates item link (must start with http:// or https://)."""
    # Ensure link starts with http or https
    while True:
        link = input("Item Link (http/https) : ").strip()
        if link.startswith(("http://", "https://")):
            return link
        else:
            print("(Note: Link must start with http/https)")

def getItemPrice():
    """Gets and validates price input (must be a valid number)."""
    # Check that price is a valid numeric value
    while True:
        price = input("Item Price ₱: ").strip()
        if price.replace(".", "", 1).isdigit():
            return float(price)
        else:
            print(f"Invalid price. Expected a number, got '{price}'.")

def getItemNotes():
    # Ensure notes field is not empty
    """Gets and validates notes/description input (cannot be empty)."""
    while True:
        notes = input("Item Notes (Description/Purpose): ").strip()
        if not notes:
            print("Notes cannot be empty.")
            continue
        elif "|" in notes:
            print("Notes cannot contain the '|' character.")
            continue
        return notes.capitalize()
