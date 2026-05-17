import os
import shutil
from pathlib import Path

def gather_and_move_registries():
    current_dir = Path.cwd()
    target_dir = current_dir / "00_Registries"
    
    # Create the target directory if it doesn't exist
    target_dir.mkdir(exist_ok=True)
    
    # Walk through all subdirectories recursively
    for root, dirs, files in os.walk(current_dir):
        root_path = Path(root)
        # Skip the target directory itself to avoid moving already moved files
        if root_path == target_dir:
            continue
        
        for file in files:
            if file.endswith("_Registry.md"):
                src_path = root_path / file
                dst_path = target_dir / file
                
                # Handle duplicate filenames (though unlikely if original dir names were unique)
                if dst_path.exists():
                    base = file[:-3]  # remove .md
                    counter = 1
                    while dst_path.exists():
                        new_name = f"{base}_{counter}.md"
                        dst_path = target_dir / new_name
                        counter += 1
                    print(f"⚠️ Duplicate: {src_path} → {dst_path.name}")
                
                shutil.move(str(src_path), str(dst_path))
                print(f"📦 Moved: {src_path} → {dst_path}")

if __name__ == "__main__":
    gather_and_move_registries()