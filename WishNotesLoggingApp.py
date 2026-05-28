"""
Wish Notes Logging App (Group 7)

This program allows users to manage a wish list of items.
Users can add wishes with name, link, price, and notes;
view all wishes; and delete wishes with confirmation.

Features:
- Modularized structure
- Duplicate name handling (Fixed iteration bug)
- Improved input validation (Decimal price support)
- Confirmation for deletions
- Nested list-based data structure (as requested)

Developer: [Bandong, John Matthew C.]
Documentation: [Orpilla Sean Aldrin B. , Santillan Mike Angel, Palig-Ad Althea Nicole ]
Date: [5/8/2026]
"""

# Import all modules
import os
from displayMenu import displayMenu
from addWish import addWish
from viewWishes import viewWishes
from deleteWish import deleteWish
from updateWish import updateWish
from fileHandler import saveWishes, loadWishes

def clearScreen():
    """Uses os.system and os.name to clear the terminal."""
    # Clear console based on operating system
    os.system('cls' if os.name == 'nt' else 'clear')

def main(): 
    """Main application loop - handles user menu choices."""
    # Load wishes, display menu, and route user input to appropriate functions
    clearScreen()
    wishes = loadWishes()  # Load existing wishes from file

    while True:
        displayMenu()  # Show menu options
        choice = input("Choose an option: ").strip() 
        
        # Route user choice to appropriate function
        if choice == "1": 
            addWish(wishes) # Access addWish function to add new wishes to the list
        elif choice == "2": 
            viewWishes(wishes, setBudgetCheck=False)  # Access viewWishes function to display all wishes in a formatted table
            
            if wishes:
                while True:
                    runCheck = input("  Run a budget check? (y/n): ").strip().upper() # Ask user if they want to run budget check after viewing wishes
                    if runCheck == 'Y':
                        viewWishes(wishes, setBudgetCheck=True) # Run viewWishes again with budget check enabled to allow user to input budget and see affordable items
                        break
                    elif runCheck == 'N':
                        break
                    else:
                        print("  Invalid input. Please enter 'Y', 'N'.")

        elif choice == "3":
            updateWish(wishes) # Access updateWish function to update existing wishes in the list
        elif choice == "4": 
            deleteWish(wishes) # Access deleteWish function to delete wishes from the list
        elif choice == "5": 
            saveWishes(wishes) # Save wishes to file before exiting
            break         
        else:
            print("Invalid option. Choose 1 - 5.")

if __name__ == "__main__":
    main()
