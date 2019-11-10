print("Enter the hight of the pyramid. Keep it between 1 and 8")
Hight = int(input("Hight: "))

if Hight < 1:
    print("Hight is too low")
elif Hight > 8:
    print("Hight is too high")
else:
    for Hight in range(Hight):
        for j in range(Hight+1):
            print("#", end="")
        print()
