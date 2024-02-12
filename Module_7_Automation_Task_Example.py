
import os
import shutil

# Example: Organizing files by extension into different directories

def organize_files_by_extension(source_dir):
    for item in os.listdir(source_dir):
        # Construct full item path
        item_path = os.path.join(source_dir, item)
        if os.path.isfile(item_path):
            # Extract file extension and create a directory name based on the extension
            file_extension = item.split('.')[-1]
            directory = os.path.join(source_dir, file_extension)
            # Create directory if it doesn't exist
            if not os.path.exists(directory):
                os.mkdir(directory)
            # Move file to its corresponding directory
            shutil.move(item_path, directory)
            print(f'Moved: {item} to {directory}/')

# Call the function with a specific directory
source_directory = '/path/to/source/directory'  # Update this path to a valid directory on your system
organize_files_by_extension(source_directory)
