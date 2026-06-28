import os
import random
import shutil
import subprocess

SOURCE_REPO = "https://github.com/ndleah/python-mini-project.git"
TEMP_DIR = "temp_source_repo"
DEST_FOLDER = "Projects"

def main():
    # 1. Clone source
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)
    subprocess.run(["git", "clone", SOURCE_REPO, TEMP_DIR], check=True)

    # 2. Get all projects from source
    all_projects = [item for item in os.listdir(TEMP_DIR) 
                    if os.path.isdir(os.path.join(TEMP_DIR, item)) and item != ".git"]

    # 3. Get projects already in your 'Projects' folder
    os.makedirs(DEST_FOLDER, exist_ok=True)
    existing_projects = os.listdir(DEST_FOLDER)

    # 4. Filter: Only pick projects NOT already in your folder
    available_projects = [p for p in all_projects if p not in existing_projects]

    if not available_projects:
        print("All projects have been fetched! No new projects to add.")
        # Optional: You could choose to clear your Projects folder here to start over
        return

    # 5. Pick randomly from the remaining list
    chosen_folder = random.choice(available_projects)
    source_folder_path = os.path.join(TEMP_DIR, chosen_folder)
    dest_folder_path = os.path.join(DEST_FOLDER, chosen_folder)
    
    # 6. Copy the new project
    shutil.copytree(source_folder_path, dest_folder_path)
    
    # 7. Add credit (same as before)
    for root, dirs, files in os.walk(dest_folder_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                # Check if we already added credit to avoid double-adding
                with open(file_path, 'r+', encoding='utf-8') as f:
                    content = f.read()
                    if "# Automated import from" not in content:
                        f.seek(0, 0)
                        f.write(f"# Automated import from: {SOURCE_REPO}\n# Original Author: ndleah\n\n" + content)

    print(f"Successfully added new project: {chosen_folder}")

    # 8. Cleanup
    shutil.rmtree(TEMP_DIR)

if __name__ == "__main__":
    main()
