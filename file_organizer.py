pythonimport os
import shutil

def organize_folder(target_directory):
    TRACKED_EXTENSIONS = {
        '.pdf': 'Documents',
        '.docx': 'Documents',
        '.txt': 'Documents',
        '.jpg': 'Images',
        '.jpeg': 'Images',
        '.png': 'Images',
        '.mp4': 'Videos',
        '.mp3': 'Audio',
        '.zip': 'Archives',
        '.csv': 'Data_Files'
    }

    if not os.path.exists(target_directory):
        print(f"Error: The directory '{target_directory}' does not exist.")
        return

    print(f"Scanning directory: {target_directory}...")
    
    for item in os.listdir(target_directory):
        item_path = os.path.join(target_directory, item)
        if os.path.isdir(item_path):
            continue
            
        _, extension = os.path.splitext(item).lower()
        
        if extension in TRACKED_EXTENSIONS:
            folder_name = TRACKED_EXTENSIONS[extension]
            destination_folder = os.path.join(target_directory, folder_name)
            
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
                
            try:
                shutil.move(item_path, os.path.join(destination_folder, item))
                print(f"Successfully moved: {item} -> {folder_name}/")
            except Exception as e:
                print(f"Could not move {item}. Error: {e}")

if __name__ == "__main__":
    test_path = "./my_messy_folder" 
    organize_folder(test_path)
