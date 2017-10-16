import BatterySensor

batterySensor = BatterySensor.BatterySensor()

print("Source is : {0}; Voltage pourcentage: {1:5.2f}".format(batterySensor.HaveSource, batterySensor.VoltageLevel))
