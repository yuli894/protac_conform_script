import csv

import os
import re
import csv

def extract_data(file_path):
    data = []
    start_pattern = re.compile(r'Running xtb: xtb xtb\.xyz --opt --gfn 2 --gbsa h2o --chrg 0 --uhf 0')
    end_pattern = re.compile(r'If you want to exit, directly press ENTER button.*?Press ENTER button to exit')

    with open(file_path, 'r') as file:
        lines = file.readlines()

    started = False
    for line in lines:
        if start_pattern.search(line):
            started = True
            data = []
        if started:
            data.append(line.split()[-1].strip())
        if end_pattern.search(line):
            started = False

    return data

def process_folder(folder_path):
    csv_data = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".out"):
                file_path = os.path.join(root, file)
                folder_name = os.path.basename(os.path.dirname(file_path))
                data = extract_data(file_path)
                if data:
                    line_count = len(data)
                    last_column = data[-1]
                    csv_data.append([folder_name, last_column, line_count])

    return csv_data

def main():
    root_folder = 'C:/Users\lyh16\Desktop\pythonProject/test_min_xyz'  # 替换为你的根文件夹路径
    output_csv = 'output.csv'  # 输出的CSV文件名

    csv_data = process_folder(root_folder)

    with open(output_csv, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Folder Name', 'Last Column Text', 'Line Count'])
        csv_writer.writerows(csv_data)

    print(f"CSV file '{output_csv}' has been created.")

if __name__ == "__main__":
    main()

def count_elements_in_each_row(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            # 统计每一行从第二个元素开始的元素个数
            element_count = len(row) - 1
            # 在原csv文件中将每一行统计的个数保存在行的开头
            new_row = [element_count] + row
            # 写入新的行到输出文件
            writer.writerow(new_row)

# 输入文件路径
input_file_path = 'output.csv'
# 输出文件路径
output_file_path = 'put.csv'

# 调用函数进行处理
count_elements_in_each_row(input_file_path, output_file_path)

