"""
Mr. Scrooge has a sum of money 'P' that wants to invest, and he wants to know how many years 'Y' this sum has to be
 kept in the bank in order for this sum of money to amount to 'D'.

The sum is kept for 'Y' years in the bank where interest 'I' is paid yearly, and the new sum is re-invested yearly
 after paying tax 'T'

Note that the principal is not taxed but only the year's accrued interest
"""

def calculate_years(principal, interest, tax, desired):
    years = 0
    while principal < desired:
        principal += principal * interest - (principal * interest) * tax
        years += 1
    return years



print(calculate_years(1000, 0.05, 0.18, 1100))
print(calculate_years(1000,0.01625,0.18,1200))
print(calculate_years(1000,0.05,0.18,1000))
