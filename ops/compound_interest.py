import matplotlib.pyplot as plt
import numpy as np

warning = "==============================================\n" \
          "ASSUMPTIONS:\n" \
          "-Daily interest is consistent and predictable.\n" \
          "-Daily profits will be reinvested constantly.\n" \
          "==============================================\n"

print(warning)

# make drop-down and search UI.
coin_type = input("Coin: ")

# ensure your amounts are constantly calculating and updating.
baseline = 200
baseline_daily_interest = 0.0440
baseline_weekly_interest = 0.36
baseline_monthly_interest = 1.40
baseline_yearly_interest = 16.78

baseline_daily_interest_rate = 1 / (baseline / baseline_daily_interest) * 100
baseline_yearly_interest_rate = 1 / (baseline / baseline_yearly_interest) * 100

print("Daily interest: " + str(baseline_daily_interest_rate) + "%")
print("Weekly interest: " + str(1 / (baseline / baseline_weekly_interest) * 100) + "%")
print("Monthly interest: " + str(1 / (baseline / baseline_monthly_interest) * 100) + "%")
print("Yearly interest: " + str(baseline_yearly_interest_rate) + "%")

# ============== #

year = 365
month = 31
week = 7


def check_compound(time_frame, baseline, baseline_daily_interest_rate, return_data=False):
    """
    :param time_frame: int. number of days.
    :param baseline: int. investment amount.
    :param baseline_interest_rate: int. percentage. should be way below 1.
    :return:
    """
    # Day 1:
    daily_interest = baseline * baseline_daily_interest_rate
    amount = baseline + daily_interest
    y_coins = [amount]
    for i in range(time_frame - 1):
        daily_interest = amount * baseline_daily_interest_rate / 100
        amount += daily_interest
        gains = amount - baseline
        y_coins.append(gains)
    interest = amount - baseline
    interest_rate = 1 / (baseline / interest) * 100

    # plotting
    x_days = np.asarray(list(range(time_frame)))
    y_coins = np.asarray(y_coins)
    print(x_days.shape)
    print(y_coins.shape)
    graph = plt.plot(x_days, y_coins)
    plt.show(graph)

    if return_data:
        return interest_rate, interest, x_days, y_coins
    else:
        return interest_rate, interest


compound_rate, compound_amount, x, y = check_compound(year * 100, 2000, baseline_daily_interest_rate, True)
print("Compound rate = " + str(compound_rate) + " %")
print("Interest = " + str(compound_amount) + " " + coin_type)

run_status = True
while run_status:
    year = input("Check your profits in x years: ")
    if year in ["Y", "y"]:
        run_status = False
    else:
        year = float(year)
        print("Gains in " + str(year) + " years: " + str(y[round(365 * year)]))


# COINMARKETCAP API. pro.coinmarketcap.com/account
API_key = "6d7f5365-d3c4-4210-804e-c3c36302499d"