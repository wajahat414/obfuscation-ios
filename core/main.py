from obfuscate_class import obfuscate_class, obfuscate_all_custom_classes
import file_utility as fu
import config

if __name__ == "__main__":
    from_class = "LogOutViewController"
    to_class = "SignOutViewController"

    # obfuscate_class(
    #     project_path=PROJECT_DIR, class_name=from_class, obf_class_name=to_class
    # )

    # obfuscate_all_custom_classes(config.PROJECT_DIR, custom_classes)
    # files = fu.get_all_files_in_project(config.PROJECT_CONFIG_DIR)
    # for file in files:
    #     print(file)
    obfuscate_all_custom_classes(config.PROJECT_DIR, config.custom_classes)
