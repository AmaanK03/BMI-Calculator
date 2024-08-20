print("Welcome to the BMI calculator")

height = float(input('what is your height (meters):'))

weight = int(input('what is your weight (kg):'))


calc = weight / height**2
bmi = round(calc,2)


print(f'\nYour bmi is {bmi}')


if bmi < 18.5:
    print("you are underweight")
elif bmi == 18.5 or bmi < 25:  # Error: The condition "bmi == 18.5" is redundant because "bmi < 25" already includes it.
    print("you are at a healthy weight")

elif bmi == 25 or bmi < 30:  # Error: The condition "bmi == 25" is redundant because "bmi < 30" already includes it.
    print("you are overweight !")

elif bmi > 30:  # Error: This condition should be "bmi >= 30" to properly include a BMI of 30 in the obese category.
    print("you are obese !")

