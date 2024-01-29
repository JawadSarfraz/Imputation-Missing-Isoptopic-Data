import pandas as pd
import os

def split_and_save(file_path, output_dir, dataset_folders):
    try:
        excel_data = pd.ExcelFile(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return

    for sheet_name in excel_data.sheet_names:
        if sheet_name in dataset_folders:
            try:
                data = pd.read_excel(excel_data, sheet_name=sheet_name)
                save_path = os.path.join(output_dir, sheet_name, 'Original_Data', f'{sheet_name}.xlsx')
                data.to_excel(save_path, index=False)
                print(f"Saved: {save_path}")
            except Exception as e:
                print(f"An error occurred while processing the sheet '{sheet_name}': {e}")

# Usage
file_path = 'subdatasets.xlsx'  # Update with the correct path
output_dir = 'Data_Analysis_Project'
dataset_folders = ['mammals (without humans)', 'terrestrial mammals', 'marine mammals', 'terrestrial herbivorous mammals', 'terr herb and marine mammals', 'fish', 'bird', 'human']
split_and_save(file_path, output_dir, dataset_folders)