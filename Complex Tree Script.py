import os

root_dir = "../Complex Folder Tree"

# Create the root directory
os.makedirs(root_dir, exist_ok=True)

# Create subdirectories
for i in range(1, 6):
    subdir = os.path.join(root_dir, f"{i}")
    os.makedirs(subdir, exist_ok=True)

    # Create subdirectories in each subdirectory
    if i == 3:
        for j in range(1, 4):
            subsubdir = os.path.join(subdir, f"{i} {j}")
            os.makedirs(subsubdir, exist_ok=True)

            # Create subdirectories in each subdirectory
            if j == 2:
                for k in range(1, 4):
                    subsubsubdir = os.path.join(subsubdir, f"{i} {j} {k}")
                    os.makedirs(subsubsubdir, exist_ok=True)

                    # Create subdirectories in each subdirectory
                    if k == 1:
                        for l in range(1, 3):
                            subsubsubsubdir = os.path.join(subsubsubdir, f"{i} {j} {k} {l}")
                            os.makedirs(subsubsubsubdir, exist_ok=True)
                    elif k == 2:
                        for l in range(1, 3):
                            subsubsubsubdir = os.path.join(subsubsubdir, f"{i} {j} {k} {l}")
                            os.makedirs(subsubsubsubdir, exist_ok=True)
                    else:
                        for l in range(1, 3):
                            subsubsubsubdir = os.path.join(subsubsubdir, f"{i} {j} {k} {l}")
                            os.makedirs(subsubsubsubdir, exist_ok=True)
    elif i == 4:
        for j in range(1, 3):
            subsubdir = os.path.join(subdir, f"{i} {j}")
            os.makedirs(subsubdir, exist_ok=True)

            # Create subdirectories in each subdirectory
            for k in range(1, 4):
                subsubsubdir = os.path.join(subsubdir, f"{i} {j} {k}")
                os.makedirs(subsubsubdir, exist_ok=True)
    elif i == 5:
        for j in range(1, 4):
            subsubdir = os.path.join(subdir, f"{i} {j}")
            os.makedirs(subsubdir, exist_ok=True)

            # Create subdirectories in each subdirectory
            if j == 1:
                for k in range(1, 3):
                    subsubsubdir = os.path.join(subsubdir, f"{i} {j} {k}")
                    os.makedirs(subsubsubdir, exist_ok=True)
            else:
                os.makedirs(subsubdir, exist_ok=True)

print("Directory tree created successfully!")
