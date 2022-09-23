def mToKm(miles):
    km = miles * 1.609344
    print("The speed value in KM is: ", km)

def kmToM(km):
    miles = km * 0.621371
    print("The speed value in Miles is: ", miles)

user_text = input("Which value you would like to convert? Enter 1:Miles to KM, 2:KM to Miles: ")

if user_text == "1":
    miles = float(input('Enter miles: '))
    mToKm(miles)
else:
    km = float(input('Enter kilometre: '))
    kmToM(km)
