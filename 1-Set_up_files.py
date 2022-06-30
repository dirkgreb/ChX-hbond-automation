import Make_cxc_file as cxc

def main():
    cxc.make_dir("hb_reports")
    cxc.make_dir("hb_reports_csv")
    cxc.write_commands("pdbs")
    return
    
if __name__ == '__main__' :
    main()