# MIT6_0001: PROBLEM SET 1


# User's data input
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# Default CONSTANT values
PORTION_DOWN_PAYMENT = 0.25
ANNUAL_RETURN = 0.04

# Sample test case data
# annual_salary = 120000
# portion_saved = .10
# total_cost = 1000000

monthly_salary = annual_salary / 12.0
need_down_payment = PORTION_DOWN_PAYMENT * total_cost
current_savings = 0.0
need_months = 0

while current_savings < need_down_payment:
    current_savings += current_savings * ANNUAL_RETURN / 12.0 + monthly_salary * portion_saved
    # print(need_months, ': ', current_savings)
    need_months += 1

print('Number of months: ', need_months)