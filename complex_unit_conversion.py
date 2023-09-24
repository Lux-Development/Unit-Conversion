import os

os.system("title joelb.services")

def length_print():
    print("  [1] Inches to Centimeters\n")
    print("  [2] Feet to Meters\n")
    length_type = input("\n\n  [ # ] Please select length converision: ")

    if length_type == "1":
        Inches = float(input("  Enter Inches: "))
        print(f"  {Inches*2.54} Centimeters")

    if length_type == "2":
        Feet = float(input("  Enter Feet: "))
        print(f"  {Feet*0.3048} Meters")

def volume_print():
    print("  [1] Gallons to Liters\n")
    print("  [2] Cubic Inches to Cubic Centimeters\n")
    volume_type = input("\n\n  [ # ] Please select volume converision: ")

    if volume_type == "1":
        Gallons = float(input("  Enter Gallons: "))
        print(f"  {Gallons*3.78541} Liters")

    if volume_type == "2":
        Cubic = float(input("  Enter Cubic Inches: "))
        print(f"  {Cubic*16.3871} Cubic Centimeters")

def mass_print():
    print("  [1] Pounds to Kilograms\n")
    print("  [2] Ounces to Grams\n")
    mass_type = input("\n\n  [ # ] Please select mass converision: ")

    if mass_type == "1":
        Pounds = float(input("  Enter Pounds: "))
        print(f"  {Pounds*0.453592} Kilograms")

    if mass_type == "2":
        Ounces = float(input("  Enter Ounces: "))
        print(f"  {Ounces*28.3495} Grams")

def temperature_print():
    print("  [1] Celsius to Fahrenheit\n")
    print("  [2] Fahrenheit to Celsius\n")
    temperature_type = input("\n\n  [ # ] Please select temperature converision: ")

    if temperature_type == "1":
        Celsius = float(input("  Enter Celsius: "))
        print(f"  {(Celsius * 9/5) + 32} Fahrenheit")

    if temperature_type == "2":
        Fahrenheit = float(input("  Enter Fahrenheit: "))
        print(f"  {(Fahrenheit - 32) * 5/9} Celsius")

def area_print():
    print("  [1] Square Feet to Square Meters\n")
    print("  [2] Square Miles to Square Kilometers\n")
    area_type = input("\n\n  [ # ] Please select area converision: ")

    if area_type == "1":
        Square_Feet = float(input("  Enter Square Feet: "))
        print(f"  {Square_Feet*0.092903} Square Meters")

    if area_type == "2":
        Square_Miles = float(input("  Enter Square Miles: "))
        print(f"  {Square_Miles*2.58999} Square Kilometers")

def time_print():
    print("  [1] Hours to Minutes\n")
    print("  [2] Days to Hours\n")
    time_type = input("\n\n  [ # ] Please select time converision: ")

    if time_type == "1":
        Hours = float(input("  Enter Hours: "))
        print(f"  {Hours*60} Minutes")

    if time_type == "2":
        Days = float(input("  Enter Days: "))
        print(f"  {Days*24} Square Hours")

def speed_print():
    print("  [1] MPH to KPH\n")
    speed_type = input("\n\n  [ # ] Please select speed converision: ")

    if speed_type == "1":
        MPH = float(input("  Enter MPH: "))
        print(f"  {MPH*1.60934} KPH")

def pressure_print():
    print("  [1] Pounds per Square Inch (psi) to Kilopascals (kPa)\n")
    pressure_type = input("\n\n  [ # ] Please select pressure converision: ")

    if pressure_type == "1":
        psi = float(input("  Enter Pounds per Square Inch: "))
        print(f"  {psi*6.89476} Kilopascals")

def energy_print():
    print("  [1] Joules to Calories\n")
    energy_type = input("\n\n  [ # ] Please select energy converision: ")

    if energy_type == "1":
        Joules = float(input("  Enter Joules: "))
        print(f"  {Joules/4.184} Calories")

def power_print():
    print("  [1] Watts to Horsepower\n")
    power_type = input("\n\n  [ # ] Please select power converision: ")

    if power_type == "1":
        Watts = float(input("  Enter Watts: "))
        print(f"  {Watts/745.7} Horsepower")

print("\n  [1] Length  [2] Volume  [3] Mass  [4] Temperature  [5] Area")
print("\n  [6] Time  [7] Speed  [8] Pressure  [9] Energy  [10] Power")
selection_type = input("\n\n  [ # ] Please select conversion type: ")
os.system("cls")
print("")

if selection_type == "1":
    length_print()

elif selection_type == "2":
    volume_print()

elif selection_type == "3":
    mass_print()

elif selection_type == "4":
    temperature_print()

elif selection_type == "5":
    area_print()

elif selection_type == "6":
    time_print()

elif selection_type == "7":
    speed_print()

elif selection_type == "8":
    pressure_print()

elif selection_type == "9":
    energy_print()

elif selection_type == "10":
    power_print()

else:
    print("  Incorrect selection, please retry.")
    os.system("pause")

os.system("pause >nul")