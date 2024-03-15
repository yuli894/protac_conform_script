import csv

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
input_file_path = 'output2.csv'
# 输出文件路径
output_file_path = 'output3.csv'

# 调用函数进行处理
count_elements_in_each_row(input_file_path, output_file_path)
