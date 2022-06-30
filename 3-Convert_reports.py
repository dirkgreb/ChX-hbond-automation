import Extract_hbond_info as ehi

def main():

    files = ehi.get_txt_paths(".")
    ehi.batch_convert(files)

if __name__ == '__main__' :
    main()