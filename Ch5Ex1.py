x = 1
number = float(0)
while x > 0:
    num = input("Enter a number: ",)
    if num == "done":
        break 
    else:
        try:
            float(num)
        except:
            print("Invalid Input")
            continue
        num = float(num)
        number = number + num
        x = x + 1

if x == 1:
    print("The total is 0 etc")
else:
    count = x - 1
    print("The total is: " + str(number))
    print("The count is: " + str(count))
    print("The average is: " + str(number/count))