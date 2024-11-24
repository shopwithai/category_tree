fashion_and_accessories = [

    {"id": 38, "name": "Women's Clothing", "is_root": False, "parents": [2], "properties": []},

    {"id": 39, "name": "Tops", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("sleeve_length", str, ["Sleeveless", "Short Sleeve", "3/4 Sleeve", "Long Sleeve"]),
        ("neckline", str, ["V-Neck", "Round Neck", "Collared", "Boat Neck", "Off Shoulder"]),
        ("style", str, ["Blouse", "T-Shirt", "Tank Top", "Sweater", "Cardigan", "Hoodie"]),
        ("pattern", str, ["Solid", "Striped", "Floral", "Polka Dot", "Plaid", "Graphic"]),
        ("fit", str, ["Regular", "Slim", "Loose", "Oversized"]),
        ("occasion", str, ["Casual", "Formal", "Party", "Workwear", "Athleisure"]),
    ]},

    {"id": 40, "name": "Dresses", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("dress_length", str, ["Mini", "Knee Length", "Midi", "Maxi"]),
        ("sleeve_length", str, ["Sleeveless", "Short Sleeve", "3/4 Sleeve", "Long Sleeve"]),
        ("neckline", str, ["V-Neck", "Round Neck", "Halter", "Off Shoulder", "Sweetheart"]),
        ("style", str, ["A-line", "Bodycon", "Shift", "Wrap", "Sheath", "Fit & Flare"]),
        ("pattern", str, ["Solid", "Striped", "Floral", "Polka Dot", "Plaid", "Print"]),
        ("occasion", str, ["Casual", "Formal", "Party", "Cocktail", "Evening", "Wedding"]),
    ]},

    {"id": 41, "name": "Bottoms (Jeans, Skirts, Pants)", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("type", str, ["Jeans", "Skirt", "Pants", "Shorts", "Leggings", "Capris"]),
        ("fit", str, ["Skinny", "Slim", "Regular", "Relaxed", "Wide Leg", "Bootcut"]),
        ("rise", str, ["High Rise", "Mid Rise", "Low Rise"]),
        ("length", str, ["Full Length", "Ankle Length", "Knee Length", "Above Knee", "Short"]),
        ("pattern", str, ["Solid", "Striped", "Floral", "Printed", "Plaid", "Embroidered"]),
        ("closure_type", str, ["Button", "Zipper", "Elastic", "Drawstring"]),
        ("style", str, ["Denim", "Chinos", "Cargo", "Pencil Skirt", "A-line Skirt"]),
    ]},

    {"id": 42, "name": "Outerwear (Coats, Jackets)", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("type", str, ["Coat", "Jacket", "Blazer", "Vest", "Raincoat", "Poncho"]),
        ("style", str, ["Trench", "Bomber", "Denim", "Leather", "Puffer", "Cardigan"]),
        ("closure_type", str, ["Button", "Zipper", "Open Front", "Belted"]),
        ("hooded", bool),
        ("insulated", bool),
        ("pattern", str, ["Solid", "Plaid", "Printed", "Fur Trim", "Embroidered"]),
        ("length", str, ["Waist Length", "Hip Length", "Thigh Length", "Knee Length", "Long"]),
    ]},

    {"id": 43, "name": "Swimwear", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("type", str, ["One-Piece", "Bikini", "Tankini", "Cover-Up", "Swim Dress"]),
        ("top_style", str, ["Triangle", "Halter", "Bandeau", "Underwire", "Sport"]),
        ("bottom_style", str, ["Brief", "Hipster", "High Waist", "Thong", "Skirted"]),
        ("pattern", str, ["Solid", "Striped", "Floral", "Polka Dot", "Printed"]),
        ("features", str, ["Push-Up", "Tummy Control", "Quick Dry", "UV Protection"]),
    ]},

    {"id": 44, "name": "Activewear", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("type", str, ["Leggings", "Sports Bra", "Tank Top", "Shorts", "Jacket", "Sweatshirt"]),
        ("activity", str, ["Yoga", "Running", "Gym", "Training", "Cycling", "Hiking"]),
        ("features", str, ["Moisture-Wicking", "Breathable", "Compression", "Stretch"]),
        ("pattern", str, ["Solid", "Printed", "Color Block", "Mesh"]),
        ("fit", str, ["Fitted", "Regular", "Loose"]),
    ]},

    {"id": 45, "name": "Intimates & Sleepwear", "is_root": False, "parents": [38], "properties": [
        ("brand", str),
        ("size", str),
        ("material", str),
        ("type", str, ["Bra", "Panties", "Lingerie", "Pajamas", "Nightgown", "Robe", "Camisole"]),
        ("cup_size", str),
        ("band_size", int),
        ("style", str, ["Push-Up", "Underwire", "Wireless", "Balconette", "Bralette", "Chemise"]),
        ("pattern", str, ["Solid", "Lace", "Printed", "Embroidered", "Satin"]),
        ("features", str, ["Padded", "Non-Padded", "Seamless", "Adjustable Straps"]),
    ]},

    {"id": 46, "name": "Men's Clothing", "is_root": False, "parents": [2], "properties": []},

    {"id": 47, "name": "Shirts", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]),
        ("material", str),
        ("sleeve_length", str, ["Short Sleeve", "Long Sleeve", "Sleeveless"]),
        ("collar_type", str, ["Spread", "Button-Down", "Mandarin", "Crew Neck", "V-Neck"]),
        ("fit", str, ["Regular", "Slim", "Tailored", "Relaxed"]),
        ("pattern", str, ["Solid", "Striped", "Plaid", "Printed", "Checked"]),
        ("style", str, ["Dress Shirt", "Casual Shirt", "T-Shirt", "Polo", "Henley"]),
        ("occasion", str, ["Casual", "Formal", "Workwear", "Sports"]),
    ]},

    {"id": 48, "name": "Trousers & Jeans", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size_waist", int),
        ("size_length", int),
        ("material", str),
        ("type", str, ["Jeans", "Chinos", "Dress Pants", "Cargo Pants", "Shorts"]),
        ("fit", str, ["Regular", "Slim", "Skinny", "Relaxed", "Straight"]),
        ("rise", str, ["High Rise", "Mid Rise", "Low Rise"]),
        ("pattern", str, ["Solid", "Printed", "Distressed", "Washed"]),
        ("closure_type", str, ["Button", "Zipper", "Drawstring"]),
        ("style", str, ["Denim", "Formal", "Casual", "Workwear"]),
    ]},

    {"id": 49, "name": "Suits & Blazers", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size", str, ["36", "38", "40", "42", "44", "46", "48", "50"]),
        ("material", str),
        ("type", str, ["Suit", "Blazer", "Sport Coat", "Tuxedo"]),
        ("fit", str, ["Regular", "Slim", "Tailored", "Classic"]),
        ("pattern", str, ["Solid", "Pinstripe", "Plaid", "Herringbone", "Checked"]),
        ("number_of_buttons", int, [1, 2, 3]),
        ("lapel_style", str, ["Notch", "Peak", "Shawl"]),
        ("vent_style", str, ["Single Vent", "Double Vent", "No Vent"]),
        ("occasion", str, ["Formal", "Business", "Wedding", "Casual"]),
    ]},

    {"id": 50, "name": "Outerwear", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size", str, ["XS", "S", "M", "L", "XL", "XXL", "XXXL"]),
        ("material", str),
        ("type", str, ["Coat", "Jacket", "Blazer", "Vest", "Raincoat"]),
        ("style", str, ["Trench", "Bomber", "Denim", "Leather", "Puffer", "Peacoat"]),
        ("closure_type", str, ["Button", "Zipper", "Open Front", "Snap"]),
        ("hooded", bool),
        ("insulated", bool),
        ("pattern", str, ["Solid", "Plaid", "Printed", "Striped"]),
        ("length", str, ["Waist Length", "Hip Length", "Thigh Length", "Knee Length"]),
    ]},

    {"id": 51, "name": "Activewear", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size", str, ["S", "M", "L", "XL", "XXL", "XXXL"]),
        ("material", str),
        ("type", str, ["Shorts", "T-Shirts", "Sweatpants", "Hoodies", "Tracksuits", "Jackets"]),
        ("activity", str, ["Running", "Gym", "Training", "Cycling", "Hiking"]),
        ("features", str, ["Moisture-Wicking", "Breathable", "Compression", "Stretch"]),
        ("pattern", str, ["Solid", "Printed", "Color Block", "Striped"]),
        ("fit", str, ["Fitted", "Regular", "Loose"]),
    ]},

    {"id": 52, "name": "Underwear & Socks", "is_root": False, "parents": [46], "properties": [
        ("brand", str),
        ("size", str, ["S", "M", "L", "XL", "XXL"]),
        ("material", str),
        ("type", str, ["Boxers", "Briefs", "Boxer Briefs", "Trunks", "Socks", "Undershirts"]),
        ("pattern", str, ["Solid", "Striped", "Printed", "Plaid"]),
        ("features", str, ["Moisture-Wicking", "Breathable", "Seamless", "Stretch"]),
        ("sock_length", str, ["No Show", "Ankle", "Crew", "Knee High"]),
    ]},

    {"id": 53, "name": "Kids' Clothing", "is_root": False, "parents": [2], "properties": []},

    {"id": 54, "name": "Boys' Clothing", "is_root": False, "parents": [53], "properties": [
        ("brand", str),
        ("size", str, ["Infant", "Toddler", "XS", "S", "M", "L", "XL"]),
        ("material", str),
        ("type", str, ["Tops", "Bottoms", "Outerwear", "Sleepwear", "Activewear"]),
        ("pattern", str, ["Solid", "Striped", "Printed", "Graphic", "Plaid"]),
        ("features", str, ["Adjustable Waist", "Easy Closure", "Tagless"]),
        ("age_group", str, ["0-12 Months", "1-3 Years", "4-6 Years", "7-9 Years", "10-12 Years"]),
    ]},

    {"id": 55, "name": "Girls' Clothing", "is_root": False, "parents": [53], "properties": [
        ("brand", str),
        ("size", str, ["Infant", "Toddler", "XS", "S", "M", "L", "XL"]),
        ("material", str),
        ("type", str, ["Tops", "Dresses", "Bottoms", "Outerwear", "Sleepwear", "Activewear"]),
        ("pattern", str, ["Solid", "Floral", "Printed", "Graphic", "Plaid"]),
        ("features", str, ["Adjustable Waist", "Easy Closure", "Tagless"]),
        ("age_group", str, ["0-12 Months", "1-3 Years", "4-6 Years", "7-9 Years", "10-12 Years"]),
    ]},

    {"id": 56, "name": "Baby Clothing", "is_root": False, "parents": [53], "properties": [
        ("brand", str),
        ("size", str, ["Preemie", "Newborn", "0-3 Months", "3-6 Months", "6-9 Months", "9-12 Months"]),
        ("material", str),
        ("type", str, ["Onesies", "Sleepers", "Sets", "Outerwear", "Accessories"]),
        ("pattern", str, ["Solid", "Animal", "Printed", "Striped"]),
        ("features", str, ["Easy Closure", "Tagless", "Organic Material"]),
        ("gender", str, ["Unisex", "Boy", "Girl"]),
    ]},

    {"id": 57, "name": "Shoes", "is_root": False, "parents": [2], "properties": []},

    {"id": 58, "name": "Women's Shoes", "is_root": False, "parents": [57], "properties": [
        ("brand", str),
        ("size", float),
        ("width", str, ["Narrow", "Regular", "Wide"]),
        ("material", str),
        ("type", str, ["Heels", "Flats", "Sneakers", "Sandals", "Boots", "Slippers"]),
        ("heel_height_inches", float),
        ("closure_type", str, ["Slip-On", "Lace-Up", "Buckle", "Velcro", "Zip"]),
        ("pattern", str, ["Solid", "Animal Print", "Floral", "Embellished"]),
        ("occasion", str, ["Casual", "Formal", "Athletic", "Work"]),
    ]},

    {"id": 59, "name": "Men's Shoes", "is_root": False, "parents": [57], "properties": [
        ("brand", str),
        ("size", float),
        ("width", str, ["Narrow", "Regular", "Wide"]),
        ("material", str),
        ("type", str, ["Dress Shoes", "Casual Shoes", "Sneakers", "Boots", "Sandals", "Slippers"]),
        ("closure_type", str, ["Slip-On", "Lace-Up", "Velcro", "Buckle"]),
        ("pattern", str, ["Solid", "Printed", "Textured"]),
        ("occasion", str, ["Casual", "Formal", "Athletic", "Work"]),
    ]},

    {"id": 60, "name": "Kids' Shoes", "is_root": False, "parents": [57], "properties": [
        ("brand", str),
        ("size", float),
        ("material", str),
        ("type", str, ["Sneakers", "Sandals", "Boots", "Dress Shoes", "Slippers"]),
        ("closure_type", str, ["Slip-On", "Lace-Up", "Velcro", "Buckle"]),
        ("pattern", str, ["Solid", "Character", "Printed", "Light-Up"]),
        ("features", str, ["Non-Slip", "Light-Up", "Easy On/Off"]),
        ("gender", str, ["Unisex", "Boys", "Girls"]),
    ]},

    {"id": 61, "name": "Accessories", "is_root": False, "parents": [2], "properties": []},

    {"id": 62, "name": "Bags & Wallets", "is_root": False, "parents": [61], "properties": []},

    {"id": 63, "name": "Handbags", "is_root": False, "parents": [62], "properties": [
        ("brand", str),
        ("material", str),
        ("type", str, ["Tote", "Satchel", "Crossbody", "Clutch", "Shoulder Bag", "Hobo"]),
        ("pattern", str, ["Solid", "Printed", "Embossed", "Quilted"]),
        ("closure_type", str, ["Zipper", "Magnetic", "Snap", "Open"]),
        ("number_of_pockets", int),
        ("strap_length_cm", int),
        ("features", str, ["Adjustable Strap", "Convertible", "Detachable Strap"]),
    ]},

    {"id": 64, "name": "Backpacks", "is_root": False, "parents": [62], "properties": [
        ("brand", str),
        ("material", str),
        ("capacity_liters", int),
        ("compartments", int),
        ("laptop_compartment", bool),
        ("water_resistant", bool),
        ("pattern", str, ["Solid", "Printed", "Camouflage"]),
        ("features", str, ["Padded Straps", "USB Port", "Anti-Theft"]),
    ]},

    {"id": 65, "name": "Wallets", "is_root": False, "parents": [62], "properties": [
        ("brand", str),
        ("material", str),
        ("type", str, ["Bi-Fold", "Tri-Fold", "Card Holder", "Money Clip", "Wristlet"]),
        ("number_of_card_slots", int),
        ("pattern", str, ["Solid", "Embossed", "Printed"]),
        ("closure_type", str, ["Snap", "Zipper", "None"]),
        ("rfid_blocking", bool),
    ]},

    {"id": 66, "name": "Luggage", "is_root": False, "parents": [62], "properties": [
        ("brand", str),
        ("material", str),
        ("type", str, ["Carry-On", "Checked", "Duffel", "Spinner", "Set"]),
        ("size_inches", str, ["Under 21", "21-24", "25-27", "28 and above"]),
        ("number_of_wheels", int),
        ("expandable", bool),
        ("lock_type", str, ["Combination", "Key", "TSA Approved", "None"]),
        ("weight_kg", float),
    ]},

    {"id": 67, "name": "Jewelry", "is_root": False, "parents": [61], "properties": []},

    {"id": 68, "name": "Necklaces", "is_root": False, "parents": [67], "properties": [
        ("brand", str),
        ("material", str, ["Gold", "Silver", "Platinum", "Stainless Steel", "Leather", "Beads"]),
        ("length_cm", int),
        ("style", str, ["Pendant", "Chain", "Choker", "Locket"]),
        ("gemstone", str),
        ("carat_weight", float),
        ("clasp_type", str, ["Lobster", "Spring Ring", "Toggle", "Magnetic"]),
        ("features", str, ["Adjustable Length", "Engravable"]),
    ]},

    {"id": 69, "name": "Rings", "is_root": False, "parents": [67], "properties": [
        ("brand", str),
        ("material", str, ["Gold", "Silver", "Platinum", "Titanium", "Stainless Steel"]),
        ("ring_size", float),
        ("style", str, ["Engagement", "Wedding Band", "Fashion", "Statement"]),
        ("gemstone", str),
        ("carat_weight", float),
        ("setting_type", str, ["Prong", "Bezel", "Channel", "Pave"]),
        ("features", str, ["Stackable", "Adjustable"]),
    ]},

    {"id": 70, "name": "Earrings", "is_root": False, "parents": [67], "properties": [
        ("brand", str),
        ("material", str, ["Gold", "Silver", "Platinum", "Stainless Steel", "Beads"]),
        ("style", str, ["Stud", "Hoop", "Dangle", "Drop", "Chandelier"]),
        ("gemstone", str),
        ("carat_weight", float),
        ("back_finding", str, ["Push Back", "Screw Back", "Leverback", "Fish Hook"]),
        ("features", str, ["Hypoallergenic", "Handmade"]),
    ]},

    {"id": 71, "name": "Bracelets", "is_root": False, "parents": [67], "properties": [
        ("brand", str),
        ("material", str, ["Gold", "Silver", "Platinum", "Leather", "Beads"]),
        ("length_cm", int),
        ("style", str, ["Bangle", "Chain", "Cuff", "Charm"]),
        ("gemstone", str),
        ("carat_weight", float),
        ("clasp_type", str, ["Lobster", "Spring Ring", "Toggle", "Magnetic"]),
        ("features", str, ["Adjustable", "Engravable"]),
    ]},

    {"id": 72, "name": "Watches", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("model", str),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
        ("movement_type", str, ["Quartz", "Mechanical", "Automatic", "Digital", "Smart"]),
        ("band_material", str, ["Leather", "Metal", "Rubber", "Nylon"]),
        ("case_material", str, ["Stainless Steel", "Gold", "Titanium", "Plastic"]),
        ("water_resistant_meters", int),
        ("features", str, ["Chronograph", "Date", "Alarm", "GPS", "Heart Rate Monitor"]),
    ]},

    {"id": 73, "name": "Sunglasses & Eyewear", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
        ("frame_material", str, ["Metal", "Plastic", "Wood", "Titanium"]),
        ("lens_material", str, ["Glass", "Plastic", "Polycarbonate"]),
        ("lens_color", str),
        ("frame_shape", str, ["Aviator", "Round", "Square", "Rectangular", "Cat Eye", "Wayfarer"]),
        ("polarized", bool),
        ("uv_protection", bool),
        ("features", str, ["Photochromic", "Mirrored", "Gradient"]),
    ]},

    {"id": 74, "name": "Hats", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("size", str, ["S", "M", "L", "XL", "One Size"]),
        ("material", str),
        ("type", str, ["Baseball Cap", "Beanie", "Fedora", "Sun Hat", "Bucket Hat", "Visor"]),
        ("pattern", str, ["Solid", "Printed", "Embroidered"]),
        ("features", str, ["Adjustable", "Foldable", "Breathable"]),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
    ]},

    {"id": 75, "name": "Belts", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("size", str),
        ("material", str, ["Leather", "Synthetic", "Fabric", "Canvas"]),
        ("width_cm", float),
        ("buckle_type", str, ["Pin", "Plate", "Automatic", "D-Ring"]),
        ("pattern", str, ["Solid", "Braided", "Embossed"]),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
    ]},

    {"id": 76, "name": "Scarves & Wraps", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("material", str, ["Wool", "Cotton", "Silk", "Cashmere", "Synthetic"]),
        ("length_cm", int),
        ("width_cm", int),
        ("pattern", str, ["Solid", "Plaid", "Printed", "Striped"]),
        ("style", str, ["Infinity", "Pashmina", "Shawl", "Wrap"]),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
    ]},

    {"id": 77, "name": "Ties & Pocket Squares", "is_root": False, "parents": [61], "properties": [
        ("brand", str),
        ("material", str, ["Silk", "Polyester", "Cotton", "Wool"]),
        ("length_cm", int),
        ("width_cm", float),
        ("pattern", str, ["Solid", "Striped", "Paisley", "Plaid", "Printed"]),
        ("type", str, ["Necktie", "Bow Tie", "Pocket Square", "Tie Set"]),
        ("features", str, ["Pre-Tied", "Handmade"]),
    ]},

    {"id": 78, "name": "Beauty & Personal Care", "is_root": False, "parents": [2], "properties": []},

    {"id": 79, "name": "Skincare", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("product_type", str, ["Moisturizer", "Cleanser", "Serum", "Toner", "Exfoliant", "Mask"]),
        ("skin_type", str, ["Normal", "Dry", "Oily", "Combination", "Sensitive"]),
        ("ingredients", str),
        ("volume_ml", int),
        ("features", str, ["Organic", "Paraben-Free", "Cruelty-Free", "Hypoallergenic", "Fragrance-Free"]),
    ]},

    {"id": 80, "name": "Makeup", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("product_type", str, ["Foundation", "Lipstick", "Mascara", "Eyeshadow", "Blush", "Concealer"]),
        ("shade", str),
        ("skin_tone", str, ["Fair", "Light", "Medium", "Tan", "Deep"]),
        ("finish", str, ["Matte", "Glossy", "Satin", "Shimmer"]),
        ("features", str, ["Long-Lasting", "Waterproof", "Vegan", "Cruelty-Free"]),
    ]},

    {"id": 81, "name": "Fragrances", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("fragrance_type", str, ["Eau de Parfum", "Eau de Toilette", "Cologne", "Body Mist"]),
        ("scent_family", str, ["Floral", "Woody", "Fresh", "Oriental", "Citrus"]),
        ("volume_ml", int),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
        ("features", str, ["Natural", "Alcohol-Free"]),
    ]},

    {"id": 82, "name": "Hair Care", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("product_type", str, ["Shampoo", "Conditioner", "Hair Treatment", "Styling Product", "Hair Color"]),
        ("hair_type", str, ["Normal", "Dry", "Oily", "Curly", "Straight", "Color-Treated"]),
        ("ingredients", str),
        ("volume_ml", int),
        ("features", str, ["Sulfate-Free", "Paraben-Free", "Organic", "Cruelty-Free"]),
    ]},

    {"id": 83, "name": "Nail Care", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("product_type", str, ["Nail Polish", "Nail Treatment", "Manicure Tools", "Pedicure Tools"]),
        ("color", str),
        ("finish", str, ["Matte", "Glossy", "Glitter", "Metallic"]),
        ("features", str, ["Quick-Dry", "Long-Lasting", "Vegan", "Cruelty-Free"]),
    ]},

    {"id": 84, "name": "Tools & Accessories", "is_root": False, "parents": [78], "properties": [
        ("brand", str),
        ("product_type", str, ["Makeup Brush", "Hair Dryer", "Curling Iron", "Straightener", "Shaving Tool"]),
        ("features", str, ["Cordless", "Heat Settings", "Travel Size"]),
        ("material", str),
        ("gender", str, ["Men's", "Women's", "Unisex"]),
    ]},

]
