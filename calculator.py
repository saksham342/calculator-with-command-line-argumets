import sys

guideline = '''\n
<<< Please run the code with three extra arguments >>>
[+] Format: python3 calculator.py 12 4 a
[+] Addition: a, Subtraction: s, Multiplication: m, Division: d
'''

def calculate(num1, num2, operation):
    if operation == "a":
        return num1+num2
    elif operation == "s":
        return num1-num2
    elif operation == "d":
        return num1/num2
    elif operation == "m":
        return num1*num2
    else:
        return f"\nPlease provide appropriate operation\n{guideline}"

if len(sys.argv)==2:
    if sys.argv[1] in ("-h", "--help"):
        print(f"\n[+] Help Section: ")
        print(guideline)
    else:
        print(f"\n[+] Parsing Error\n{guideline}")
elif len(sys.argv) != 4:
    print("\n[+] Parsing Error")
    print(guideline)
else:
    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
        operation = str(sys.argv[3].lower())
        try:
            result = float(calculate(num1,num2,operation))
            print(f"\nThe result is: {result}")
        except ValueError:
            print(calculate(num1,num2,operation))
    except ValueError:
        print(f"\nPlease input arguments in appropriate format \n {guideline} ")
    
    
        
        

        

