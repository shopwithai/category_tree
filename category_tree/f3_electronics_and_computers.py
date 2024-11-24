electronics_and_computers = [
    {"id": 85, "name": "Computers & Tablets", "is_root": False, "parents": [3], "properties": []},

    {"id": 86, "name": "Laptops", "is_root": False, "parents": [85], "properties": [
        ("brand", str),
        ("model", str),
        ("cpu_type", str),
        ("ram_gb", int),
        ("storage_gb", int),
        ("storage_type", str, ["HDD", "SSD", "Hybrid", "eMMC"]),
        ("screen_size_inches", float),
        ("screen_resolution", str, ["1366x768", "1920x1080", "2560x1440", "3840x2160"]),
        ("gpu_type", str),
        ("operating_system", str, ["Windows", "macOS", "Linux", "Chrome OS", "Other"]),
        ("battery_life_hours", float),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("touchscreen", bool),
        ("keyboard_backlight", bool),
    ]},

    {"id": 87, "name": "Desktops", "is_root": False, "parents": [85], "properties": [
        ("brand", str),
        ("model", str),
        ("cpu_type", str),
        ("ram_gb", int),
        ("storage_gb", int),
        ("storage_type", str, ["HDD", "SSD", "Hybrid"]),
        ("gpu_type", str),
        ("operating_system", str, ["Windows", "macOS", "Linux", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("form_factor", str, ["Tower", "Mini PC", "All-in-One", "Workstation", "Server"]),
    ]},

    {"id": 88, "name": "Tablets", "is_root": False, "parents": [85], "properties": [
        ("brand", str),
        ("model", str),
        ("screen_size_inches", float),
        ("storage_gb", int),
        ("connectivity", str, ["WiFi", "WiFi + Cellular"]),
        ("operating_system", str, ["iOS", "Android", "Windows", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("camera_mp", int),
        ("battery_life_hours", float),
    ]},

    {"id": 89, "name": "Computer Components", "is_root": False, "parents": [85], "properties": []},

    {"id": 90, "name": "Processors (CPUs)", "is_root": False, "parents": [89], "properties": [
        ("brand", str, ["Intel", "AMD", "Other"]),
        ("model", str),
        ("socket_type", str),
        ("core_count", int),
        ("thread_count", int),
        ("base_clock_ghz", float),
        ("max_boost_clock_ghz", float),
        ("tdp_watts", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 91, "name": "Graphics Cards (GPUs)", "is_root": False, "parents": [89], "properties": [
        ("brand", str),
        ("model", str),
        ("gpu_chipset", str, ["NVIDIA", "AMD", "Other"]),
        ("gpu_series", str),
        ("memory_size_gb", int),
        ("memory_type", str, ["GDDR6", "GDDR5", "HBM2", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 92, "name": "Motherboards", "is_root": False, "parents": [89], "properties": [
        ("brand", str),
        ("model", str),
        ("socket_type", str),
        ("chipset", str),
        ("form_factor", str, ["ATX", "Micro ATX", "Mini ITX", "Other"]),
        ("memory_slots", int),
        ("max_memory_gb", int),
        ("supported_memory_type", str, ["DDR4", "DDR5", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 93, "name": "Memory (RAM)", "is_root": False, "parents": [89], "properties": [
        ("brand", str),
        ("model", str),
        ("memory_type", str, ["DDR4", "DDR3", "DDR5", "Other"]),
        ("capacity_gb", int),
        ("speed_mhz", int),
        ("number_of_modules", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 94, "name": "Storage (HDDs, SSDs)", "is_root": False, "parents": [89], "properties": [
        ("brand", str),
        ("model", str),
        ("storage_type", str, ["HDD", "SSD", "Hybrid"]),
        ("capacity_gb", int),
        ("interface", str, ["SATA", "PCIe", "NVMe", "SAS", "USB", "Other"]),
        ("form_factor", str, ["2.5 inch", "3.5 inch", "M.2", "mSATA", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 95, "name": "Power Supplies", "is_root": False, "parents": [89], "properties": [
        ("brand", str),
        ("model", str),
        ("wattage_w", int),
        ("efficiency_rating", str, ["80 Plus", "Bronze", "Silver", "Gold", "Platinum", "Titanium"]),
        ("modular", str, ["Non-Modular", "Semi-Modular", "Fully Modular"]),
        ("form_factor", str, ["ATX", "SFX", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 96, "name": "Computer Accessories", "is_root": False, "parents": [85], "properties": []},

    {"id": 97, "name": "Monitors", "is_root": False, "parents": [96], "properties": [
        ("brand", str),
        ("model", str),
        ("screen_size_inches", float),
        ("resolution", str),
        ("panel_type", str, ["IPS", "TN", "VA", "OLED", "Other"]),
        ("refresh_rate_hz", int),
        ("aspect_ratio", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 98, "name": "Keyboards & Mice", "is_root": False, "parents": [96], "properties": [
        ("type", str, ["Keyboard", "Mouse", "Keyboard & Mouse Combo"]),
        ("brand", str),
        ("model", str),
        ("connection_type", str, ["Wired", "Wireless"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("keyboard_type", str, ["Mechanical", "Membrane", "Other"]),
        ("backlit", bool),
        ("key_switch_type", str),
        ("dpi", int),
        ("number_of_buttons", int),
    ]},

    {"id": 426, "name": "USB flash drives", "is_root": False, "parents": [96], "properties": [
        ("brand", str),
        ("model", str),
        ("capacity_gb", int),
        ("interface", str, ["USB 2.0", "USB 3.0", "USB 3.1", "USB 3.2", "USB-C"]),
        ("encrypted", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 99, "name": "Networking Equipment", "is_root": False, "parents": [96], "properties": []},

    {"id": 100, "name": "Routers", "is_root": False, "parents": [99], "properties": [
        ("brand", str),
        ("model", str),
        ("wireless_standard", str, ["802.11n", "802.11ac", "802.11ax"]),
        ("max_speed_mbps", int),
        ("band", str, ["Single Band", "Dual Band", "Tri-Band"]),
        ("number_of_ports", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 101, "name": "Modems", "is_root": False, "parents": [99], "properties": [
        ("brand", str),
        ("model", str),
        ("type", str, ["Cable", "DSL", "Fiber", "Satellite", "Other"]),
        ("max_speed_mbps", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 102, "name": "Switches", "is_root": False, "parents": [99], "properties": [
        ("brand", str),
        ("model", str),
        ("number_of_ports", int),
        ("port_speed", str, ["10/100 Mbps", "Gigabit", "10 Gigabit", "Other"]),
        ("managed", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 103, "name": "Cameras & Lenses", "is_root": False, "parents": [3], "properties": []},

    {"id": 104, "name": "Cameras", "is_root": False, "parents": [103], "properties": [
        ("brand", str),
        ("model", str),
        ("camera_type", str, ["DSLR", "Mirrorless", "Point & Shoot", "Action Camera", "Camcorder", "Other"]),
        ("megapixels", float),
        ("sensor_size", str),
        ("video_resolution", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 105, "name": "Lenses", "is_root": False, "parents": [103], "properties": [
        ("brand", str),
        ("model", str),
        ("focal_length_mm", str),
        ("maximum_aperture", str),
        ("mount_type", str),
        ("lens_type", str, ["Prime", "Zoom", "Telephoto", "Wide Angle", "Macro", "Other"]),
        ("image_stabilization", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 106, "name": "Camera Accessories", "is_root": False, "parents": [103], "properties": [
        ("type", str, ["Tripod", "Bag", "Flash", "Battery", "Memory Card", "Filter", "Other"]),
        ("brand", str),
        ("model", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 107, "name": "Phones & Accessories", "is_root": False, "parents": [3], "properties": []},

    {"id": 108, "name": "Smartphones", "is_root": False, "parents": [107], "properties": [
        ("brand", str, ["Apple", "Samsung", "Google", "Huawei", "Xiaomi", "Other"]),
        ("model", str),
        ("storage_gb", int),
        ("screen_size_inches", float),
        ("operating_system", str, ["iOS", "Android", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("camera_mp", int),
        ("connectivity", str, ["4G", "5G", "Other"]),
        ("dual_sim", bool),
    ]},

    {"id": 109, "name": "Feature Phones", "is_root": False, "parents": [107], "properties": [
        ("brand", str),
        ("model", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("connectivity", str, ["2G", "3G", "4G"]),
        ("battery_life_hours", float),
        ("dual_sim", bool),
    ]},

    {"id": 110, "name": "Phone Accessories", "is_root": False, "parents": [107], "properties": [
        ("type", str, ["Case", "Screen Protector", "Charger", "Cable", "Headphones", "Other"]),
        ("brand", str),
        ("model", str),
        ("compatible_with", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 111, "name": "Audio Equipment", "is_root": False, "parents": [3], "properties": []},

    {"id": 112, "name": "Headphones", "is_root": False, "parents": [111], "properties": [
        ("brand", str),
        ("model", str),
        ("type", str, ["In-Ear", "Over-Ear", "On-Ear", "Earbuds", "Other"]),
        ("connection_type", str, ["Wired", "Wireless"]),
        ("noise_cancellation", bool),
        ("microphone", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 113, "name": "Speakers", "is_root": False, "parents": [111], "properties": [
        ("brand", str),
        ("model", str),
        ("type", str, ["Portable", "Bookshelf", "Floor-standing", "Soundbar", "Subwoofer", "Other"]),
        ("connection_type", str, ["Wired", "Wireless", "Bluetooth"]),
        ("power_output_watts", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 114, "name": "Home Theater Systems", "is_root": False, "parents": [111], "properties": [
        ("brand", str),
        ("model", str),
        ("number_of_channels", str, ["2.1", "5.1", "7.1", "9.1", "Other"]),
        ("connection_type", str, ["Wired", "Wireless"]),
        ("power_output_watts", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 115, "name": "Musical Instruments", "is_root": False, "parents": [111, 8], "properties": [
        ("instrument_type", str, ["Guitar", "Piano", "Violin", "Drums", "Keyboard", "Other"]),
        ("brand", str),
        ("model", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
        ("acoustic_or_electric", str, ["Acoustic", "Electric", "Both"]),
    ]},

    {"id": 116, "name": "TVs & Home Theater", "is_root": False, "parents": [3], "properties": []},

    {"id": 117, "name": "Televisions", "is_root": False, "parents": [116], "properties": [
        ("brand", str),
        ("model", str),
        ("screen_size_inches", float),
        ("resolution", str, ["HD", "Full HD", "4K", "8K"]),
        ("smart_tv", bool),
        ("display_type", str, ["LED", "OLED", "QLED", "Plasma", "LCD", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 118, "name": "Projectors", "is_root": False, "parents": [116], "properties": [
        ("brand", str),
        ("model", str),
        ("resolution", str),
        ("brightness_lumens", int),
        ("contrast_ratio", str),
        ("lamp_life_hours", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 119, "name": "Streaming Devices", "is_root": False, "parents": [116], "properties": [
        ("brand", str),
        ("model", str),
        ("supported_resolution", str, ["1080p", "4K", "Other"]),
        ("operating_system", str, ["Roku OS", "Fire OS", "Android TV", "Apple tvOS", "Other"]),
        ("voice_control", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 120, "name": "Gaming", "is_root": False, "parents": [3], "properties": []},

    {"id": 121, "name": "Video Game Consoles", "is_root": False, "parents": [120], "properties": [
        ("brand", str, ["Sony", "Microsoft", "Nintendo", "Other"]),
        ("model", str),
        ("storage_gb", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 122, "name": "Video Games", "is_root": False, "parents": [120], "properties": [
        ("title", str),
        ("platform", str, ["PlayStation", "Xbox", "Nintendo Switch", "PC", "Other"]),
        ("genre", str, ["Action", "Adventure", "RPG", "Sports", "Other"]),
        ("age_rating", str, ["E", "T", "M", "Other"]),
        ("condition", str, ["New", "Used"]),
    ]},

    {"id": 123, "name": "Gaming Accessories", "is_root": False, "parents": [120], "properties": [
        ("type", str, ["Controller", "Headset", "Keyboard", "Mouse", "Chair", "Other"]),
        ("brand", str),
        ("model", str),
        ("platform", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 124, "name": "Wearable Technology", "is_root": False, "parents": [3], "properties": []},

    {"id": 125, "name": "Smartwatches", "is_root": False, "parents": [124], "properties": [
        ("brand", str),
        ("model", str),
        ("operating_system", str, ["watchOS", "Wear OS", "Tizen", "Other"]),
        ("screen_size_inches", float),
        ("connectivity", str, ["Bluetooth", "WiFi", "Cellular"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 126, "name": "Fitness Trackers", "is_root": False, "parents": [124], "properties": [
        ("brand", str),
        ("model", str),
        ("heart_rate_monitor", bool),
        ("gps", bool),
        ("water_resistant", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 127, "name": "Drones & Remote Control", "is_root": False, "parents": [3], "properties": []},

    {"id": 128, "name": "Drones", "is_root": False, "parents": [127], "properties": [
        ("brand", str),
        ("model", str),
        ("camera_resolution", str, ["1080p", "2.7K", "4K", "6K", "8K", "Other"]),
        ("flight_time_minutes", float),
        ("control_range_meters", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 129, "name": "RC Vehicles", "is_root": False, "parents": [127], "properties": [
        ("type", str, ["Car", "Truck", "Plane", "Boat", "Other"]),
        ("brand", str),
        ("model", str),
        ("scale", str, ["1:10", "1:8", "1:16", "Other"]),
        ("power_source", str, ["Electric", "Nitro", "Gasoline"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 130, "name": "Office Electronics", "is_root": False, "parents": [3], "properties": []},

    {"id": 131, "name": "Printers & Scanners", "is_root": False, "parents": [130], "properties": [
        ("brand", str),
        ("model", str),
        ("type", str, ["Inkjet Printer", "Laser Printer", "All-in-One", "Scanner", "Other"]),
        ("color_printing", bool),
        ("duplex_printing", bool),
        ("wireless", bool),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 132, "name": "Projectors", "is_root": False, "parents": [130], "properties": [
        ("brand", str),
        ("model", str),
        ("resolution", str),
        ("brightness_lumens", int),
        ("contrast_ratio", str),
        ("lamp_life_hours", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 133, "name": "Telephones & Communication", "is_root": False, "parents": [130], "properties": [
        ("type", str, ["Landline Phone", "VoIP Phone", "Conference Phone", "Intercom", "Other"]),
        ("brand", str),
        ("model", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 134, "name": "Other Electronics", "is_root": False, "parents": [3], "properties": []},

    {"id": 135, "name": "Batteries & Power", "is_root": False, "parents": [134], "properties": [
        ("type", str, ["Battery", "Power Bank", "Charger", "Adapter", "UPS", "Other"]),
        ("brand", str),
        ("model", str),
        ("capacity_mah", int),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 136, "name": "Smart Home Devices", "is_root": False, "parents": [134], "properties": [
        ("type", str, ["Smart Speaker", "Smart Light", "Thermostat", "Security Camera", "Other"]),
        ("brand", str),
        ("model", str),
        ("voice_assistant", str, ["Alexa", "Google Assistant", "Siri", "Other"]),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

    {"id": 137, "name": "Miscellaneous Electronics", "is_root": False, "parents": [134], "properties": [
        ("description", str),
        ("condition", str, ["New", "Used", "Refurbished"]),
    ]},

]