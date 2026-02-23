# /// script
# requires-python = ">=3.9"
# dependencies = [
# "adafruit-blinka",
# "adafruit-circuitpython-ahtx0",
# "adafruit-circuitpython-vcnl4200",
# "rpi.gpio",
# ]
# ///
"""
Lecture combinee AHT20 et VCNL4200 sur le meme bus I2C
Cours 243-413-SH, Semaine 3
"""

import board
import adafruit_ahtx0
import adafruit_vcnl4200

# Initialiser le bus I2C (partage par les deux capteurs)
i2c = board.I2C()
# Creer les objets capteurs
aht20 = adafruit_ahtx0.AHTx0(i2c) # 0x38
vcnl = adafruit_vcnl4200.Adafruit_VCNL4200(i2c) # 0x51
print("=== Station IoT Multi-Capteurs ===")
print("Capteurs sur le bus I2C :")
print(" - AHT20 (0x38) : temperature, humidite")
print(" - VCNL4200 (0x51) : proximite, lumiere")
print()
# Lire AHT20 (donnees environnementales)
print("--- Donnees environnementales (AHT20) ---")
print(f"Temperature : {aht20.temperature:.1f} C")
print(f"Humidite : {aht20.relative_humidity:.1f} %")
print()
# Lire VCNL4200 (donnees spatiales)
print("--- Donnees spatiales (VCNL4200) ---")
print(f"Proximite : {vcnl.proximity}")
print(f"Lumiere : {vcnl.lux:.1f} lux")
print()
# Interpretation combinee
if vcnl.proximity > 100:
    print("Objet detecte a proximite!")
if vcnl.lux < 50:
    print("Faible eclairage ambiant")
    
print("\n=== Termine ===")
