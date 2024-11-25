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
    # moved to own file

    # Sports & Outdoors
    # moved to own file

    # toys, baby
    # moved to own file

    # Food, pets
    # moved to own file

    # Travel and Experiences
    # moved to own file

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

from .f6_books_movies_music import books_movies_music
categories += books_movies_music

from .f7_sports_outdoors import sports_outdoors
categories += sports_outdoors

from .f8_f9_toys_baby import toys_baby
categories += toys_baby

from .f10_f11_food_pets import food_pets
categories += food_pets

from .f12_f13_travel_experiences import travel_experiences
categories += travel_experiences




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
