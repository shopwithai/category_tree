home_and_garden = [
    {"id": 138, "name": "Furniture", "is_root": False, "parents": [4], "properties": []},

    {"id": 139, "name": "Living Room Furniture", "is_root": False, "parents": [138], "properties": []},

    {"id": 140, "name": "Sofas & Sectionals", "is_root": False, "parents": [139], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Leather", "Fabric", "Microfiber", "Velvet", "Linen", "Faux Leather", "Other"]),
        ("sofa_type", str, ["Sofa", "Sectional", "Loveseat", "Sleeper Sofa", "Recliner", "Futon", "Chaise Lounge", "Other"]),
        ("seating_capacity", int),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Transitional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("weight_capacity_kg", int),
    ]},

    {"id": 141, "name": "Coffee & End Tables", "is_root": False, "parents": [139], "properties": [
        ("brand", str),
        ("model", str),
        ("table_type", str, ["Coffee Table", "End Table", "Console Table", "Nest of Tables", "Other"]),
        ("material", str, ["Wood", "Metal", "Glass", "Marble", "Stone", "Acrylic", "Composite", "Other"]),
        ("shape", str, ["Rectangle", "Square", "Round", "Oval", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("storage_features", bool),
    ]},

    {"id": 142, "name": "TV Stands & Entertainment Centers", "is_root": False, "parents": [139], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Glass", "Composite", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("max_tv_size_inches", int),
        ("storage_features", bool),
        ("mount_included", bool),
        ("number_of_shelves", int),
    ]},

    {"id": 143, "name": "Bedroom Furniture", "is_root": False, "parents": [138], "properties": []},

    {"id": 144, "name": "Beds & Headboards", "is_root": False, "parents": [143], "properties": [
        ("brand", str),
        ("model", str),
        ("bed_type", str, ["Platform Bed", "Panel Bed", "Sleigh Bed", "Canopy Bed", "Storage Bed", "Bunk Bed", "Daybed", "Headboard", "Other"]),
        ("size", str, ["Twin", "Full", "Queen", "King", "California King", "Other"]),
        ("material", str, ["Wood", "Metal", "Upholstered", "Leather", "Fabric", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("storage_included", bool),
        ("headboard_included", bool),
        ("footboard_included", bool),
    ]},

    {"id": 145, "name": "Dressers & Chests", "is_root": False, "parents": [143], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Composite", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("number_of_drawers", int),
        ("assembly_required", bool),
        ("mirror_included", bool),
    ]},

    {"id": 146, "name": "Nightstands", "is_root": False, "parents": [143], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Composite", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("number_of_drawers", int),
        ("assembly_required", bool),
    ]},

    {"id": 147, "name": "Dining Room Furniture", "is_root": False, "parents": [138], "properties": []},

    {"id": 148, "name": "Dining Tables", "is_root": False, "parents": [147], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Glass", "Marble", "Composite", "Other"]),
        ("shape", str, ["Rectangle", "Square", "Round", "Oval", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("seating_capacity", int),
        ("assembly_required", bool),
        ("extendable", bool),
    ]},

    {"id": 149, "name": "Dining Chairs & Benches", "is_root": False, "parents": [147], "properties": [
        ("brand", str),
        ("model", str),
        ("chair_type", str, ["Dining Chair", "Armchair", "Side Chair", "Bench", "Bar Stool", "Other"]),
        ("material", str, ["Wood", "Metal", "Upholstered", "Leather", "Fabric", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("set_size", int),
    ]},

    {"id": 150, "name": "Bar Stools", "is_root": False, "parents": [147], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Upholstered", "Leather", "Fabric", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("adjustable_height", bool),
        ("swivel", bool),
        ("backrest_included", bool),
        ("assembly_required", bool),
        ("set_size", int),
    ]},

    {"id": 151, "name": "Office Furniture", "is_root": False, "parents": [138], "properties": []},

    {"id": 152, "name": "Desks", "is_root": False, "parents": [151], "properties": [
        ("brand", str),
        ("model", str),
        ("desk_type", str, ["Writing Desk", "Computer Desk", "Executive Desk", "Standing Desk", "L-Shaped Desk", "Corner Desk", "Other"]),
        ("material", str, ["Wood", "Metal", "Glass", "Composite", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("assembly_required", bool),
        ("number_of_drawers", int),
        ("adjustable_height", bool),
    ]},

    {"id": 153, "name": "Office Chairs", "is_root": False, "parents": [151], "properties": [
        ("brand", str),
        ("model", str),
        ("chair_type", str, ["Ergonomic Chair", "Executive Chair", "Task Chair", "Gaming Chair", "Drafting Chair", "Stool", "Other"]),
        ("material", str, ["Leather", "Mesh", "Fabric", "Vinyl", "Other"]),
        ("adjustable_height", bool),
        ("lumbar_support", bool),
        ("armrests", bool),
        ("swivel", bool),
        ("tilt", bool),
        ("assembly_required", bool),
        ("weight_capacity_kg", int),
    ]},

    {"id": 154, "name": "Bookcases & Shelving", "is_root": False, "parents": [151], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wood", "Metal", "Glass", "Composite", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Industrial", "Other"]),
        ("number_of_shelves", int),
        ("assembly_required", bool),
        ("wall_mountable", bool),
    ]},

    {"id": 155, "name": "Outdoor Furniture", "is_root": False, "parents": [138], "properties": []},

    {"id": 156, "name": "Patio Sets", "is_root": False, "parents": [155], "properties": [
        ("brand", str),
        ("model", str),
        ("material", str, ["Wicker", "Metal", "Wood", "Plastic", "Other"]),
        ("set_includes", str, ["Table & Chairs", "Sofa Set", "Dining Set", "Bistro Set", "Other"]),
        ("number_of_pieces", int),
        ("seating_capacity", int),
        ("weather_resistant", bool),
        ("assembly_required", bool),
    ]},

    {"id": 157, "name": "Outdoor Seating", "is_root": False, "parents": [155], "properties": [
        ("brand", str),
        ("model", str),
        ("seating_type", str, ["Chair", "Bench", "Sofa", "Swing", "Hammock", "Other"]),
        ("material", str, ["Wicker", "Metal", "Wood", "Plastic", "Fabric", "Other"]),
        ("weather_resistant", bool),
        ("assembly_required", bool),
        ("weight_capacity_kg", int),
    ]},

    {"id": 158, "name": "Umbrellas & Shade", "is_root": False, "parents": [155], "properties": [
        ("brand", str),
        ("model", str),
        ("shade_type", str, ["Patio Umbrella", "Gazebo", "Pergola", "Awning", "Canopy", "Other"]),
        ("size_diameter_cm", int),
        ("material", str, ["Polyester", "Acrylic", "Canvas", "Metal", "Wood", "Other"]),
        ("uv_protection", bool),
        ("water_resistant", bool),
        ("assembly_required", bool),
    ]},

    {"id": 159, "name": "Home Décor", "is_root": False, "parents": [4], "properties": []},

    {"id": 160, "name": "Rugs", "is_root": False, "parents": [159], "properties": [
        ("brand", str),
        ("model", str),
        ("rug_type", str, ["Area Rug", "Runner", "Round Rug", "Shag Rug", "Outdoor Rug", "Other"]),
        ("material", str, ["Wool", "Cotton", "Jute", "Polypropylene", "Silk", "Synthetic", "Other"]),
        ("style", str, ["Modern", "Traditional", "Transitional", "Vintage", "Shag", "Other"]),
        ("pile_height_cm", float),
        ("pattern", str, ["Solid", "Geometric", "Floral", "Abstract", "Striped", "Other"]),
    ]},

    {"id": 161, "name": "Lighting", "is_root": False, "parents": [159], "properties": []},

    {"id": 162, "name": "Ceiling Lights", "is_root": False, "parents": [161], "properties": [
        ("brand", str),
        ("model", str),
        ("light_type", str, ["Chandelier", "Pendant", "Flush Mount", "Semi-Flush Mount", "Track Lighting", "Recessed Lighting", "Other"]),
        ("material", str, ["Metal", "Glass", "Crystal", "Fabric", "Wood", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Industrial", "Other"]),
        ("number_of_lights", int),
        ("bulb_type", str, ["LED", "Incandescent", "Halogen", "Fluorescent", "Other"]),
        ("dimmable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 163, "name": "Lamps", "is_root": False, "parents": [161], "properties": [
        ("brand", str),
        ("model", str),
        ("lamp_type", str, ["Table Lamp", "Floor Lamp", "Desk Lamp", "Torchiere", "Arc Lamp", "Other"]),
        ("material", str, ["Metal", "Glass", "Crystal", "Fabric", "Wood", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Industrial", "Other"]),
        ("bulb_type", str, ["LED", "Incandescent", "Halogen", "Fluorescent", "Other"]),
        ("dimmable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 164, "name": "Wall Lights", "is_root": False, "parents": [161], "properties": [
        ("brand", str),
        ("model", str),
        ("light_type", str, ["Sconce", "Vanity Light", "Picture Light", "Swing Arm", "Other"]),
        ("material", str, ["Metal", "Glass", "Crystal", "Fabric", "Wood", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Industrial", "Other"]),
        ("number_of_lights", int),
        ("bulb_type", str, ["LED", "Incandescent", "Halogen", "Fluorescent", "Other"]),
        ("dimmable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 165, "name": "Wall Art & Decor", "is_root": False, "parents": [159], "properties": [
        ("type", str, ["Painting", "Print", "Wall Sculpture", "Wall Sticker", "Tapestry", "Other"]),
        ("artist", str),
        ("theme", str, ["Abstract", "Landscape", "Figurative", "Animals", "Nature", "Other"]),
        ("material", str, ["Canvas", "Metal", "Wood", "Paper", "Fabric", "Other"]),
        ("framed", bool),
    ]},

    {"id": 166, "name": "Mirrors", "is_root": False, "parents": [159], "properties": [
        ("brand", str),
        ("model", str),
        ("mirror_type", str, ["Wall Mirror", "Floor Mirror", "Dresser Mirror", "Vanity Mirror", "Other"]),
        ("shape", str, ["Rectangle", "Square", "Round", "Oval", "Arch", "Other"]),
        ("frame_material", str, ["Wood", "Metal", "Glass", "Frameless", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Rustic", "Other"]),
        ("assembly_required", bool),
    ]},

    {"id": 167, "name": "Clocks", "is_root": False, "parents": [159], "properties": [
        ("brand", str),
        ("model", str),
        ("clock_type", str, ["Wall Clock", "Table Clock", "Mantel Clock", "Grandfather Clock", "Cuckoo Clock", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Glass", "Other"]),
        ("style", str, ["Modern", "Contemporary", "Traditional", "Vintage", "Other"]),
        ("power_source", str, ["Battery", "Electric", "Mechanical", "Other"]),
        ("assembly_required", bool),
    ]},

    {"id": 168, "name": "Kitchen & Dining", "is_root": False, "parents": [4], "properties": []},

    {"id": 169, "name": "Cookware & Bakeware", "is_root": False, "parents": [168], "properties": [
        ("brand", str),
        ("model", str),
        ("product_type", str, ["Cookware Set", "Frying Pan", "Saucepan", "Dutch Oven", "Baking Dish", "Bakeware Set", "Other"]),
        ("material", str, ["Stainless Steel", "Aluminum", "Cast Iron", "Ceramic", "Nonstick", "Glass", "Other"]),
        ("number_of_pieces", int),
        ("oven_safe_temperature_c", int),
        ("induction_ready", bool),
        ("dishwasher_safe", bool),
        ("lid_included", bool),
    ]},

    {"id": 170, "name": "Dinnerware & Serveware", "is_root": False, "parents": [168], "properties": [
        ("brand", str),
        ("model", str),
        ("product_type", str, ["Dinnerware Set", "Plate", "Bowl", "Serving Tray", "Serving Bowl", "Other"]),
        ("material", str, ["Porcelain", "Ceramic", "Glass", "Stoneware", "Bone China", "Melamine", "Other"]),
        ("number_of_pieces", int),
        ("microwave_safe", bool),
        ("dishwasher_safe", bool),
        ("pattern", str, ["Solid", "Patterned", "Floral", "Geometric", "Other"]),
    ]},

    {"id": 171, "name": "Kitchen Appliances", "is_root": False, "parents": [168], "properties": []},

    {"id": 172, "name": "Refrigerators", "is_root": False, "parents": [171], "properties": [
        ("brand", str),
        ("model", str),
        ("refrigerator_type", str, ["French Door", "Side-by-Side", "Top Freezer", "Bottom Freezer", "Compact", "Wine Cooler", "Other"]),
        ("capacity_liters", int),
        ("energy_star_certified", bool),
        ("ice_maker", bool),
        ("water_dispenser", bool),
        ("smart_technology", bool),
        ("number_of_doors", int),
        ("defrost_type", str, ["Automatic", "Manual"]),
        ("annual_energy_consumption_kwh", float),
    ]},

    {"id": 173, "name": "Ovens & Ranges", "is_root": False, "parents": [171], "properties": [
        ("brand", str),
        ("model", str),
        ("product_type", str, ["Range", "Wall Oven", "Cooktop", "Other"]),
        ("fuel_type", str, ["Electric", "Gas", "Dual Fuel", "Induction", "Other"]),
        ("number_of_burners", int),
        ("oven_capacity_liters", int),
        ("convection_oven", bool),
        ("self_cleaning", bool),
        ("energy_star_certified", bool),
        ("smart_technology", bool),
    ]},

    {"id": 174, "name": "Dishwashers", "is_root": False, "parents": [171], "properties": [
        ("brand", str),
        ("model", str),
        ("dishwasher_type", str, ["Built-In", "Portable", "Countertop", "Drawer", "Other"]),
        ("capacity_place_settings", int),
        ("energy_star_certified", bool),
        ("noise_level_db", int),
        ("number_of_wash_cycles", int),
        ("delay_start", bool),
        ("smart_technology", bool),
    ]},

    {"id": 175, "name": "Microwaves", "is_root": False, "parents": [171], "properties": [
        ("brand", str),
        ("model", str),
        ("microwave_type", str, ["Countertop", "Over-the-Range", "Built-In", "Drawer", "Other"]),
        ("capacity_liters", float),
        ("power_watts", int),
        ("sensor_cooking", bool),
        ("convection", bool),
        ("child_lock", bool),
        ("smart_technology", bool),
    ]},

    {"id": 176, "name": "Kitchen Tools & Gadgets", "is_root": False, "parents": [168], "properties": [
        ("brand", str),
        ("product_type", str, ["Cutlery", "Utensils", "Measuring Tools", "Kitchen Scales", "Thermometers", "Other"]),
        ("material", str, ["Stainless Steel", "Silicone", "Plastic", "Wood", "Other"]),
        ("dishwasher_safe", bool),
        ("number_of_pieces", int),
    ]},

    {"id": 177, "name": "Bedding & Bath", "is_root": False, "parents": [4], "properties": []},

    {"id": 178, "name": "Bedding Sets", "is_root": False, "parents": [177], "properties": [
        ("brand", str),
        ("model", str),
        ("size", str, ["Twin", "Full", "Queen", "King", "California King", "Other"]),
        ("set_includes", str, ["Comforter", "Duvet Cover", "Sheets", "Pillowcases", "Shams", "Bed Skirt", "Other"]),
        ("material", str, ["Cotton", "Polyester", "Linen", "Silk", "Microfiber", "Bamboo", "Other"]),
        ("thread_count", int),
        ("pattern", str, ["Solid", "Striped", "Floral", "Geometric", "Plaid", "Other"]),
        ("care_instructions", str, ["Machine Washable", "Dry Clean", "Other"]),
    ]},

    {"id": 179, "name": "Sheets & Pillowcases", "is_root": False, "parents": [177], "properties": [
        ("brand", str),
        ("model", str),
        ("size", str, ["Twin", "Full", "Queen", "King", "California King", "Other"]),
        ("material", str, ["Cotton", "Polyester", "Linen", "Silk", "Microfiber", "Bamboo", "Other"]),
        ("thread_count", int),
        ("number_of_pieces", int),
        ("pattern", str, ["Solid", "Striped", "Floral", "Geometric", "Plaid", "Other"]),
        ("care_instructions", str, ["Machine Washable", "Dry Clean", "Other"]),
    ]},

    {"id": 180, "name": "Comforters & Duvet Inserts", "is_root": False, "parents": [177], "properties": [
        ("brand", str),
        ("model", str),
        ("size", str, ["Twin", "Full", "Queen", "King", "California King", "Other"]),
        ("fill_material", str, ["Down", "Down Alternative", "Cotton", "Wool", "Silk", "Polyester", "Other"]),
        ("warmth_rating", str, ["Lightweight", "Medium", "Heavyweight"]),
        ("thread_count", int),
        ("hypoallergenic", bool),
        ("care_instructions", str, ["Machine Washable", "Dry Clean", "Other"]),
    ]},

    {"id": 181, "name": "Towels", "is_root": False, "parents": [177], "properties": [
        ("brand", str),
        ("model", str),
        ("towel_type", str, ["Bath Towel", "Hand Towel", "Washcloth", "Bath Sheet", "Towel Set", "Other"]),
        ("material", str, ["Cotton", "Bamboo", "Microfiber", "Other"]),
        ("gsm", int),
        ("number_of_pieces", int),
        ("pattern", str, ["Solid", "Striped", "Other"]),
        ("care_instructions", str, ["Machine Washable", "Other"]),
    ]},

    {"id": 182, "name": "Bath Accessories", "is_root": False, "parents": [177], "properties": [
        ("product_type", str, ["Shower Curtain", "Bath Mat", "Soap Dispenser", "Toothbrush Holder", "Towel Rack", "Other"]),
        ("material", str, ["Cotton", "Plastic", "Metal", "Ceramic", "Other"]),
        ("color", str),
        ("set_includes", str),
    ]},

    {"id": 183, "name": "Appliances", "is_root": False, "parents": [4], "properties": []},

    {"id": 184, "name": "Washers & Dryers", "is_root": False, "parents": [183], "properties": [
        ("brand", str),
        ("model", str),
        ("product_type", str, ["Washer", "Dryer", "Washer-Dryer Combo"]),
        ("washer_type", str, ["Front Load", "Top Load"]),
        ("dryer_type", str, ["Electric", "Gas"]),
        ("capacity_cubic_feet", float),
        ("energy_star_certified", bool),
        ("smart_technology", bool),
        ("steam_function", bool),
        ("number_of_cycles", int),
    ]},

    {"id": 185, "name": "Vacuum Cleaners", "is_root": False, "parents": [183], "properties": [
        ("brand", str),
        ("model", str),
        ("vacuum_type", str, ["Upright", "Canister", "Stick", "Handheld", "Robotic", "Other"]),
        ("bagless", bool),
        ("cordless", bool),
        ("battery_runtime_minutes", int),
        ("hepa_filter", bool),
        ("smart_technology", bool),
        ("weight_kg", float),
    ]},

    {"id": 186, "name": "Air Conditioners & Heaters", "is_root": False, "parents": [183], "properties": [
        ("brand", str),
        ("model", str),
        ("product_type", str, ["Air Conditioner", "Heater", "Fan", "Air Purifier", "Humidifier", "Dehumidifier", "Other"]),
        ("unit_type", str, ["Window", "Portable", "Split", "Tower", "Other"]),
        ("cooling_capacity_btu", int),
        ("heating_capacity_btu", int),
        ("coverage_area_sq_ft", int),
        ("energy_star_certified", bool),
        ("smart_technology", bool),
        ("noise_level_db", int),
    ]},

    {"id": 187, "name": "Tools & Home Improvement", "is_root": False, "parents": [4], "properties": []},

    {"id": 188, "name": "Power Tools", "is_root": False, "parents": [187], "properties": [
        ("brand", str),
        ("model", str),
        ("tool_type", str, ["Drill", "Saw", "Sander", "Grinder", "Router", "Compressor", "Other"]),
        ("power_source", str, ["Corded Electric", "Battery", "Pneumatic", "Gas", "Other"]),
        ("voltage", int),
        ("battery_included", bool),
        ("number_of_speeds", int),
        ("variable_speed", bool),
        ("accessories_included", bool),
    ]},

    {"id": 189, "name": "Hand Tools", "is_root": False, "parents": [187], "properties": [
        ("brand", str),
        ("model", str),
        ("tool_type", str, ["Hammer", "Screwdriver", "Wrench", "Pliers", "Chisel", "Saw", "Other"]),
        ("material", str, ["Steel", "Alloy", "Wood", "Plastic", "Other"]),
        ("number_of_pieces", int),
        ("set_included", bool),
    ]},

    {"id": 190, "name": "Hardware", "is_root": False, "parents": [187], "properties": [
        ("product_type", str, ["Fasteners", "Door Hardware", "Cabinet Hardware", "Brackets", "Other"]),
        ("material", str, ["Steel", "Brass", "Aluminum", "Plastic", "Other"]),
        ("finish", str, ["Polished", "Matte", "Antique", "Other"]),
        ("quantity", int),
    ]},

    {"id": 191, "name": "Electrical Supplies", "is_root": False, "parents": [187], "properties": [
        ("product_type", str, ["Wiring", "Outlets", "Switches", "Circuit Breakers", "Conduits", "Other"]),
        ("voltage_rating", int),
        ("amperage_rating", int),
        ("material", str, ["Copper", "Aluminum", "Plastic", "Other"]),
        ("certifications", str, ["UL Listed", "CSA Certified", "Other"]),
    ]},

    {"id": 192, "name": "Plumbing Supplies", "is_root": False, "parents": [187], "properties": [
        ("product_type", str, ["Pipes", "Fittings", "Valves", "Faucets", "Fixtures", "Other"]),
        ("material", str, ["PVC", "Copper", "Brass", "Stainless Steel", "Other"]),
        ("pipe_size_inches", float),
        ("pressure_rating_psi", int),
        ("finish", str, ["Chrome", "Brushed Nickel", "Oil-Rubbed Bronze", "Other"]),
    ]},

    {"id": 193, "name": "Paint & Wall Treatments", "is_root": False, "parents": [187], "properties": [
        ("product_type", str, ["Paint", "Wallpaper", "Primer", "Stain", "Varnish", "Other"]),
        ("color", str),
        ("finish", str, ["Matte", "Eggshell", "Satin", "Semi-Gloss", "Gloss", "High-Gloss"]),
        ("volume_liters", float),
        ("coverage_sq_m_per_liter", float),
        ("application_method", str, ["Brush", "Roller", "Spray", "Other"]),
        ("indoor_outdoor", str, ["Indoor", "Outdoor", "Both"]),
    ]},

    {"id": 194, "name": "Lawn & Garden", "is_root": False, "parents": [4], "properties": []},

    {"id": 195, "name": "Gardening Tools", "is_root": False, "parents": [194], "properties": [
        ("brand", str),
        ("model", str),
        ("tool_type", str, ["Shovel", "Rake", "Hoe", "Pruner", "Trowel", "Other"]),
        ("material", str, ["Steel", "Aluminum", "Wood", "Fiberglass", "Other"]),
        ("handle_length_cm", int),
        ("number_of_pieces", int),
        ("set_included", bool),
    ]},

    {"id": 196, "name": "Plants & Seeds", "is_root": False, "parents": [194], "properties": [
        ("product_type", str, ["Plant", "Seed", "Bulb", "Seedling", "Other"]),
        ("plant_type", str, ["Flower", "Vegetable", "Herb", "Tree", "Shrub", "Succulent", "Other"]),
        ("sunlight_requirement", str, ["Full Sun", "Partial Sun", "Shade"]),
        ("water_requirement", str, ["High", "Medium", "Low"]),
        ("hardiness_zone", int),
        ("mature_height_cm", int),
    ]},

    {"id": 197, "name": "Outdoor Power Equipment", "is_root": False, "parents": [194], "properties": []},

    {"id": 198, "name": "Lawn Mowers", "is_root": False, "parents": [197], "properties": [
        ("brand", str),
        ("model", str),
        ("mower_type", str, ["Gas", "Electric Corded", "Electric Cordless", "Manual", "Ride-On", "Robotic", "Other"]),
        ("cutting_width_cm", int),
        ("power_output_hp", float),
        ("battery_included", bool),
        ("self_propelled", bool),
        ("mulching_capable", bool),
        ("bag_included", bool),
        ("deck_material", str, ["Steel", "Aluminum", "Plastic", "Other"]),
    ]},

    {"id": 199, "name": "Trimmers", "is_root": False, "parents": [197], "properties": [
        ("brand", str),
        ("model", str),
        ("trimmer_type", str, ["String Trimmer", "Hedge Trimmer", "Brush Cutter", "Other"]),
        ("power_source", str, ["Gas", "Electric Corded", "Electric Cordless", "Other"]),
        ("cutting_swath_cm", int),
        ("line_diameter_mm", float),
        ("battery_included", bool),
        ("attachments_included", bool),
        ("weight_kg", float),
    ]},

    {"id": 200, "name": "Grills & Outdoor Cooking", "is_root": False, "parents": [194], "properties": [
        ("brand", str),
        ("model", str),
        ("grill_type", str, ["Gas", "Charcoal", "Electric", "Pellet", "Smoker", "Other"]),
        ("cooking_area_sq_cm", int),
        ("number_of_burners", int),
        ("side_burner", bool),
        ("material", str, ["Stainless Steel", "Cast Iron", "Aluminum", "Other"]),
        ("portable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 201, "name": "Garden Decor", "is_root": False, "parents": [194], "properties": [
        ("product_type", str, ["Statue", "Fountain", "Planter", "Wind Chime", "Bird Feeder", "Other"]),
        ("material", str, ["Stone", "Metal", "Ceramic", "Plastic", "Wood", "Other"]),
        ("weather_resistant", bool),
        ("solar_powered", bool),
        ("assembly_required", bool),
    ]},

    {"id": 202, "name": "Storage & Organization", "is_root": False, "parents": [4], "properties": []},

    {"id": 203, "name": "Closet Storage", "is_root": False, "parents": [202], "properties": [
        ("product_type", str, ["Closet Organizer", "Hanger", "Shoe Rack", "Storage Bin", "Shelf", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Fabric", "Other"]),
        ("number_of_pieces", int),
        ("assembly_required", bool),
    ]},

    {"id": 204, "name": "Garage Storage", "is_root": False, "parents": [202], "properties": [
        ("product_type", str, ["Cabinet", "Shelving", "Tool Chest", "Wall Organizer", "Other"]),
        ("material", str, ["Steel", "Plastic", "Wood", "Other"]),
        ("number_of_shelves", int),
        ("weight_capacity_kg", int),
        ("lockable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 205, "name": "Shelving Units", "is_root": False, "parents": [202], "properties": [
        ("brand", str),
        ("model", str),
        ("shelf_type", str, ["Freestanding", "Wall Mounted", "Adjustable", "Corner", "Other"]),
        ("material", str, ["Wood", "Metal", "Plastic", "Glass", "Other"]),
        ("number_of_shelves", int),
        ("weight_capacity_per_shelf_kg", int),
        ("assembly_required", bool),
    ]},

    {"id": 206, "name": "Bins & Containers", "is_root": False, "parents": [202], "properties": [
        ("product_type", str, ["Storage Bin", "Basket", "Box", "Container", "Other"]),
        ("material", str, ["Plastic", "Fabric", "Wood", "Metal", "Other"]),
        ("capacity_liters", float),
        ("stackable", bool),
        ("lid_included", bool),
    ]},

    {"id": 207, "name": "Cleaning Supplies", "is_root": False, "parents": [4], "properties": []},

    {"id": 208, "name": "Cleaning Tools", "is_root": False, "parents": [207], "properties": [
        ("product_type", str, ["Broom", "Mop", "Duster", "Brush", "Cleaning Cloth", "Other"]),
        ("material", str, ["Plastic", "Metal", "Microfiber", "Cotton", "Other"]),
        ("set_included", bool),
        ("extendable_handle", bool),
        ("machine_washable", bool),
    ]},

    {"id": 209, "name": "Household Cleaners", "is_root": False, "parents": [207], "properties": [
        ("product_type", str, ["All-Purpose Cleaner", "Glass Cleaner", "Disinfectant", "Floor Cleaner", "Laundry Detergent", "Other"]),
        ("volume_liters", float),
        ("scent", str),
        ("eco_friendly", bool),
        ("antibacterial", bool),
    ]},

    {"id": 210, "name": "Trash & Recycling", "is_root": False, "parents": [207], "properties": [
        ("product_type", str, ["Trash Can", "Recycle Bin", "Compost Bin", "Trash Bags", "Other"]),
        ("material", str, ["Plastic", "Stainless Steel", "Metal", "Wood", "Other"]),
        ("capacity_liters", float),
        ("lid_type", str, ["Open Top", "Swing", "Step-On", "Sensor", "Other"]),
        ("indoor_outdoor", str, ["Indoor", "Outdoor", "Both"]),
    ]},

    {"id": 211, "name": "Safety & Security", "is_root": False, "parents": [4], "properties": []},

    {"id": 212, "name": "Home Security Systems", "is_root": False, "parents": [211], "properties": [
        ("brand", str),
        ("model", str),
        ("system_type", str, ["DIY", "Professional", "Smart Home", "Other"]),
        ("number_of_pieces", int),
        ("includes_camera", bool),
        ("connectivity", str, ["Wired", "Wireless", "Both"]),
        ("smart_technology", bool),
        ("monitoring_options", str, ["Self-Monitored", "Professional Monitoring", "Both"]),
    ]},

    {"id": 213, "name": "Smoke & Carbon Monoxide Detectors", "is_root": False, "parents": [211], "properties": [
        ("brand", str),
        ("model", str),
        ("detector_type", str, ["Smoke", "Carbon Monoxide", "Combination"]),
        ("power_source", str, ["Battery", "Hardwired", "Plug-In", "Other"]),
        ("smart_technology", bool),
        ("battery_backup", bool),
        ("test_button", bool),
        ("hush_feature", bool),
    ]},

    {"id": 214, "name": "Safes", "is_root": False, "parents": [211], "properties": [
        ("brand", str),
        ("model", str),
        ("safe_type", str, ["Fireproof", "Waterproof", "Gun Safe", "Wall Safe", "Floor Safe", "Other"]),
        ("lock_type", str, ["Key", "Combination", "Digital Keypad", "Biometric", "Other"]),
        ("fire_rating_minutes", int),
        ("capacity_liters", float),
        ("weight_kg", float),
        ("mounting_hardware_included", bool),
    ]},

    {"id": 215, "name": "Pet Supplies", "is_root": False, "parents": [4, 11], "properties": []},

    {"id": 216, "name": "Beds & Furniture", "is_root": False, "parents": [215], "properties": [
        ("brand", str),
        ("product_type", str, ["Bed", "Cage", "Crate", "Hutch", "Perch", "Other"]),
        ("pet_type", str, ["Dog", "Cat", "Bird", "Small Animal", "Other"]),
        ("material", str, ["Fabric", "Plastic", "Metal", "Wood", "Other"]),
        ("washable", bool),
        ("assembly_required", bool),
    ]},

    {"id": 217, "name": "Feeding & Watering Supplies", "is_root": False, "parents": [215], "properties": [
        ("product_type", str, ["Bowl", "Feeder", "Water Dispenser", "Food Storage", "Other"]),
        ("pet_type", str, ["Dog", "Cat", "Bird", "Small Animal", "Other"]),
        ("material", str, ["Plastic", "Stainless Steel", "Ceramic", "Glass", "Other"]),
        ("capacity_liters", float),
        ("automatic", bool),
        ("dishwasher_safe", bool),
    ]},

    {"id": 218, "name": "Toys", "is_root": False, "parents": [215], "properties": [
        ("product_type", str, ["Chew Toy", "Fetch Toy", "Interactive Toy", "Scratching Post", "Other"]),
        ("pet_type", str, ["Dog", "Cat", "Bird", "Small Animal", "Other"]),
        ("material", str, ["Rubber", "Plastic", "Fabric", "Wood", "Other"]),
        ("interactive", bool),
        ("squeaker", bool),
    ]},

    {"id": 219, "name": "Grooming", "is_root": False, "parents": [215], "properties": [
        ("product_type", str, ["Brush", "Shampoo", "Clippers", "Toothbrush", "Other"]),
        ("pet_type", str, ["Dog", "Cat", "Other"]),
        ("scent", str),
        ("ingredients", str),
        ("battery_included", bool),
    ]},

    {"id": 220, "name": "Other Home & Garden Items", "is_root": False, "parents": [4], "properties": [
        ("description", str),
    ]},
]
