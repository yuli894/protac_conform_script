
import oddt
from oddt.interactions import hbonds

# 读取两个分子
mol1 = next(oddt.toolkit.readfile('sdf', '1.sdf'))
mol2 = next(oddt.toolkit.readfile('sdf', '1.sdf'))

protein_atoms, ligand_atoms, strict = hbonds(mol1, mol2)
print(protein_atoms)