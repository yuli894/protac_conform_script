# 修改第二行注释为文件名
import os

def modify_xyz_comments(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".xyz"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r') as file:
                lines = file.readlines()

            if len(lines) > 1:
                file_name_without_extension = os.path.splitext(filename)[0]  # 获取文件名（不含文件格式）
                lines[1] = file_name_without_extension + '\n'  # 修改第二行注释为文件名

            with open(file_path, 'w') as file:
                file.writelines(lines)

if __name__ == "__main__":
    folder_path = "C:/Users\lyh16\Desktop\molclus_str"  # 修改为包含xyz文件的文件夹路径
    modify_xyz_comments(folder_path)
