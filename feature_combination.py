import pandas as pd
from itertools import combinations
import os

def load_data(file_path):
    return pd.read_excel(file_path)

def generate_and_save_feature_combinations(data, output_dir, fixed_columns, additional_columns_count):
    variable_columns = data.columns[len(fixed_columns):len(fixed_columns) + additional_columns_count]
    
    for r in range(4, 7):  # 4, 5, and 6 features
        for cols in combinations(variable_columns, r):
            selected_columns = list(fixed_columns) + list(cols)
            combination_df = data[selected_columns]
            combination_df.dropna(inplace=True)
            
            filename = f"{output_dir}/combination_{'_'.join(selected_columns)}.xlsx"
            combination_df.to_excel(filename, index=False)
            print(f"Saved file: {filename}")

def process_all_datasets(base_dir, dataset_folders, fixed_columns):
    for dataset in dataset_folders:
        file_path = os.path.join(base_dir, dataset, 'Original_Data', f'{dataset}.xlsx')
        if os.path.exists(file_path):
            print(f"Processing dataset: {dataset}")
            data = load_data(file_path)
            output_dir = os.path.join(base_dir, dataset, 'Feature_Combinations')

            # Adjust this count based on the specific dataset
            additional_columns_count = len(data.columns) - len(fixed_columns)
            generate_and_save_feature_combinations(data, output_dir, fixed_columns, additional_columns_count)
        else:
            print(f"File not found: {file_path}")

# Usage Example
base_dir = 'Data_Analysis_Project'
dataset_folders = ['mammals (without humans)', 'terrestrial mammals', 'marine mammals', 'terrestrial herbivorous mammals', 'terr herb and marine mammals', 'fish', 'bird', 'human']
fixed_columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
process_all_datasets(base_dir, dataset_folders, fixed_columns)