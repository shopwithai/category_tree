categories = [
    # Root Categories
    {"id": 1, "name": "Automotive & Vehicles", "is_root": True, "parents": []},
    {"id": 2, "name": "Fashion & Accessories", "is_root": True, "parents": []},
    {"id": 3, "name": "Electronics & Computers", "is_root": True, "parents": []},
    {"id": 4, "name": "Home & Garden", "is_root": True, "parents": []},
    {"id": 5, "name": "Health & Beauty", "is_root": True, "parents": []},
    {"id": 6, "name": "Books, Movies & Music", "is_root": True, "parents": []},
    {"id": 7, "name": "Sports & Outdoors", "is_root": True, "parents": []},
    {"id": 8, "name": "Toys, Games & Hobbies", "is_root": True, "parents": []},
    {"id": 9, "name": "Baby & Kids", "is_root": True, "parents": []},
    {"id": 10, "name": "Food & Grocery", "is_root": True, "parents": []},
    {"id": 11, "name": "Pets", "is_root": True, "parents": []},
    {"id": 12, "name": "Travel & Experiences", "is_root": True, "parents": []},
    {"id": 13, "name": "Services", "is_root": True, "parents": []},
    {"id": 14, "name": "Industrial & Business", "is_root": True, "parents": []},
    {"id": 15, "name": "Real Estate", "is_root": True, "parents": []},
    {"id": 16, "name": "Deals & Discounts", "is_root": True, "parents": []},
    {"id": 17, "name": "Software & Subscriptions", "is_root": True, "parents": []},
    {"id": 18, "name": "Luxury & High-End Goods", "is_root": True, "parents": []},
    {"id": 19, "name": "Gifts & Occasions", "is_root": True, "parents": []},
    {"id": 20, "name": "Miscellaneous", "is_root": True, "parents": []},

    # Automotive & Vehicles
    {"id": 21, "name": "Cars", "is_root": False, "parents": [1]},
    {"id": 22, "name": "New Cars", "is_root": False, "parents": [21]},
    {"id": 23, "name": "Used Cars", "is_root": False, "parents": [21]},
    {"id": 24, "name": "Motorcycles", "is_root": False, "parents": [1]},
    {"id": 25, "name": "Trucks & Vans", "is_root": False, "parents": [1]},
    {"id": 26, "name": "Recreational Vehicles (RVs)", "is_root": False, "parents": [1]},
    {"id": 27, "name": "Boats & Watercraft", "is_root": False, "parents": [1]},
    {"id": 28, "name": "Vehicle Parts & Accessories", "is_root": False, "parents": [1]},
    {"id": 29, "name": "Car Parts", "is_root": False, "parents": [28]},
    {"id": 30, "name": "Motorcycle Parts", "is_root": False, "parents": [28]},
    {"id": 31, "name": "Tires & Wheels", "is_root": False, "parents": [28]},
    {"id": 32, "name": "Vehicle Electronics", "is_root": False, "parents": [28]},
    {"id": 33, "name": "Exterior Accessories", "is_root": False, "parents": [28]},
    {"id": 34, "name": "Interior Accessories", "is_root": False, "parents": [28]},
    {"id": 35, "name": "Other Vehicles", "is_root": False, "parents": [1]},
    {"id": 36, "name": "Bicycles", "is_root": False, "parents": [35]},
    {"id": 37, "name": "ATVs & UTVs", "is_root": False, "parents": [35]},

    # Fashion & Accessories
    {"id": 38, "name": "Women's Clothing", "is_root": False, "parents": [2]},
    {"id": 39, "name": "Tops", "is_root": False, "parents": [38]},
    {"id": 40, "name": "Dresses", "is_root": False, "parents": [38]},
    {"id": 41, "name": "Bottoms (Jeans, Skirts, Pants)", "is_root": False, "parents": [38]},
    {"id": 42, "name": "Outerwear (Coats, Jackets)", "is_root": False, "parents": [38]},
    {"id": 43, "name": "Swimwear", "is_root": False, "parents": [38]},
    {"id": 44, "name": "Activewear", "is_root": False, "parents": [38]},
    {"id": 45, "name": "Intimates & Sleepwear", "is_root": False, "parents": [38]},
    {"id": 46, "name": "Men's Clothing", "is_root": False, "parents": [2]},
    {"id": 47, "name": "Shirts", "is_root": False, "parents": [46]},
    {"id": 48, "name": "Trousers & Jeans", "is_root": False, "parents": [46]},
    {"id": 49, "name": "Suits & Blazers", "is_root": False, "parents": [46]},
    {"id": 50, "name": "Outerwear", "is_root": False, "parents": [46]},
    {"id": 51, "name": "Activewear", "is_root": False, "parents": [46]},
    {"id": 52, "name": "Underwear & Socks", "is_root": False, "parents": [46]},
    {"id": 53, "name": "Kids' Clothing", "is_root": False, "parents": [2]},
    {"id": 54, "name": "Boys' Clothing", "is_root": False, "parents": [53]},
    {"id": 55, "name": "Girls' Clothing", "is_root": False, "parents": [53]},
    {"id": 56, "name": "Baby Clothing", "is_root": False, "parents": [53]},
    {"id": 57, "name": "Shoes", "is_root": False, "parents": [2]},
    {"id": 58, "name": "Women's Shoes", "is_root": False, "parents": [57]},
    {"id": 59, "name": "Men's Shoes", "is_root": False, "parents": [57]},
    {"id": 60, "name": "Kids' Shoes", "is_root": False, "parents": [57]},
    {"id": 61, "name": "Accessories", "is_root": False, "parents": [2]},
    {"id": 62, "name": "Bags & Wallets", "is_root": False, "parents": [61]},
    {"id": 63, "name": "Handbags", "is_root": False, "parents": [62]},
    {"id": 64, "name": "Backpacks", "is_root": False, "parents": [62]},
    {"id": 65, "name": "Wallets", "is_root": False, "parents": [62]},
    {"id": 66, "name": "Luggage", "is_root": False, "parents": [62]},
    {"id": 67, "name": "Jewelry", "is_root": False, "parents": [61]},
    {"id": 68, "name": "Necklaces", "is_root": False, "parents": [67]},
    {"id": 69, "name": "Rings", "is_root": False, "parents": [67]},
    {"id": 70, "name": "Earrings", "is_root": False, "parents": [67]},
    {"id": 71, "name": "Bracelets", "is_root": False, "parents": [67]},
    {"id": 72, "name": "Watches", "is_root": False, "parents": [61]},
    {"id": 73, "name": "Sunglasses & Eyewear", "is_root": False, "parents": [61]},
    {"id": 74, "name": "Hats", "is_root": False, "parents": [61]},
    {"id": 75, "name": "Belts", "is_root": False, "parents": [61]},
    {"id": 76, "name": "Scarves & Wraps", "is_root": False, "parents": [61]},
    {"id": 77, "name": "Ties & Pocket Squares", "is_root": False, "parents": [61]},
    {"id": 78, "name": "Beauty & Personal Care", "is_root": False, "parents": [2]},
    {"id": 79, "name": "Skincare", "is_root": False, "parents": [78]},
    {"id": 80, "name": "Makeup", "is_root": False, "parents": [78]},
    {"id": 81, "name": "Fragrances", "is_root": False, "parents": [78]},
    {"id": 82, "name": "Hair Care", "is_root": False, "parents": [78]},
    {"id": 83, "name": "Nail Care", "is_root": False, "parents": [78]},
    {"id": 84, "name": "Tools & Accessories", "is_root": False, "parents": [78]},

    # Electronics & Computers
    # moved to own file

    # Home & Garden
    {"id": 138, "name": "Furniture", "is_root": False, "parents": [4]},
    {"id": 139, "name": "Living Room Furniture", "is_root": False, "parents": [138]},
    {"id": 140, "name": "Sofas & Sectionals", "is_root": False, "parents": [139]},
    {"id": 141, "name": "Coffee & End Tables", "is_root": False, "parents": [139]},
    {"id": 142, "name": "TV Stands & Entertainment Centers", "is_root": False, "parents": [139]},
    {"id": 143, "name": "Bedroom Furniture", "is_root": False, "parents": [138]},
    {"id": 144, "name": "Beds & Headboards", "is_root": False, "parents": [143]},
    {"id": 145, "name": "Dressers & Chests", "is_root": False, "parents": [143]},
    {"id": 146, "name": "Nightstands", "is_root": False, "parents": [143]},
    {"id": 147, "name": "Dining Room Furniture", "is_root": False, "parents": [138]},
    {"id": 148, "name": "Dining Tables", "is_root": False, "parents": [147]},
    {"id": 149, "name": "Dining Chairs & Benches", "is_root": False, "parents": [147]},
    {"id": 150, "name": "Bar Stools", "is_root": False, "parents": [147]},
    {"id": 151, "name": "Office Furniture", "is_root": False, "parents": [138]},
    {"id": 152, "name": "Desks", "is_root": False, "parents": [151]},
    {"id": 153, "name": "Office Chairs", "is_root": False, "parents": [151]},
    {"id": 154, "name": "Bookcases & Shelving", "is_root": False, "parents": [151]},
    {"id": 155, "name": "Outdoor Furniture", "is_root": False, "parents": [138]},
    {"id": 156, "name": "Patio Sets", "is_root": False, "parents": [155]},
    {"id": 157, "name": "Outdoor Seating", "is_root": False, "parents": [155]},
    {"id": 158, "name": "Umbrellas & Shade", "is_root": False, "parents": [155]},
    {"id": 159, "name": "Home Décor", "is_root": False, "parents": [4]},
    {"id": 160, "name": "Rugs", "is_root": False, "parents": [159]},
    {"id": 161, "name": "Lighting", "is_root": False, "parents": [159]},
    {"id": 162, "name": "Ceiling Lights", "is_root": False, "parents": [161]},
    {"id": 163, "name": "Lamps", "is_root": False, "parents": [161]},
    {"id": 164, "name": "Wall Lights", "is_root": False, "parents": [161]},
    {"id": 165, "name": "Wall Art & Decor", "is_root": False, "parents": [159]},
    {"id": 166, "name": "Mirrors", "is_root": False, "parents": [159]},
    {"id": 167, "name": "Clocks", "is_root": False, "parents": [159]},
    {"id": 168, "name": "Kitchen & Dining", "is_root": False, "parents": [4]},
    {"id": 169, "name": "Cookware & Bakeware", "is_root": False, "parents": [168]},
    {"id": 170, "name": "Dinnerware & Serveware", "is_root": False, "parents": [168]},
    {"id": 171, "name": "Kitchen Appliances", "is_root": False, "parents": [168]},
    {"id": 172, "name": "Refrigerators", "is_root": False, "parents": [171]},
    {"id": 173, "name": "Ovens & Ranges", "is_root": False, "parents": [171]},
    {"id": 174, "name": "Dishwashers", "is_root": False, "parents": [171]},
    {"id": 175, "name": "Microwaves", "is_root": False, "parents": [171]},
    {"id": 176, "name": "Kitchen Tools & Gadgets", "is_root": False, "parents": [168]},
    {"id": 177, "name": "Bedding & Bath", "is_root": False, "parents": [4]},
    {"id": 178, "name": "Bedding Sets", "is_root": False, "parents": [177]},
    {"id": 179, "name": "Sheets & Pillowcases", "is_root": False, "parents": [177]},
    {"id": 180, "name": "Comforters & Duvet Inserts", "is_root": False, "parents": [177]},
    {"id": 181, "name": "Towels", "is_root": False, "parents": [177]},
    {"id": 182, "name": "Bath Accessories", "is_root": False, "parents": [177]},
    {"id": 183, "name": "Appliances", "is_root": False, "parents": [4]},
    {"id": 184, "name": "Washers & Dryers", "is_root": False, "parents": [183]},
    {"id": 185, "name": "Vacuum Cleaners", "is_root": False, "parents": [183]},
    {"id": 186, "name": "Air Conditioners & Heaters", "is_root": False, "parents": [183]},
    {"id": 187, "name": "Tools & Home Improvement", "is_root": False, "parents": [4]},
    {"id": 188, "name": "Power Tools", "is_root": False, "parents": [187]},
    {"id": 189, "name": "Hand Tools", "is_root": False, "parents": [187]},
    {"id": 190, "name": "Hardware", "is_root": False, "parents": [187]},
    {"id": 191, "name": "Electrical Supplies", "is_root": False, "parents": [187]},
    {"id": 192, "name": "Plumbing Supplies", "is_root": False, "parents": [187]},
    {"id": 193, "name": "Paint & Wall Treatments", "is_root": False, "parents": [187]},
    {"id": 194, "name": "Lawn & Garden", "is_root": False, "parents": [4]},
    {"id": 195, "name": "Gardening Tools", "is_root": False, "parents": [194]},
    {"id": 196, "name": "Plants & Seeds", "is_root": False, "parents": [194]},
    {"id": 197, "name": "Outdoor Power Equipment", "is_root": False, "parents": [194]},
    {"id": 198, "name": "Lawn Mowers", "is_root": False, "parents": [197]},
    {"id": 199, "name": "Trimmers", "is_root": False, "parents": [197]},
    {"id": 200, "name": "Grills & Outdoor Cooking", "is_root": False, "parents": [194]},
    {"id": 201, "name": "Garden Decor", "is_root": False, "parents": [194]},
    {"id": 202, "name": "Storage & Organization", "is_root": False, "parents": [4]},
    {"id": 203, "name": "Closet Storage", "is_root": False, "parents": [202]},
    {"id": 204, "name": "Garage Storage", "is_root": False, "parents": [202]},
    {"id": 205, "name": "Shelving Units", "is_root": False, "parents": [202]},
    {"id": 206, "name": "Bins & Containers", "is_root": False, "parents": [202]},
    {"id": 207, "name": "Cleaning Supplies", "is_root": False, "parents": [4]},
    {"id": 208, "name": "Cleaning Tools", "is_root": False, "parents": [207]},
    {"id": 209, "name": "Household Cleaners", "is_root": False, "parents": [207]},
    {"id": 210, "name": "Trash & Recycling", "is_root": False, "parents": [207]},
    {"id": 211, "name": "Safety & Security", "is_root": False, "parents": [4]},
    {"id": 212, "name": "Home Security Systems", "is_root": False, "parents": [211]},
    {"id": 213, "name": "Smoke & Carbon Monoxide Detectors", "is_root": False, "parents": [211]},
    {"id": 214, "name": "Safes", "is_root": False, "parents": [211]},
    {"id": 215, "name": "Pet Supplies", "is_root": False, "parents": [4, 11]},  # Also under "Pets"
    {"id": 216, "name": "Beds & Furniture", "is_root": False, "parents": [215]},
    {"id": 217, "name": "Feeding & Watering Supplies", "is_root": False, "parents": [215]},
    {"id": 218, "name": "Toys", "is_root": False, "parents": [215]},
    {"id": 219, "name": "Grooming", "is_root": False, "parents": [215]},
    {"id": 220, "name": "Other Home & Garden Items", "is_root": False, "parents": [4]},

    # Health & Beauty
    {"id": 221, "name": "Makeup", "is_root": False, "parents": [5]},
    {"id": 222, "name": "Face", "is_root": False, "parents": [221]},
    {"id": 223, "name": "Eyes", "is_root": False, "parents": [221]},
    {"id": 224, "name": "Lips", "is_root": False, "parents": [221]},
    {"id": 225, "name": "Skincare", "is_root": False, "parents": [5]},
    {"id": 226, "name": "Cleansers", "is_root": False, "parents": [225]},
    {"id": 227, "name": "Moisturizers", "is_root": False, "parents": [225]},
    {"id": 228, "name": "Treatments & Serums", "is_root": False, "parents": [225]},
    {"id": 229, "name": "Sunscreen", "is_root": False, "parents": [225]},
    {"id": 230, "name": "Hair Care", "is_root": False, "parents": [5]},
    {"id": 231, "name": "Shampoo & Conditioner", "is_root": False, "parents": [230]},
    {"id": 232, "name": "Styling Products", "is_root": False, "parents": [230]},
    {"id": 233, "name": "Hair Treatments", "is_root": False, "parents": [230]},
    {"id": 234, "name": "Hair Color", "is_root": False, "parents": [230]},
    {"id": 235, "name": "Hair Tools", "is_root": False, "parents": [230]},
    {"id": 236, "name": "Fragrances", "is_root": False, "parents": [5]},
    {"id": 237, "name": "Women's Fragrances", "is_root": False, "parents": [236]},
    {"id": 238, "name": "Men's Fragrances", "is_root": False, "parents": [236]},
    {"id": 239, "name": "Personal Care", "is_root": False, "parents": [5]},
    {"id": 240, "name": "Oral Care", "is_root": False, "parents": [239]},
    {"id": 241, "name": "Shaving & Hair Removal", "is_root": False, "parents": [239]},
    {"id": 242, "name": "Deodorants & Antiperspirants", "is_root": False, "parents": [239]},
    {"id": 243, "name": "Bath & Body", "is_root": False, "parents": [239]},
    {"id": 244, "name": "Health Care", "is_root": False, "parents": [5]},
    {"id": 245, "name": "Vitamins & Supplements", "is_root": False, "parents": [244]},
    {"id": 246, "name": "Over-the-Counter Medications", "is_root": False, "parents": [244]},
    {"id": 247, "name": "First Aid", "is_root": False, "parents": [244]},
    {"id": 248, "name": "Medical Equipment", "is_root": False, "parents": [244]},
    {"id": 249, "name": "Fitness & Nutrition", "is_root": False, "parents": [5]},
    {"id": 250, "name": "Exercise Equipment", "is_root": False, "parents": [249]},
    {"id": 251, "name": "Sports Nutrition", "is_root": False, "parents": [249]},
    {"id": 252, "name": "Sexual Wellness", "is_root": False, "parents": [5]},
    {"id": 253, "name": "Contraceptives", "is_root": False, "parents": [252]},
    {"id": 254, "name": "Lubricants", "is_root": False, "parents": [252]},
    {"id": 255, "name": "Adult Toys", "is_root": False, "parents": [252]},
    {"id": 256, "name": "Other Health & Beauty Items", "is_root": False, "parents": [5]},

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

    # Industrial & Business
    {"id": 399, "name": "Office Supplies", "is_root": False, "parents": [14]},
    {"id": 400, "name": "Industrial Equipment", "is_root": False, "parents": [14]},
    {"id": 401, "name": "Safety Equipment", "is_root": False, "parents": [14]},
    {"id": 402, "name": "Packaging & Shipping", "is_root": False, "parents": [14]},

    # Real Estate
    {"id": 403, "name": "Residential", "is_root": False, "parents": [15]},
    {"id": 404, "name": "Commercial", "is_root": False, "parents": [15]},
    {"id": 405, "name": "Land", "is_root": False, "parents": [15]},
    {"id": 406, "name": "Rental Properties", "is_root": False, "parents": [15]},

    # Deals & Discounts
    {"id": 407, "name": "Daily Deals", "is_root": False, "parents": [16]},
    {"id": 408, "name": "Clearance", "is_root": False, "parents": [16]},
    {"id": 409, "name": "Seasonal Sales", "is_root": False, "parents": [16]},

    # Software & Subscriptions
    {"id": 410, "name": "Productivity Software", "is_root": False, "parents": [17]},
    {"id": 411, "name": "Security Software", "is_root": False, "parents": [17]},
    {"id": 412, "name": "Design Software", "is_root": False, "parents": [17]},
    {"id": 413, "name": "Streaming Services", "is_root": False, "parents": [17]},

    # Luxury & High-End Goods
    {"id": 414, "name": "Luxury Fashion", "is_root": False, "parents": [18]},
    {"id": 415, "name": "Fine Jewelry & Watches", "is_root": False, "parents": [18]},
    {"id": 416, "name": "Luxury Vehicles", "is_root": False, "parents": [18]},
    {"id": 417, "name": "Fine Art", "is_root": False, "parents": [18]},

    # Gifts & Occasions
    {"id": 418, "name": "Birthday", "is_root": False, "parents": [19]},
    {"id": 419, "name": "Wedding", "is_root": False, "parents": [19]},
    {"id": 420, "name": "Holiday", "is_root": False, "parents": [19]},
    {"id": 421, "name": "Personalized Gifts", "is_root": False, "parents": [19]},

    # Miscellaneous
    {"id": 422, "name": "Specialty Items", "is_root": False, "parents": [20]},
    {"id": 423, "name": "Novelty Products", "is_root": False, "parents": [20]},
    {"id": 424, "name": "Uncategorized", "is_root": False, "parents": [20]}
]


from .f3_electronics_and_computers import electronics_and_computers
categories += electronics_and_computers


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
