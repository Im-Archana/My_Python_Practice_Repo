
def ride_fare(car_type,kms):
    if(car_type == 1):
        fare=int(50*kms)
        return int(fare)
    elif (car_type == 2):
        fare=int(75*kms)
        return int(fare)
    else:
        fare = int(25*kms)
        return int(fare)
print("                   ############  Greetings!!!   ############ ")
print("                 Welcome to Jiffy Car Rentals                  ")
#car_type = input(" Select your ride for today : Sedan(1)/Prime SUV(2)/Mini(3):")
#kms = input("Could you guess the approximate kilometers for your ride? ")
total_fare= ride_fare("Sedan",25)
print("Your total fare for the ride:" + str(total_fare))
print("Thanks for your ride!!!")
    
