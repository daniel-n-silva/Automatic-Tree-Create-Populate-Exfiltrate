import os

root_dir = "my_tree"

# Create the root directory
os.makedirs(root_dir, exist_ok=True)

# Create subdirectories
for i in range(3):
    subdir = os.path.join(root_dir, f"subdir_{i}")
    os.makedirs(subdir, exist_ok=True)

    # Create subdirectories in each subdirectory
    for j in range(2):
        subsubdir = os.path.join(subdir, f"subsubdir_{j}")
        os.makedirs(subsubdir, exist_ok=True)

print("Directory tree created successfully!")