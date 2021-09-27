cityName = ""
petName = ""
bandName = ""

print(f"welcome to the band name generator")

cityName = input("what city were you born in? \n")
petName = input("what is your pets name? \n")

bandName =  cityName + " " + petName
bandName = bandName.title()
print(f"Your band name is {bandName}")