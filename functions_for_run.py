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

def generate_randomseed(number_of_seed, range_floor = 1, range_upper = 1000000):
    random_numbers = []
    
    for _ in range(number_of_seed):
        random_number = random.randint(range_floor, range_upper)
        random_numbers.append(random_number)
    
    return random_numbers

def mkdir_1(path):
    try:
        os.makedirs(path)
        # print(f"Folder '{path}' created successfully") ## used for tests 
    except FileExistsError:
        exist_warning = f"Folder '{path}' already exists"
        # print(exist_warning) ## used for tests 
    return path

def import_headers():
    os.chdir('/Users/shiyuzhe/Documents/University/LLP/Second_Term/pythia8/examples')# The path of your BtoKa.cc/main41.cc
    command0 = f'export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/shiyuzhe/Documents/University/LLP/Second_Term/HepMC2/build/lib'
    # The path of your HepMC's libs
    process0 = subprocess.Popen(command0, stdout = subprocess.PIPE, shell = True)
    output0, error0 = process0.communicate()
    command1 = f'export DYLD_LIBRARY_PATH=$DYLD_LIBRARY_PATH:/Users/shiyuzhe/Documents/University/LLP/Second_Term/pythia8/include'
    # The path of your Pythia's 'include'
    process1 = subprocess.Popen(command0, stdout = subprocess.PIPE, shell = True)
    output1, error1 = process1.communicate()
    print(output0, error0, output1, error1)
    return 0