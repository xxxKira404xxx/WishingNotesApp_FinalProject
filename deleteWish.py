from viewWishes import viewWishes

def deleteWish(wishes):
    """Deletes wishes from the list - supports deleting by number, random, or clearing all."""
    # Check if wish list is empty
    if not wishes: 
        print("\nNo wishes to delete.")
        return

    viewWishes(wishes)

    print("Options:")
    print(" [Number]  Delete specific wish")
    print(" [C]       Clear all wishes")
    print(" [R]       Delete a RANDOM wish")

    # Handle user choice
    while True: 
        userInput = input("\nChoice: ").strip() 

        # Clear all wishes
        if userInput.upper() == 'C':
            confirm = input("Are you sure you want to CLEAR ALL? (y/n): ").strip().lower()
            if confirm == 'y':
                wishes.clear()
                print("\nWish list cleared!")
                return
            else:
                print("Action cancelled.")
                return

        # Delete random wish
        elif userInput.upper() == 'R':
            import random
            random_wish = random.choice(wishes)
            wishName = random_wish[0][1]
            confirm = input(f"Delete random wish '{wishName}'? (y/n): ").strip().lower()
            if confirm == 'y':
                wishes.remove(random_wish)
                print(f"Randomly removed '{wishName}'.")
                return
            else:
                return

        # Delete specific wish by number
        elif userInput.isdigit(): 
            index = int(userInput) - 1 

            if 0 <= index < len(wishes): 
                wishName = wishes[index][0][1] 

                while True:
                    confirm = input(f"Delete '{wishName}'? (y/n): ").strip().lower() 
                    if confirm == 'y':
                        removed_item = wishes.pop(index) 
                        print(f"\n✓ \"{removed_item[0][1].title()}\" was removed from the wish list.")
                        return
                    elif confirm == 'n':
                        print("Deletion cancelled.")
                        return  
                    else:
                        print("Invalid input.")
            else:
                print("Number out of range.")
        else:
            print("Invalid input. Enter a number, 'C', or 'R'.")
