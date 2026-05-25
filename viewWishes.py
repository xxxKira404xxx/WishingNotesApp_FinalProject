import os

def viewWishes(wishes):
    """Displays all wishes in a formatted table with item details and total price."""
    # Clear screen and display all wishes with their details
    os.system('cls' if os.name == 'nt' else 'clear')

    # Check if wish list is empty
    if not wishes:
        print("\nNo wishes yet. Add one!".upper())
        return

    # Display header with item count
    header = f"★ WISH LIST ({len(wishes)} item/s) ★".upper()
    print(f"\n{header}")
    print("══" * 60)


    total = 0 
    for i, wish in enumerate(wishes, start=1): 
        name = wish[0][1]
        link = wish[1][1]
        
        raw_price = str(wish[2][1]).strip()
        if raw_price.replace(".", "", 1).isdigit():
            price_float = float(raw_price)
            total += price_float 
        else:
            price_float = 0.0

        # Truncate link if too long for better display
        if len(link) > 50:
            link = link[:50] + "..."

        print(f"  [{i}] {name.upper()}") 
        print(f"       ID    : {wish[4][1]} ")
        print(f"       Cat   : {wish[5][1]} ")
        print(f"       Link  : {link} ")
        print(f"       Price : ₱{price_float:.2f}") 
        print(f"       Notes : {wish[3][1]}")
        print("══" * 60)

    # Display summary footer
    print(f"       Total wishes : {len(wishes)}")
    print(f"  Total price (all) : ₱{total:.2f}")  
    print("══" * 60)
    input("\nPress Enter to continue...")
