import os

import numpy as np


# use genfromtxt to read the data from 11 files called V1_10.csv to V1_70.csv
def read_data():
    # get current working directory
    path = os.getenv('DATA_PATH')
    if not path:
        raise ValueError("DATA_PATH environment variable is not set")

    converters = {i: lambda s: float(s.decode().replace(',', '.')) for i in range(2)}

    data_list = []  # list to store the data from each file
    for i in range(10, 71, 3):
        # Replace the German decimal comma with a dot and remove separators
        csv_data = np.genfromtxt(f"{path}\\V1_{i}.csv", delimiter=";", skip_header=1000, skip_footer=1, dtype=float, converters=converters)
        data_list.append(csv_data)

    local_data = np.concatenate(data_list)
    return local_data


# call read_data() in main
if __name__ == "__main__":
    data = read_data()
    print(data)
    # print first 5 rows and columns
    print(data.shape)
