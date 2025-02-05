print ("hello world")

#variables
name = "Vonda"
last_name = "Dunigan"
age = 57
found = False
print (name)

#if statement
if age < 100:
    print ("no worry you are not that old")
    print ("I'm using the indentation")
    print ("I'm in on the if statement")
elif age == 100: #else if
    print ("wow you are a century")
else:
    print ("seems that you are really old")

    # functions
    def sayHello():
        print ("hello world")

    # call functions
    def sayGoodbye(name):
        print("bye" + str(name))

    # call functions
    sayHello()
    sayGoodbye(2)

    # arrays are called lists

    color = ("red", "green", "blue", "yellow")
    #add an element
    color.append("pink")
    print (color)
    print (color[0])
    color.remove("yellow")
    print (color)

    # for loop
    for col in color:
        print(col)

    # for(let i=0; color.length>0;i++)
    # let temp = color[i]
    # print temp

    # dictionaries
    me = {
        "name": "Vonda",
        "last_name": "Dunigan",
        "age":57
    }
    print(me["last_name"])
    me["last_Name"] = "Doe"
    print(me)
    me["color"] = "blue"
    print(me)

ages = [32, 74, 20, 69, 52, 26, 31, 77, 43, 73, 51, 57, 19, 79, 40, 34, 27, 23, 21, 44, 53, 55, 24, 36, 41, 47, 78, 46, 68, 75, 49, 83, 61, 60, 29, 56, 67, 17, 70, 81, 87, 38]
#print all the numbers
# count how many users are equal or older than 21
def example1():
    total = 0
    for age in ages:
        total = total +age
    print(total)

def example2():
    counter = 0
    for age in ages:
        if age>= 21:
            counter +=1
    print(counter)
# call the functions

# how many users are between 30 and 40 years old 
def example3():
    counter = 0
    for age in ages:
        if age>=30 and age <=40:
            counter += 1
    print("There are "+ str(counter)+" users between 30 and 40")
         
example1()
example2()
example3()
