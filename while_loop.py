
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
        
