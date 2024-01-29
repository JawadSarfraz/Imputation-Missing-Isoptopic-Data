import pandas as pd
import os
import string

def split_and_save(file_path, output_dir):
    try:
        excel_data = pd.ExcelFile(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while opening the file: {e}")
        return

    # Generate column names A, B, C, ..., AA, AB, ...
    col_names = list(string.ascii_uppercase)
    for first_letter in string.ascii_uppercase:
        for second_letter in string.ascii_uppercase:
            col_names.append(first_letter + second_letter)

    dataset_folders = excel_data.sheet_names  # List of sheet names from the Excel file
    for sheet_name in dataset_folders:
        try:
            data = pd.read_excel(excel_data, sheet_name=sheet_name)
            # Rename columns
            data.columns = col_names[:data.shape[1]]
            save_path = os.path.join(output_dir, sheet_name, 'Original_Data', f'{sheet_name}.xlsx')
            os.makedirs(os.path.dirname(save_path), exist_ok=True)  # Ensure the directory exists
            data.to_excel(save_path, index=False)
            print(f"Saved: {save_path}")
        except Exception as e:
            print(f"An error occurred while processing the sheet '{sheet_name}': {e}")

# Usage
file_path = 'subdatasets.xlsx'  # Path to the main Excel file
output_dir = 'Data_Analysis_Project'
split_and_save(file_path, output_dir)