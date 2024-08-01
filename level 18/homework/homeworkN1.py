num1 = int(input("Enter Quantity  of how many you to enter: "))

numbers = []

for i in range(num1):
    num = int(input("Pleace Enter Number " + str(i+1) +": "))

numbers.append(num)
print(numbers)

print(len(numbers))    


