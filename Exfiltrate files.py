# -*- coding: utf-8 -*-

import os
import shutil

root_dir = r'/Projecto Dir Tree/Complex Folder Tree'
new_dir = r'/Projecto Dir Tree/Tree'

for dirpath, dirnames, filenames in os.walk(root_dir):
    # Check if there are files in the current directory
    if len(filenames) > 0:
        # Create the new directory if it doesn't exist
        if not os.path.exists(new_dir):
            os.makedirs(new_dir)

        # Copy all files to the new directory
        for i, filename in enumerate(filenames):
            file_path = os.path.join(dirpath, filename)
            new_filename = filename
            new_file_path = os.path.join(new_dir, new_filename)

            # If the file already exists, rename it with a counter
            while os.path.exists(new_file_path):
                name, ext = os.path.splitext(filename)
                new_filename = f"{name}_{i}{ext}"
                new_file_path = os.path.join(new_dir, new_filename)
                i += 1

            shutil.copy(file_path, new_file_path)

            # Remove the original file
            os.remove(file_path)
