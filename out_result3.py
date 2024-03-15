import os
import csv


def find_text_in_file(file_path, text_A, text_B, csv_writer, folder_name):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            count_A = 0
            count_over_1_percent = 0  # 计数器
            over_1_percent_data = []  # 存储大于1%的数据
            for idx, line in enumerate(lines, start=1):
                if text_A in line:
                    count_A += 1
                    if count_A == 2:  # 找到第二个文本A
                        start_idx = idx
                elif text_B in line and count_A >= 2:  # 当找到文本B并且已经找到过两次文本A时
                    for i in range(start_idx, idx - 1):
                        # 将每行按空格分割，并获取最后一列
                        columns = lines[i].strip().split()
                        last_column = columns[-1]
                        # 检查最后一列的值是否大于1%
                        try:
                            value = float(last_column.replace('%', ''))
                            if value > 0:
                                count_over_1_percent += 1  # 如果大于1%，计数器加一
                                over_1_percent_data.append(last_column)  # 存储大于1%的数据
                        except ValueError:
                            # 如果无法转换为float，则忽略该行
                            continue
                    # 将结果写入CSV文件
                    csv_writer.writerow([folder_name, count_over_1_percent] + over_1_percent_data)
                    return
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到.")


def search_files(folder_path, text_A, text_B, csv_writer, folder_name):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.out'):
                file_path = os.path.join(root, file_name)
                find_text_in_file(file_path, text_A, text_B, csv_writer, folder_name)


def main(root_folder_path, text_A, text_B):
    # 获取输出文件的路径
    output_file_path = os.path.join(os.path.dirname(root_folder_path), 'best_mol_1p.csv')

    # 创建CSV文件并写入表头
    with open(output_file_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Folder', 'Data Count', 'Data'])

        for folder_name in os.listdir(root_folder_path):
            folder_path = os.path.join(root_folder_path, folder_name)
            if os.path.isdir(folder_path):
                search_files(folder_path, text_A, text_B, csv_writer, folder_name)


if __name__ == "__main__":
    root_folder_path = "F:\protac_data\molclus_result2\output"
    text_A = "If you want to exit, directly press ENTER button"
    text_B = "Press ENTER button to exit"
    main(root_folder_path, text_A, text_B)
