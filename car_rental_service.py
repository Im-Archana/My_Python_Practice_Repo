

def car_type(car):           #Function Receives car type as parameter and returns car_id
    if(car == "Sedan"):
        car_id=1  
    elif (car == "Prime SUV"):
        car_id=2
    elif(car =="SUV"):
        car_id=3
    else:
        car_id=4
    return car_id


def ride_fare(car_id,kms):   #Function receives car_id and kms and returns total fare
    if(car_id==1):
        fare=(30*kms)
    elif(car_id==2):
        fare=(40*kms)
    elif(car_id==3):
        fare=(50*kms)
    else:
        fare=(10*kms)
    return fare

print("                   ############  Greetings!!!   ############ ")
print("                 Welcome to Jiffy Car Rentals                  ")

car= input(" Select your ride for today : Sedan/Prime SUV/SUV/Mini:")
car_id=car_type(car)
#kms = input("Could you guess the approximate kilometers for your ride? ")
total=ride_fare(car_id,10)


#car_id=car_type(car)  #Function call to get car_id

#total_fare=ride_fare(car_id,kms)


print("Your total fare for the ride:" + str(total))
print("Thanks for your ride!!!")
    
