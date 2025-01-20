# iOS Obfuscation Tool

The **iOS Obfuscation Tool** is designed to provide code obfuscation for iOS projects by renaming source files and classes based on a user-defined configuration. It helps safeguard your source code by making it harder to reverse-engineer. The tool is currently under development, and contributions are welcome!

---

## Features

- **Rename Source Files**  
  Uses Python scripts to rename source files based on definitions provided in a configuration file.

- **Custom Class Name Generation**  
  Dynamically generates unique class names and assigns them unique obfuscation IDs.

- **Xcode Project Integration**  
  Utilizes a Ruby gem to rename classes within the `.xcodeproj` file for seamless project integration.

- **Objective-C Compatibility**  
  Supports obfuscation for Objective-C source code.

- **Open Source and Extensible**  
  Open to contributions and improvements to address edge cases and enhance functionality.

---

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/wajahat414/obfuscation-ios.git
   cd obfuscation-ios

2. **Install dependencies::**
   ```bash
   pip install -r requirements.txt

3. **Set up your configuration file::**
  Define your source file mapping and obfuscation rules in the provided configuration file


## Usage

1. **python generate_class_names.py:**
   ```bash
   python generate_class_names.py
   python getSystemClasses.py
2. **Run the main obfuscation script:**
   ```bash
   python core/main.py

## Current Limitations
	•	Some edge cases are yet to be resolved, particularly with specific Objective-C constructs.
	•	Limited support for Swift source files (planned for future releases).
	•	The tool is still in development, and stability may vary.

## Contributing

We welcome contributions! Feel free to:
	1.	Report issues and bugs.
	2.	Submit pull requests with improvements.
	3.	Suggest new features or enhancements.

To contribute, fork the repository, make your changes, and create a pull request.
