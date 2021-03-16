weight = float(input())
height = float(input())
bmi = weight/height**2
# print(height**2)
# print(weight/height**2)

if bmi < 18.5:
    print('Underweight')

else:
    if bmi <= 18.5 or bmi<25:
        print('Normal')

    else:
        if bmi <= 25 or bmi <30:
            print('Overweight')
        else:
            print ('Obesity')