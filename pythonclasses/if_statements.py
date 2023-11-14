height = 1.9
weight = 70
bmi = weight/height**2

print(f"BMI is {bmi}")

if bmi < 18.5:
    print("You're underweight")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You have Normal Weight")
elif bmi >= 25 and bmi <=29.9:
    print("Overweight")
else:
    print("Obese")
my_sentence = "Kenya, Uganda and Ethiopia"

if "kenya" in my_sentence.lower():
    print("That's my lovely country")
else:
    print("I dont like that countries")

