import sys
#def solve(meal_cost, tip_percent, tax_percent):
    if __name__ == '__main__':
        meal_cost = float(input().strip())
        tip_percentage = int(input().strip())
        tax_percentage = int(input().strip())

        tip_amount = meal_cost * tip_percentage / 100
        tax_amount = meal_cost * tax_percentage / 100
        tolal_cost = round(meal_cost + tip_amount + tax_amount)

        print("The Total meal cost is "+ str(tolal_cost)+" dollars")