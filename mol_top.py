# 提取所有子文件夹内占比最高的结构
import os


def process_folder(folder_path, output_path):
    with open(output_path, 'w') as output_file:
        for subdir, _, files in os.walk(folder_path):
            for file in files:
                if file.endswith('.xyz'):
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r') as input_file:
                        # 读取第一行的数字 n
                        first_line = input_file.readline().strip()
                        try:
                            n = int(first_line)
                        except ValueError:
                            print(f"Error: Unable to extract a valid number from the first line of {file_path}")
                            continue

                        # 读取前 n+2 行的文本
                        content = [first_line] + [input_file.readline().strip() for _ in range(n + 1)]

                        # 在第 2 行末尾写入子文件夹名
                        content[1] = f'{os.path.basename(subdir)} {content[1]}'

                        # 将提取的内容写入输出文件
                        output_file.write('\n'.join(content))
                        # 添加空行分隔不同子文件夹的内容
                        output_file.write('\n')

if __name__ == "__main__":
    folder_path = "C:/Users\lyh16\Desktop\pythonProject/test_min_xyz"
    output_path = "C:/Users\lyh16\Desktop\pythonProject/test_min_xyz\output.xyz"

    process_folder(folder_path, output_path)
    print("Task completed. Output file is:", output_path)
