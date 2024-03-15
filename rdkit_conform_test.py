from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import AllChem
#from rdkit import Chem
#from rdkit.Chem import rdDistGeom
#from rdkit.Chem import rdFMCS
#from rdkit.Chem import Draw
#from rdkit.Chem.Draw import IPythonConsole
#from rdkit.Chem import rdDepictor
#rdDepictor.SetPreferCoordGen(True)
#IPythonConsole.ipython_3d = True
import rdkit
print(rdkit.__version__)
# 读入分子SMILES字符串
mol = Chem.MolFromSmiles('C([H])(C(C([H])([H])[H])(C([H])([H])[H])[C@@](C(=O)N1[C@@](C(=O)N([C@@](C([H])([H])[H])(c2:c([H]):c([H]):c(c3c(C([H])([H])[H])nc([H])s3):c([H]):c:2[H])[H])[H])([H])C([H])([H])[C@](O[H])([H])C1([H])[H])(N(C(=O)C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])C([H])([H])N4C([H])([H])C([H])([H])N(S(=O)(=O)c(:c([H]):c([H]):c(:c5[H])N([H])C(N([H])C(c6:c([H]):c([H]):c([H]):n:c:6[H])([H])[H])=O):c:5[H])C([H])([H])C4([H])[H])[H])[H])([H])[H]')

# 生成初始3D构象
AllChem.EmbedMolecule(mol)

# 进行能量最小化优化
AllChem.MMFFOptimizeMolecule(mol)
AllChem.EmbedMolecule(mol, randomSeed=10, useExpTorsionAnglePrefs=False, useBasicKnowledge=False)
Draw.MolToImage(mol, size=(250,250))

# 输出优化后的3D结构
print(Chem.MolToMolBlock(mol))

Chem.MolToMolFile(mol, 'mol.sdf')
