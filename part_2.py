from main import dab_board
from main import check_for_bingo_part_2

import pandas as pd

path = "/Users/carianne.wilson/Dropbox (Convex)/Personal - Carianne Wilson/Python Files/AdventCode/2021/day_4_input.xlsx"

xl = pd.ExcelFile(path)

# Bingo Input provided
bingo_input = pd.read_excel(xl, sheet_name="part_2", header=None)

# Extract the bingo numbers that are called
bingo_numbers = bingo_input.loc[0, :]

# Data manipulation for bingo scorecards
bingo_cards = bingo_input.loc[2:, 0:4]
bingo_cards.reset_index(inplace=True, drop=True)


for idx, number_called in enumerate(bingo_numbers):

    dabbed_board = dab_board(bingo_cards, number_called)
    bingo_cards, last_card = check_for_bingo_part_2(dabbed_board)

    if last_card:
        bingo_cards.replace(to_replace=-1.0, value=0, inplace=True)
        total_total = 0
        for total in bingo_cards.sum():
            total_total += total

        print(f"The number last called is: {int(number_called)}.\n"
              f"The total of the uncalled numbers in the scorecard is: {int(total_total)}.\n"
              f"The Day 4 Part 2 Answer is {int(number_called * total_total)}.")

        break

#
#     # Loop through the bingo cards
#     # Count the unique cards that have got bingo - the same card might get bingo more than once
#     # So need someway of being able to count the ID everytime
#     # Once the count is 99, the next card will be the last one to win
#     # Can create a list which appends the idx everytime bingo is found, can check to see if the number already
#     # exists in this list
#
# # bingo_input.drop(labels=[0,1,2,3,4,5], inplace=True)
# #
# # print(bingo_input)
# #
# # bingo_input.reset_index(inplace=True)
# #
# # print(bingo_input)