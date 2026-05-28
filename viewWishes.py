import os

def viewWishes(wishes, setBudgetCheck=False):
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
        priceFloat = wish[2][1]
        total += priceFloat 

        # Truncate link if too long for better display
        if len(link) > 50:
            link = link[:50] + "..."

        print(f"  [{i}] {name.upper()}") 
        print(f"       ID    : {wish[4][1]} ")
        print(f"       Cat   : {wish[5][1]} ")
        print(f"       Link  : {link} ")
        print(f"       Price : ₱{priceFloat:.2f}") 
        print(f"       Notes : {wish[3][1]}")
        print("══" * 60)

    # Display summary footer
    print(f"       Total wishes : {len(wishes)}")
    print(f"  Total price (all) : ₱{total:.2f}")  
    print("══" * 60)

    if setBudgetCheck: # If budget check is enabled, ask user for budget and show affordable items
        while True: 
            budgetInput = input("  What is your current budget?: ₱").strip()
        
            if budgetInput.replace(".", "", 1).isdigit():
                budget = float(budgetInput)
                print("══" * 60)
                
                affordableCount = 0
                print(f"  ✓ AFFORDABLE ITEMS (Budget: ₱{budget:.2f}):")
                
                for wish in wishes: # Check each wish against the user's budget
                    itemPrice = wish[2][1]

                    if itemPrice <= budget:
                        print(f"    - {wish[0][1].title()} (₱{itemPrice:.2f})")
                        affordableCount += 1
                
                # If no items are affordable, show a message
                if affordableCount == 0:
                    print("    (None - All items are above your budget)")
                
                # Final budget summary
                if budget >= total:
                    print(f"\n  ★ GREAT NEWS: You can buy everything! ★")
                else:
                    shortage = total - budget
                    print(f"\n  ! TARGET: You need ₱{shortage:.2f} more to buy everything.")
                
                print("══" * 60)
                break
            else:
                print("\n  Invalid budget. Please enter a valid number.")
    
    input("\nPress Enter to continue...")
