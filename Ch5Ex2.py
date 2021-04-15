x = 1
numbers = [float(0)]
while x > 0:
    num = input ("Enter a number: ",)
    if num == "done":
        break
    else:
        try:
            float(num)
        except:
            print("Invalid Input")
            continue
        num = float(num)
        if x == 1:
            numbers[x-1] = num
        else:
            numbers.append(num)
    x = x + 1

print("The maximum value is: " + str(max(numbers)))
print("The minimum value is: " + str(min(numbers)))