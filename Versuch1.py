import os

import numpy as np
from matplotlib import pyplot as plt

mean_list = None
std_list = None


# use genfromtxt to read the data from 11 files called V1_10.csv to V1_70.csv
def read_data():
    # get current working directory
    path = os.getenv('DATA_PATH')
    if not path:
        raise ValueError("DATA_PATH environment variable is not set")

    converters = {i: lambda s: float(s.decode().replace(',', '.')) for i in range(2)}

    global mean_list
    global std_list

    mean_list = []  # list to store the mean of the data from each file
    std_list = []  # list to store the standard deviation of the data from each file
    for i in range(10, 71, 3):
        # Replace the German decimal comma with a dot and remove separators
        csv_data = np.genfromtxt(f"{path}\\V1_{i}.csv", delimiter=";", skip_header=1000, skip_footer=1, dtype=float,
                                 converters=converters)

        # Write only voltage in array
        voltage_data = csv_data[:, 1]

        # get the mean of the data
        mean = np.mean(voltage_data, axis=0)
        print(f"{i} {mean}")
        # get the standard deviation of the data
        std = np.std(voltage_data, axis=0, ddof=1)
        # print(f"{i} {std}")
        mean_list.append(mean)
        std_list.append(std)
    # plot the mean data with matplotlib
    # Create a plot
    voltage = np.array(range(10, 71, 3))

    plt.figure(figsize=(10, 6))
    plt.plot(voltage, mean_list, marker='o', linestyle='-', color='b')
    plt.title('Mean Data from CSV Files')
    plt.xlabel('Distance')
    plt.ylabel('Voltage')
    plt.xticks(voltage)  # Set x-ticks to match column indices
    plt.yticks(np.arange(0.3, 1.4, 0.1))  # Set y-ticks
    plt.grid(True)
    plt.show()
    return


# call read_data() in main
if __name__ == "__main__":
    read_data()
