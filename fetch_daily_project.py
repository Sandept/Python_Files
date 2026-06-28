import os
import random
import shutil
import subprocess

# 1. Define the source repository
SOURCE_REPO = "https://github.com/ndleah/python-mini-project.git"
TEMP_DIR = "temp_source_repo"

def main():
    # 2. Clone the source repository temporarily
    print(f"Cloning {SOURCE_REPO}...")
    subprocess.run(["git", "clone", SOURCE_REPO, TEMP_DIR], check=True)

    # 3. Find all Python (.py) files in the cloned repository
    python_files = []
    for root, dirs, files in os.walk(TEMP_DIR):
        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))

    if not python_files:
        print("No Python files found in the source repository.")
        return

    # 4. Pick a random Python file
    chosen_file = random.choice(python_files)
    filename = os.path.basename(chosen_file)
    
    # 5. Copy the file into your repository (the current directory)
    # If a file with the same name exists, it will overwrite it or you can modify the name
    destination = filename
    shutil.copy(chosen_file, destination)
    
    # Add a comment at the top to give credit to the original author
    with open(destination, 'r+', encoding='utf-8') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(f"# Automated import from: {SOURCE_REPO}\n# Original Author: ndleah\n\n" + content)

    print(f"Successfully copied: {filename}")

    # 6. Clean up the temporary cloned repository
    # Handle read-only files in the .git folder which can cause rmtree to fail
    def remove_readonly(func, path, excinfo):
        os.chmod(path, 0o777)
        func(path)
        
    shutil.rmtree(TEMP_DIR, onerror=remove_readonly)

if __name__ == "__main__":
    main()
