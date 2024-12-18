# This is a sample Python script.

import redlab as rl
import csv

#print("------- einzelne Werte -------------------------")
#print("16 Bit Value: " + str(rl.cbAIn(0, 0, 1)))
#print("Voltage Value: " + str(rl.cbVIn(0, 0, 1)))
print("------- Messreihe -------------------------")
#print("Messreihe: " + str(rl.cbAInScan(0, 0, 0, 300, 6000, 1)))
messreihe = rl.cbVInScan(0, 0, 0, 1000, 6000, 1)
print("Messreihe: " + str(messreihe))

# Save to CSV
filename = "teil5_1500"
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)

    for value in messreihe:
        writer.writerow([value])
#print("------- Ausgabe -------------------------")
#text = input("Spannung eingeben\n")
#print("Voltage Value: " + str(rl.cbVOut(0, 0, 101, float(text))))
