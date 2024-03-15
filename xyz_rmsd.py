from rdkit import Chem
from rdkit.Chem import AllChem

def read_xyz_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Assuming the first line contains the number of atoms
    num_atoms = int(lines[0].strip())

    # Extracting atom coordinates
    coords = [list(map(float, line.split()[1:4])) for line in lines[2:]]

    return num_atoms, coords

def generate_rdkit_mol(coords):
    mol = Chem.MolFromSmiles('')  # An empty molecule

    for coord in coords:
        atom = Chem.Atom('C')  # Carbon atom (you can change it based on your atoms)
        mol.AddAtom(atom)

    return mol

def calculate_rmsd(file_path1, file_path2):
    # Read coordinates from XYZ files
    _, coords1 = read_xyz_file(file_path1)
    _, coords2 = read_xyz_file(file_path2)

    # Generate RDKit Mol objects
    mol1 = generate_rdkit_mol(coords1)
    mol2 = generate_rdkit_mol(coords2)

    # Generate 3D coordinates for the molecules
    AllChem.EmbedMolecule(mol1)
    AllChem.EmbedMolecule(mol2)

    # Align molecules and calculate RMSD
    rmsd = AllChem.GetBestRMS(mol1, mol2)

    return rmsd

if __name__ == "__main__":
    file_path1 = "1.xyz"
    file_path2 = "2.xyz"

    rmsd_value = calculate_rmsd(file_path1, file_path2)
    print(f"RMSD between {file_path1} and {file_path2}: {rmsd_value:.4f} Angstroms")
