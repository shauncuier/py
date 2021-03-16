weight = float(input())
height = float(input())

# print(height**2)
# print(weight/height**2)

if weight/height**2 < 18.5:
    print('Underweight')

else:
    if weight/height**2 <= 18.5 or weight/height<25:
        print('Normal')

    else:
        if weight/height**2 <= 25 or weight/height <30:
            print('Overweight')
        else:
            print ('Obesity')