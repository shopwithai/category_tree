health_and_beauty = [
    # Health and Beauty
    {"id": 221, "name": "Makeup", "is_root": False, "parents": [5], "properties": []},

    {"id": 222, "name": "Face", "is_root": False, "parents": [221], "properties": [
        ("brand", str),
        ("product_type", str, ["Foundation", "Concealer", "Blush", "Bronzer", "Powder", "Primer"]),
        ("shade_name", str),
        ("shade_number", str),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("coverage", str, ["Sheer", "Light", "Medium", "Full"]),
        ("finish", str, ["Matte", "Dewy", "Natural", "Satin", "Radiant"]),
        ("SPF", int),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 223, "name": "Eyes", "is_root": False, "parents": [221], "properties": [
        ("brand", str),
        ("product_type", str, ["Mascara", "Eyeliner", "Eyeshadow", "Eyebrow Pencil", "Eyebrow Gel", "Eye Primer"]),
        ("shade_name", str),
        ("shade_number", str),
        ("waterproof", bool),
        ("finish", str, ["Matte", "Shimmer", "Metallic", "Glitter", "Satin"]),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 224, "name": "Lips", "is_root": False, "parents": [221], "properties": [
        ("brand", str),
        ("product_type", str, ["Lipstick", "Lip Gloss", "Lip Liner", "Lip Balm", "Lip Stain", "Lip Plumper"]),
        ("shade_name", str),
        ("shade_number", str),
        ("finish", str, ["Matte", "Cream", "Glossy", "Satin", "Sheer", "Metallic"]),
        ("long_wearing", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
        ("SPF", int),
    ]},

    {"id": 225, "name": "Skincare", "is_root": False, "parents": [5], "properties": []},

    {"id": 226, "name": "Cleansers", "is_root": False, "parents": [225], "properties": [
        ("brand", str),
        ("product_type", str, ["Foam Cleanser", "Gel Cleanser", "Cream Cleanser", "Oil Cleanser", "Micellar Water", "Exfoliating Cleanser"]),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("fragrance_free", bool),
        ("sulfate_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 227, "name": "Moisturizers", "is_root": False, "parents": [225], "properties": [
        ("brand", str),
        ("product_type", str, ["Cream", "Lotion", "Gel", "Oil", "Serum", "Balm"]),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("SPF", int),
        ("fragrance_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 228, "name": "Treatments & Serums", "is_root": False, "parents": [225], "properties": [
        ("brand", str),
        ("product_type", str, ["Serum", "Essence", "Ampoule", "Spot Treatment", "Oil"]),
        ("skin_concerns", str, ["Acne", "Aging", "Dryness", "Dark Spots", "Pores", "Redness", "Dullness"]),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("fragrance_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 229, "name": "Sunscreen", "is_root": False, "parents": [225], "properties": [
        ("brand", str),
        ("SPF", int),
        ("sunscreen_type", str, ["Chemical", "Physical", "Combination"]),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("water_resistant", bool),
        ("reef_safe", bool),
        ("fragrance_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 230, "name": "Hair Care", "is_root": False, "parents": [5], "properties": []},

    {"id": 231, "name": "Shampoo & Conditioner", "is_root": False, "parents": [230], "properties": [
        ("brand", str),
        ("product_type", str, ["Shampoo", "Conditioner", "2-in-1"]),
        ("hair_type", str, ["Straight", "Wavy", "Curly", "Coily", "Fine", "Thick", "Dry", "Oily", "Color-treated", "Damaged"]),
        ("sulfate_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 232, "name": "Styling Products", "is_root": False, "parents": [230], "properties": [
        ("brand", str),
        ("product_type", str, ["Hair Gel", "Hair Spray", "Mousse", "Wax", "Pomade", "Cream", "Serum", "Heat Protectant"]),
        ("hair_type", str, ["Straight", "Wavy", "Curly", "Coily", "Fine", "Thick", "Dry", "Oily", "Color-treated", "Damaged"]),
        ("hold_level", str, ["Light", "Medium", "Strong", "Extra Strong"]),
        ("shine", str, ["Matte", "Low Shine", "High Shine"]),
        ("alcohol_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 233, "name": "Hair Treatments", "is_root": False, "parents": [230], "properties": [
        ("brand", str),
        ("product_type", str, ["Hair Mask", "Leave-in Conditioner", "Scalp Treatment", "Hair Oil", "Serum", "Protein Treatment"]),
        ("hair_concerns", str, ["Dryness", "Damage", "Frizz", "Color Fading", "Hair Loss", "Scalp Issues"]),
        ("hair_type", str, ["Straight", "Wavy", "Curly", "Coily", "Fine", "Thick"]),
        ("sulfate_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 234, "name": "Hair Color", "is_root": False, "parents": [230], "properties": [
        ("brand", str),
        ("color_type", str, ["Permanent", "Semi-Permanent", "Demi-Permanent", "Temporary"]),
        ("shade", str),
        ("suitable_hair_types", str, ["All", "Natural Hair", "Color-treated Hair", "Bleached Hair"]),
        ("ammonia_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 235, "name": "Hair Tools", "is_root": False, "parents": [230], "properties": [
        ("brand", str),
        ("tool_type", str, ["Hair Dryer", "Straightener", "Curling Iron", "Curling Wand", "Hair Clippers", "Hair Brush", "Comb"]),
        ("material", str, ["Ceramic", "Titanium", "Tourmaline", "Plastic", "Wood", "Metal"]),
        ("heat_settings", int),
        ("cordless", bool),
        ("voltage", str, ["110V", "220V", "Dual Voltage"]),
        ("warranty_years", int),
    ]},

    {"id": 236, "name": "Fragrances", "is_root": False, "parents": [5], "properties": []},

    {"id": 237, "name": "Women's Fragrances", "is_root": False, "parents": [236], "properties": [
        ("brand", str),
        ("fragrance_name", str),
        ("fragrance_type", str, ["Eau de Parfum", "Eau de Toilette", "Eau de Cologne", "Perfume Oil", "Body Mist"]),
        ("scent_family", str, ["Floral", "Woody", "Oriental", "Fresh", "Citrus", "Gourmand"]),
        ("size_ml", int),
    ]},

    {"id": 238, "name": "Men's Fragrances", "is_root": False, "parents": [236], "properties": [
        ("brand", str),
        ("fragrance_name", str),
        ("fragrance_type", str, ["Eau de Parfum", "Eau de Toilette", "Eau de Cologne", "Aftershave", "Body Spray"]),
        ("scent_family", str, ["Woody", "Fresh", "Oriental", "Citrus", "Aromatic", "Leather"]),
        ("size_ml", int),
    ]},

    {"id": 239, "name": "Personal Care", "is_root": False, "parents": [5], "properties": []},

    {"id": 240, "name": "Oral Care", "is_root": False, "parents": [239], "properties": [
        ("brand", str),
        ("product_type", str, ["Toothpaste", "Toothbrush", "Electric Toothbrush", "Mouthwash", "Floss", "Whitening Kit"]),
        ("flavor", str),
        ("fluoride_free", bool),
        ("sensitivity_protection", bool),
        ("whitening", bool),
    ]},

    {"id": 241, "name": "Shaving & Hair Removal", "is_root": False, "parents": [239], "properties": [
        ("brand", str),
        ("product_type", str, ["Razor", "Electric Shaver", "Epilator", "Hair Removal Cream", "Waxing Kit", "Trimmer"]),
        ("gender", str, ["Men", "Women", "Unisex"]),
        ("cordless", bool),
        ("number_of_blades", int),
        ("waterproof", bool),
    ]},

    {"id": 242, "name": "Deodorants & Antiperspirants", "is_root": False, "parents": [239], "properties": [
        ("brand", str),
        ("product_type", str, ["Deodorant", "Antiperspirant", "Deodorant Stick", "Roll-On", "Spray", "Gel", "Cream"]),
        ("scent", str),
        ("gender", str, ["Men", "Women", "Unisex"]),
        ("aluminum_free", bool),
        ("long_lasting", bool),
    ]},

    {"id": 243, "name": "Bath & Body", "is_root": False, "parents": [239], "properties": [
        ("brand", str),
        ("product_type", str, ["Body Wash", "Soap", "Body Scrub", "Bath Oil", "Bath Bomb", "Body Lotion", "Body Butter"]),
        ("scent", str),
        ("skin_type", str, ["Oily", "Dry", "Combination", "Normal", "Sensitive"]),
        ("sulfate_free", bool),
        ("paraben_free", bool),
        ("vegan", bool),
        ("cruelty_free", bool),
    ]},

    {"id": 244, "name": "Health Care", "is_root": False, "parents": [5], "properties": []},

    {"id": 245, "name": "Vitamins & Supplements", "is_root": False, "parents": [244], "properties": [
        ("brand", str),
        ("product_type", str, ["Multivitamin", "Mineral Supplement", "Herbal Supplement", "Protein Powder", "Omega-3", "Probiotic"]),
        ("form", str, ["Tablet", "Capsule", "Softgel", "Powder", "Liquid", "Gummy"]),
        ("target_gender", str, ["Men", "Women", "Unisex"]),
        ("age_group", str, ["Adult", "Senior", "Child", "Teen"]),
        ("vegan", bool),
        ("gluten_free", bool),
        ("sugar_free", bool),
        ("allergen_free", bool),
    ]},

    {"id": 246, "name": "Over-the-Counter Medications", "is_root": False, "parents": [244], "properties": [
        ("brand", str),
        ("medication_type", str, ["Pain Reliever", "Cold & Flu", "Allergy", "Digestive Health", "Sleep Aid", "Skin Care"]),
        ("active_ingredient", str),
        ("form", str, ["Tablet", "Capsule", "Liquid", "Cream", "Gel", "Spray"]),
        ("age_group", str, ["Adult", "Child"]),
        ("dosage_mg", int),
    ]},

    {"id": 247, "name": "First Aid", "is_root": False, "parents": [244], "properties": [
        ("product_type", str, ["Bandages", "Gauze", "Antiseptic", "First Aid Kit", "Medical Tape", "Burn Care", "Wound Care"]),
        ("brand", str),
        ("sterile", bool),
        ("hypoallergenic", bool),
        ("waterproof", bool),
    ]},

    {"id": 248, "name": "Medical Equipment", "is_root": False, "parents": [244], "properties": [
        ("product_type", str, ["Blood Pressure Monitor", "Thermometer", "Glucose Meter", "Inhaler", "Nebulizer", "Oximeter", "Wheelchair", "Crutches"]),
        ("brand", str),
        ("digital", bool),
        ("portable", bool),
        ("warranty_years", int),
    ]},

    {"id": 249, "name": "Fitness & Nutrition", "is_root": False, "parents": [5], "properties": []},

    {"id": 250, "name": "Exercise Equipment", "is_root": False, "parents": [249], "properties": [
        ("equipment_type", str, ["Treadmill", "Exercise Bike", "Elliptical", "Dumbbells", "Barbells", "Kettlebells", "Resistance Bands", "Yoga Mat", "Foam Roller"]),
        ("brand", str),
        ("weight_capacity_kg", int),
        ("adjustable", bool),
        ("foldable", bool),
        ("digital_display", bool),
        ("warranty_years", int),
    ]},

    {"id": 251, "name": "Sports Nutrition", "is_root": False, "parents": [249], "properties": [
        ("product_type", str, ["Protein Powder", "Pre-Workout", "Post-Workout", "Amino Acids", "Creatine", "Energy Gel", "Electrolyte Drink"]),
        ("brand", str),
        ("flavor", str),
        ("form", str, ["Powder", "Liquid", "Gel", "Bar", "Capsule"]),
        ("serving_size_g", int),
        ("servings_per_container", int),
        ("vegan", bool),
        ("gluten_free", bool),
        ("sugar_free", bool),
    ]},

    {"id": 252, "name": "Sexual Wellness", "is_root": False, "parents": [5], "properties": []},

    {"id": 253, "name": "Contraceptives", "is_root": False, "parents": [252], "properties": [
        ("product_type", str, ["Condoms", "Birth Control", "Emergency Contraception", "Spermicide"]),
        ("brand", str),
        ("material", str, ["Latex", "Non-Latex", "Polyurethane", "Sheep Skin"]),
        ("lubricated", bool),
        ("size", str, ["Regular", "Large", "Extra Large", "Snug"]),
        ("spermicidal", bool),
    ]},

    {"id": 254, "name": "Lubricants", "is_root": False, "parents": [252], "properties": [
        ("brand", str),
        ("lubricant_type", str, ["Water-based", "Silicone-based", "Oil-based", "Hybrid"]),
        ("flavor", str),
        ("warming", bool),
        ("cooling", bool),
        ("condom_safe", bool),
    ]},

    {"id": 255, "name": "Adult Toys", "is_root": False, "parents": [252], "properties": [
        ("product_type", str, ["Vibrator", "Dildo", "Masturbator", "Anal Toy", "Couples' Toy", "Bondage Gear"]),
        ("brand", str),
        ("material", str, ["Silicone", "Glass", "Metal", "ABS Plastic", "TPE"]),
        ("waterproof", bool),
        ("rechargeable", bool),
        ("remote_controlled", bool),
    ]},

    {"id": 256, "name": "Other Health & Beauty Items", "is_root": False, "parents": [5], "properties": [
        ("description", str),
    ]},

]