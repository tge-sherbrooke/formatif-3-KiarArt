# /// script
# requires-python = ">=3.9"
# dependencies = [
# "adafruit-blinka",
# "adafruit-circuitpython-ahtx0",
# "rpi.gpio",
# ]
# ///
"""
Lecture basique du capteur AHT20 (I2C)
Cours 243-413-SH, Semaine 3
"""

import board
import adafruit_ahtx0

i2c = board.I2C()

capteur = adafruit_ahtx0.AHTx0(i2c)

print("=== Lecture AHT20 ===")
print(f"Adresse I2C : 0x38")
print()

temperature = capteur.temperature
humidite = capteur.relative_humidity

print(f"Temperature : {temperature:.1f} C")
print(f"Humidite : {humidite:.1f} %")

print("\n=== Termine ===")
