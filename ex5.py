name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")



# convert inches to cm
def convertInchToCm(num):
    num*=2.54
    return num

# convert pounds to kilos
def convertPoundsToKilos(num):
    num*=0.453592
    return num


convertedNum = convertInchToCm(7)
# print out the value in cm
print(convertedNum)

convertedNum2 = convertPoundsToKilos(2000)
# print out the value in kilos
print(convertedNum2)

