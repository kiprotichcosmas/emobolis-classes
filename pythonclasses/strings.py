name = "Mohaa"
city = "Eldoret"
age = 27
weight = 69.80

print(name + city)
print(name * 5)

print(f"I am  {name}, I am {age} years old and i live in {city} and i weigh (weight) Kgs")

sentence = "I am learning python functionalities to do with strings, and its so lovely that it does great things with short lines of codes"
upper_case = sentence.upper()
print(upper_case)
print(sentence.lower())

print(len(sentence))
if len(sentence) > 60:
    print("The message is too long")
else:
    print("you are within the limit")
