# ChimeraX hydrogen bond automation  
## Overview
This group of scripts aim to make it easier to batch analyze hydrogen-bonds between proteins and ligands that have been docked using [GOLD](https://www.ccdc.cam.ac.uk/solutions/csd-discovery/components/gold/).  
This is still a work in progress but the basic functionality is there. Unfortunatley, 3 scripts must be individually invoked, since I don't have a method worked out for opening and running ChimeraX from the command line, it is [possible though](https://www.cgl.ucsf.edu/chimerax/docs/user/startup.html).  
An arbitrary number of pdb files containing protein + ligands docked by GOLD can be placed in the `pdbs/` directory. A corresponding `.cxc` command file is generated by script 1. This `.cxc` file must then be manually dragged into an open session of ChimeraX. A third script is then run to clean up the files and convert ChimeraX's output to csv.  
Scripts were written with Python 3.9.7, and the only external package requiremnet is pandas.  

## Steps to run  

1. From Terminal. Clone this respository, cd into it, add PDB files of interest to the `pdbs/` folder.

2. Run `python 1-Set_up_files.py` to generate srtarting folders and the `.cxc` command file for ChimeraX.

3. Open ChimeraX. From Finder, drag `2-DRAG-TO-ChimeraX_hbondsPlus_measure.cxc` into the ChimeraX window. It should automatically register the hbPlus command, open each structure in the pdbs folder, and measure the H-bonds.

4. From Terminal, run `python 3-Convert_reports.py`. The end result is `.csv` files in directory `hbond_reports_csv/` detailing H-bonds between each protein-ligand in the strucutres provided.  

*Note that only ligand docking files from GOLD will likely work the way this is set up. How the ligand is encoded in the .pdb files might not be consistent with other software. I have not tested this with more than one ligand per protein, but it should just do the calculation for all available ligands in a session.*  

## Future Imporvements  

- Write a master script that executes subroutines and runs ChimeraX from the command line (no GUI, should be faster for big projects).

- Do more with the `.csv` data - specifiers to more usable names, use in downstream ChimeraX analysis (i.e. grab the residue names, highlight them on the structure, take pics etc.).  

- Deploy this with photo taking, protein-protein interaction scripts for full batch processing (long term).  
