import matplotlib.pyplot as plt
import numpy as np

#Modifico las coordenadas
#xpoints = np.array([0, -8])
#ypoints = np.array([3, 10])
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.show()
