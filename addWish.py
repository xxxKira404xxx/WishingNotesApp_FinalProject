import random
from inputUtils import get_item_name, get_item_link, get_item_price, get_item_notes

def suggestCategory(itemName, notes):
    """Suggests a category based on keywords found in item name and notes."""
    # Search for matching category keywords in item name and notes
    keywords = [
        ["Personal", ["bag", "wallet", "watch", "clothes", "shoes", "shirt", "belt", "sunglasses", "hat", "socks", "jacket", "pants", "sweater", "coat", "scarf", "gloves", "ring", "necklace", "bracelet", "earrings", "perfume", "cologne"]],
        ["Gadgets", ["phone", "laptop", "keyboard", "mouse", "monitor", "headset", "tablet", "smartwatch", "charger", "cable", "usb", "speaker", "microphone", "webcam", "screen", "router", "printer", "scanner", "power bank", "adapter", "dock", "stand"]],
        ["Travel", ["ticket", "luggage", "passport", "hotel", "backpack", "visa", "travel insurance", "map", "compass", "suitcase", "travel pillow", "travel bag", "luggage tag", "airport", "flight", "cruise", "resort"]],
        ["Food", ["coffee", "snack", "drink", "food", "restaurant", "cake", "pizza", "sandwich", "juice", "milk", "tea", "chocolate", "candy", "cookies", "bread", "cheese", "fruit", "vegetable", "meat", "seafood", "dessert", "breakfast", "lunch", "dinner"]],
        ["Hobbies", ["book", "guitar", "camera", "game", "controller", "lego", "painting", "drawing", "board game", "puzzle", "sketch", "art", "music", "instrument", "piano", "ukulele", "video game", "playstation", "xbox", "nintendo", "puzzle game", "puzzle cube"]],
        ["Others", []]
    ]

    # Search keywords in item name and notes
    combined = (itemName + " " + notes).lower()
    for category, words in keywords:
        for word in words:
            if word in combined:
                return category

    # If no match, ask user to pick category
    categories = [cat[0] for cat in keywords]
    print("  Categories: " + ", ".join(categories))
    while True:
        pick = input("  No category detected. Pick one: ").strip().title()
        if pick in categories:
            return pick
        print("  Invalid category.")

def addWish(wishes):
    """Adds a new wish to the wishlist with name, link, price, notes, and auto-detected category."""
    # Get item details from user
    print("\n── Add a Wish ──") 

    itemName = get_item_name()
    link = get_item_link()
    price = get_item_price()
    notes = get_item_notes()

    # Suggest category and generate unique ID
    suggested_category = suggestCategory(itemName, notes)
    wish_id = random.randint(1000, 9999) 

    # Create wish structure with all details
    wish = [
        ["name",  itemName],
        ["link",  link ],
        ["price", price],
        ["notes", notes],
        ["id",    str(wish_id)],
        ["cat",   suggested_category],
    ]

    # Add to wish list and confirm
    wishes.append(wish)
    print(f"\n✓ \"{itemName}\" (ID: {wish_id}) added to your wish list!")
    print(f"  Category: {suggested_category} | Price: ₱{price:,.2f}")