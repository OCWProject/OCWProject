# MIT6_0001: PROBLEM SET 1
# Part C: Finding the right amount to save away

################## NOT COMPLETED YET! ################


# User's data input

# Default CONSTANT values

SEMI_ANNUAL_RAISE = 0.07
ANNUAL_RETURN = 0.04
RAISE_MONTHS = 6
PORTION_DOWN_PAYMENT = 0.25
NEED_DOWN_PAYMENT = PORTION_DOWN_PAYMENT * 1000000

# PORTION_SAVED = ????

start_salary = float(input('Enter the starting salary: '))

monthly_salary = start_salary / 12.0

#
INC = 1 + SEMI_ANNUAL_RAISE * 6
print(INC)
#

current_savings = 0.0
need_months = 0

while current_savings < NEED_DOWN_PAYMENT:
    current_savings += current_savings * ANNUAL_RETURN / 12.0 + monthly_salary * PORTION_SAVED
    # print(need_months, ': ', current_savings)
    need_months += 1
    if need_months % 6 == 0:
        monthly_salary *= (1 + SEMI_ANNUAL_RAISE)



print('Number of months: ', need_months)