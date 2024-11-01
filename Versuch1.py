import os

import numpy as np


# use genfromtxt to read the data from 11 files called V1_10.csv to V1_70.csv
def read_data():
    # get current working directory
    path = os.getenv('DATA_PATH')
    if not path:
        raise ValueError("DATA_PATH environment variable is not set")

    local_data = np.array([])
    for i in range(10, 71, 3):
        local_data = np.append(local_data, np.genfromtxt(f"{path}\\V1_{i}.csv", delimiter=";", skip_header=1000, skip_footer=1, dtype=float))
    return local_data


# call read_data() in main
if __name__ == "__main__":
    data = read_data()
    print(data)
    print(data.shape)
