import numpy as np

# use genfromtxt to read the data from 11 files called V1_10.csv to V1_70.csv
def read_data():
    data = []
    for i in range(10, 71):
        data.append(np.genfromtxt(f"V1_{i}.csv", delimiter=",", skip_header=1000))
    return data