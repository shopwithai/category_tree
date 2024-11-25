toys_baby = [
    # Toys, Games & Hobbies

    {"id": 319, "name": "Toys", "is_root": False, "parents": [8], "properties": [
        ("brand", str),
        ("age_range", str, ["0-2 years", "3-5 years", "6-8 years", "9-12 years", "13+ years"]),
        ("material", str, ["Plastic", "Wood", "Metal", "Fabric", "Rubber", "Other"]),
        ("battery_required", bool),
    ]},

    {"id": 320, "name": "Action Figures", "is_root": False, "parents": [319], "properties": [
        ("character", str),
        ("franchise", str),
        ("articulated", bool),
        ("scale", str, ["1:6", "1:12", "1:18", "Other"]),
        ("limited_edition", bool),
        ("collectible", bool),
        ("accessories_included", bool),
    ]},

    {"id": 321, "name": "Dolls & Accessories", "is_root": False, "parents": [319], "properties": [
        ("doll_type", str, ["Fashion Doll", "Baby Doll", "Interactive Doll", "Collectible Doll", "Other"]),
        ("brand", str),
        ("character", str),
        ("franchise", str),
        ("includes_accessories", bool),
        ("interactive_features", bool),
        ("material", str, ["Plastic", "Fabric", "Vinyl", "Other"]),
    ]},

    {"id": 322, "name": "Building Toys", "is_root": False, "parents": [319], "properties": [
        ("brand", str),
        ("number_of_pieces", int),
        ("theme", str),
        ("compatible_with", str),
        ("age_range", str, ["0-2 years", "3-5 years", "6-8 years", "9-12 years", "13+ years"]),
        ("material", str, ["Plastic", "Wood", "Metal", "Other"]),
    ]},

    {"id": 323, "name": "Educational Toys", "is_root": False, "parents": [319], "properties": [
        ("brand", str),
        ("subject", str, ["Math", "Science", "Language", "Music", "Art", "Other"]),
        ("skill_development", str, ["Fine Motor", "Gross Motor", "Cognitive", "Social", "Emotional"]),
        ("age_range", str, ["0-2 years", "3-5 years", "6-8 years", "9-12 years", "13+ years"]),
        ("battery_required", bool),
        ("interactive", bool),
    ]},

    {"id": 324, "name": "Outdoor Toys", "is_root": False, "parents": [319], "properties": [
        ("brand", str),
        ("type", str, ["Swing", "Slide", "Trampoline", "Ride-On", "Water Toy", "Other"]),
        ("age_range", str, ["0-2 years", "3-5 years", "6-8 years", "9-12 years", "13+ years"]),
        ("maximum_weight_capacity_kg", int),
        ("material", str, ["Plastic", "Wood", "Metal", "Other"]),
        ("assembly_required", bool),
    ]},

    {"id": 325, "name": "Games", "is_root": False, "parents": [8], "properties": []},

    {"id": 326, "name": "Board Games", "is_root": False, "parents": [325], "properties": [
        ("brand", str),
        ("title", str),
        ("age_range", str),
        ("number_of_players", str),
        ("play_time_minutes", int),
        ("genre", str, ["Strategy", "Family", "Party", "Cooperative", "Abstract", "Other"]),
        ("award_winning", bool),
    ]},

    {"id": 327, "name": "Card Games", "is_root": False, "parents": [325], "properties": [
        ("brand", str),
        ("title", str),
        ("age_range", str),
        ("number_of_players", str),
        ("play_time_minutes", int),
        ("type", str, ["Deck Building", "Collectible Card Game", "Traditional", "Other"]),
    ]},

    {"id": 328, "name": "Puzzles", "is_root": False, "parents": [325], "properties": [
        ("brand", str),
        ("title", str),
        ("puzzle_type", str, ["Jigsaw", "3D Puzzle", "Brain Teaser", "Other"]),
        ("number_of_pieces", int),
        ("age_range", str),
        ("material", str, ["Cardboard", "Wood", "Plastic", "Metal", "Other"]),
        ("theme", str),
    ]},

    {"id": 329, "name": "Hobbies & Crafts", "is_root": False, "parents": [8], "properties": []},

    {"id": 330, "name": "Art Supplies", "is_root": False, "parents": [329], "properties": [
        ("type", str, ["Paint", "Brush", "Canvas", "Drawing Pencil", "Marker", "Other"]),
        ("brand", str),
        ("color", str),
        ("quantity", int),
        ("material", str, ["Acrylic", "Oil", "Watercolor", "Graphite", "Ink", "Other"]),
    ]},

    {"id": 331, "name": "Craft Kits", "is_root": False, "parents": [329], "properties": [
        ("type", str, ["Knitting", "Sewing", "Jewelry Making", "Paper Craft", "Other"]),
        ("brand", str),
        ("skill_level", str, ["Beginner", "Intermediate", "Advanced", "All Levels"]),
        ("age_range", str),
        ("materials_included", bool),
    ]},

    {"id": 332, "name": "Model Building", "is_root": False, "parents": [329], "properties": [
        ("brand", str),
        ("model_type", str, ["Aircraft", "Automobile", "Ship", "Train", "Sci-Fi", "Other"]),
        ("scale", str, ["1:72", "1:48", "1:35", "1:24", "1:18", "Other"]),
        ("number_of_pieces", int),
        ("skill_level", str, ["Beginner", "Intermediate", "Advanced"]),
        ("paint_glue_included", bool),
        ("material", str, ["Plastic", "Wood", "Metal", "Other"]),
    ]},

    {"id": 333, "name": "Collectibles", "is_root": False, "parents": [8], "properties": []},

    {"id": 334, "name": "Stamps", "is_root": False, "parents": [333], "properties": [
        ("country_of_origin", str),
        ("year_of_issue", int),
        ("face_value", float),
        ("topic_theme", str),
        ("condition_grade", str, ["Mint", "Used", "Unused", "Cancelled"]),
        ("certified", bool),
    ]},

    {"id": 335, "name": "Coins", "is_root": False, "parents": [333], "properties": [
        ("country_of_origin", str),
        ("year_of_issue", int),
        ("denomination", str),
        ("metal_type", str, ["Gold", "Silver", "Copper", "Nickel", "Other"]),
        ("grade", str, ["Uncirculated", "Proof", "Mint", "Circulated", "Other"]),
        ("certified", bool),
    ]},

    {"id": 336, "name": "Figurines", "is_root": False, "parents": [333], "properties": [
        ("brand", str),
        ("character", str),
        ("franchise", str),
        ("material", str, ["Resin", "Vinyl", "Plastic", "Porcelain", "Other"]),
        ("limited_edition", bool),
        ("scale", str),
        ("year_released", int),
    ]},

    # Baby & Kids

    {"id": 337, "name": "Baby Gear", "is_root": False, "parents": [9], "properties": []},

    {"id": 338, "name": "Strollers", "is_root": False, "parents": [337], "properties": [
        ("brand", str),
        ("model", str),
        ("stroller_type", str, ["Standard", "Lightweight", "Jogging", "Double", "Travel System", "Other"]),
        ("age_range", str, ["Newborn", "0-6 months", "6-12 months", "1-2 years", "2-4 years"]),
        ("weight_limit_kg", int),
        ("foldable", bool),
        ("number_of_wheels", int),
        ("wheel_type", str, ["Plastic", "Rubber", "Air-filled", "Foam-filled"]),
        ("adjustable_handle", bool),
        ("reversible_seat", bool),
    ]},

    {"id": 339, "name": "Car Seats", "is_root": False, "parents": [337], "properties": [
        ("brand", str),
        ("model", str),
        ("car_seat_type", str, ["Infant", "Convertible", "Booster", "All-in-One"]),
        ("age_range", str, ["Newborn", "0-6 months", "6-12 months", "1-2 years", "2-4 years", "4+ years"]),
        ("weight_limit_kg", int),
        ("installation_type", str, ["LATCH", "Seat Belt"]),
        ("rear_facing", bool),
        ("forward_facing", bool),
        ("side_impact_protection", bool),
        ("certified", bool),
    ]},

    {"id": 340, "name": "Baby Carriers", "is_root": False, "parents": [337], "properties": [
        ("brand", str),
        ("model", str),
        ("carrier_type", str, ["Wrap", "Sling", "Structured", "Mei Tai", "Other"]),
        ("age_range", str, ["Newborn", "0-6 months", "6-12 months", "1-2 years"]),
        ("weight_limit_kg", int),
        ("material", str, ["Cotton", "Polyester", "Blend", "Other"]),
        ("machine_washable", bool),
        ("multiple_positions", bool),
    ]},

    {"id": 341, "name": "Nursery", "is_root": False, "parents": [9], "properties": []},

    {"id": 342, "name": "Cribs & Bedding", "is_root": False, "parents": [341], "properties": [
        ("brand", str),
        ("crib_type", str, ["Standard", "Convertible", "Mini", "Portable", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Other"]),
        ("mattress_included", bool),
        ("adjustable_height", bool),
        ("bedding_included", bool),
        ("assembly_required", bool),
        ("dimensions_cm", str),
    ]},

    {"id": 343, "name": "Changing Tables", "is_root": False, "parents": [341], "properties": [
        ("brand", str),
        ("material", str, ["Wood", "Metal", "Plastic", "Other"]),
        ("includes_pad", bool),
        ("storage_features", str, ["Shelves", "Drawers", "Cubbies", "Other"]),
        ("dimensions_cm", str),
        ("assembly_required", bool),
        ("safety_straps_included", bool),
    ]},

    {"id": 344, "name": "Decor", "is_root": False, "parents": [341], "properties": [
        ("type", str, ["Wall Art", "Lighting", "Rugs", "Curtains", "Mobiles", "Other"]),
        ("brand", str),
        ("theme", str),
        ("material", str),
        ("dimensions_cm", str),
        ("gender", str, ["Unisex", "Boy", "Girl"]),
    ]},

    {"id": 345, "name": "Feeding", "is_root": False, "parents": [9], "properties": []},

    {"id": 346, "name": "Bottles & Nursing", "is_root": False, "parents": [345], "properties": [
        ("brand", str),
        ("product_type", str, ["Bottle", "Nipple", "Breast Pump", "Nursing Pillow", "Bottle Warmer", "Other"]),
        ("material", str, ["Plastic", "Glass", "Silicone", "Other"]),
        ("capacity_ml", int),
        ("bpa_free", bool),
        ("dishwasher_safe", bool),
        ("age_range", str, ["Newborn", "0-6 months", "6-12 months", "1-2 years"]),
    ]},

    {"id": 347, "name": "High Chairs", "is_root": False, "parents": [345], "properties": [
        ("brand", str),
        ("model", str),
        ("high_chair_type", str, ["Standard", "Convertible", "Booster Seat", "Hook-On", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Other"]),
        ("foldable", bool),
        ("adjustable_height", bool),
        ("tray_included", bool),
        ("weight_limit_kg", int),
        ("age_range", str, ["6-12 months", "1-2 years", "2-4 years"]),
    ]},

    {"id": 348, "name": "Baby Food", "is_root": False, "parents": [345], "properties": [
        ("brand", str),
        ("product_type", str, ["Formula", "Puree", "Snack", "Cereal", "Other"]),
        ("age_range", str, ["Newborn", "0-6 months", "6-12 months", "1-2 years"]),
        ("flavor", str),
        ("organic", bool),
        ("allergen_free", bool),
        ("net_weight_g", int),
        ("pack_size", int),
    ]},

    {"id": 349, "name": "Kids' Furniture", "is_root": False, "parents": [9], "properties": []},

    {"id": 350, "name": "Beds", "is_root": False, "parents": [349], "properties": [
        ("brand", str),
        ("bed_type", str, ["Toddler Bed", "Bunk Bed", "Loft Bed", "Trundle Bed", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Other"]),
        ("dimensions_cm", str),
        ("mattress_included", bool),
        ("assembly_required", bool),
        ("age_range", str, ["1-2 years", "2-4 years", "4+ years"]),
    ]},

    {"id": 351, "name": "Desks", "is_root": False, "parents": [349], "properties": [
        ("brand", str),
        ("material", str, ["Wood", "Metal", "Plastic", "Other"]),
        ("dimensions_cm", str),
        ("adjustable_height", bool),
        ("storage_features", str, ["Drawers", "Shelves", "Cubbies", "Other"]),
        ("chair_included", bool),
        ("assembly_required", bool),
        ("age_range", str, ["2-4 years", "4+ years"]),
    ]},

    {"id": 352, "name": "Storage", "is_root": False, "parents": [349], "properties": [
        ("brand", str),
        ("storage_type", str, ["Toy Box", "Bookshelf", "Closet Organizer", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Fabric", "Other"]),
        ("dimensions_cm", str),
        ("assembly_required", bool),
        ("theme", str),
        ("age_range", str),
    ]},

]