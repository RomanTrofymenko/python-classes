from matplotlib import pyplot as plt
import numpy

thrust = 37770000
thrustV = 39600000
startingMass = 2900000
fuelMass = 2077000
mass = startingMass
burnTime = 177
time = 0
startTime = 9
velocity = 0
altitude = 0
timeStep = 0.1
acceleration = 0
altitudeData = []
g = 9.8

fuelConsumption = (fuelMass/burnTime)*timeStep

while time < burnTime:
    if (time > startTime):
        altitude+=velocity * timeStep
        velocity+=acceleration * timeStep
    mass-= fuelConsumption
    acceleration = thrustV/mass - g
    time += timeStep
    altitudeData.append(altitude)

plt.plot(numpy.arange(0, burnTime + timeStep, timeStep), altitudeData)
plt.ylabel('Altitude')
plt.xlabel('Time')
plt.show()