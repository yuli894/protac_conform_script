#####################################
# 读取out文件结果后，将结果保存在csv文件中
# 根据构象分布结果，提取xyz文件的指定构象，命名文件为靶点分子名+大于1%的构象数
#######################################

import os
import re
import csv

def extract_content(file_path):
    start_pattern = r"Running xtb: xtb xtb.xyz --opt --gfn 2 --gbsa h2o --chrg 0 --uhf 0 > xtb.out"
    end_pattern = r"Press ENTER button to exit"

    with open(file_path, 'r') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1

    for i, line in enumerate(lines):
        if re.search(start_pattern, line):
            start_index = i
        elif re.search(end_pattern, line):
            end_index = i
            break

    if start_index != -1 and end_index != -1:
        extracted_content = lines[start_index+1:end_index]
        return extracted_content
    else:
        return None

def process_folders(root_folder):
    result = []

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".out"):
                folder_name = os.path.basename(os.path.dirname(dirpath))
                file_path = os.path.join(dirpath, filename)

                content = extract_content(file_path)

                if content:
                    result.append({
                        'FolderName': folder_name,
                        'Content': content,
                        'LineCount': len(content)
                    })

    return result

def write_to_csv(data, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['FolderName', 'Content', 'LineCount']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == "__main__":
    root_folder = "C:/Users\lyh16\Desktop\pythonProject/test_min_xyz"
    output_file = "output.csv"

    result_data = process_folders(root_folder)
    write_to_csv(result_data, output_file)





