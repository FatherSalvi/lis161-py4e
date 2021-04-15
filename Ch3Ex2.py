hours = input("Enter Hours: ")
try:
    float(hours)
except:
    print("Error, please enter numeric input.")
    quit()

rate = input("Enter Rate: ")
try:
    float(rate)
except:
    print("Error, please enter numeric input.")
    quit()

hours = float(hours)
rate = float(rate)

if hours > 40:
    pay = 40 * rate + (hours - 40) * rate * 1.5
    print("Pay: " + str(pay))
else:
    pay = hours * rate
    print("Pay: " + str(pay))