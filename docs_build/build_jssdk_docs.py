in_dir = ""
out_dir = ""

import os


def rename_files_in_directory(directory):
    """Renames files in the directory to only keep the part after the last dot."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Split the filename by the last dot
            if '.' in filename:
                new_filename = filename.split('.')[-2] + '.' + filename.split('.')[-1]
                # Get full paths for old and new filenames
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, new_filename)

                # Rename the file
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {filename} -> {new_filename}")
def create_index_for_directory(directory):
    """Create an index.md file for a given directory listing all files."""
    index_file_path = os.path.join(directory, 'index.md')

    # Start writing the index content
    with open(index_file_path, 'w') as index_file:
        index_file.write(f"# Index of {os.path.basename(directory)}\n\n")

        # List all files in the current directory (but not subdirectories)
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)

            if os.path.isfile(file_path) and filename != 'index.md':
                # Write links to the files
                index_file.write(f"- [{filename}]({filename})\n")

        # List all subdirectories and link to their respective index.md
        for subdir in os.listdir(directory):
            subdir_path = os.path.join(directory, subdir)
            if os.path.isdir(subdir_path):
                # Link to the subdirectory's index.md
                subdir_index_path = os.path.join(subdir, 'index.md')
                index_file.write(f"- [{subdir}/](./{subdir_index_path})\n")

def traverse_directories_and_create_indices(base_dir):
    """Traverse all directories under base_dir and create an index.md file in each."""
    for root, dirs, files in os.walk(base_dir):
        # Create index.md for the current directory
        create_index_for_directory(root)


# Define the base directory you want to start from
base_directory = r"E:\Shabtay\platform\jssdk\new-docs"  # Change this to the path of your documentation

rename_files_in_directory(base_directory)

# Start the process
traverse_directories_and_create_indices(base_directory)

print("Index files created successfully.")
