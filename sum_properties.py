import csv

def print_csv_file_without_header(file_path):
    data = []
    with open(file_path, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            data.append(row[1:])  # Append elements from index 1 to the end of each row
    return data

def convert_percentage_to_float(percentage):
    percentage = percentage.strip('%')
    if percentage:
        try:
            return float(percentage) / 100
        except ValueError:
            # Handle the case where the value is not a valid percentage
            return 0.0  # or any other appropriate value
    else:
        return 0.0  # or any other appropriate value

def calculate_weighted_sum(file1_data, file2_data):
    weighted_sums = []
    for row1, row2 in zip(file1_data, file2_data):
        weighted_sum = 0
        for value1, value2 in zip(row1, row2):
            if value1.strip() and value2.strip():  # Check if both values are non-empty strings
                weighted_sum += convert_percentage_to_float(value1) * float(value2)
        weighted_sums.append(weighted_sum)
    return weighted_sums

def write_weighted_sum_to_csv(file_path, weighted_sum):
    with open(file_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(['Weighted Sum'])
        for value in weighted_sum:
            csvwriter.writerow([value])

if __name__ == "__main__":
    file1_path = "F:\protac_data\protac_properties_output/best_mol_1p_nocount.csv"
    file2_path = "F:\protac_data\protac_properties_output/area_data.csv"
    output_file_path = "sum_area.csv"

    print("Processing data from file1.csv and file2.csv...")

    file1_data = print_csv_file_without_header(file1_path)
    file2_data = print_csv_file_without_header(file2_path)
    weighted_sum = calculate_weighted_sum(file1_data, file2_data)

    write_weighted_sum_to_csv(output_file_path, weighted_sum)

    print("Weighted sum written to:", output_file_path)
