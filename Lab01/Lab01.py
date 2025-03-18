print("What is the temp")
temperature = int(input())
print("what is the weather condition")
weatherCondition = str(input())
print("What is the budget")
budget = float(input())

if(temperature > 75) and weatherCondition == "sunny":
    if budget > 20:
        print("go to the beach")
    else:
        print("Have a picnic in the park")
if weatherCondition == "rainy":
    if budget > 15:
        print("Visit a musuem.")
    else:
        print("Stay in and watch a movie at home.")
if weatherCondition == "cloudy" or (temperature < 60):
    print("Go to a coffee shop and enjoy a warm drink.")