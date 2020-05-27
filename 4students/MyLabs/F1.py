FuelLap = 2.25
Laps = 45
FuelNeeded = Laps * FuelLap
print(FuelNeeded)

Fuel = FuelNeeded * 1.5
print("Full fuel need:",Fuel,"kg")

QLapTime = 80.45
TLapTime = QLapTime - (0.35/10) * 5
print("Theoretical initial lap time:",TLapTime)
LapOneTime = TLapTime + ((Fuel/10) * 0.35)
print("Lap one time:", LapOneTime, "seconds")