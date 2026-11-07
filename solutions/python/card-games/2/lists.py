"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

def get_rounds(number):
    return [number, number + 1, number + 2]

def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2

def list_contains_round(rounds, number):
    return number in rounds

def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    average = sum(hand) / len(hand)

    first_last_average = (hand[0] + hand[-1]) / 2

    if len(hand) % 2 == 1:
        middle_average = hand[len(hand) // 2]
    else:
        middle_average = (
            hand[len(hand) // 2 - 1] + hand[len(hand) // 2]
        ) / 2

    return average in (first_last_average, middle_average)

def average_even_is_average_odd(hand):
    even_average = sum(hand[::2]) / len(hand[::2])
    odd_average = sum(hand[1::2]) / len(hand[1::2])
    return even_average == odd_average

def maybe_double_last(hand):
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand

