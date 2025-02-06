#function

def menu():
    print ("1) Sum")
    print ("2) Subtract")
    print ("3) Multiply")
    print ("4) Divide")
    
# call the function
menu()
# read the input of the keyboard
opt = input("Select and option")
# Try to continue with the calculator app
num1 = float(input("Please enter a number"))
num2 = float(input("Please enter another number"))

if opt == "1":
    total = num1 + num2
    print ("the total is" + str(total))
elif opt =="2":
    total = num1 + num2
    print ("the total is" + str(total))
elif opt =="3":
    total = num1 + num2
    print ("the total is" + str(total))
elif opt =="4":
    if num2 == 0:
        print("you cannot divide by 0")
    else:
        total = num1 / num2
        print ("the total is" + str(total))
else: 
    print("thats not a valid option")