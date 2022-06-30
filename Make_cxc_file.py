def make_dir(dir_name):
    from os import mkdir
    try:
        mkdir(f'./{dir_name}')
        return 
    except:
        pass
        return 

def get_pdbs(path):
    fname = []
    from os import walk
    for root, d_names, f_names in walk(path):
        for f in f_names:
            # print(f)
            from os import path
            fname.append(path.join(root, f))
    pdb_paths = []
    for name in fname:
        if name.endswith(".pdb"):
            split_up = name.split('/')
            protein = split_up[1]
            parent_path = '/'.join(split_up[:2])
            pdb_path = name
            pdb_paths.append(pdb_path)
    return pdb_paths

def write_commands(starting_path):
    pdb_paths = get_pdbs(starting_path)
    command = 'hbPlus'
    from os import getcwd
    working_directory = getcwd()
    with open('2-DRAG-TO-ChimeraX_hbondsPlus_measure.cxc', "w+") as fileObj:
        fileObj.write(f"cd {working_directory}\n")
        fileObj.write("open ChimeraX_cmd_hbondsPlus.py\n")
        for i in range(len(pdb_paths)):
            fileObj.write("open %s ; wait 1 \n" % (pdb_paths[i]))
            fileObj.write('%s #1\n' % command)
            fileObj.write('wait 1\n')
            fileObj.write('close session\n')
    return


if __name__ == '__main__' :
    make_dir("pdbs")
    make_dir("hb_reports")
    make_dir("hb_reports_csv")
    write_commands("pdbs")
    

