import os

def saveWishes(wishes, filename="Logged_Wishes.txt"):
    """
    Saves wishes in a 'Table' format. This looks organized in Notepad
    but still uses pipes '|' so the code can split the data easily.
    """
    # Write wishes to file in table format with header and rows
    totalPrice = 0
    with open(filename, "w", encoding="utf-8") as file:
        # Write Header
        header = f"{'ITEM NAME':<20} | {'PRICE':<10} | {'CATEGORY':<12} | {'ID':<6} | {'LINK':<50} | {'NOTES'}\n"
        file.write(header)
        file.write("=" * 140 + "\n")

        for wish in wishes:
        # Extract details from wish structure
            name    = wish[0][1]
            link    = wish[1][1]
            price   = float(wish[2][1]) # Ensure float for formatting
            notes   = wish[3][1]
            wish_id = wish[4][1]
            category = wish[5][1]

            # Write Row
            line = f"{name:<20} | {price:<10.2f} | {category:<12} | {wish_id:<6} | {link:<50} | {notes}\n"
            file.write(line)
            
            totalPrice += price
            
    print(f"\n✓ {len(wishes)} wish(es) saved to {filename}.")
    print(f"  Total Value: ₱{totalPrice:,.2f}")

def loadWishes(filename="Logged_Wishes.txt"):
    """
    Loads wishes from the table-formatted file. 
    """
    # Read file and parse wishes from table format
    if not os.path.exists(filename): # If file doesn't exist, return empty list
        return []

    wishes = []    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Skip non-data lines
            if "|" not in line or "ITEM NAME" in line or "===" in line:
                continue

            data = line.split("|")            

            if len(data) == 6:
                # Convert price to float safely
                try:
                    priceVal = float(data[1].strip())
                except ValueError:
                    priceVal = 0.0

                wish = [
                    ["name",  data[0].strip()], # Column 0
                    ["link",  data[4].strip()], # Column 4
                    ["price", priceVal],       # Column 1
                    ["notes", data[5].strip()], # Column 5
                    ["id",    data[3].strip()], # Column 3
                    ["category",   data[2].strip()]  # Column 2
                ]

                wishes.append(wish)
    
    return wishes
