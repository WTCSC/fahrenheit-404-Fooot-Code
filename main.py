from time import sleep

goneThroughLoopOnce = False
CELSIUS_TO_KELVIN = 273.15

while True:
    # Asking what unit they want to convert
    unitOptions = ["F", "C", "K", "Q"]
    if not goneThroughLoopOnce:
        currentUnit = input("What is the unit of the temperature you want to convert (F, C, or K): ").upper()
        while not currentUnit in unitOptions:
            currentUnit = input("Please enter either F, C or K (is not case sensitive): ").upper()
    else:
        # Gone through for more than one time, allows person to quit
        currentUnit = input("What is the unit of the temperature you want to convert (F, C, K, or Q if you want to stop): ").upper()
        while not currentUnit in unitOptions:
            currentUnit = input("Please enter either F, C, K, or Q (is not case sensitive): ").upper()

    if currentUnit == "Q":
        break
    
    # Current temperature and unit to convert to
    availibleConversionUnits = [unit for unit in unitOptions if unit != currentUnit]
    try:
        currentTemperature = float(input("What is the temperature number you would like to convert: "))
    except ValueError:
        currentTemperature = float(input("What is the temperature number you would like to convert (make sure its a number): "))

    conversionUnit = input(f"What unit would you like to convert {currentTemperature} to ({availibleConversionUnits[0]} or {availibleConversionUnits[1]}): ").upper()
    while not conversionUnit.upper() in availibleConversionUnits:
        conversionUnit = input(f"Please enter either {availibleConversionUnits[0]} or {availibleConversionUnits[1]} (is not case sensitive): ").upper()

    # Does the conversions based on entered values
    if currentUnit == "C" and conversionUnit == "F":
        convertedTemperature = (currentTemperature * 1.8) + 32
    elif currentUnit == "C" and conversionUnit == "K":
        convertedTemperature = currentTemperature + CELSIUS_TO_KELVIN
    elif currentUnit == "F" and conversionUnit == "C":
        convertedTemperature = (currentTemperature - 32) * 5 / 9
    elif currentUnit == "F" and conversionUnit == "K":
        convertedTemperature = ((currentTemperature - 32) * 5 / 9) + CELSIUS_TO_KELVIN
    elif currentUnit == "K" and conversionUnit == "C":
        convertedTemperature = currentTemperature - CELSIUS_TO_KELVIN
    else: 
        convertedTemperature = ((currentTemperature - CELSIUS_TO_KELVIN) * 1.8) + 32

    # Prints the converted temperature, rounded to 2 decimals. 
    if conversionUnit == "F" or conversionUnit == "C":
        print(f"The value is: {convertedTemperature:.2f}°{conversionUnit}")
    else:
        print(f"The value is: {convertedTemperature:.2f}K") # Kelvin doesn't have a degree symbol

    sleep(2)
    # The user will be prompted to quit after 1 conversion if they would like to
    if not goneThroughLoopOnce:
        goneThroughLoopOnce = True 
    