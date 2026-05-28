from viewWishes import viewWishes
from addWish import suggestCategory
from inputUtils import getItemName, getItemLink, getItemPrice, getItemNotes

def updateWish(wishes):
    """Updates an existing wish with new name, link, price, notes, and category."""
    # Check if wish list is empty
    if not wishes:
        print("\nNo wishes to update.")
        return

    viewWishes(wishes) # Display all wishes to let user choose which one to update

    while True: # Ask user if they want to update a wish or cancel
        userConfirmation = input("\nUpdate a wish? (y/n): ").strip().upper()
        if userConfirmation == 'N' :
            print("Update cancelled.")
            return
        elif userConfirmation == 'Y':
            break
        else:
            print("Invalid input. Please enter 'Y' to update, 'N' to cancel.")

    while True: # Ask user which wish to update by number with validation 
        userInput = input("Enter the number of the wish to update: ").strip()

        if userInput.isdigit():
            index = int(userInput) - 1

            if 0 <= index < len(wishes):
                wish = wishes[index]
                print(f"\nEditing Item: {wish[0][1]}")

                while True: # Get new item name with duplicate check against other items in the list
                    itemName = getItemName()

                    is_duplicate = False
                    for i, w in enumerate(wishes):
                        if w[0][1].lower() == itemName.lower() and i != index:
                            print(f"  ! '{itemName}' is already in your wish list.")
                            is_duplicate = True
                            break
                    
                    if not is_duplicate:
                        break
                    
                    while True: # Ask user if they want to try a different name or cancel the update
                        retry = input("  Try a different name? (y/n): ").strip().upper()
                        if retry == 'Y':
                            break
                        if retry == 'N':
                            print("Update cancelled.")
                            return

                link = getItemLink()
                price = getItemPrice()
                notes = getItemNotes()

                # Update Category based on new info
                suggestedCategory = suggestCategory(itemName, notes, link)

                # Save all updated values back to the nested list
                wishes[index][0] = ["name",  itemName]
                wishes[index][1] = ["link",  link]
                wishes[index][2] = ["price", price]
                wishes[index][3] = ["notes", notes]
                wishes[index][5] = ["category",   suggestedCategory]

                # Confirm update success
                print(f"\n✓ \"{itemName}\" updated successfully!")
                print(f"  Category: {suggestedCategory} | Price: ₱{price:,.2f}")
                return
            
            else:
                print("Number out of range.")
        else:
            print("Invalid input. Enter a number.")
