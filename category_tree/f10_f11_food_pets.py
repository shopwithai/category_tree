food_pets = [
    # Food & Grocery
    {"id": 353, "name": "Fresh Food", "is_root": False, "parents": [10], "properties": []},

    {"id": 354, "name": "Produce", "is_root": False, "parents": [353], "properties": [
        ("produce_type", str, ["Fruit", "Vegetable", "Herb", "Mushroom"]),
        ("organic", bool),
        ("origin_country", str),
        ("packaging", str, ["Loose", "Bagged", "Boxed"]),
        ("weight_per_unit_g", int),
    ]},

    {"id": 355, "name": "Meat & Seafood", "is_root": False, "parents": [353], "properties": [
        ("meat_type", str, ["Beef", "Pork", "Chicken", "Lamb", "Turkey", "Fish", "Shellfish", "Other"]),
        ("cut", str),
        ("organic", bool),
        ("free_range", bool),
        ("origin_country", str),
        ("fresh_or_frozen", str, ["Fresh", "Frozen"]),
        ("weight_per_unit_g", int),
    ]},

    {"id": 356, "name": "Dairy & Eggs", "is_root": False, "parents": [353], "properties": [
        ("dairy_type", str, ["Milk", "Cheese", "Yogurt", "Butter", "Cream", "Eggs", "Other"]),
        ("organic", bool),
        ("fat_content_percent", float),
        ("lactose_free", bool),
        ("origin_country", str),
        ("packaging", str, ["Carton", "Bottle", "Tub", "Other"]),
        ("quantity", int),
    ]},

    {"id": 357, "name": "Pantry Staples", "is_root": False, "parents": [10], "properties": []},

    {"id": 358, "name": "Baking", "is_root": False, "parents": [357], "properties": [
        ("ingredient_type", str, ["Flour", "Sugar", "Yeast", "Baking Powder", "Baking Soda", "Chocolate", "Other"]),
        ("organic", bool),
        ("gluten_free", bool),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 359, "name": "Canned Goods", "is_root": False, "parents": [357], "properties": [
        ("canned_item_type", str, ["Vegetables", "Fruits", "Soup", "Beans", "Fish", "Meat", "Other"]),
        ("organic", bool),
        ("low_sodium", bool),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 360, "name": "Pasta & Grains", "is_root": False, "parents": [357], "properties": [
        ("product_type", str, ["Pasta", "Rice", "Quinoa", "Couscous", "Other"]),
        ("organic", bool),
        ("gluten_free", bool),
        ("whole_grain", bool),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 361, "name": "Snacks & Sweets", "is_root": False, "parents": [10], "properties": []},

    {"id": 362, "name": "Chips & Crackers", "is_root": False, "parents": [361], "properties": [
        ("snack_type", str, ["Chips", "Crackers", "Pretzels", "Popcorn", "Other"]),
        ("flavor", str),
        ("organic", bool),
        ("gluten_free", bool),
        ("baked_or_fried", str, ["Baked", "Fried"]),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 363, "name": "Candy & Chocolate", "is_root": False, "parents": [361], "properties": [
        ("candy_type", str, ["Chocolate", "Gummy", "Hard Candy", "Licorice", "Mints", "Other"]),
        ("flavor", str),
        ("sugar_free", bool),
        ("chocolate_type", str, ["Dark", "Milk", "White"]),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 364, "name": "Cookies", "is_root": False, "parents": [361], "properties": [
        ("cookie_type", str),
        ("flavor", str),
        ("organic", bool),
        ("gluten_free", bool),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 365, "name": "Beverages", "is_root": False, "parents": [10], "properties": []},

    {"id": 366, "name": "Coffee & Tea", "is_root": False, "parents": [365], "properties": [
        ("beverage_type", str, ["Coffee", "Tea"]),
        ("form", str, ["Ground", "Whole Bean", "Instant", "Pods", "Loose Leaf", "Tea Bags"]),
        ("variety", str),
        ("caffeinated", bool),
        ("decaf", bool),
        ("organic", bool),
        ("fair_trade", bool),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 367, "name": "Soft Drinks", "is_root": False, "parents": [365], "properties": [
        ("drink_type", str, ["Soda", "Energy Drink", "Flavored Water", "Other"]),
        ("flavor", str),
        ("sugar_free", bool),
        ("caffeine", bool),
        ("package_size_ml", int),
        ("package_type", str, ["Can", "Bottle", "Box"]),
        ("brand", str),
    ]},

    {"id": 368, "name": "Juices", "is_root": False, "parents": [365], "properties": [
        ("juice_type", str),
        ("organic", bool),
        ("no_added_sugar", bool),
        ("package_size_ml", int),
        ("package_type", str, ["Bottle", "Carton", "Box"]),
        ("brand", str),
    ]},

    # Pets
    {"id": 369, "name": "Dog Supplies", "is_root": False, "parents": [11], "properties": []},

    {"id": 370, "name": "Food", "is_root": False, "parents": [369], "properties": [
        ("food_type", str, ["Dry", "Wet", "Freeze-Dried", "Raw", "Other"]),
        ("flavor", str),
        ("breed_size", str, ["Small", "Medium", "Large", "All"]),
        ("life_stage", str, ["Puppy", "Adult", "Senior", "All"]),
        ("organic", bool),
        ("grain_free", bool),
        ("package_size_kg", float),
        ("brand", str),
    ]},

    {"id": 371, "name": "Toys", "is_root": False, "parents": [369], "properties": [
        ("toy_type", str, ["Chew Toy", "Fetch Toy", "Puzzle Toy", "Squeaky Toy", "Plush Toy", "Other"]),
        ("material", str),
        ("size", str, ["Small", "Medium", "Large"]),
        ("squeaky", bool),
        ("interactive", bool),
        ("brand", str),
    ]},

    {"id": 372, "name": "Grooming", "is_root": False, "parents": [369], "properties": [
        ("product_type", str, ["Shampoo", "Conditioner", "Brush", "Comb", "Clippers", "Nail Trimmer", "Other"]),
        ("scented", bool),
        ("hypoallergenic", bool),
        ("suitable_for", str),
        ("brand", str),
    ]},

    {"id": 373, "name": "Cat Supplies", "is_root": False, "parents": [11], "properties": []},

    {"id": 374, "name": "Food", "is_root": False, "parents": [373], "properties": [
        ("food_type", str, ["Dry", "Wet", "Freeze-Dried", "Raw", "Other"]),
        ("flavor", str),
        ("life_stage", str, ["Kitten", "Adult", "Senior", "All"]),
        ("organic", bool),
        ("grain_free", bool),
        ("indoor_or_outdoor", str, ["Indoor", "Outdoor", "Both"]),
        ("package_size_kg", float),
        ("brand", str),
    ]},

    {"id": 375, "name": "Litter & Accessories", "is_root": False, "parents": [373], "properties": [
        ("product_type", str, ["Litter", "Litter Box", "Litter Mat", "Scoop", "Other"]),
        ("litter_type", str, ["Clumping", "Non-Clumping", "Silica", "Biodegradable", "Other"]),
        ("scented", bool),
        ("dust_free", bool),
        ("package_size_kg", float),
        ("brand", str),
    ]},

    {"id": 376, "name": "Toys", "is_root": False, "parents": [373], "properties": [
        ("toy_type", str, ["Interactive", "Catnip", "Balls", "Wands", "Laser Pointers", "Scratching Posts", "Other"]),
        ("material", str),
        ("contains_catnip", bool),
        ("brand", str),
    ]},

    {"id": 377, "name": "Fish Supplies", "is_root": False, "parents": [11], "properties": []},

    {"id": 378, "name": "Aquariums", "is_root": False, "parents": [377], "properties": [
        ("aquarium_type", str, ["Glass", "Acrylic", "Other"]),
        ("size_gallons", float),
        ("shape", str, ["Rectangle", "Bow Front", "Hexagon", "Cylinder", "Other"]),
        ("starter_kit", bool),
        ("brand", str),
        ("dimensions_cm", str),
    ]},

    {"id": 379, "name": "Food", "is_root": False, "parents": [377], "properties": [
        ("food_type", str, ["Flakes", "Pellets", "Freeze-Dried", "Frozen", "Live", "Other"]),
        ("species", str, ["Freshwater", "Saltwater", "Tropical", "Goldfish", "Betta", "Other"]),
        ("package_size_g", int),
        ("brand", str),
    ]},

    {"id": 380, "name": "Decorations", "is_root": False, "parents": [377], "properties": [
        ("decoration_type", str, ["Plants", "Rocks", "Ornaments", "Gravel", "Backgrounds", "Other"]),
        ("material", str, ["Plastic", "Resin", "Ceramic", "Natural", "Other"]),
        ("suitable_for", str, ["Freshwater", "Saltwater", "Both"]),
        ("brand", str),
    ]},

]