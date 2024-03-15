import os
import pandas as pd

# 读取CSV文件
file_path = 'C:/Users\lyh16\Desktop\pythonProject/test_min_xyz\output2.csv'
df = pd.read_csv(file_path, header= None)

# 提取前两列数据
matrix = df.iloc[:, :2]
print(matrix)
# 遍历二级文件夹
root_folder = 'C:/Users\lyh16\Desktop\pythonProject/test_min_xyz'
for root, dirs, files in os.walk(root_folder):
    for folder_name in dirs:
        # 尝试在矩阵中查找与文件夹名相匹配的行
        matching_row = matrix[matrix.iloc[:, 0] == folder_name]

        # 检查是否有匹配行
        if not matching_row.empty:
            # 获取匹配行的索引
            index = matching_row.index[0]

            # 获取第二列的数字
            second_column_value = matrix.iloc[index, 1]

            # 构建xyz文件路径
            xyz_file_path = os.path.join(root, folder_name, 'cluster.xyz')

            # 读取xyz文件
            with open(xyz_file_path, 'r') as xyz_file:
                # 获取文件的第一行数字
                first_line = xyz_file.readline()
                try:
                    n = int(first_line)
                except ValueError:
                    print(f"Error: Unable to extract a valid number from the first line of {file_path}")
                    continue
                # 计算行数
                m = int(second_column_value)

                # 读取文件内容
                xyz_content = [first_line] + [xyz_file.readline() for _ in range(m * (n + 2)-1)]

                xyz_content[1] = f'{os.path.basename(folder_name)} {xyz_content[1]}'

            # 构建新的xyz文件路径
            new_xyz_file_path = os.path.join(root, folder_name + 'conform.xyz')

            # 写入新的xyz文件
            with open(new_xyz_file_path, 'w') as new_xyz_file:
                new_xyz_file.writelines(xyz_content)

            print(f"Processed: {folder_name}, Created: {new_xyz_file_path}")
