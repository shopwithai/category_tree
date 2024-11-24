# Industrial & Business
{"id": 399, "name": "Office Supplies", "is_root": False, "parents": [14], "properties": [
    ("type", str, ["Paper", "Writing Instruments", "Organizers", "Desk Accessories", "Filing Supplies", "Other"]),
    ("brand", str),
    ("material", str, ["Plastic", "Metal", "Paper", "Wood", "Other"]),
    ("color", str),
    ("quantity_per_package", int),
    ("size", str),
]},

{"id": 400, "name": "Industrial Equipment", "is_root": False, "parents": [14], "properties": [
    ("type", str, ["Machinery", "Tools", "Heavy Equipment", "Other"]),
    ("brand", str),
    ("model", str),
    ("power_source", str, ["Electric", "Gasoline", "Diesel", "Hydraulic", "Pneumatic", "Manual"]),
    ("voltage_v", int),
    ("capacity_tons", float),
]},

{"id": 401, "name": "Safety Equipment", "is_root": False, "parents": [14], "properties": [
    ("type", str, ["Protective Clothing", "Helmets", "Gloves", "Safety Glasses", "Ear Protection", "Respirators", "Fall Protection", "First Aid", "Other"]),
    ("brand", str),
    ("size", str),
    ("material", str),
    ("certification", str),
    ("color", str),
]},

{"id": 402, "name": "Packaging & Shipping", "is_root": False, "parents": [14], "properties": [
    ("type", str, ["Boxes", "Envelopes", "Packing Material", "Labels", "Tapes", "Strapping", "Other"]),
    ("material", str, ["Cardboard", "Plastic", "Paper", "Metal", "Other"]),
    ("brand", str),
    ("quantity_per_package", int),
    ("color", str),
    ("weight_capacity_kg", float),
]},

# Real Estate
{"id": 403, "name": "Residential", "is_root": False, "parents": [15], "properties": [
    ("property_type", str, ["House", "Apartment", "Condo", "Townhouse", "Villa", "Other"]),
    ("number_of_bedrooms", int),
    ("number_of_bathrooms", int),
    ("square_meters", float),
    ("lot_size_sq_m", float),
    ("year_built", int),
    ("location", str),
    ("parking_spaces", int),
    ("furnished", bool),
    ("amenities", str),
]},

{"id": 404, "name": "Commercial", "is_root": False, "parents": [15], "properties": [
    ("property_type", str, ["Office", "Retail", "Industrial", "Warehouse", "Other"]),
    ("square_meters", float),
    ("location", str),
    ("year_built", int),
    ("parking_spaces", int),
    ("floor_number", int),
    ("amenities", str),
]},

{"id": 405, "name": "Land", "is_root": False, "parents": [15], "properties": [
    ("land_type", str, ["Residential", "Commercial", "Agricultural", "Industrial", "Other"]),
    ("lot_size_sq_m", float),
    ("location", str),
    ("zoning", str),
    ("utilities_available", bool),
]},

{"id": 406, "name": "Rental Properties", "is_root": False, "parents": [15], "properties": [
    ("property_type", str, ["House", "Apartment", "Condo", "Townhouse", "Commercial", "Other"]),
    ("number_of_bedrooms", int),
    ("number_of_bathrooms", int),
    ("square_meters", float),
    ("location", str),
    ("monthly_rent", int),
    ("lease_term_months", int),
    ("furnished", bool),
    ("amenities", str),
]},

# Deals & Discounts
{"id": 407, "name": "Daily Deals", "is_root": False, "parents": [16], "properties": [
    ("product_category", str),
    ("discount_percentage", float),
    ("original_price", int),
    ("deal_price", int),
    ("deal_expiry_date", str),
    ("limited_quantity", bool),
]},

{"id": 408, "name": "Clearance", "is_root": False, "parents": [16], "properties": [
    ("product_category", str),
    ("discount_percentage", float),
    ("original_price", int),
    ("clearance_price", int),
    ("stock_remaining", int),
]},

{"id": 409, "name": "Seasonal Sales", "is_root": False, "parents": [16], "properties": [
    ("product_category", str),
    ("season", str, ["Spring", "Summer", "Autumn", "Winter", "Holiday", "Other"]),
    ("discount_percentage", float),
    ("sale_start_date", str),
    ("sale_end_date", str),
]},

# Software & Subscriptions
{"id": 410, "name": "Productivity Software", "is_root": False, "parents": [17], "properties": [
    ("software_name", str),
    ("version", str),
    ("platform", str, ["Windows", "macOS", "Linux", "Web-based", "Mobile", "Other"]),
    ("license_type", str, ["Single User", "Multi User", "Subscription", "Perpetual", "Free"]),
    ("delivery_method", str, ["Download", "Physical Media", "Activation Code"]),
    ("subscription_duration_months", int),
]},

{"id": 411, "name": "Security Software", "is_root": False, "parents": [17], "properties": [
    ("software_name", str),
    ("version", str),
    ("platform", str, ["Windows", "macOS", "Linux", "Mobile", "Other"]),
    ("license_type", str, ["Single User", "Multi User", "Subscription", "Perpetual"]),
    ("delivery_method", str, ["Download", "Physical Media", "Activation Code"]),
    ("subscription_duration_months", int),
    ("features", str),
]},

{"id": 412, "name": "Design Software", "is_root": False, "parents": [17], "properties": [
    ("software_name", str),
    ("version", str),
    ("platform", str, ["Windows", "macOS", "Linux", "Other"]),
    ("license_type", str, ["Single User", "Multi User", "Subscription", "Perpetual"]),
    ("delivery_method", str, ["Download", "Physical Media", "Activation Code"]),
    ("subscription_duration_months", int),
    ("category", str, ["Graphic Design", "3D Modeling", "Video Editing", "Animation", "Other"]),
]},

{"id": 413, "name": "Streaming Services", "is_root": False, "parents": [17], "properties": [
    ("service_name", str),
    ("subscription_duration_months", int),
    ("platform", str, ["Web", "Mobile", "Smart TV", "Console", "Other"]),
    ("content_type", str, ["Video", "Music", "Gaming", "Other"]),
    ("number_of_screens", int),
    ("quality", str, ["SD", "HD", "4K", "Other"]),
]},

# Luxury & High-End Goods
{"id": 414, "name": "Luxury Fashion", "is_root": False, "parents": [18], "properties": [
    ("brand", str),
    ("product_type", str, ["Clothing", "Shoes", "Accessories", "Bags", "Other"]),
    ("material", str),
    ("size", str),
    ("color", str),
    ("gender", str, ["Men", "Women", "Unisex"]),
    ("collection", str),
    ("season", str),
]},

{"id": 415, "name": "Fine Jewelry & Watches", "is_root": False, "parents": [18], "properties": [
    ("brand", str),
    ("product_type", str, ["Necklace", "Ring", "Bracelet", "Earrings", "Watch", "Other"]),
    ("material", str, ["Gold", "Silver", "Platinum", "Titanium", "Other"]),
    ("gemstone", str, ["Diamond", "Ruby", "Sapphire", "Emerald", "Other", "None"]),
    ("carat_weight", float),
    ("size", str),
    ("gender", str, ["Men", "Women", "Unisex"]),
]},

{"id": 416, "name": "Luxury Vehicles", "is_root": False, "parents": [18], "properties": [
    ("make", str),
    ("model", str),
    ("year", int),
    ("vehicle_type", str, ["Car", "SUV", "Motorcycle", "Other"]),
    ("mileage_km", int),
    ("engine_type", str, ["Gasoline", "Diesel", "Electric", "Hybrid", "Other"]),
    ("transmission", str, ["Automatic", "Manual", "Other"]),
    ("color", str),
    ("interior_material", str),
]},

{"id": 417, "name": "Fine Art", "is_root": False, "parents": [18], "properties": [
    ("artist", str),
    ("title", str),
    ("year_created", int),
    ("art_type", str, ["Painting", "Sculpture", "Photograph", "Print", "Other"]),
    ("medium", str),
    ("dimensions_cm", str),
    ("framed", bool),
    ("signed", bool),
]},

# Gifts & Occasions
{"id": 418, "name": "Birthday", "is_root": False, "parents": [19], "properties": [
    ("product_type", str, ["Gift", "Card", "Decoration", "Other"]),
    ("recipient", str, ["Child", "Adult", "Friend", "Family", "Other"]),
    ("gender", str, ["Male", "Female", "Unisex"]),
    ("age_group", str, ["Kids", "Teens", "Adults", "Seniors"]),
    ("theme", str),
    ("personalizable", bool),
]},

{"id": 419, "name": "Wedding", "is_root": False, "parents": [19], "properties": [
    ("product_type", str, ["Gift", "Card", "Decoration", "Accessory", "Other"]),
    ("recipient", str, ["Bride", "Groom", "Couple", "Guest", "Other"]),
    ("personalizable", bool),
    ("theme", str),
]},

{"id": 420, "name": "Holiday", "is_root": False, "parents": [19], "properties": [
    ("holiday", str, ["Christmas", "Easter", "Thanksgiving", "Halloween", "Valentine's Day", "Other"]),
    ("product_type", str, ["Gift", "Decoration", "Card", "Other"]),
    ("personalizable", bool),
    ("theme", str),
]},

{"id": 421, "name": "Personalized Gifts", "is_root": False, "parents": [19], "properties": [
    ("product_type", str, ["Mug", "T-Shirt", "Photo Frame", "Jewelry", "Other"]),
    ("personalization_type", str, ["Name", "Photo", "Message", "Monogram", "Other"]),
    ("recipient", str, ["Child", "Adult", "Friend", "Family", "Other"]),
    ("occasion", str, ["Birthday", "Wedding", "Anniversary", "Other"]),
]},

# Miscellaneous
{"id": 422, "name": "Specialty Items", "is_root": False, "parents": [20], "properties": [
    ("description", str),
    ("category", str),
]},

{"id": 423, "name": "Novelty Products", "is_root": False, "parents": [20], "properties": [
    ("product_type", str),
    ("theme", str),
    ("intended_use", str),
    ("age_group", str, ["Kids", "Teens", "Adults", "All Ages"]),
    ("material", str),
]},

{"id": 424, "name": "Uncategorized", "is_root": False, "parents": [20], "properties": [
    ("description", str),
    ("category", str),
]},
