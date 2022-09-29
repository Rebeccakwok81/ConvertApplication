def mToKm(miles):
    km = miles * 1.609344
    print("The speed value in KM is: ", km)

def kmToM(km):
    miles = km * 0.621371
    print("The speed value in Miles is: ", miles)

user_text = ''

#keep asking user input
while user_text != 'q':
    user_text = input("Which value you would like to convert? \nEnter [1]:Miles to KM, [2]:KM to Miles, [q]:quit : ")

    if user_text == "1":
        miles = float(input('Enter miles: '))
        mToKm(miles)
    elif user_text == "2":
        km = float(input('Enter kilometre: '))
        kmToM(km)
    elif user_text =='q':
        print('Thanks for using:)')
    else:
        print('Sorry. Please input valid choice')

print("Goodbye!")
        


       
