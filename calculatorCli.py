Print("Mini calculator program")

x = float(input("enter the first number:"))
y = float(input("enter the second number:"))

operation = input("choose the operation: \n 1)-addition\n 2)-substraction \n 3)-multiplication\n")

def addition():

    some = x + y
    print(some)

def substration():
        some = x / y
        print(some)

def multplication():
            some = x * y
            print(some)


if(operation =="1"):
    addition()


if(operation =="2"):
    substration()

if(operation =="3"):
    multplication()

match operation:
    case "1":
        addition()
    case "2":
        substration()
    case "3":
        multplication()