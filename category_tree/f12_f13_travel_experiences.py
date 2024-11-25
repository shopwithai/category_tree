travel_experiences = [
    # Travel & Experiences
    {"id": 381, "name": "Hotels & Accommodations", "is_root": False, "parents": [12], "properties": [
        ("city", str),
        ("country", str),
        ("hotel_class", int),
        ("room_type", str, ["Single", "Double", "Suite", "Family", "Studio", "Dormitory"]),
        ("guest_rating", float),
        ("breakfast_included", bool),
        ("free_wifi", bool),
        ("parking_available", bool),
        ("pet_friendly", bool),
        ("pool", bool),
        ("gym", bool),
        ("spa", bool),
        ("air_conditioning", bool),
        ("non_smoking_rooms", bool),
        ("distance_to_city_center_km", float),
    ]},

    {"id": 382, "name": "Flights", "is_root": False, "parents": [12], "properties": [
        ("origin", str),
        ("destination", str),
        ("airline", str),
        ("flight_class", str, ["Economy", "Premium Economy", "Business", "First"]),
        ("stops", int),
        ("direct_flight", bool),
        ("refundable", bool),
        ("baggage_included", bool),
        ("seat_selection", bool),
        ("meal_included", bool),
        ("ticket_type", str, ["One-way", "Round-trip", "Multi-city"]),
        ("flight_duration_hours", float),
        ("departure_time", str),
        ("arrival_time", str),
    ]},

    {"id": 383, "name": "Car Rentals", "is_root": False, "parents": [12], "properties": [
        ("car_type", str, ["Economy", "Compact", "Intermediate", "Standard", "Full-size", "Luxury", "SUV", "Minivan", "Convertible", "Truck", "Electric"]),
        ("brand", str),
        ("model", str),
        ("seats", int),
        ("doors", int),
        ("transmission_type", str, ["Automatic", "Manual"]),
        ("air_conditioning", bool),
        ("unlimited_mileage", bool),
        ("fuel_policy", str, ["Full-to-Full", "Full-to-Empty", "Pre-Purchase"]),
        ("gps_included", bool),
        ("child_seat_available", bool),
        ("driver_age_minimum", int),
        ("pickup_location", str),
        ("dropoff_location", str),
    ]},

    {"id": 384, "name": "Vacation Packages", "is_root": False, "parents": [12], "properties": [
        ("destination", str),
        ("duration_days", int),
        ("package_type", str, ["All-Inclusive", "Flight + Hotel", "Cruise", "Tour Package"]),
        ("departure_city", str),
        ("accommodation_type", str, ["Hotel", "Resort", "Villa", "Apartment", "Cabin"]),
        ("activities_included", bool),
        ("meals_included", bool),
        ("airport_transfers_included", bool),
        ("travel_dates_flexible", bool),
        ("family_friendly", bool),
        ("adult_only", bool),
        ("travel_insurance_included", bool),
    ]},

    {"id": 385, "name": "Cruises", "is_root": False, "parents": [12], "properties": [
        ("cruise_line", str),
        ("ship_name", str),
        ("departure_port", str),
        ("destination", str),
        ("duration_days", int),
        ("cabin_type", str, ["Interior", "Oceanview", "Balcony", "Suite"]),
        ("meals_included", bool),
        ("drinks_included", bool),
        ("onboard_activities_included", bool),
        ("shore_excursions_included", bool),
        ("family_friendly", bool),
        ("adult_only", bool),
        ("gratuities_included", bool),
    ]},

    {"id": 386, "name": "Activities & Tours", "is_root": False, "parents": [12], "properties": [
        ("activity_type", str, ["City Tour", "Adventure", "Cultural", "Nature", "Food & Drink", "Water Activities", "Sightseeing", "Entertainment"]),
        ("location", str),
        ("duration_hours", float),
        ("group_size", int),
        ("language", str),
        ("guide_included", bool),
        ("transportation_included", bool),
        ("meals_included", bool),
        ("family_friendly", bool),
        ("wheelchair_accessible", bool),
        ("age_restrictions", str),
    ]},

    # Services
    {"id": 387, "name": "Home Services", "is_root": False, "parents": [13], "properties": []},

    {"id": 388, "name": "Cleaning", "is_root": False, "parents": [387], "properties": [
        ("service_type", str, ["Regular Cleaning", "Deep Cleaning", "Move-In/Move-Out", "Post-Construction", "Office Cleaning"]),
        ("frequency", str, ["One-time", "Weekly", "Bi-weekly", "Monthly"]),
        ("number_of_rooms", int),
        ("number_of_bathrooms", int),
        ("square_footage", int),
        ("supplies_included", bool),
        ("eco_friendly_products", bool),
        ("pet_friendly", bool),
        ("insured_and_bonded", bool),
        ("satisfaction_guarantee", bool),
    ]},

    {"id": 389, "name": "Repair & Maintenance", "is_root": False, "parents": [387], "properties": [
        ("service_type", str, ["Plumbing", "Electrical", "HVAC", "Appliance Repair", "Roofing", "Painting", "Carpentry", "General Handyman"]),
        ("emergency_service", bool),
        ("licensed", bool),
        ("insured", bool),
        ("free_estimate", bool),
        ("satisfaction_guarantee", bool),
        ("years_of_experience", int),
    ]},

    {"id": 390, "name": "Landscaping", "is_root": False, "parents": [387], "properties": [
        ("service_type", str, ["Lawn Mowing", "Garden Design", "Tree Trimming", "Irrigation Installation", "Hardscaping", "Snow Removal", "Pest Control"]),
        ("frequency", str, ["One-time", "Weekly", "Bi-weekly", "Monthly", "Seasonal"]),
        ("licensed", bool),
        ("insured", bool),
        ("free_estimate", bool),
        ("organic_products", bool),
        ("satisfaction_guarantee", bool),
    ]},

    {"id": 391, "name": "Professional Services", "is_root": False, "parents": [13], "properties": []},

    {"id": 392, "name": "Legal", "is_root": False, "parents": [391], "properties": [
        ("area_of_practice", str, ["Family Law", "Criminal Law", "Corporate Law", "Immigration Law", "Intellectual Property", "Real Estate Law", "Personal Injury", "Tax Law", "Employment Law"]),
        ("licensed", bool),
        ("years_of_experience", int),
        ("free_consultation", bool),
        ("languages_spoken", str),
        ("success_rate_percentage", float),
    ]},

    {"id": 393, "name": "Financial", "is_root": False, "parents": [391], "properties": [
        ("service_type", str, ["Accounting", "Tax Preparation", "Financial Planning", "Investment Advice", "Bookkeeping", "Auditing", "Payroll Services"]),
        ("certified", bool),
        ("years_of_experience", int),
        ("free_consultation", bool),
        ("languages_spoken", str),
        ("industries_served", str),
    ]},

    {"id": 394, "name": "Consulting", "is_root": False, "parents": [391], "properties": [
        ("consulting_field", str, ["Management", "IT", "Human Resources", "Marketing", "Operations", "Strategy", "Environmental", "Engineering"]),
        ("years_of_experience", int),
        ("free_consultation", bool),
        ("industries_served", str),
        ("languages_spoken", str),
    ]},

    {"id": 395, "name": "Health & Wellness Services", "is_root": False, "parents": [13], "properties": []},

    {"id": 396, "name": "Massage", "is_root": False, "parents": [395], "properties": [
        ("massage_type", str, ["Swedish", "Deep Tissue", "Sports", "Hot Stone", "Aromatherapy", "Thai", "Reflexology", "Prenatal"]),
        ("session_duration_minutes", int),
        ("in_home_service", bool),
        ("certified_therapist", bool),
        ("gender_preference", str, ["Male", "Female", "No Preference"]),
        ("aromatherapy_included", bool),
        ("couples_massage_available", bool),
    ]},

    {"id": 397, "name": "Personal Training", "is_root": False, "parents": [395], "properties": [
        ("training_type", str, ["Strength Training", "Cardio", "Yoga", "Pilates", "CrossFit", "Martial Arts", "Rehabilitation"]),
        ("session_duration_minutes", int),
        ("in_home_service", bool),
        ("certified_trainer", bool),
        ("gender_preference", str, ["Male", "Female", "No Preference"]),
        ("group_training_available", bool),
        ("nutrition_advice_included", bool),
    ]},

    {"id": 398, "name": "Nutrition Counseling", "is_root": False, "parents": [395], "properties": [
        ("counseling_type", str, ["Weight Loss", "Sports Nutrition", "Vegan/Vegetarian", "Clinical Nutrition", "General Health"]),
        ("session_duration_minutes", int),
        ("in_person_or_online", str, ["In-Person", "Online", "Both"]),
        ("certified_nutritionist", bool),
        ("meal_planning_included", bool),
        ("follow_up_support", bool),
    ]},

]