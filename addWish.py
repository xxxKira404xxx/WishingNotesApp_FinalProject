import random
from inputUtils import getItemName, getItemLink, getItemPrice, getItemNotes

def suggestCategory(itemName, notes, link):
    """Suggests a category based on keywords found in item name, notes, and link."""
    # Search for matching category keywords in item name and notes
    keywords = [
        ["Personal", ["bag", "wallet", "watch", "clothes", "shoes", "shirt", "belt", "sunglasses", "hat", "socks", "jacket", "pants", "sweater", "coat", "scarf", "gloves", "ring", "necklace", "bracelet", "earrings", "perfume", "cologne"]],
        ["Gadgets", ["phone", "laptop", "keyboard", "mouse", "monitor", "headset", "tablet", "smartwatch", "charger", "cable", "usb", "speaker", "microphone", "webcam", "screen", "router", "printer", "scanner", "power bank", "adapter", "dock", "stand"]],
        ["Travel", ["ticket", "luggage", "passport", "hotel", "backpack", "visa", "travel insurance", "map", "compass", "suitcase", "travel pillow", "travel bag", "luggage tag", "airport", "flight", "cruise", "resort"]],
        ["Food", ["coffee", "snack", "drink", "food", "restaurant", "cake", "pizza", "sandwich", "juice", "milk", "tea", "chocolate", "candy", "cookies", "bread", "cheese", "fruit", "vegetable", "meat", "seafood", "dessert", "breakfast", "lunch", "dinner"]],
        ["Hobbies", ["book", "guitar", "camera", "game", "controller", "lego", "painting", "drawing", "board game", "puzzle", "sketch", "art", "music", "instrument", "piano", "ukulele", "video game", "playstation", "xbox", "nintendo", "puzzle game", "puzzle cube"]],
        ["Others", []]
    ]

    # Search keywords in item name, notes, and link
    combined = (itemName + " " + notes + " " + link).lower()
    for category, words in keywords:
        for word in words:
            if word in combined:
                return category

    # If no match, ask user to pick category
    categories = [cat[0] for cat in keywords]
    print("  Categories:")
    for i, cat in enumerate(categories, 1):
        print(f"  {i}. {cat}")
    while True:
        pick = input("  No category detected. Pick one (1-6): ").strip()
        if pick.isdigit() and 1 <= int(pick) <= len(categories):
            return categories[int(pick) - 1]
        print("  Invalid choice. Please enter a number between 1 and 6.")

def addWish(wishes):
    """Adds a new wish to the wishlist with name, link, price, notes, and auto-detected category."""
    # Get item details from user
    print("\n── Add a Wish ──") 

    while True:
        itemName = getItemName()
        
        # Duplicate check
        isDuplicate = False
        for wish in wishes:
            if wish[0][1].lower() == itemName.lower():
                print(f"  ! '{itemName}' is already in your wish list.")
                isDuplicate = True
                break
        
        if not isDuplicate:
            break
        
        while True: # Ask user if they want to try a different name or cancel adding the wish
            choice = input("  Try a different name? (y/n): ").strip().upper()
            if  choice == 'Y':
                break
            elif choice == 'N':
                print("Wish not added. (Action Cancelled)")
                return
            else:
                print("  Invalid input. Please enter 'Y' or 'N'.")

    link = getItemLink() # Get item link from user input with validation
    price = getItemPrice() # Get item price from user input with validation
    notes = getItemNotes() # Get item notes from user input with validation

    # Suggest category and generate unique ID
    suggestedCategory = suggestCategory(itemName, notes, link)
    wish_id = random.randint(1000, 9999) 

    # Create wish structure with all details
    wish = [
        ["name",  itemName],
        ["link",  link ],
        ["price", price],
        ["notes", notes],
        ["id",    str(wish_id)],
        ["category",   suggestedCategory],
    ]

    # Add to wish list and confirm
    wishes.append(wish)
    print(f"\n✓ \"{itemName}\" (ID: {wish_id}) added to your wish list!")
    print(f"  Category: {suggestedCategory} | Price: ₱{price:,.2f}")
