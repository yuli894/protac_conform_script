import os
import csv
import re

###########################
# 读取out文件中，构象分布结果  #
###########################
def extract_data_from_out(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()

    # 查找 " Setting file: settings2.ini" “ > crest -mdopt traj.xyz -gfn 2 --gbsa h2o --chrg 0 --uhf 0 -opt normal -niceprint”所在的行数
    setting_line = next((i for i, line in enumerate(lines) if " > crest -mdopt traj.xyz -gfn 2 --gbsa h2o --chrg 0 --uhf 0 -opt normal -niceprint" in line), None)

    if setting_line is not None:
        # 提取从 n 行开始到文本结束的内容
        data_text = ''.join(lines[setting_line + 1:])

        # 使用正则表达式提取文本
        pattern = re.compile(r'If you want to exit, directly press ENTER button(.*?)Press ENTER button to exit', re.DOTALL)
        match = pattern.search(data_text)

        if match:
            data = match.group(1).split('\n')
            # 保存最后一列中大于1%的数据，并按降序排序
            data = sorted([float(line.split()[-1].replace('%', '')) for line in data if line.strip() and float(line.split()[-1].replace('%', '')) > 1], reverse=True)
            return data
    return ['no_data']

def process_folder(folder_path, output_csv):
    with open(output_csv, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        # 写入CSV的表头
        csv_writer.writerow(['Folder', 'Data'])

        for subdir, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.out'):
                    file_path = os.path.join(subdir, file)

                    # 获取相对于母文件夹的文件夹路径
                    rel_folder_path = os.path.relpath(subdir, folder_path)
                    # 如果xyz文件在三级文件夹下，则写入二级文件夹名
                    if os.path.dirname(subdir) != folder_path:
                        rel_folder_path = os.path.basename(os.path.dirname(subdir)) + '_' + rel_folder_path

                    # 提取数据
                    data = extract_data_from_out(file_path)
                    # 将数据按降序排序，并每个数据作为一个单元格，接在文件名后面
                    csv_writer.writerow([rel_folder_path] + data)

if __name__ == "__main__":
    folder_path = "C:/Users\lyh16\Desktop\molclus_result"
    output_csv = "C:/Users\lyh16\Desktop\molclus_result\output3.csv"

    process_folder(folder_path, output_csv)
    print("Task completed. Output CSV file is:", output_csv)

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
input_file_path = 'C:/Users\lyh16\Desktop\molclus_result/output3.csv'
# 输出文件路径
output_file_path = 'C:/Users\lyh16\Desktop\molclus_result/output4.csv'

# 调用函数进行处理
count_elements_in_each_row(input_file_path, output_file_path)

