balance = 100.0
rate = 0.03

print(0, round(balance,2))
for n in range(1,11):
    balance = round(balance * (1 + rate), 2)
    print(n, round(balance,2))


def compound(balance, rate, num_periods):
    """
    Calculates the ending balance compounded after investing an amount at a particular 
    interst rate over a certain period of time.

    Parameters
    balance: starting investment
    rate: fixed interest rate
    num_periods: length of time in units
    """

    balance
    for n in range(1,num_periods+1):
        balance = round(balance * (1 + rate), 2)
    return balance


def compound_by_period(balance, rate, num_periods):
    """
    Calculates compounded total for each period when given initial investment and fixed interest rate.

    Parameters
    balance: starting investment
    rate: fixed interest rate
    num_periods: length of time in units
    """

    compounded_balances = []
    compounded_balances.append(round(balance, 2))
    for n in range(1,num_periods+1):
        balance = round(balance * (1 + rate), 2)
        compounded_balances.append(balance)
    return compounded_balances


def change_per_period(balances):
    """
    Calculates the amount added each year.

    Parameters
    balances: list of ending balances for each period
    """

    change_list = []
    for n in range(1, len(balances)):
        change_list.append(round(balances[n] - balances[n-1], 2))
    return change_list

wheat = compound_by_period(1,1,63)
print(wheat)

total_wheat = sum(wheat)
print(total_wheat)