import os

# Define the root directory to search for files
root_dir = '/path/to/root/directory'

# Define the file extension to search for
extension = '.txt'

# Define a list to store the file paths
file_paths = []

# Walk through the directory tree and add file paths with the desired extension to the list
for dirpath, dirnames, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename.endswith(extension):
            file_paths.append(os.path.join(dirpath, filename))

# Print the list of file paths
for path in file_paths:
    print(path)
