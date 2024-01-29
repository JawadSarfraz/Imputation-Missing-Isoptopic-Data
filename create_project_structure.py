import os

def create_project_folders(main_dir, dataset_folders, subfolders):
    os.makedirs(main_dir, exist_ok=True)
    for dataset_folder in dataset_folders:
        for subfolder in subfolders:
            folder_path = os.path.join(main_dir, dataset_folder, subfolder)
            os.makedirs(folder_path, exist_ok=True)
            print(f"Created folder: {folder_path}")

# Usage Example
main_dir = 'Data_Analysis_Project'
dataset_folders = ['mammals (without humans)', 'terrestrial mammals', 'marine mammals', 'terrestrial herbivorous mammals', 'terr herb and marine mammals', 'fish', 'bird', 'human']
subfolders = ['Original_Data', 'Feature_Combinations', 'Random_Value_Removal', 'Model_Results']
create_project_folders(main_dir, dataset_folders, subfolders)