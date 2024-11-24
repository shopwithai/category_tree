categories = [
    {"id": 0, "name": "(Internal) Master Category, do not use", "is_root": True, "parents": [], "properties": [("atomicprice", int), ("condition", str, ["New", "Used", "Refurbished"]), ("widthcm", int), ("heightcm", int), ("lengthcm", int), ("weightg", int), ("rgb_color", [int, int, int])]},
    # Root Categories
    {"id": 1, "name": "Automotive & Vehicles", "is_root": True, "parents": [0]},
    {"id": 2, "name": "Fashion & Accessories", "is_root": True, "parents": [0]},
    {"id": 3, "name": "Electronics & Computers", "is_root": True, "parents": [0]},
    {"id": 4, "name": "Home & Garden", "is_root": True, "parents": [0]},
    {"id": 5, "name": "Health & Beauty", "is_root": True, "parents": [0]},
    {"id": 6, "name": "Books, Movies & Music", "is_root": True, "parents": [0]},
    {"id": 7, "name": "Sports & Outdoors", "is_root": True, "parents": [0]},
    {"id": 8, "name": "Toys, Games & Hobbies", "is_root": True, "parents": [0]},
    {"id": 9, "name": "Baby & Kids", "is_root": True, "parents": [0]},
    {"id": 10, "name": "Food & Grocery", "is_root": True, "parents": [0]},
    {"id": 11, "name": "Pets", "is_root": True, "parents": [0]},
    {"id": 12, "name": "Travel & Experiences", "is_root": True, "parents": [0]},
    {"id": 13, "name": "Services", "is_root": True, "parents": [0]},
    {"id": 14, "name": "Industrial & Business", "is_root": True, "parents": [0]},
    {"id": 15, "name": "Real Estate", "is_root": True, "parents": [0]},
    {"id": 16, "name": "Deals & Discounts", "is_root": True, "parents": [0]},
    {"id": 17, "name": "Software & Subscriptions", "is_root": True, "parents": [0]},
    {"id": 18, "name": "Luxury & High-End Goods", "is_root": True, "parents": [0]},
    {"id": 19, "name": "Gifts & Occasions", "is_root": True, "parents": [0]},
    {"id": 20, "name": "Miscellaneous", "is_root": True, "parents": [0]},

    # Automotive & Vehicles
    # moved to own file

    # Fashion & Accessories
    # moved to own file

    # Electronics & Computers
    # moved to own file

    # Home & Garden
    # moved to own file

    # Health & Beauty
    # moved to own file

    # Books, Movies & Music
    {"id": 257, "name": "Books", "is_root": False, "parents": [6]},
    {"id": 258, "name": "Fiction", "is_root": False, "parents": [257]},
    {"id": 259, "name": "Non-Fiction", "is_root": False, "parents": [257]},
    {"id": 260, "name": "Children's Books", "is_root": False, "parents": [257]},
    {"id": 261, "name": "Educational & Textbooks", "is_root": False, "parents": [257]},
    {"id": 262, "name": "Comics & Graphic Novels", "is_root": False, "parents": [257]},
    {"id": 263, "name": "Movies & TV Shows", "is_root": False, "parents": [6]},
    {"id": 264, "name": "DVDs & Blu-rays", "is_root": False, "parents": [263]},
    {"id": 265, "name": "Digital Downloads", "is_root": False, "parents": [263]},
    {"id": 425, "name": "Prime Video Streaming", "is_root": False, "parents": [263]},
    {"id": 266, "name": "VHS", "is_root": False, "parents": [263]},
    {"id": 267, "name": "Music", "is_root": False, "parents": [6]},
    {"id": 268, "name": "CDs", "is_root": False, "parents": [267]},
    {"id": 269, "name": "Vinyl Records", "is_root": False, "parents": [267]},
    {"id": 270, "name": "Digital Music", "is_root": False, "parents": [267]},
    {"id": 271, "name": "Video Games", "is_root": False, "parents": [6]},
    {"id": 272, "name": "Games", "is_root": False, "parents": [271]},
    {"id": 273, "name": "Accessories", "is_root": False, "parents": [271]},
    {"id": 274, "name": "Musical Instruments", "is_root": False, "parents": [6, 8]},  # Also under "Toys, Games & Hobbies"
    {"id": 275, "name": "String Instruments", "is_root": False, "parents": [274]},
    {"id": 276, "name": "Wind Instruments", "is_root": False, "parents": [274]},
    {"id": 277, "name": "Percussion Instruments", "is_root": False, "parents": [274]},
    {"id": 278, "name": "Electronic Instruments", "is_root": False, "parents": [274]},
    {"id": 279, "name": "Collectibles", "is_root": False, "parents": [6]},
    {"id": 280, "name": "Trading Cards", "is_root": False, "parents": [279]},
    {"id": 281, "name": "Memorabilia", "is_root": False, "parents": [279]},
    {"id": 282, "name": "Limited Editions", "is_root": False, "parents": [279]},
    {"id": 283, "name": "Other Media", "is_root": False, "parents": [6]},

    # Sports & Outdoors
    {"id": 284, "name": "Exercise & Fitness", "is_root": False, "parents": [7]},
    {"id": 285, "name": "Cardio Equipment", "is_root": False, "parents": [284]},
    {"id": 286, "name": "Strength Training Equipment", "is_root": False, "parents": [284]},
    {"id": 287, "name": "Fitness Accessories", "is_root": False, "parents": [284]},
    {"id": 288, "name": "Outdoor Recreation", "is_root": False, "parents": [7]},
    {"id": 289, "name": "Camping & Hiking", "is_root": False, "parents": [288]},
    {"id": 290, "name": "Cycling", "is_root": False, "parents": [288]},
    {"id": 291, "name": "Water Sports", "is_root": False, "parents": [288]},
    {"id": 292, "name": "Winter Sports", "is_root": False, "parents": [288]},
    {"id": 293, "name": "Climbing", "is_root": False, "parents": [288]},
    {"id": 294, "name": "Fishing", "is_root": False, "parents": [288]},
    {"id": 295, "name": "Team Sports", "is_root": False, "parents": [7]},
    {"id": 296, "name": "Soccer", "is_root": False, "parents": [295]},
    {"id": 297, "name": "Basketball", "is_root": False, "parents": [295]},
    {"id": 298, "name": "Baseball & Softball", "is_root": False, "parents": [295]},
    {"id": 299, "name": "Football", "is_root": False, "parents": [295]},
    {"id": 300, "name": "Volleyball", "is_root": False, "parents": [295]},
    {"id": 301, "name": "Racquet Sports", "is_root": False, "parents": [7]},
    {"id": 302, "name": "Tennis", "is_root": False, "parents": [301]},
    {"id": 303, "name": "Badminton", "is_root": False, "parents": [301]},
    {"id": 304, "name": "Squash", "is_root": False, "parents": [301]},
    {"id": 305, "name": "Golf", "is_root": False, "parents": [7]},
    {"id": 306, "name": "Clubs", "is_root": False, "parents": [305]},
    {"id": 307, "name": "Balls", "is_root": False, "parents": [305]},
    {"id": 308, "name": "Bags & Carts", "is_root": False, "parents": [305]},
    {"id": 309, "name": "Accessories", "is_root": False, "parents": [305]},
    {"id": 310, "name": "Hunting & Shooting", "is_root": False, "parents": [7]},
    {"id": 311, "name": "Firearms", "is_root": False, "parents": [310]},  # Subject to regulations
    {"id": 312, "name": "Archery", "is_root": False, "parents": [310]},
    {"id": 313, "name": "Hunting Gear", "is_root": False, "parents": [310]},
    {"id": 314, "name": "Other Sports & Outdoors", "is_root": False, "parents": [7]},
    {"id": 315, "name": "Equestrian", "is_root": False, "parents": [314]},
    {"id": 316, "name": "Martial Arts", "is_root": False, "parents": [314]},
    {"id": 317, "name": "Skateboarding & Scooters", "is_root": False, "parents": [314]},
    {"id": 318, "name": "Other Sports Equipment", "is_root": False, "parents": [314]},
    
    # Toys, Games & Hobbies
    {"id": 319, "name": "Toys", "is_root": False, "parents": [8]},
    {"id": 320, "name": "Action Figures", "is_root": False, "parents": [319]},
    {"id": 321, "name": "Dolls & Accessories", "is_root": False, "parents": [319]},
    {"id": 322, "name": "Building Toys", "is_root": False, "parents": [319]},
    {"id": 323, "name": "Educational Toys", "is_root": False, "parents": [319]},
    {"id": 324, "name": "Outdoor Toys", "is_root": False, "parents": [319]},
    {"id": 325, "name": "Games", "is_root": False, "parents": [8]},
    {"id": 326, "name": "Board Games", "is_root": False, "parents": [325]},
    {"id": 327, "name": "Card Games", "is_root": False, "parents": [325]},
    {"id": 328, "name": "Puzzles", "is_root": False, "parents": [325]},
    {"id": 329, "name": "Hobbies & Crafts", "is_root": False, "parents": [8]},
    {"id": 330, "name": "Art Supplies", "is_root": False, "parents": [329]},
    {"id": 331, "name": "Craft Kits", "is_root": False, "parents": [329]},
    {"id": 332, "name": "Model Building", "is_root": False, "parents": [329]},
    {"id": 333, "name": "Collectibles", "is_root": False, "parents": [8]},
    {"id": 334, "name": "Stamps", "is_root": False, "parents": [333]},
    {"id": 335, "name": "Coins", "is_root": False, "parents": [333]},
    {"id": 336, "name": "Figurines", "is_root": False, "parents": [333]},

    # Baby & Kids
    {"id": 337, "name": "Baby Gear", "is_root": False, "parents": [9]},
    {"id": 338, "name": "Strollers", "is_root": False, "parents": [337]},
    {"id": 339, "name": "Car Seats", "is_root": False, "parents": [337]},
    {"id": 340, "name": "Baby Carriers", "is_root": False, "parents": [337]},
    {"id": 341, "name": "Nursery", "is_root": False, "parents": [9]},
    {"id": 342, "name": "Cribs & Bedding", "is_root": False, "parents": [341]},
    {"id": 343, "name": "Changing Tables", "is_root": False, "parents": [341]},
    {"id": 344, "name": "Decor", "is_root": False, "parents": [341]},
    {"id": 345, "name": "Feeding", "is_root": False, "parents": [9]},
    {"id": 346, "name": "Bottles & Nursing", "is_root": False, "parents": [345]},
    {"id": 347, "name": "High Chairs", "is_root": False, "parents": [345]},
    {"id": 348, "name": "Baby Food", "is_root": False, "parents": [345]},
    {"id": 349, "name": "Kids' Furniture", "is_root": False, "parents": [9]},
    {"id": 350, "name": "Beds", "is_root": False, "parents": [349]},
    {"id": 351, "name": "Desks", "is_root": False, "parents": [349]},
    {"id": 352, "name": "Storage", "is_root": False, "parents": [349]},

    # Food & Grocery
    {"id": 353, "name": "Fresh Food", "is_root": False, "parents": [10]},
    {"id": 354, "name": "Produce", "is_root": False, "parents": [353]},
    {"id": 355, "name": "Meat & Seafood", "is_root": False, "parents": [353]},
    {"id": 356, "name": "Dairy & Eggs", "is_root": False, "parents": [353]},
    {"id": 357, "name": "Pantry Staples", "is_root": False, "parents": [10]},
    {"id": 358, "name": "Baking", "is_root": False, "parents": [357]},
    {"id": 359, "name": "Canned Goods", "is_root": False, "parents": [357]},
    {"id": 360, "name": "Pasta & Grains", "is_root": False, "parents": [357]},
    {"id": 361, "name": "Snacks & Sweets", "is_root": False, "parents": [10]},
    {"id": 362, "name": "Chips & Crackers", "is_root": False, "parents": [361]},
    {"id": 363, "name": "Candy & Chocolate", "is_root": False, "parents": [361]},
    {"id": 364, "name": "Cookies", "is_root": False, "parents": [361]},
    {"id": 365, "name": "Beverages", "is_root": False, "parents": [10]},
    {"id": 366, "name": "Coffee & Tea", "is_root": False, "parents": [365]},
    {"id": 367, "name": "Soft Drinks", "is_root": False, "parents": [365]},
    {"id": 368, "name": "Juices", "is_root": False, "parents": [365]},

    # Pets
    {"id": 369, "name": "Dog Supplies", "is_root": False, "parents": [11]},
    {"id": 370, "name": "Food", "is_root": False, "parents": [369]},
    {"id": 371, "name": "Toys", "is_root": False, "parents": [369]},
    {"id": 372, "name": "Grooming", "is_root": False, "parents": [369]},
    {"id": 373, "name": "Cat Supplies", "is_root": False, "parents": [11]},
    {"id": 374, "name": "Food", "is_root": False, "parents": [373]},
    {"id": 375, "name": "Litter & Accessories", "is_root": False, "parents": [373]},
    {"id": 376, "name": "Toys", "is_root": False, "parents": [373]},
    {"id": 377, "name": "Fish Supplies", "is_root": False, "parents": [11]},
    {"id": 378, "name": "Aquariums", "is_root": False, "parents": [377]},
    {"id": 379, "name": "Food", "is_root": False, "parents": [377]},
    {"id": 380, "name": "Decorations", "is_root": False, "parents": [377]},

    # Travel & Experiences
    {"id": 381, "name": "Hotels & Accommodations", "is_root": False, "parents": [12]},
    {"id": 382, "name": "Flights", "is_root": False, "parents": [12]},
    {"id": 383, "name": "Car Rentals", "is_root": False, "parents": [12]},
    {"id": 384, "name": "Vacation Packages", "is_root": False, "parents": [12]},
    {"id": 385, "name": "Cruises", "is_root": False, "parents": [12]},
    {"id": 386, "name": "Activities & Tours", "is_root": False, "parents": [12]},

    # Services
    {"id": 387, "name": "Home Services", "is_root": False, "parents": [13]},
    {"id": 388, "name": "Cleaning", "is_root": False, "parents": [387]},
    {"id": 389, "name": "Repair & Maintenance", "is_root": False, "parents": [387]},
    {"id": 390, "name": "Landscaping", "is_root": False, "parents": [387]},
    {"id": 391, "name": "Professional Services", "is_root": False, "parents": [13]},
    {"id": 392, "name": "Legal", "is_root": False, "parents": [391]},
    {"id": 393, "name": "Financial", "is_root": False, "parents": [391]},
    {"id": 394, "name": "Consulting", "is_root": False, "parents": [391]},
    {"id": 395, "name": "Health & Wellness Services", "is_root": False, "parents": [13]},
    {"id": 396, "name": "Massage", "is_root": False, "parents": [395]},
    {"id": 397, "name": "Personal Training", "is_root": False, "parents": [395]},
    {"id": 398, "name": "Nutrition Counseling", "is_root": False, "parents": [395]},

    # misc stuff moved to own file
]

from .f1_automotive_and_vehicles import automotive_and_vehicles
categories += automotive_and_vehicles

from .f2_fashion_and_accessories import fashion_and_accessories
categories += fashion_and_accessories

from .f3_electronics_and_computers import electronics_and_computers
categories += electronics_and_computers

from .f4_home_and_garden import home_and_garden
categories += home_and_garden

from .f5_health_and_beauty import health_and_beauty
categories += health_and_beauty




from .misc import misc_categories
categories += misc_categories


def inherit_properties(categories):
    # Create a dictionary for quick access to categories by their ID
    id_to_category = {cat["id"]: cat for cat in categories}
    
    # Ensure every category has a "properties" list
    for category in categories:
        category["properties"] = category.get("properties", [])

    def get_inherited_properties(category_id, visited=None):
        """
        Recursively fetch all properties inherited from the entire parent chain.
        """
        if visited is None:
            visited = set()

        if category_id in visited:
            # Avoid circular references
            return []

        visited.add(category_id)

        category = id_to_category[category_id]
        all_properties = []

        # Inherit properties from parents recursively
        for parent_id in category.get("parents", []):
            parent_properties = get_inherited_properties(parent_id, visited)
            all_properties.extend(parent_properties)

        # Add this category's own properties
        all_properties.extend(category["properties"])

        # Resolve clashes (child overwrites parent)
        resolved_properties = {}
        for prop in all_properties:
            resolved_properties[prop[0]] = prop  # Later properties overwrite earlier ones

        return list(resolved_properties.values())

    # Update categories with fully resolved properties
    for category in categories:
        category["properties"] = get_inherited_properties(category["id"])

    return categories


categories = inherit_properties(categories)


# Find next available id:
max_idx = 0
for c in categories:
    idx = c["id"]
    max_idx = max(idx, max_idx)
print("Next available id is", max_idx)


def get_implied_categories(category_id, categories):
    """
    Returns a set of category IDs that are implied by the given category ID,
    including the category itself and all its descendants in the tree.
    
    Args:
        category_id (int): The ID of the category to start from
        categories (list): List of category dictionaries with id, name, and parents fields
    
    Returns:
        set: Set of category IDs that are implied by the given category
    """
    implied = {category_id}  # Start with the given category
    
    # Create a mapping of parent IDs to child IDs for faster lookup
    parent_to_children = {}
    for category in categories:
        for parent_id in category['parents']:
            if parent_id not in parent_to_children:
                parent_to_children[parent_id] = set()
            parent_to_children[parent_id].add(category['id'])
    
    # Helper function to recursively find all descendants
    def find_descendants(current_id):
        if current_id in parent_to_children:
            children = parent_to_children[current_id]
            for child_id in children:
                if child_id not in implied:  # Avoid cycles
                    implied.add(child_id)
                    find_descendants(child_id)
    
    # Find all descendants of the starting category
    find_descendants(category_id)
    
    return implied


def build_category_tree(categories, parent_id=None, level=0):
    tree = []
    # Find categories at current level
    current_level = [cat for cat in categories if parent_id in (cat["parents"] if cat["parents"] else [None])]
    
    # Sort by name for consistent display
    current_level.sort(key=lambda x: x["name"])
    
    for category in current_level:
        # Add current category with proper indentation
        indent = "    " * level  # 4 spaces per level
        tree.append(f"{indent}{category['id']}: {category['name']}")
        
        # Recursively add children
        children = build_category_tree(categories, category["id"], level + 1)
        tree.extend(children)
    
    return tree

def display_category_hierarchy(categories):
    # Start with root categories (those with empty parents list)
    tree = build_category_tree(categories)
    return "\n".join(tree)
