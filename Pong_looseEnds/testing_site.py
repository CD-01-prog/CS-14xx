userAnswer = 5.5
while True:
    try:
        str(userAnswer)
    except(ValueError):
        userAnswer = input("please be reasonable")
    else:
        break
