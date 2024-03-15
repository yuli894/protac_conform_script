import os
import csv

def extract_content_between_lines(file_path, start_line_text, end_line_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            start_found = False
            end_found = False
            second_start_found = False

            extracted_data = []  # Store extracted data

            for line in file:
                if start_line_text in line:
                    if start_found and not second_start_found:
                        second_start_found = True
                    elif second_start_found and end_found:
                        break
                    start_found = True

                elif end_line_text in line:
                    if second_start_found:
                        end_found = True
                        break

                elif second_start_found:
                    columns = line.strip().split()
                    try:
                        if columns and float(columns[-2]) < 3:
                            extracted_data.append(columns[-2])
                            print(columns[-2])
                    except ValueError:
                        print(f"Error converting to float in file: {file_path}")
                        print(f"Offending line: {line.strip()}")

            if not start_found:
                print(f"Start line '{start_line_text}' not found in file: {file_path}")
            elif not second_start_found:
                print(f"Second start line '{start_line_text}' not found after the first one in file: {file_path}")
            elif not end_found:
                print(f"End line '{end_line_text}' not found after the second start line in file: {file_path}")

            return extracted_data

    except FileNotFoundError:
        print(f"File '{file_path}' not found.")


def extract_content_from_all_out_files(directory_path, start_line_text, end_line_text, output_csv):
    extracted_data_all = []
    folder_data = []  # Store folder-wise data counts

    for root, _, files in os.walk(directory_path):
        for filename in files:
            if filename.endswith(".out"):
                file_path = os.path.join(root, filename)
                extracted_data = extract_content_between_lines(file_path, start_line_text, end_line_text)
                print(extracted_data)
                if extracted_data:
                    folder_name = os.path.relpath(root, directory_path)
                    data_count = len(extracted_data)
                    folder_data.append((folder_name, data_count))
                    extracted_data_all.extend(extracted_data)

    # Write extracted data to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Folder', 'Data Count', 'Data'])
        for folder, data_count in folder_data:
            writer.writerow([folder, data_count])


# Specify folder path containing ".out" files and other parameters
directory_path = "C:/Users\lyh16\Desktop\mol_low_str"
start_line_text = "In below output, DE is energy difference with respect to the lowest one. DGmin quantifies minimal geometry difference with respect to all other clusters"
end_line_text = "Representative geometry of each cluster along with their energies have been outputted to cluster.xyz in current folder"
output_csv = "low_mol_3.csv"

# Call the function to extract content from all ".out" files in the specified folder and subfolders
extract_content_from_all_out_files(directory_path, start_line_text, end_line_text, output_csv)
