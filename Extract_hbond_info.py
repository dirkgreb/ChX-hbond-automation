import pandas as pd
import re
import os

# Goal is to simply convert the hbond output text files into usable data

def get_txt_paths(path):
    txt_paths = []
    for f in os.listdir(path):
        if f.endswith("_Report.txt"):
            os.replace(f"{f}", f"hb_reports/{f}")
            new_path =  f"hb_reports/{f}"
            txt_paths.append(new_path)          
    return txt_paths


def covert_hbond_report(text_file):
    # This should be broken up into many different functions. 
    # The Hbond-report text files from ChimeraX for 1 structure 
    # are always 8 lines of header. The data for each interacting pair,
    # is fixed width, has to be read in and converted to CSV
    
    regexp = r"(\/.\s...\s\w+\s\w+\s+)"
    col_names = ["donor","acceptor","hydrogen","D..A dist","D-H..A dist"]
    df = pd.DataFrame(columns=col_names)
    
    lines = []
    with open(text_file) as f:
        for line in f:
            line = line.rstrip()
            lines.append(line)
    # Name of the model is stored on line 4 of the file, might as well use it
    model_name = lines[3]
    model_name = model_name.lstrip("\t1 ")
    
    for i in range(len(lines)):
        # Ignore the first 8 lines since they are useless
        if i > 7 :
            # Collect the values for 'D..A dist' and 'D-H..A dist'
            new_row = lines[i]
            num = new_row[-12:-1] # Lose the last digit from 'D-H..A dist' by mistake, value is too percise anyway
            num = num.split()
            # regex to seperate out each residue specifier
            x = re.findall(regexp,new_row)
            # remove whitespace from residue specifiers
            for i in range(len(x)):
                xi = x[i]
                x[i] = xi.rstrip() 
            # Some entries don't have a hydrogen column
            if len(x) == 3:
                df = df.append({'donor': x[0],
                 'acceptor': x[1], 
                 'hydrogen' : x[2], 
                 'D..A dist': num[0], 
                 'D-H..A dist': num[1] }, 
                 ignore_index=True)
            elif len(x) == 2:
                df = df.append({'donor': x[0], 
                'acceptor': x[1], 
                'hydrogen' : 'no hydrogen', 
                'D..A dist': num[0]}, 
                ignore_index=True)
    # Ready to be written out to csv
    return (model_name, df)

def batch_convert(files):
    for i in range(len(files)):
        y = covert_hbond_report(files[i])
        df2 = y[1]
        name = y[0]
        df2.to_csv(f"./hb_reports_csv/{name}_Hbond_report.csv", index=False)
    return


if __name__ == '__main__' :
    
    files = get_txt_paths(".")
    batch_convert(files)

