import math
loan_amount = 100000
monthly_interest_rate = 0.01
no_years = 7
monthly_payment = loan_amount * monthly_interest_rate /( 1 - 1 / math.pow(1 + monthly_interest_rate, no_years * 12 ))
print(monthly_payment)