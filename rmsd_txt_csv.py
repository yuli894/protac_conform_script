import os
import csv
import numpy as np


def extract_txt_content(folder_path, output_file):
    # 检查文件夹路径是否存在
    if not os.path.isdir(folder_path):
        print(f"指定路径 '{folder_path}' 不存在或者不是一个文件夹。")
        return

    # 打开输出文件以写入 CSV
    with open(output_file, 'w', newline='') as csvfile:
        # 创建 CSV 写入器
        csv_writer = csv.writer(csvfile)

        # 写入 CSV 表头
        csv_writer.writerow(['文件名', '平均数', '中位数', '最大值', '最小值', '标准差'])

        # 遍历文件夹中的文件
        for filename in os.listdir(folder_path):
            filepath = os.path.join(folder_path, filename)
            # 检查文件是否为txt文件
            if os.path.isfile(filepath) and filename.endswith('.txt'):
                # 打开文件并读取内容
                with open(filepath, 'r', encoding='utf-8') as file:
                    content = file.read()

                    # 将内容转换为浮点数列表
                    data = [float(x) for x in content.split()]

                    # 删除第一个值
                    if data:
                        data.pop(0)

                    # 检查数据是否为空
                    if data:
                        # 计算统计量
                        mean_val = np.mean(data)
                        median_val = np.median(data)
                        max_val = np.max(data)
                        min_val = np.min(data)
                        std_dev = np.std(data)

                        # 写入 CSV 文件
                        csv_writer.writerow([filename, mean_val, median_val, max_val, min_val, std_dev])
                    else:
                        print(f"文件 '{filename}' 的数据为空，无法计算统计信息。")


# 指定文件夹路径
folder_path = 'F:/protac_data/molclus_result2/rmsd_reslut'

# 指定输出的 CSV 文件路径
output_file = 'statistics.csv'

# 提取txt文件内容并将统计信息写入 CSV 文件
extract_txt_content(folder_path, output_file)

print("统计信息已成功写入 CSV 文件。")
