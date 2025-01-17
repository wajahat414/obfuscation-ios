require 'xcodeproj'

if ARGV.length != 3
  puts "Usage: ruby rename_pbxproj.rb <project_path> <search_string> <replace_string>"
  exit 1
end

project_path, search_string, replace_string = ARGV

begin
  # Open the Xcode project
  project = Xcodeproj::Project.open(project_path)

  # Count occurrences and perform replacement
  occurrences = 0
  project.files.each do |file|
    if file.path && file.path.include?(search_string)
      file.path = file.path.gsub(search_string, replace_string)
      occurrences += 1
    end
  end

  # Save changes to the project
  project.save
  puts "Replaced #{occurrences} occurrence(s) of '#{search_string}' with '#{replace_string}' in #{project_path}"
  exit 0
rescue => e
  puts "An error occurred: #{e.message}"
  exit 1
end
