import os
import csv

def extract_folder_names(folder_path, output_file):
    folder_names = []
    for root, dirs, files in os.walk(folder_path):
        for directory in dirs:
            folder_names.append(directory)

    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Folder Name'])
        for folder_name in folder_names:
            csv_writer.writerow([folder_name])

# 指定要搜索的文件夹路径
folder_path = "C:/Users\lyh16\Desktop\molclus_result"
# 指定要保存的CSV文件路径
output_file = "folder_names.csv"

extract_folder_names(folder_path, output_file)
