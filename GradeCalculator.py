percentage = float(input("WHAT ARE YOUR GRADES "))

if percentage > 75:
    print("Congratulations, your grade is A!!")
elif 60 <= percentage < 75:
    print("Congratulations, your grade is B")
elif 45 <= percentage < 60:
    print("congratulations, your grade is c")
elif 32 <= percentage < 45:
    print("YOU NEARLY FAILED")
elif percentage < 32:
    print("DO YOUR STUDIES")