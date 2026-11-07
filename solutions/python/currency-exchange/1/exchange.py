"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
  return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    return round(amount / denomination)

def get_leftover_of_bills(amount, denomination):
    return amount % denomination

#def exchangeable_value(budget, exchange_rate, spread, denomination):
    
def exchangeable_value(budget, exchange_rate, spread, denomination):
    actual_exchange_rate = exchange_rate + (exchange_rate * spread / 100)
    exchanged_amount = budget / actual_exchange_rate
    whole_bills = int(exchanged_amount / denomination)
    return whole_bills * denomination

    """Calculate the maximum value of the new currency.

    Parameters:
        budget (float): The amount of your money you are planning to exchange.
        exchange_rate (float): The unit value of the foreign currency.
        spread (int): The percentage that is taken as an exchange fee.
        denomination (int) The value of a single unit (bill).

    Returns:
        int: The maximum value you can get in the new currency.

    Examples:
        >>> exchangeable_value(127.25, 1.20, 10, 20)
        80

        >>> exchangeable_value(127.25, 1.20, 10, 5)
        95

    Note:
        The currency denomination is a whole number and cannot be sub-divided.

    This function calculates and returns the maximum value of the new currency after
    determining the exchange rate plus the spread.
    """


