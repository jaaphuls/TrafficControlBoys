from code.visualisation.visualise import gameboard as gb 
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("input", help = "input file (csv)")

# Read arguments from command line
args = parser.parse_args()

# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(args.input)
    
# Run main with provide arguments
board_visualized = gb(dataframe, 6)
