#根据中位数抽取结构文件夹
import shutil
import os
import csv
import random
from statistics import median

def process_csv_file(csv_path, output_folder):
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        folder_names = next(csv_reader)[1:]  # Get folder names from the first row (excluding the first cell)

        for row in csv_reader:
            subfolder_name = row[0]  # Get subfolder name from the first column
            data = list(map(float, row[1:]))  # Convert data to floats

            if data:  # Check if data list is not empty
                median_value = median(data)  # Calculate median

                # Find indices where median value occurs
                median_indices = [i for i, val in enumerate(data) if val == median_value]
                # Choose a random index from the list of median indices
                chosen_index = random.choice(median_indices)

                chosen_folder = folder_names[chosen_index]  # Choose the corresponding folder name
                subfolder_path = os.path.join(folder_path, chosen_folder, subfolder_name)
                print(f"Median value {median_value} found in folder '{chosen_folder}' of subfolder '{subfolder_name}' at path: {subfolder_path}")
                #print(subfolder_path)

                # Check if source subfolder exists and is a directory
                source_subfolder = os.path.join(os.path.dirname(csv_path), subfolder_name)
                if os.path.isdir(source_subfolder):
                    # Copy subfolder to new location
                    if not os.path.exists(subfolder_path):
                        shutil.copytree(source_subfolder, subfolder_path)
                    else:
                        print(f"Destination folder '{subfolder_path}' already exists. Skipping copying.")
                #else:
                    #print(f"Source subfolder '{source_subfolder}' not found. Skipping copying.")

def main(folder_path):
    output_folder = os.path.join(folder_path, "output")  # New folder for copied subfolders
    os.makedirs(output_folder, exist_ok=True)  # Create output folder if it doesn't exist

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.csv'):
            process_csv_file(file_path, output_folder)

if __name__ == "__main__":
    folder_path = "F:/protac_data/molclus_result2"  # 指定包含CSV文件的文件夹路径
    main(folder_path)
