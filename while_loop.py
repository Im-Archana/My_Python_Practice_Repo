#def while_eg(number):
#    print("Starting to loop x")
 #   x=0
  #  while x<5:
   #     print(x)
    #    x=x+1
    #print("Finished looping x")
    
#number=input("Press any number please!!!")
#while_eg(number)

print("While loop example")
selection=input("Hello! Do you want to enter a number? Press y or n")
while selection =="y":
    number=input("Enter a number:")
    print(number)
    if input("Do you want to continue(c) or break(b)?") == "c":
        continue
    else:
        break
print("Thank you")
        
