#根据比例个数提取xyz结构，分割，用于properties
import os
import csv


def extract_structures(csv_filename, folder_path):
    # 读取CSV文件
    with open(csv_filename, 'r') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # 获取Data Count列的数据
            data_count = int(row['Data Count'])
            # 获取行开头名称
            folder_name = row['Folder'].strip()
            # 构建匹配的文件夹路径
            folder_path_to_search = os.path.join(folder_path, folder_name)

            # 检查文件夹是否存在
            if os.path.exists(folder_path_to_search):
                # 遍历文件夹中的文件
                for filename in os.listdir(folder_path_to_search):
                    # 检查文件是否是xyz文件
                    if filename.endswith('.xyz'):
                        xyz_file_path = os.path.join(folder_path_to_search, filename)
                        # 提取前n个结构并保存为单独的xyz文件
                        extract_xyz_structures(xyz_file_path, data_count, folder_name)


def extract_xyz_structures(xyz_file_path, data_count, folder_name):
    # 创建文件夹以保存提取的结构文件
    output_folder = 'extracted_structures'
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 读取xyz文件中的原子数目和所有原子信息
    with open(xyz_file_path, 'r') as xyz_file:
        lines = xyz_file.readlines()
        num_atoms = int(lines[0].strip())  # 原子总数
        total_structures = (len(lines)) // (num_atoms + 2)  # 计算总结构数目
        print(total_structures)
        print(data_count)
        # 读取前n个结构
        for i in range(min(total_structures, data_count)):
            start_index = i * (num_atoms + 2)
            end_index = min(start_index + num_atoms + 2, len(lines))
            # 生成结构文件名
            output_filename = f"{folder_name}_{i + 1}.xyz"
            output_file_path = os.path.join(output_folder, output_filename)
            # 写入结构数据到文件
            with open(output_file_path, 'w') as output_file:
                output_file.writelines(lines[start_index:end_index])


# 指定CSV文件路径和文件夹路径
csv_filename = 'F:\protac_data\molclus_result2/best_mol_1p.csv'
folder_path = 'F:\protac_data\molclus_result2\output'

# 调用函数提取结构
extract_structures(csv_filename, folder_path)
