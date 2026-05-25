import os

def saveWishes(wishes, filename="Logged_Wishes.txt"):
    """
    Saves wishes in a 'Table' format. This looks organized in Notepad
    but still uses pipes '|' so the code can split the data easily.
    """
    # Write wishes to file in table format with header and rows
    total_price = 0
    with open(filename, "w", encoding="utf-8") as file:
        # 1. Write Header
        header = f"{'ITEM NAME':<20} | {'PRICE':<10} | {'CATEGORY':<12} | {'ID':<6} | {'LINK':<100} | {'NOTES'}\n"
        file.write(header)
        file.write("=" * 120 + "\n")

        for wish in wishes:
            
            name    = wish[0][1]
            link    = wish[1][1]
            price   = wish[2][1]
            notes   = wish[3][1]
            wish_id = wish[4][1]
            cat     = wish[5][1]

            # Write Row
            line = f"{name:<20} | {price:<10} | {cat:<12} | {wish_id:<6} | {link:<30} | {notes}\n"
            file.write(line)
            
            if isinstance(price, (int, float)):
                total_price += price
            elif str(price).replace(".", "", 1).isdigit():
                total_price += float(price)
            
    print(f"\n✓ {len(wishes)} wish(es) saved to {filename}.")
    print(f"  Total Value: ₱{total_price:,.2f}")

def loadWishes(filename="Logged_Wishes.txt"):
    """
    Loads wishes from the table-formatted file. 
    """
    # Read file and parse wishes from table format
    if not os.path.exists(filename):
        return []

    wishes = []    
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            # Skip non-data lines
            if "|" not in line or "ITEM NAME" in line or "===" in line:
                continue

            data = line.split("|")            

            if len(data) == 6:
                
                wish = [
                    ["name",  data[0].strip()], # Column 0
                    ["link",  data[4].strip()], # Column 4
                    ["price", data[1].strip()], # Column 1
                    ["notes", data[5].strip()], # Column 5
                    ["id",    data[3].strip()], # Column 3
                    ["cat",   data[2].strip()]  # Column 2
                ]
                wishes.append(wish)
    
    return wishes
