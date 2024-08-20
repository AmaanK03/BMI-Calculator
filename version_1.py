print("Welcome to the BMI calculator")

height = float(input('what is your height (meters):'))

weight = int(input('what is your weight (kg):'))


calc = weight / height**2
bmi = round(calc,2)


print(f'\nYour bmi is {bmi}')

if bmi < 18.5:
    print("you are underweight")
elif 18.5 <= bmi < 25:
    print("you are at a healthy weight")
elif 25 <= bmi < 30:
    print("you are overweight")
else:
    print("You are obese")



