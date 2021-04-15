def computegrade(score):
    try:
        float(score)
    except:
        print("Enter a numeric score between 0.0 and 1.0")
        return
    
    score = float(score)
    if score < 0 or score > 1.0:
        print("Enter a numeric score between 0.0 and 1.0")
        return
    elif score >= 0.9:
        return "A"
    elif score >= 0.8:
        return "B"
    elif score >= 0.7:
        return "C"
    elif score >= 0.6:
        return "D"
    elif score < 0.6:
        return "F"
    else:
        print("Enter a numeric score between 0.0 and 1.0")
        return
