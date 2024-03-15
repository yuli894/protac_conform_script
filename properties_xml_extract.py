#处理vega后的xml文件
import os
import xml.etree.ElementTree as ET
import csv


def extract_data_from_xml(xml_file, keyword):
    # 解析XML文件
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # 遍历XML树并查找包含特定关键词的行
    for value in root.findall('value'):
        if value.attrib.get('name') == keyword:
            return value.text.strip()  # 返回找到的文本

    # 如果未找到特定关键词，则返回None
    return None


# 指定要处理的文件夹路径
folder_path = "F:\protac_data\protac_properties_output"

# 指定要提取的关键词列表
keywords = ["psa", "atoms", "hydrogens", "heavyatoms", "gyrrad", "volume", "asa", "area", "chiralnum", "logpvirtual", "logpbroto", "torflexnum" ]  # 添加更多关键词到列表中

# 获取文件夹下所有XML文件的文件路径
xml_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith(".xml")]

# 根据文件名相似部分进行分组
file_groups = {}
for xml_file in xml_files:
    filename = os.path.splitext(os.path.basename(xml_file))[0].rsplit('_', 1)[0]  # 去掉文件扩展名并获取相似部分
    if filename in file_groups:
        file_groups[filename].append(xml_file)
    else:
        file_groups[filename] = [xml_file]

# 遍历分组并提取数据，并将数据写入CSV文件
for keyword in keywords:
    with open(f"{keyword}_data.csv", "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["XML文件名", "数据"])  # 写入CSV文件头部

        for group_files in file_groups.values():
            filename = os.path.splitext(os.path.basename(group_files[0]))[0].rsplit('_', 1)[0]  # 去掉文件扩展名并获取相似部分

            group_data = []
            for xml_file in group_files:
                result = extract_data_from_xml(xml_file, keyword)
                if result is not None:
                    group_data.append(result)
                else:
                    group_data.append("未找到")  # 如果未找到数据，则写入"未找到"

            csvwriter.writerow([filename] + group_data)  # 写入文件名和数据

print("数据已成功写入CSV文件。")
