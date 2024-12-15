# Chain A
# mk_prepare_receptor.py --pdbqt mgl_2b4y.pdbqt -o chainA_receptor  -
# siramin 

# mode |   affinity | dist from | best mode
#      | (kcal/mol) | rmsd l.b. | rmsd u.b.
# -----+------------+----------+----------
#    1        -10.9          0          0
#    2        -10.8      2.644      5.075
#    3       -10.76      2.987      8.519
#    4       -10.74      2.671      6.094
#    5       -10.57      1.909       5.68
#    6        -10.5       2.65      5.677
#    7       -10.46      2.063      5.522
#    8       -10.45      2.278      6.206
#    9       -10.41       1.99      4.799

# Chain B
# mk_prepare_receptor.py --pdbqt mgl_2b4y.pdbqt -o chainB_receptor  --box_center 39.4391 -4.00074 37.0545 --box_size 28.2222 29.9131 43.0876



# Chain C
# mk_prepare_receptor.py --pdbqt mgl_2b4y.pdbqt -o chainC_receptor  --box_center 52.1049 37.5142 -23.7416 --box_size 24.032 26.0408 34.9869 

# Chain D
# mk_prepare_receptor.py --pdbqt mgl_2b4y.pdbqt -o chainD_receptor  --box_center 27.1013 37.0673 51.9274  --box_size 24.032 26.0408 42.631 

### Prepare Ligands

#  mk_prepare_ligand.py -i molecule_14_2.sdf -o molecule_14.pdbqt


# Tutorial Followed: https://autodock-vina.readthedocs.io/en/latest/docking_basic.html

