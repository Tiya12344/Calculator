num1 = int(input("please enter a number "))
num2 = int(input("please enter another number "))
print("please select an operation")
print("1. addition")
print("2. subtraction")
print("3. multiplication")
print("4. division")
print ("5. modulus")
print("6. floor division")
print("7. exponent")
choice = int(input())
if choice == 1:
    print(num1+num2)
elif choice == 2:
    print(num1-num2)
if choice == 3:
    print(num1*num2)
elif choice == 4:
    print(num1/num2)
elif choice == 5:
    print(num1%num2)
elif choice == 6:
    print(num1//num2)
elif choice == 7:
    print(num1**num2)
else:
    print("error")



