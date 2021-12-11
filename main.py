# BINGO Generator

import pandas as pd

def dab_board(bingo_card, number):
    """
    :param bingo_card: dataframe of bingocard
    :param number: number called by bingo caller
    :return: new dataframe with numbers checked off
    """
    # Bingo Cards are 5 x 5 cards, however we will dab as if they are one
    bingo_card = bingo_card.replace(to_replace=number, value=-1)
    return bingo_card


def check_for_bingo_part_1(bingo_card):
    """
    Function to check if any bingo card has got bingo
    :param bingo_card:
    :return:
    """
    bingo_found = False

    # Loop through each of the bingo scorecards
    for i in range(0, 500, 5):
        # Create the individual scorecard to check
        new_card = pd.DataFrame()
        new_card = bingo_card.loc[i: i + 4, :]

        # Column / Row totals (if this equals -5 then bingo has been achieved!)
        column_totals = new_card.sum(axis=0)
        row_totals = new_card.sum(axis=1)

        for idx in range(0, 5):
            if int(column_totals.iloc[idx]) == -5:
                print("Total Found")
                bingo_found = True
                return bingo_found, new_card

            elif int(row_totals.iloc[idx]) == -5:
                print("Total Found")
                bingo_found = True
                return bingo_found, new_card

    return bingo_found, new_card


def check_for_bingo_part_2(bingo_card):
    """
    Check if a 5x5 scorecard has achieved bingo
    Once located, note down the index of the scorecard and add to a list
    Once you have looped through all scorecards, drop the rows of the cards with bingo
    :param bingo_card: dataframe
    :return:
    """
    rows_to_drop = []

    bingo_card_input = bingo_card
    return_bingo_card = bingo_card

    # Loop through each of the bingo scorecards
    for i in range(0, len(bingo_card_input), 5):

        # Create the individual scorecard to check
        new_card = bingo_card_input.loc[i: i + 4, :]

        # Column / Row totals (if this equals -5 then bingo has been achieved!)
        column_totals = new_card.sum(axis=0)
        row_totals = new_card.sum(axis=1)

        for idx in range(0, 5):
            if int(column_totals.iloc[idx]) == -5:
                rows_to_drop += [j for j in range(i, i + 5)]

            elif int(row_totals.iloc[idx]) == -5:
                rows_to_drop += [j for j in range(i, i + 5)]

            if len(rows_to_drop) == 5:
                if len(bingo_card_input) == 5:
                    last_card = True

                    return bingo_card_input, last_card

    return_bingo_card.drop(labels=rows_to_drop, inplace=True)
    return_bingo_card.reset_index(inplace=True, drop=True)
    last_card = False

    return return_bingo_card, last_card
