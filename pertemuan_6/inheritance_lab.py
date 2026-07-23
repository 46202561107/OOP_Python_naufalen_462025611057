"""
Tugas Pertemuan 6 - Inheritance & Diamond Problem
File: inheritance_lab.py
"""

# ---------------------------------------------------
# Base Class (A)
# ---------------------------------------------------
class Device:
    def __init__(self, name):
        self.name = name
        print(f"[Device] Initializing {self.name}")

    def turn_on(self):
        print(f"[Device] {self.name} is now powered ON.")


# ---------------------------------------------------
# Derived Class 1 (B) - Inherits from Device
# ---------------------------------------------------
class SmartDisplay(Device):
    def __init__(self, name, resolution):
        print(f"[SmartDisplay] Initializing display...")
        super().__init__(name)
        self.resolution = resolution

    def turn_on(self):
        print(f"[SmartDisplay] Displaying visual UI ({self.resolution}).")
        super().turn_on()


# ---------------------------------------------------
# Derived Class 2 (C) - Inherits from Device
# ---------------------------------------------------
class SmartSpeaker(Device):
    def __init__(self, name, volume):
        print(f"[SmartSpeaker] Initializing audio...")
        super().__init__(name)
        self.volume = volume

    def turn_on(self):
        print(f"[SmartSpeaker] Playing startup chime (Volume: {self.volume}).")
        super().turn_on()


# ---------------------------------------------------
# Multiple Inheritance / Diamond Problem (D) - Inherits from B & C
# ---------------------------------------------------
class SmartHub(SmartDisplay, SmartSpeaker):
    def __init__(self, name, resolution, volume):
        print(f"\n--- Initializing SmartHub: {name} ---")
        # super() mengalir sesuai MRO (Method Resolution Order)
        super().__init__(name=name, resolution=resolution)
        self.volume = volume  # Mengisi atribut volume yang belum terisi lewat MRO

    def turn_on(self):
        print(f"\n--- Turning On SmartHub ---")
        super().turn_on()


# ---------------------------------------------------
# Main Execution & Verification
# ---------------------------------------------------
if __name__ == "__main__":
    # Membuat objek SmartHub
    hub = SmartHub(name="Echo Show", resolution="1080p", volume=80)
    
    # Memanggil method turn_on()
    hub.turn_on()

    # Menampilkan Method Resolution Order (MRO)
    print("\n--- Method Resolution Order (MRO) ---")
    for i, cls in enumerate(SmartHub.__mro__, start=1):
        print(f"{i}. {cls.__name__}")