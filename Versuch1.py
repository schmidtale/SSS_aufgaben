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

def regression():
    distance = np.array(range(10, 71, 3))

    log_distance = np.log(distance)
    log_mean = np.log(mean_list)
    # plot the log data with matplotlib

    plt.figure(figsize=(10, 6))
    plt.plot(log_distance, log_mean, marker='o', linestyle='-', color='b')
    plt.title('Mean Data from CSV Files')
    plt.xlabel('Log Distance')
    plt.ylabel('Log Voltage')
    plt.grid(True)
    plt.show()

    numerator = 0
    for i in range(len(log_distance)):
        numerator += (log_distance[i] - np.mean(log_distance)) * (log_mean[i] - np.mean(log_mean))
    denominator = 0
    for i in range(len(log_distance)):
        denominator += (log_distance[i] - np.mean(log_distance)) ** 2
    a = numerator / denominator
    b = np.mean(log_mean) - a * np.mean(log_distance)

    regression = a * distance + b

    # plot the log data with matplotlib
    # plot the mean data with matplotlib
    # Create a plot
    distance = np.array(range(10, 71, 3))

    # Calculate the corresponding y-values for the line y = a * x + b
    # Plot the regression line
    plt.plot(distance, regression, color='r', label=f'Fit Line: y = {a:.2f}x + {b:.2f}')

    # plot the log data with matplotlib

    plt.figure(figsize=(10, 6))
    plt.plot(log_distance, log_mean, marker='o', linestyle='-', color='b')
    plt.title('Mean Data from CSV Files')
    plt.xlabel('Log Distance')
    plt.ylabel('Log Voltage')
    plt.grid(True)
    plt.show()


# call read_data() in main
if __name__ == "__main__":
    read_data()
    regression()
