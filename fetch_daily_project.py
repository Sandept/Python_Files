import os
import random
import shutil
import subprocess

# 1. Define the source repository and destination folder
SOURCE_REPO = "https://github.com/ndleah/python-mini-project.git"
TEMP_DIR = "temp_source_repo"
DEST_FOLDER = "Projects"

def main():
    # 2. Clone the source repository temporarily
    print(f"Cloning {SOURCE_REPO}...")
    subprocess.run(["git", "clone", SOURCE_REPO, TEMP_DIR], check=True)

    # 3. Find all project folders in the root of the cloned repo
    # We ignore the hidden '.git' folder and only look for directories
    project_folders = []
    for item in os.listdir(TEMP_DIR):
        item_path = os.path.join(TEMP_DIR, item)
        if os.path.isdir(item_path) and item != ".git":
            project_folders.append(item)

    if not project_folders:
        print("No project folders found in the source repository.")
        return

    # 4. Pick a random project folder
    chosen_folder = random.choice(project_folders)
    source_folder_path = os.path.join(TEMP_DIR, chosen_folder)
    dest_folder_path = os.path.join(DEST_FOLDER, chosen_folder)
    
    # 5. Copy the entire folder (including READMEs) to your repository
    print(f"Chosen project folder: {chosen_folder}")
    # dirs_exist_ok=True prevents errors if the folder happens to already exist
    shutil.copytree(source_folder_path, dest_folder_path, dirs_exist_ok=True)
    
    # 6. Add credit to any Python files inside the newly copied folder
    for root, dirs, files in os.walk(dest_folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    f.seek(0, 0)
                    f.write(f"# Automated import from: {SOURCE_REPO}\n# Original Author: ndleah\n\n" + content)

    print(f"Successfully copied the entire '{chosen_folder}' folder into {DEST_FOLDER}/")

    # 7. Clean up the temporary cloned repository
    def remove_readonly(func, path, excinfo):
        os.chmod(path, 0o777)
        func(path)
        
    shutil.rmtree(TEMP_DIR, onerror=remove_readonly)

if __name__ == "__main__":
    main()
