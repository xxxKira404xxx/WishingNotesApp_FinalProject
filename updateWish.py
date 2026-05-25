from viewWishes import viewWishes
from addWish import suggestCategory
from inputUtils import get_item_name, get_item_link, get_item_price, get_item_notes

def updateWish(wishes):
    """Updates an existing wish with new name, link, price, notes, and category."""
    # Check if wish list is empty
    if not wishes:
        print("\nNo wishes to update.")
        return

    viewWishes(wishes)

    # Get wish index from user
    while True:
        userInput = input("Enter the number of the wish to update: ").strip()

        if userInput.isdigit():
            index = int(userInput) - 1

            if 0 <= index < len(wishes):
                wish = wishes[index]
                print(f"\nEditing: {wish[0][1]}")

                itemName = get_item_name()

                # Duplicate check: Must check against OTHER items only
                for i, w in enumerate(wishes):
                    if w[0][1].lower() == itemName.lower() and i != index:
                        while True:
                            overwriteItem = input(f"'{itemName}' already exists. Overwrite? (y/n): ").strip().lower() 
                            if overwriteItem == 'y':
                                wishes.pop(i) 
                                # if a duplicate item was removed from earlier in the list
                                if i < index:
                                    index -= 1
                                break
                            elif overwriteItem == 'n':
                                print("Wish not updated.")
                                return
                            else:
                                print("Invalid input.")
                        break

                link = get_item_link()
                price = get_item_price()
                notes = get_item_notes()

                # Update Category based on new info
                suggested_category = suggestCategory(itemName, notes)

                # Save all updated values back to the nested list
                wishes[index][0] = ["name",  itemName]
                wishes[index][1] = ["link",  link]
                wishes[index][2] = ["price", price]
                wishes[index][3] = ["notes", notes]
                wishes[index][5] = ["cat",   suggested_category]

                # Confirm update success
                print(f"\n✓ \"{wish[0][1]}\" updated successfully!")
                print(f"  Category: {suggested_category} | Price: ₱{price:,.2f}")
                return
            
            else:
                print("Number out of range.")
        else:
            print("Invalid input. Enter a number.")
