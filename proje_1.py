import math
print("""************************
CALCULATOR 

operations:

1.addition

2.substraction 

3.multiplication

4.division

5.square root

6.Factorial

7.ln(x)

8.x^y

9.return to radiant

10.e^x

11.sin(x)

12.cos(x)

13.tan(x)

14.Exit





*************************
""")
while True:

    operation = input("Select the operation you want to do : ")


    if operation == "1":
        a = float(input("First number : "))
        b = float(input("Second number : "))
        print(f"The result is : {a+b}")
        continue
    elif operation == "2":
        a = float(input("Firat number : "))
        b = float(input("Second number : "))
        print(f"The result is : {a-b}")
        continue

    elif operation == "3":
        a = float(input("Firat number : "))
        b = float(input("Second number : "))
        print(f"The result is : {a*b}")
        continue

    elif operation == "4":
        a = float(input("First number : "))
        b = float(input("Second number : "))
        print(f"The result is : {a/b}")
        continue

    elif operation == "5":
        x = float(input("Enter a number : "))
        print(f"The result is : {math.sqrt(x)}")
        continue

    elif operation == "6":
        x = int(input("Enter a number : "))
        print(f"The result is : {math.factorial(x)}")
        continue
    elif operation == "7":
        x = float(input("Enter a number : "))
        print(f"The result is : {math.log(x)}")
        continue
    elif operation == "8":
        x = float(input("Enter a base(x) : "))
        y = float(input("Enter a exponent(y) : "))
        print(f"The result is : {math.pow(x,y)}")
        continue
    elif operation == "9":
        d = float(input("Enter a degree : "))
        print(f"The result is : {math.radians(d)}")
        continue
    elif operation == "10":
        x = float(input("Enter a exponent : "))
        print(f"The result is : {math.exp(x)}")
        continue
    elif operation == "11":
        x = float(input("Enter a degree : "))
        print(f"The result is : {math.sin(x)}")
        continue
    elif operation == "12":
        x = float(input("Enter a degree : "))
        print(f"The result is : {math.cos(x)}")
        continue
    elif operation == "13":
        x = float(input("Enter a degree : "))
        print(f"The result is : {math.tan(x)}")
        continue

    elif operation == "14":
        print("Exit")
        break


    break

    