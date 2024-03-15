import os
import csv
######################################
##统计构象搜索后，指定范围的个数及其比例分布##
######################################
def extract_specific_text(folder_path):
    with open('extracted_data2.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Folder', 'Data Count', 'Data'])  # 写入CSV文件的标题行
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                if file.endswith(".out"):
                    file_path = os.path.join(root, file)
                    folder_name = os.path.basename(root)
                    print("Processing file:", file_path)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()
                        start_index = None
                        end_index = None
                        count = 0
                        for i, line in enumerate(lines):
                            if "If you want to exit, directly press ENTER button" in line:
                                count += 1
                                print(count)
                                if count == 2:  # 当计数器等于2时开始读取
                                    start_index = i + 1
                                    print(start_index)
                            elif "Press ENTER button to exit" in line:
                                end_index = i
                                break
                        if start_index is not None and end_index is not None:
                            extracted_text = lines[start_index:end_index]
                            last_column = [line.split()[-1] for line in extracted_text]
                            valid_data = [data.strip('%') for data in last_column if float(data.strip('%')) > 1]
                            data_count = len(valid_data)
                            if data_count > 0:  # 如果有符合条件的数据
                                csv_writer.writerow([folder_name, data_count] + valid_data)  # 写入CSV文件
                            else:
                                csv_writer.writerow([folder_name, 'nodata'])  # 没有符合条件的数据，标记为 "nodata"
                        else:
                            print("Couldn't find the specified text in the file.")
                            csv_writer.writerow([folder_name, 'nodata'])  # 文件中未找到指定文本，标记为 "nodata"

# 指定要搜索的文件夹路径
folder_path = "C:/Users\lyh16\Desktop\molclus_result2/mol3_jjh/ar_1_11"

extract_specific_text(folder_path)

