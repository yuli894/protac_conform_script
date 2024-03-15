import csv
import statistics

def process_row(row):
    row = [float(val) for val in row]
    min_val = min(row)
    max_val = max(row)
    row = [val for val in row if val != min_val and val != max_val]
    if not row:
        return "No data after removing min and max"
    elif len(row) == 1:
        return row[0]
    elif len(set(row)) == 1:
        return row[0]
    else:
        return statistics.median(row)

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as input_csv, open(output_file, 'w', newline='') as output_csv:
        reader = csv.reader(input_csv)
        writer = csv.writer(output_csv)

        for row in reader:
            result = process_row(row)
            writer.writerow([result])

if __name__ == "__main__":
    input_file = "1.csv"  # Specify your input CSV file name here
    output_file = "delminmax_1.csv"  # Specify your output CSV file name here
    process_csv(input_file, output_file)
