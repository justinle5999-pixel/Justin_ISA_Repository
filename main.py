print("Hello, World!")
print("This is my first Information Systems Project!")
name = input("What is your name? ")
print(f"Hello, {name}! Welcome to the project.")
age = input("How old are you? ")
print(f"You are {age} years old.")
next_year_age = int(age) + 1
print(f"Next year, you will be {next_year_age} years old.")
print("Now, let's calculate your Body Mass Index (BMI).")
weight = input("What is your weight in kilograms? ")
print(f"Your weight is {weight} kg.")
height = input("What is your height in meters? ")
print(f"Your height is {height} m.")
print("Calculating your Body Mass Index (BMI)...")
bmi = float(weight) / (float(height) ** 2)
print(f"Your BMI is {bmi:.1f}")
if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
