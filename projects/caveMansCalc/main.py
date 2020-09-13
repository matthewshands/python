import re

print ("Cave Man's Calculator")
print('Type ":q"or "quit" to exit\n')

previous = 0    #holds result of previous equation
run = True        #sets the state of program and allows us to exit


def performMath ():
    global run
    global previous
    
    if previous == 0:                                         #if previous is zero input the sting "Enter Equation:"
        equation = input("Enter Equation:")
    
    else:
        equation = input(str(previous))            #will replace "Enter Equation" with the previous answer as long as previous is anything but zero
        print("test")
    
    if equation == ":q":                                     #if you type ":q" or "quit" you will exit the program by changing run to False

              print("Goodbye, human...")
              run = False

    elif equation == "quit":                               #if you type "quit" or "quit" you will exit the program by changing run to False

              print("Goodbye, human...")
              run = False

    else:
        equation = re.sub("[a-zA-Z,()'\"`]", "", equation)      #Removes unnecessary characters
        
        if previous == 0:
            previous = eval(equation)
            
        else:
            previous = eval(str(previous) + equation)


while run:
    performMath()