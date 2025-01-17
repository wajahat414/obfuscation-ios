import os
import re
import subprocess
import config


def find_class_files(class_name, project_dir):
    matchingfiles = set()

    for root, _, files in os.walk(project_dir):
        for file in files:
            if file.startswith(class_name) and file.endswith(
                (".h", ".m", ".swift", ".xib", ".pbxproj")
            ):
                matchingfiles.add(os.path.join(root, file))
    return matchingfiles


def replace_inside_file(file_path, search_string, replace_string):
    try:
        # Verify the file is text and readable
        if not file_path.endswith(config.FILE_EXTENTIONS):
            return 0

        # Read the file content with proper encoding and error handling
        is_pbxproj = file_path.endswith(".pbxproj")
        if is_pbxproj:
            result = subprocess.run(
                ["ruby", "rename_pbxproj.rb", file_path, search_string, replace_string],
                capture_output=True,
                text=True,
            )
            if result.returncode == 0:
                print(result.stdout)
                return int(result.stdout.strip().split()[-1])  # Number of replacements
            else:
                print(f"Error in Ruby script: {result.stderr}")
                return -1

        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()

        # Use regex for word-boundary matching to avoid partial replacements
        pattern = rf"\b{re.escape(search_string)}\b"
        occurrences = len(re.findall(pattern, content))

        if occurrences > 0:
            updated_content = re.sub(pattern, replace_string, content)
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(updated_content)

            print(
                f"Replaced {occurrences} occurrence(s) of '{search_string}' with '{replace_string}' in {file_path}"
            )
            return occurrences
        else:
            return 0

    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")
        return -1


def rename_class_filename(file_path, new_file_name):
    try:
        # Extract the directory, old file name, and file extension
        directory, old_file_name = os.path.split(file_path)
        file_name, file_extension = os.path.splitext(old_file_name)

        # Construct the new file name with the original extension
        new_file_name_with_extension = new_file_name + file_extension
        new_file_path = os.path.join(directory, new_file_name_with_extension)

        # Rename the file
        os.rename(file_path, new_file_path)
        print(
            f"File renamed from '{old_file_name}' to '{new_file_name_with_extension}'"
        )

        return new_file_path
    except Exception as e:
        print(f"An error occurred while renaming the file: {e}")
        return None


def get_filename_from_path(file_path):
    try:
        # Extract the directory, old file name, and file extension
        directory, old_file_name = os.path.split(file_path)
        file_name, file_extension = os.path.splitext(old_file_name)
        return file_name
    except Exception as e:
        print(f"An error occurred while renaming the file: {e}")
        return None


def get_all_files_in_project(project_dir, excluded_dirs=None):
    if excluded_dirs is None:
        excluded_dirs = []

    all_files = []

    try:
        # Walk through the directory
        for root, dirs, files in os.walk(project_dir):
            # Modify `dirs` in-place to exclude specific directories
            dirs[:] = [d for d in dirs if d not in excluded_dirs]

            for file in files:
                # Append full file path
                all_files.append(os.path.join(root, file))

        return all_files
    except Exception as e:
        print(f"An error occurred while scanning the directory: {e}")
        return []
