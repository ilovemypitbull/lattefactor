print("What is your splurge?")
splurge = input()

print("How much is your", splurge,"?")
cost = float(input())

print("How many times a month do you pay for it?")
frequency = float(input())

year_frequency = frequency * 12
year_cost = year_frequency * cost

print ("You spend", round(year_cost,2), "a year on", splurge)

print("How many years until you retire?")
investment_years = float(input())

print("Optional: What's your expected rate of return (eg: 0.1)?")

rate = input()

if rate == '':
    rate = 0.1
else:
    rate = float(rate)


total_earned = year_cost * (1+rate)**investment_years

print ("You would earn", round(total_earned, 2), "investing the money you spend on", splurge, "in a single year")

print("Optional: What's your expected withdrawl rate (eg: 0.04)?")
withdrawl_rate = input()

if withdrawl_rate == '':
    withdrawl_rate = 0.04
else:
    withdrawl_rate = float(withdrawl_rate)


yearly_surplus = withdrawl_rate * total_earned

print ("You would earn", round(yearly_surplus, 2), "a year in retirement on this", splurge, "money")

print("Optional: What is the rate of inflation (eg: 0.05)?")

inflation_rate = input()

if inflation_rate == '':
    inflation_rate = 0.05
else:
    inflation_rate = float(inflation_rate)

future_cost = cost * (1+inflation_rate)**investment_years

print("In the future", splurge, "is estimated to cost", round(future_cost, 2))
print("This means that if you skip buying", splurge, "for one year and invest the money instead you can afford", splurge, 
round(yearly_surplus/future_cost, 0), "times a year indefinitely")