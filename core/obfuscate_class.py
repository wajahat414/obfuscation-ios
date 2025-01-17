import file_utility as fu
import os
import uuid
import json
import config

project_config_path = "Trader_iOS/iPhone/Egoli/Egoli.xcodeproj/project.pbxproj"
exclude = ""
mapping_file = "x_obfuscated_classes_mapping.json"


def generate_obfuscated_name(original_name, used_names):
    while True:
        obfuscated_name = f"Obf_{uuid.uuid4().hex[:8]}"
        if obfuscated_name not in used_names:
            used_names.add(obfuscated_name)
            return obfuscated_name


def load_or_create_mapping(mapping_file):
    if os.path.exists(mapping_file):
        with open(mapping_file, "r") as f:
            mapping = json.load(f)
    else:
        mapping = {}
    return mapping


def save_mapping(mapping, mapping_file):
    with open(mapping_file, "w") as f:
        json.dump(mapping, f, indent=4)
    print(f"Obfuscation mapping saved to {mapping_file}")


def obfuscate_class(project_path, class_name, obf_class_name):
    class_files_path = fu.find_class_files(
        class_name=class_name, project_dir=project_path
    )
    if class_files_path:
        for class_path in class_files_path:
            fu.rename_class_filename(class_path, obf_class_name)
    else:
        print(f"No Matching file Found for{class_name}")
    files = fu.get_all_files_in_project(
        project_path, excluded_dirs=config.EXCLUDED_DIRECTORIES
    )
    print(f"Found {len(files)} files in the project:")
    for file_path in files:
        fu.replace_inside_file(file_path, class_name, obf_class_name)


def obfuscate_all_custom_classes(project_root, custom_classes):
    mapping = load_or_create_mapping(mapping_file)
    used_names = set(mapping.values())
    files = custom_classes
    for classx in custom_classes:
        # class_name = fu.get_filename_from_path(file_path
        obfuscated_name = generate_obfuscated_name(
            original_name=classx, used_names=used_names
        )
        mapping[classx] = obfuscated_name
        print(obfuscated_name)
        obfuscate_class(
            project_path=project_root,
            class_name=classx,
            obf_class_name=obfuscated_name,
        )
    save_mapping(mapping, mapping_file=mapping_file)
