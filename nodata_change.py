# 替换nodata文本
import csv

def replace_no_data(input_file, reference_file, output_file):
    with open(input_file, 'r', newline='') as input_csv, \
         open(reference_file, 'r', newline='') as reference_csv, \
         open(output_file, 'w', newline='') as output_csv:

        input_reader = csv.reader(input_csv)
        reference_reader = csv.reader(reference_csv)
        output_writer = csv.writer(output_csv)

        reference_data = list(reference_reader)

        for reference_row in reference_data:
            if 'no_data' in reference_row:
                row_index = reference_data.index(reference_row)
                input_csv.seek(0)  # Reset the input CSV file pointer
                for i, input_row in enumerate(input_reader):
                    if i == row_index:
                        output_writer.writerow(input_row)
                        break
            else:
                output_writer.writerow(reference_row)

input_file = 'output2.csv'
reference_file = 'output4.csv'
output_file = 'result.csv'

replace_no_data(input_file, reference_file, output_file)

