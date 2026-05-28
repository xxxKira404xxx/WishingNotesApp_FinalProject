from viewWishes import viewWishes
import random
def deleteWish(wishes):
    """Deletes wishes from the list - supports deleting by number, random, or clearing all."""
    # Check if wish list is empty
    if not wishes: 
        print("\nNo wishes to delete.")
        return

    viewWishes(wishes) # Display all wishes to let user choose which one to delete

    print("\nOptions:")
    print(" [Number]  Delete specific wish")
    print(" [C]       Clear all wishes")
    print(" [R]       Delete a RANDOM wish")
    print(" [B]       Go Back")

    # Handle user choice
    while True: 
        userInput = input("\nChoice: ").strip().upper() 

        # Go back to main menu
        if userInput == 'B':
            return

        # Clear all wishes
        elif userInput == 'C':
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
            randomWish = random.choice(wishes)
            wishName = randomWish[0][1]
            confirm = input(f"Delete random wish '{wishName}'? (y/n): ").strip().lower()
            if confirm == 'y':
                wishes.remove(randomWish)
                print(f"Randomly removed '{wishName}'.")
                return
            else:
                return

        # Delete specific wish by number
        elif userInput.isdigit(): 
            index = int(userInput) - 1 

            if 0 <= index < len(wishes):  # Valid index check
                wishName = wishes[index][0][1] 

                while True:
                    confirm = input(f"Delete '{wishName}'? (y/n): ").strip().lower() 
                    if confirm == 'y':
                        removedItem = wishes.pop(index) # Remove the wish from the list and store it in removedItem for confirmation message
                        print(f"\n✓ \"{removedItem[0][1].title()}\" was removed from the wish list.")
                        return
                    elif confirm == 'n':
                        print("Deletion cancelled.")
                        return  
                    else:
                        print("Invalid input.")
            else:
                print("Number out of range.")
        else:
            print("Invalid input. Enter a number, 'C', 'R', or 'B'.")
