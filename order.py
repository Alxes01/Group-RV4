# Stacking bricks for each figure
import numpy as np
import pandas as pd
import os


def order(pard, figures, path_csv):
    # Getting number of rows for pard
    num_rows, num_cols = pard.shape

    # Creating an array to store coordinations of each brick in order to build them
    marge = np.array([[0, 0, 0, 0, 0]])
    lisa = np.array([[0, 0, 0, 0, 0]])
    maggie = np.array([[0, 0, 0, 0, 0]])
    homer = np.array([[0, 0, 0, 0, 0]])
    bart = np.array([[0, 0, 0, 0, 0]])

    # Marge
    # If function to find bricks with needed colours and putting them into an array wit specified order and height
    # in which they belong
    if figures[0] > 0:
        for i in range(num_rows):
            if pard[i][4] == 4:
                #pard[i][2] = 0
                marge = np.append(marge, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 3:
                #pard[i][2] = 19
                marge = np.append(marge, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 5:
                #pard[i][2] = 38
                marge = np.append(marge, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        # Getting number of rows and columns for marge array
        num_rows_m, num_cols_m = marge.shape

        # If all blocks for a given figure have not been found, delete the order
        if num_rows_m < 4:
            figures[0] = 0
            if num_rows_m > 1:
                marge = np.delete(marge, 0, 0)
                pard = np.append(pard, marge, axis=0)
            else:
                pass
        else:
            marge = np.delete(marge, 0, 0)

    # Lisa
    # If function to find bricks with needed colours and putting them into an array wit specified order and height
    # in which they belong
    if figures[1] > 0:
        for i in range(num_rows):
            if pard[i][4] == 3:
                #pard[i][2] = 0
                lisa = np.append(lisa, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 2:
                #pard[i][2] = 19
                lisa = np.append(lisa, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 3:
                #ard[i][2] = 38
                lisa = np.append(lisa, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        # Getting number of rows and columns for marge array
        num_rows_l, num_cols_l = lisa.shape

        # If all blocks for a given figure have not been found, delete the order
        if num_rows_l < 4:
            figures[1] = 0
            if num_rows_l > 1:
                lisa = np.delete(lisa, 0, 0)
                pard = np.append(pard, lisa, axis=0)
            else:
                pass
        else:
            lisa = np.delete(lisa, 0, 0)

    # Maggie
    # If function to find bricks with needed colours and putting them into an array wit specified order and height
    # in which they belong
    if figures[2] > 0:
        for i in range(num_rows):
            if pard[i][4] == 5:
                #pard[i][2] = 0
                maggie = np.append(maggie, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 3:
                #pard[i][2] = 19
                maggie = np.append(maggie, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        # Getting number of rows and columns for marge array
        num_rows_ma, num_cols_ma = maggie.shape

        # If all blocks for a given figure have not been found, delete the order
        if num_rows_ma < 3:
            figures[2] = 0
            if num_rows_ma > 1:
                maggie = np.delete(maggie, 0, 0)
                pard = np.append(pard, maggie, axis=0)
            else:
                pass
        else:
            maggie = np.delete(maggie, 0, 0)

    # Homer
    # If function to find bricks with needed colours and putting them into an array wit specified order and height
    # in which they belong
    if figures[3] > 0:
        for i in range(num_rows):
            if pard[i][4] == 5:
                #pard[i][2] = 0
                homer = np.append(homer, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 1:
                #pard[i][2] = 19
                homer = np.append(homer, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 3:
                #pard[i][2] = 38
                homer = np.append(homer, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        # Getting number of rows and columns for marge array
        num_rows_h, num_cols_h = homer.shape

        # If all blocks for a given figure have not been found, delete the order
        if num_rows_h < 4:
            figures[3] = 0
            if num_rows_h > 1:
                homer = np.delete(homer, 0, 0)
                pard = np.append(pard, homer, axis=0)
            else:
                pass
        else:
            homer = np.delete(homer, 0, 0)

    # Bart
    # If function to find bricks with needed colours and putting them into an array wit specified order and height
    # in which they belong
    if figures[4] > 0:
        for i in range(num_rows):
            if pard[i][4] == 5:
                #pard[i][2] = 0
                bart = np.append(bart, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break
        for i in range(num_rows):
            if pard[i][4] == 2:
                #pard[i][2] = 19
                bart = np.append(bart, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        for i in range(num_rows):
            if pard[i][4] == 3:
                #pard[i][2] = 38
                bart = np.append(bart, [pard[i, :]], axis=0)
                pard = np.delete(pard, i, 0)
                break

        # Getting number of rows and columns for marge array
        num_rows_b, num_cols_b = bart.shape

        # If all blocks for a given figure have not been found, delete the order
        if num_rows_b < 4:
            figures[4] = 0
            if num_rows_b > 1:
                bart = np.delete(bart, 0, 0)
                pard = np.append(pard, bart, axis=0)
            else:
                pass
        else:
            bart = np.delete(bart, 0, 0)

    # Saving all figures to their own .csv file
    if np.sum(figures) == 0:
        print("No figures found or cannot be made")
    else:
        if figures[0] > 0:
            marge = np.delete(marge, 4, 1)
            dfm = pd.DataFrame(marge, columns=["x", "y", "z", "rotation"])
            dfm.to_csv(os.path.join(path_csv, "fig1.csv"))
            print("Marge.csv saved")
        else:
            pass
        if figures[1] > 0:
            lisa = np.delete(lisa, 4, 1)
            dfl = pd.DataFrame(lisa, columns=["x", "y", "z", "rotation"])
            dfl.to_csv(os.path.join(path_csv, "fig2.csv"))
            print("Lisa.csv saved")
        else:
            pass
        if figures[2] > 0:
            maggie = np.delete(maggie, 4, 1)
            dfma = pd.DataFrame(maggie, columns=["x", "y", "z", "rotation"])
            dfma.to_csv(os.path.join(path_csv, "fig3.csv"))
            print("Maggie.csv saved")
        else:
            pass
        if figures[3] > 0:
            homer = np.delete(homer, 4, 1)
            dfh = pd.DataFrame(homer, columns=["x", "y", "z", "rotation"])
            dfh.to_csv(os.path.join(path_csv, "fig4.csv"))
            print("Homer.csv saved")
        else:
            pass
        if figures[4] > 0:
            bart = np.delete(bart, 4, 1)
            dfb = pd.DataFrame(bart, columns=["x", "y", "z", "rotation"])
            dfb.to_csv(os.path.join(path_csv, "fig5.csv"))
            print("Bart.csv saved")
        else:
            pass