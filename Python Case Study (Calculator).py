import math

while True:
    print("\n1.Add 2.Sub 3.Mul 4.Div 5.Power 6.Mod 7.Fact 8.Sqrt 9.Exit")
    ch = int(input("Choice: "))

    if ch == 9:
        print("Exit")
        break

    try:
        if ch in [1,2,3,4,5,6]:
            a = float(input("A: "))
            b = float(input("B: "))
            if ch == 1: print(a + b)
            elif ch == 2: print(a - b)
            elif ch == 3: print(a * b)
            elif ch == 4: print("Zero error" if b==0 else a / b)
            elif ch == 5: print(a ** b)
            elif ch == 6: print(a % b)

        elif ch == 7:
            n = int(input("N: "))
            print("Invalid" if n < 0 else math.factorial(n))

        elif ch == 8:
            n = float(input("N: "))
            print("Invalid" if n < 0 else math.sqrt(n))

        else:
            print("Wrong choice")

    except:
        print("Input error")
