from main import dab_board
from main import check_for_bingo_part_1

import pandas as pd

path = "/Users/carianne.wilson/Dropbox (Convex)/Personal - Carianne Wilson/Python Files/AdventCode/2021/day_4_input.xlsx"

xl = pd.ExcelFile(path)

# Bingo Input provided
bingo_input = pd.read_excel(xl, sheet_name="part_1", header=None)

# Extract the bingo numbers that are called
bingo_numbers = bingo_input.loc[0, :]

# Data manipulation for bingo scorecards
bingo_input.dropna(how="all", inplace=True)
bingo_input.reset_index(inplace=True, drop=True)
bingo_input = bingo_input.loc[1:, 0:4]
bingo_input.reset_index(inplace=True, drop=True)

# Code for Day 1 Part 1 - determines which board is the first to win
for number_called in bingo_numbers:
    bingo_input = dab_board(bingo_input, number_called)

    bingo_found, bingo_card = check_for_bingo_part_1(bingo_input)
    if bingo_found:
        bingo_card.replace(to_replace=-1.0, value=0, inplace=True)
        total_total = 0

        for total in bingo_card.sum():
            total_total += total

        print(f"The number last called is: {int(number_called)}.\n"
              f"The total of the uncalled numbers in the scorceard is: {int(total_total)}.\n"
              f"The Day 4 Part 1 Answer is {int(number_called * total_total)}.")
        break
