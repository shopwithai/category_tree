sports_outdoors = [

    {"id": 284, "name": "Exercise & Fitness", "is_root": False, "parents": [7], "properties": []},

    {"id": 285, "name": "Cardio Equipment", "is_root": False, "parents": [284], "properties": [
        ("equipment_type", str, ["Treadmill", "Elliptical", "Stationary Bike", "Rowing Machine", "Stair Climber", "Spin Bike", "Other"]),
        ("brand", str),
        ("model", str),
        ("max_user_weight_kg", int),
        ("resistance_levels", int),
        ("heart_rate_monitor", bool),
        ("foldable", bool),
        ("power_source", str, ["Mains", "Battery", "Self-Powered"]),
        ("display_type", str, ["LCD", "LED", "Touchscreen", "None"]),
        ("programs_available", int),
        ("adjustable_incline", bool),
    ]},

    {"id": 286, "name": "Strength Training Equipment", "is_root": False, "parents": [284], "properties": [
        ("equipment_type", str, ["Dumbbells", "Barbells", "Weight Plates", "Benches", "Racks", "Home Gyms", "Kettlebells", "Resistance Bands", "Medicine Balls", "Other"]),
        ("brand", str),
        ("model", str),
        ("weight_kg", float),
        ("material", str, ["Steel", "Iron", "Rubber-Coated", "Vinyl", "Plastic", "Other"]),
        ("adjustable", bool),
        ("max_load_capacity_kg", int),
        ("number_of_exercises", int),
    ]},

    {"id": 287, "name": "Fitness Accessories", "is_root": False, "parents": [284], "properties": [
        ("accessory_type", str, ["Yoga Mat", "Fitness Tracker", "Jump Rope", "Fitness Ball", "Gloves", "Resistance Bands", "Foam Roller", "Other"]),
        ("brand", str),
        ("model", str),
        ("material", str),
        ("size", str),
        ("length_cm", int),
        ("water_resistant", bool),
        ("battery_life_hours", float),
        ("gender", str, ["Unisex", "Male", "Female"]),
    ]},

    {"id": 288, "name": "Outdoor Recreation", "is_root": False, "parents": [7], "properties": []},

    {"id": 289, "name": "Camping & Hiking", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Tent", "Sleeping Bag", "Backpack", "Stove", "Lantern", "Sleeping Pad", "Water Filter", "Camping Furniture", "Cookware", "Other"]),
        ("brand", str),
        ("model", str),
        ("capacity_persons", int),
        ("season_rating", str, ["1-season", "2-season", "3-season", "4-season"]),
        ("material", str),
        ("water_resistant", bool),
        ("temperature_rating_c", float),
        ("fuel_type", str, ["Gas", "Liquid Fuel", "Solid Fuel", "Other"]),
        ("volume_liters", int),
        ("weight_kg", float),
    ]},

    {"id": 290, "name": "Cycling", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Bicycle", "Helmet", "Accessory", "Clothing", "Other"]),
        ("brand", str),
        ("model", str),
        ("bike_type", str, ["Mountain", "Road", "Hybrid", "BMX", "Cruiser", "Electric", "Folding", "Other"]),
        ("frame_material", str, ["Aluminum", "Carbon", "Steel", "Titanium", "Other"]),
        ("wheel_size_inches", int),
        ("frame_size_cm", int),
        ("gears", int),
        ("brake_type", str, ["Disc", "Rim", "Drum", "Coaster", "Other"]),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("suspension", str, ["Full", "Front", "None"]),
        ("helmet_size", str),
        ("safety_certification", str, ["CPSC", "EN 1078", "ASTM F1952", "Other"]),
    ]},

    {"id": 291, "name": "Water Sports", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Kayak", "Paddle Board", "Life Jacket", "Snorkeling Gear", "Wetsuit", "Surfboard", "Swimwear", "Other"]),
        ("brand", str),
        ("model", str),
        ("material", str),
        ("capacity_persons", int),
        ("size", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("skill_level", str, ["Beginner", "Intermediate", "Advanced"]),
        ("type", str),
        ("buoyancy_rating", str),
    ]},

    {"id": 292, "name": "Winter Sports", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Skis", "Snowboard", "Helmet", "Goggles", "Clothing", "Boots", "Poles", "Other"]),
        ("brand", str),
        ("model", str),
        ("length_cm", int),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("skill_level", str, ["Beginner", "Intermediate", "Advanced"]),
        ("type", str, ["Alpine", "Cross-Country", "Freestyle", "Freeride", "All-Mountain", "Other"]),
        ("size", str),
    ]},

    {"id": 293, "name": "Climbing", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Harness", "Rope", "Carabiner", "Shoes", "Helmet", "Belay Device", "Chalk Bag", "Other"]),
        ("brand", str),
        ("model", str),
        ("material", str),
        ("length_meters", float),
        ("diameter_mm", float),
        ("weight_capacity_kg", int),
        ("certification", str, ["UIAA", "CE", "Other"]),
        ("size", str),
    ]},

    {"id": 294, "name": "Fishing", "is_root": False, "parents": [288], "properties": [
        ("product_type", str, ["Rod", "Reel", "Tackle", "Lures", "Line", "Accessories", "Other"]),
        ("brand", str),
        ("model", str),
        ("rod_length_ft", float),
        ("power", str, ["Ultralight", "Light", "Medium", "Medium-Heavy", "Heavy", "Extra Heavy"]),
        ("action", str, ["Fast", "Moderate", "Slow"]),
        ("reel_type", str, ["Spinning", "Baitcasting", "Fly", "Other"]),
        ("line_weight_lb", float),
        ("material", str),
    ]},

    {"id": 295, "name": "Team Sports", "is_root": False, "parents": [7], "properties": []},

    {"id": 296, "name": "Soccer", "is_root": False, "parents": [295], "properties": [
        ("product_type", str, ["Ball", "Boots", "Jersey", "Shin Guards", "Goalkeeper Gloves", "Training Equipment", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("material", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
        ("team", str),
    ]},

    {"id": 297, "name": "Basketball", "is_root": False, "parents": [295], "properties": [
        ("product_type", str, ["Ball", "Shoes", "Jersey", "Hoop", "Training Equipment", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str, ["Size 7", "Size 6", "Size 5"]),
        ("material", str, ["Leather", "Composite", "Rubber"]),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
        ("team", str),
    ]},

    {"id": 298, "name": "Baseball & Softball", "is_root": False, "parents": [295], "properties": [
        ("product_type", str, ["Bat", "Glove", "Ball", "Helmet", "Cleats", "Uniform", "Other"]),
        ("brand", str),
        ("model", str),
        ("bat_length_inches", float),
        ("bat_weight_oz", float),
        ("material", str, ["Wood", "Aluminum", "Composite", "Alloy"]),
        ("hand_orientation", str, ["Left", "Right"]),
        ("position", str, ["Pitcher", "Catcher", "Infielder", "Outfielder", "Other"]),
        ("size", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
    ]},

    {"id": 299, "name": "Football", "is_root": False, "parents": [295], "properties": [
        ("product_type", str, ["Ball", "Helmet", "Pads", "Jersey", "Cleats", "Gloves", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("material", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
        ("position", str, ["Quarterback", "Receiver", "Linebacker", "Other"]),
    ]},

    {"id": 300, "name": "Volleyball", "is_root": False, "parents": [295], "properties": [
        ("product_type", str, ["Ball", "Knee Pads", "Shoes", "Net", "Uniform", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("material", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
    ]},

    {"id": 301, "name": "Racquet Sports", "is_root": False, "parents": [7], "properties": []},

    {"id": 302, "name": "Tennis", "is_root": False, "parents": [301], "properties": [
        ("product_type", str, ["Racquet", "Ball", "Shoes", "Clothing", "Bag", "String", "Other"]),
        ("brand", str),
        ("model", str),
        ("racquet_weight_g", int),
        ("racquet_head_size_sq_in", float),
        ("grip_size", str),
        ("string_pattern", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
    ]},

    {"id": 303, "name": "Badminton", "is_root": False, "parents": [301], "properties": [
        ("product_type", str, ["Racquet", "Shuttlecock", "Net", "Shoes", "Clothing", "Other"]),
        ("brand", str),
        ("model", str),
        ("racquet_weight_g", int),
        ("balance_point_mm", int),
        ("flex", str, ["Flexible", "Medium", "Stiff", "Extra Stiff"]),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("age_group", str, ["Adult", "Youth", "Child"]),
    ]},

    {"id": 304, "name": "Squash", "is_root": False, "parents": [301], "properties": [
        ("product_type", str, ["Racquet", "Ball", "Shoes", "Goggles", "Clothing", "Other"]),
        ("brand", str),
        ("model", str),
        ("racquet_weight_g", int),
        ("balance", str, ["Head Heavy", "Even", "Head Light"]),
        ("string_pattern", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
    ]},

    {"id": 305, "name": "Golf", "is_root": False, "parents": [7], "properties": []},

    {"id": 306, "name": "Clubs", "is_root": False, "parents": [305], "properties": [
        ("club_type", str, ["Driver", "Wood", "Hybrid", "Iron", "Wedge", "Putter"]),
        ("brand", str),
        ("model", str),
        ("shaft_material", str, ["Steel", "Graphite"]),
        ("flex", str, ["Regular", "Stiff", "Senior", "Ladies", "Extra Stiff"]),
        ("loft_degree", float),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("hand_orientation", str, ["Right", "Left"]),
    ]},

    {"id": 307, "name": "Balls", "is_root": False, "parents": [305], "properties": [
        ("brand", str),
        ("model", str),
        ("number_of_pieces", int),
        ("compression", str),
        ("cover_material", str, ["Urethane", "Surlyn", "Other"]),
    ]},

    {"id": 308, "name": "Bags & Carts", "is_root": False, "parents": [305], "properties": [
        ("type", str, ["Stand Bag", "Cart Bag", "Carry Bag", "Tour Bag", "Push Cart", "Electric Cart"]),
        ("brand", str),
        ("model", str),
        ("number_of_pockets", int),
        ("number_of_dividers", int),
        ("weight_kg", float),
    ]},

    {"id": 309, "name": "Accessories", "is_root": False, "parents": [305], "properties": [
        ("type", str, ["Glove", "Hat", "Umbrella", "Towel", "Rangefinder", "Training Aid", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
    ]},

    {"id": 310, "name": "Hunting & Shooting", "is_root": False, "parents": [7], "properties": []},

    {"id": 311, "name": "Firearms", "is_root": False, "parents": [310], "properties": [
        ("firearm_type", str, ["Rifle", "Shotgun", "Handgun", "Other"]),
        ("brand", str),
        ("model", str),
        ("caliber", str),
        ("barrel_length_inches", float),
        ("capacity", int),
        ("action_type", str, ["Bolt", "Semi-Automatic", "Lever", "Pump", "Revolver", "Other"]),
        ("material", str),
        ("finish", str),
    ]},

    {"id": 312, "name": "Archery", "is_root": False, "parents": [310], "properties": [
        ("product_type", str, ["Bow", "Arrow", "Target", "Accessory", "Other"]),
        ("bow_type", str, ["Compound", "Recurve", "Longbow", "Crossbow"]),
        ("brand", str),
        ("model", str),
        ("draw_weight_lbs", int),
        ("draw_length_inches", float),
        ("hand_orientation", str, ["Right", "Left"]),
        ("material", str),
    ]},

    {"id": 313, "name": "Hunting Gear", "is_root": False, "parents": [310], "properties": [
        ("product_type", str, ["Apparel", "Optics", "Blinds", "Decoys", "Calls", "Backpacks", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("material", str),
        ("camouflage_pattern", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
    ]},

    {"id": 314, "name": "Other Sports & Outdoors", "is_root": False, "parents": [7], "properties": []},

    {"id": 315, "name": "Equestrian", "is_root": False, "parents": [314], "properties": [
        ("product_type", str, ["Saddle", "Bridle", "Riding Boots", "Helmet", "Apparel", "Grooming Supplies", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("material", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("discipline", str, ["English", "Western", "Other"]),
    ]},

    {"id": 316, "name": "Martial Arts", "is_root": False, "parents": [314], "properties": [
        ("product_type", str, ["Uniform", "Protective Gear", "Weapons", "Training Equipment", "Other"]),
        ("martial_art_type", str, ["Karate", "Taekwondo", "Judo", "Kung Fu", "MMA", "Other"]),
        ("brand", str),
        ("model", str),
        ("size", str),
        ("gender", str, ["Unisex", "Male", "Female"]),
        ("material", str),
    ]},

    {"id": 317, "name": "Skateboarding & Scooters", "is_root": False, "parents": [314], "properties": [
        ("product_type", str, ["Skateboard", "Scooter", "Protective Gear", "Accessories", "Other"]),
        ("brand", str),
        ("model", str),
        ("deck_length_inches", float),
        ("wheel_size_mm", int),
        ("material", str),
        ("type", str, ["Longboard", "Cruiser", "Street", "Kick Scooter", "Electric Scooter"]),
    ]},

    {"id": 318, "name": "Other Sports Equipment", "is_root": False, "parents": [314], "properties": []},

]
