import pandas as pd

def find_duplicate_values(input_file, output_file):
    df = pd.read_csv(input_file)
    duplicate_values = df[df.duplicated(df.columns[0])]
    duplicate_values.to_csv(output_file, index=False)

# 指定输入的CSV文件路径
input_file = "extracted_data.csv"
# 指定输出的CSV文件路径
output_file = "output_duplicates.csv"

find_duplicate_values(input_file, output_file)
