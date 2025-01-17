import os
import re
import json

# List of system class prefixes (e.g., from Apple frameworks like UIKit, Foundation)
SYSTEM_PREFIXES = [
    "NS",
    "UI",
    "CG",
    "CA",
    "MK",
    "AB",
    "CL",  # Example prefixes from system frameworks
    "AV",
    "WK",
    "MF",
    "SK",
    "UI",
    "CN",
    "EK",  # Add more prefixes as needed
]


# Function to check if a class is part of a system framework
def is_system_class(class_name):
    return any(class_name.startswith(prefix) for prefix in SYSTEM_PREFIXES)


# Function to read file content safely
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except UnicodeDecodeError:
        # Handle files that can't be decoded properly
        print(f"Skipping non-UTF8 file: {file_path}")
        return None


# Function to collect all .h and .m files
def collect_class_files(directory, exclude_dirs=None):
    if exclude_dirs is None:
        exclude_dirs = ["Pods", "Carthage", "Frameworks"]

    class_files = []
    for root, dirs, files in os.walk(directory):
        # Exclude specific directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            if file.endswith(".h") or file.endswith(".m"):
                class_files.append(os.path.join(root, file))
    return class_files


# Function to extract class names from .h files
def extract_class_names(header_files):
    class_names = []
    for file in header_files:
        content = read_file(file)
        if content:
            # Match Objective-C class/interface declaration
            matches = re.findall(r"@interface\s+([A-Za-z_]\w*)", content)
            class_names.extend(matches)
    return class_names


# Function to classify classes as system or custom
def classify_classes(class_names):
    system_classes = [cls for cls in class_names if is_system_class(cls)]
    custom_classes = [cls for cls in class_names if not is_system_class(cls)]
    return system_classes, custom_classes


# Function to store class data in a JSON file
def store_classes_in_json(system_classes, custom_classes, json_file_path):
    class_data = {"system_classes": system_classes, "custom_classes": custom_classes}
    with open(json_file_path, "w") as json_file:
        json.dump(class_data, json_file, indent=4)
    print(f"Class data has been stored in {json_file_path}")


# Main function
def list_and_store_classes(directory, json_file_path):
    # Step 1: Collect .h and .m files
    class_files = collect_class_files(directory)

    # Step 2: Extract class names from .h files
    header_files = [f for f in class_files if f.endswith(".h")]
    class_names = extract_class_names(header_files)

    # Step 3: Classify classes into system and custom
    system_classes, custom_classes = classify_classes(class_names)

    # Step 4: Store the data in a JSON file
    store_classes_in_json(system_classes, custom_classes, json_file_path)


# Example usage
project_path = "./Trader_iOS"  # Replace with your project directory path
output_json_file = "class_data.json"  # The JSON file where the data will be stored
list_and_store_classes(project_path, output_json_file)
