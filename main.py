while True:
    unitOptions = ["F", "C", "K"]
    currentUnit = input("What is the unit of the temperature you want to convert (F, C, or K): ")
    while not currentUnit.upper() in unitOptions:
        currentUnit = input("Please enter either F, C or K (is not case sensitive): ")

    availibleConversionUnits = [unit for unit in unitOptions if unit != currentUnit]
    currentTemperature = float(input("What is the temperature number you would like to convert: "))
    conversionUnit = input(f"What unit would you like to convert {currentTemperature} to ({availibleConversionUnits[0]} or {availibleConversionUnits[1]}): ")
    while not conversionUnit.upper() in availibleConversionUnits:
        conversionUnit = input(f"Please enter either {availibleConversionUnits[0]} or {availibleConversionUnits[1]} (is not case sensitive): ")

    if currentUnit == "C" and conversionUnit == "F":
        convertedTemperature = (currentTemperature * 1.8) + 32
    
    if conversionUnit == "F" or conversionUnit == "C":
        print(f"The value is: {convertedTemperature:.2f}°{conversionUnit}")
    else:
        print(f"The value is: {convertedTemperature:.2f}K") # Kelvin doesn't have a degree symbol

    