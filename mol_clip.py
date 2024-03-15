def split_xyz_file(input_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    compound_count = 0
    compound_lines = []

    for line in lines:
        if line.strip().isdigit():
            if compound_count > 0:
                save_xyz_file(compound_lines, f'{compound_lines[1].strip()}.xyz')
                compound_lines = []
            compound_count += 1
        compound_lines.append(line)

    if compound_count > 0:
        save_xyz_file(compound_lines, f'{compound_lines[1].strip()}.xyz')

def save_xyz_file(lines, filename):
    with open(filename, 'w') as file:
        file.writelines(lines)

if __name__ == "__main__":
    input_filename = "Molecule.xyz"
    split_xyz_file(input_filename)
