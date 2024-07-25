import subprocess
from datetime import datetime
import os
import subprocess
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep
import pandas as pd
import random
from tqdm import tqdm
import glob
from mpl_toolkits.mplot3d import Axes3D
from functions_for_run import mkdir_1

# print(filename)
def run_save_main41_txt(m, seed, Br, tau):
    now = datetime.now()
    mass = str(m)
    Br_str = str(Br)
    today = str(datetime.now().date())
    out_dir = '/Users/shiyuzhe/Documents/University/LLP/Second_Term/pythia8/BtoKa/auto_data/' + today +'/'
    # The folder Directory where you want to place your outputs, only the first part needs be changed
    random_seed = str(seed)
    mass_line = 'the mass = '
    seed_line = 'the seed is: '
    Br_line= 'the Br = '
    # Change the working path
    os.chdir('/Users/shiyuzhe/Documents/University/LLP/Second_Term/pythia8/examples')
    # The folder Directory where your main41.cc/BtoKa.cc is at
    command0 = f'make main41 -j4'
    process0 = subprocess.Popen(command0, stdout = subprocess.PIPE, shell = True)
    print('command 0 complated')
    # 运行你的命令
    command1 = f'./main41 {mass} run{now.strftime("%Y-%m-%d_%H:%M:%S")} {random_seed}'
    process1 = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
    print('command 1 complated')
    filename = 'm_'+f'{mass}_' + 'seed_'+f'{random_seed}_' + 'br_'+f'{Br}_' + 'tau_'+f'{tau}' + '.txt'
    # Get the output (and error if any)
    output, error = process1.communicate()
    mkdir_1(out_dir)
    # Save the OUTPUT to .txt
    out_path = out_dir+filename
    with open(out_path, 'w') as file:
        file.write(seed_line + random_seed + '\n')
        file.write(mass_line + mass + '\n')
        file.write(Br_line + str(Br))
        file.write(output.decode('utf-8'))

    
        

    # Save errors if any
    if error:
        with open('error_'+filename, 'w') as file:
            file.write(error.decode('utf-8'))
    
    return out_path, mass, seed

def runtxt_to_csv(txt_file):
    # Setting file names and paths
    file_path, file_name = os.path.split(txt_file)
    base_name = os.path.splitext(file_name)[0]
    csv_path = mkdir_1(file_path + 'csv/')
    file_name_all = csv_path + base_name + '_all_events.csv'
    file_name_trimed = csv_path + base_name + '_trimed_events.csv'
    # print(file_name_trimed)

    #new .csv file name 
    csv_file_all = os.path.join(file_name_all)
    csv_file_trimed = os.path.join(file_name_trimed)
    base_csv_name = os.path.splitext(csv_file_trimed)[0] # This Contains the data we care
    all_lines = []
    n = 0

    #Processing & Saving data
    with open(txt_file, 'r') as in_file:
        lines = in_file.readlines()
        start = end = 0

        # Skip the first group of data
        try:
            start = lines.index(" --------  PYTHIA Event Listing  (complete event)  ---------------------------------------------------------------------------------\n", end)
            end = lines.index(" --------  End PYTHIA Event Listing  -----------------------------------------------------------------------------------------------\n", start)
        except ValueError:
            pass

        while True:
            try:
                start = lines.index(" --------  PYTHIA Event Listing  (complete event)  ---------------------------------------------------------------------------------\n", end)
                end = lines.index(" --------  End PYTHIA Event Listing  -----------------------------------------------------------------------------------------------\n", start)
                data_lines = lines[start+4:end-2]

                # Process the data_lines here...
                for i in range(0, len(data_lines), 2):
                    line1 = data_lines[i]
                    if i+1 < len(data_lines):
                        line2 = data_lines[i+1]
                    else:
                        line2 = ''
                    if not line1.strip() and not line2.strip():
                        continue
                    if 'mothers:' in line1 or 'daughters:' in line1:
                        # Remove the part after 'mothers:' or 'daughters:'
                        line1 = line1.split('mothers:')[0].split('daughters:')[0]
                        line1 = line1.rstrip()

                    all_lines.append(line1 + ' ' + line2)

                n += 1

                csv_file_trimed_n = base_csv_name + str(n) + '.csv'

                with open(csv_file_trimed_n, 'w', newline='') as out_file2:
                    writer = csv.writer(out_file2)
                    writer.writerow(('no', 'id', 'name', 'status1', 'mother1','mother2', 'daughter1','daughter2', 'colour1','colour2', 'p_x', 'p_y', 'p_z', 'e', 'm', 'scale', 'pol', 'xProd', 'yProd', 'zProd', 'tProd', 'tau'))  

                    for line in all_lines:
                        stripped_line = line.strip().split()
                        if not stripped_line:
                            continue
                        writer.writerow(stripped_line)

                all_lines = []  # Reset for next file

            except ValueError: 
                # No more sections found
                break

    return file_name_all, file_name_trimed


def run_para_save(filename_trimed, mass, seed, Br):
    path, filename = os.path.split(filename_trimed)
    # print(filename)
    basename = os.path.splitext(filename)[0]
    cc_save_name = path + '/' + basename + '_run_para' + '.txt'
    # print(cc_save_name)
    lines_to_read_cc = [95, 96, 97, 98, 108, 113, 118, 119]
    with open('/Users/shiyuzhe/Documents/University/LLP/Second_Term/pythia8/examples/main41.cc', 'r') as cc_file:
    #The path of main41.cc or BtoKa.cc
        lines = cc_file.readlines()
        selected_lines = [lines[i-1] for i in lines_to_read_cc if i <= len(lines)]
    
    with open(cc_save_name, 'w') as file:
        file.writelines(selected_lines)
        file.write('\n')
        file.write('mass = ' + str(mass))
        file.write('\n')
        file.write('seed = ' + str(seed))
        file.write('\n')
        file.write('Br = ' + str(Br))
    
    return cc_save_name

    
    
    
