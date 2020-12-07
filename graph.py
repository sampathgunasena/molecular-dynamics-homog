import numpy as np
import matplotlib.pyplot as plt

##x = [1,2,3]
##y = [1,2,3]

with open("rdf.out", "r") as f:

    x = []
    y = []

    for line in f:

        if line.startswith("#") or len(line.split(" ")) != 4:
            continue
        
        row = line.split(" ")
        x.append(float(row[0]))
        y.append(float(row[2]))

plt.plot(x,y)
plt.show()

##print(x,y)
