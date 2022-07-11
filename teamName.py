import numpy as np
import pandas as pd

nInst=100
currentPos = np.zeros(nInst)

def getMyPosition (prcSoFar):
    global currentPos

    # Build your function body here

    # if (prcSoFar == "hist"):
    #     pass


    # with open("C:/Users/Neal Dai/Documents/PYTHON_SNAKE/algothon/algothon2022-starter-code/prices.txt") as f:
    #     lines = f.read().rstrip()

    if prcSoFar == 1:
        df = pd.read_csv("C:/Users/Neal Dai/Documents/PYTHON_SNAKE/algothon/algothon2022-starter-code/prices.txt", nrows=2)
        print(df)

    #currentPos = np.full(100, 120)

    

    return currentPos

getMyPosition(1)