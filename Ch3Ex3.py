score = input("Enter score: ")
try:
    float(score)
except:
    print("Enter a numeric score between 0.0 and 1.0")
    quit()

score = float(score)
if score < 0 or score > 1.0:
    print("Enter a numeric score between 0.0 and 1.0")
elif score >= 0.9:
    print("The grade equivalent is A")
elif score >= 0.8:
    print("The grade equivalent is B")
elif score >= 0.7:
    print("The grade equivalent is C")
elif score >= 0.6:
    print("The grade equivalent is D")
elif score < 0.6:
    print("The grade equivalent is F")
else:
    print("Enter a numeric score between 0.0 and 1.0")