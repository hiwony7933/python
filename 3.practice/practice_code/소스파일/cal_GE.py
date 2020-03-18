# cal.py
def cal(num1, num2, arg):
    num1 = int(num1)
    num2 = int(num2)

    if arg == "1":
        return num1 + num2
    elif arg == "2":
        return num1 - num2
    elif arg == "3":
        return num1 * num2
    elif arg == "4":
        return num1 / num2

# actual body
num1 = 0
num2 = 0
arg = ""

cue = (input("Enter 'doit' if you want to start: "))

if cue == "doit":
    num1 = input("Insert the first number: ")
    num2 = input("Insert  the second number: ")
    arg = input("Choose a type of transaction:\n\n1. add (+)\n2. subtract (-)\n3. multiplication (*)\n4. division (/)\n\n")
else:
    print("Gooood Bye ~.")

# function: cal()
outcome = cal(num1, num2, arg)

# Output
print("Your result is {0}.".format(outcome))
