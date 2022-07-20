from math import floor
import numpy as np

nInst = 100
currentPos = np.zeros(nInst)

vol_index = np.zeros(nInst)

first_el = np.zeros(9999)
second_el = np.zeros(9999)

current_first_stock = np.zeros(100)
current_second_stock = np.zeros(100)

first_stock_arr = np.zeros(100)
second_stock_arr = np.zeros(100)

first_stock = 0
second_stock = 0

index_pos_ref = np.zeros(100)

ratio_arr = np.zeros(75000).reshape(100, 750)

def getMyPosition (prcSoFar):
    global currentPos
    global current_first_stock, current_second_stock
    global ratio_arr

    # Build your function body here
    
    # Creating the correlation matrix between each stock
    cor = np.corrcoef(prcSoFar)
    np.fill_diagonal(cor, 0)

    # Captures the indexes that have correlation to specified degree
    index_pos = np.where(cor > 0.95)
    index_neg = np.where(cor < -0.93)

    first_el = np.zeros(9999)
    second_el = np.zeros(9999)

    # Initialising the array to store the average prices
    avgArr = np.zeros(nInst)
   
    for i in range(100):
        
        avgArr[i] = np.average(prcSoFar[i][-10:])
      

    # # Transferring the indicies of correlation
    # for i in range(int(0.5 * len(index_pos[0]))):
     
    #     if index_pos[0][i] not in index_pos[0][0:i]:
    #         if index_pos[1][i] not in index_pos[1][0:i]:
    #             if index_pos[0][i] not in index_pos[1][0:i]:
    #                 if index_pos[1][i] not in index_pos[0][0:i]:
    #                     first_el[i] = index_pos[0][i]
    #                     second_el[i] = index_pos[1][i]
    
    # first_el_ref = first_el[first_el != 0]
    # second_el_ref = second_el[second_el != 0]

    # for i in range(len(first_el_ref)): 

    #     # Storing the stock pairs to detect any changes
    #     first_stock_arr[i] = int(first_el_ref[i])
    #     second_stock_arr[i] = int(second_el_ref[i]) 

    #     first_stock = int(first_el_ref[i])
    #     second_stock = int(second_el_ref[i]) 

    #     # Index correlation is subject to change, this will reset the ratio_arr array if a change is detected
    #     if current_first_stock[i] != first_stock_arr[i] or current_second_stock[i] != second_stock_arr[i]:
    #         ratio_arr[i] = np.zeros(750)

    #     current_first_stock[i] = first_stock_arr[i]
    #     current_second_stock[i] = second_stock_arr[i]  

    #     ratio = prcSoFar[first_stock][-1] / prcSoFar[second_stock][-1] if prcSoFar[second_stock][-1] !=0 else 1

    #     current_day = 0
        
    #     if len(prcSoFar[1]) > current_day:
    #         ratio_arr[i][len(prcSoFar[1])] = ratio
    #         current_day = len(prcSoFar[1])
        
    #     list = np.nonzero(ratio_arr[i])

    #     # As most of the ratio array will be filled with 0 after it resets, this finds all the non zero terms to take an average
    #     average_ratio = np.average(ratio_arr[i][list[0][0]:list[0][-1]])

    #     # Comparing the current ratio to the average ratio
    #     ratio_diff = ratio / average_ratio
      
    #     if ratio_diff > 1.07:

    #         if (prcSoFar[first_stock][-1] > avgArr[first_stock] * 1.07):

    #             currentPos[first_stock] = -int(floor(8600/prcSoFar[first_stock][-1]))

    #         elif (prcSoFar[second_stock][-1] < avgArr[second_stock] * 0.93):

    #             currentPos[second_stock] = int(floor(8600/prcSoFar[second_stock][-1]))
            
    #         else:
    #             currentPos[first_stock] = -int(floor(8600/prcSoFar[first_stock][-1]))
    #             currentPos[second_stock] = int(floor(8600/prcSoFar[second_stock][-1]))
        
    #     if ratio_diff < 0.97:

    #         if (prcSoFar[first_stock][-1] < avgArr[first_stock] * 0.97):
    #             currentPos[first_stock] = int(floor(8600/prcSoFar[first_stock][-1]))

    #         elif (prcSoFar[first_stock][-1] < avgArr[first_stock] * 1.03):
    #             currentPos[second_stock] = - int(floor(8600/prcSoFar[second_stock][-1]))
            
    #         else:
    #             currentPos[first_stock] = int(floor(8600/prcSoFar[first_stock][-1]))
    #             currentPos[second_stock] = -int(floor(8600/prcSoFar[second_stock][-1]))
    
    """Simple Moving Average"""
    
    for i in range(100):

        # Indexing each instrument's volatility 
        vol_index[i] = np.std(prcSoFar[i])

        
        # Checks if volatility is lower than 0.249, if so the instrument will be considered
        if vol_index[i] < 0.25: 
            current_price = prcSoFar[i][-1]

            # Consider the price with relation to the 10 day moving average
            if (current_price * 0.95 < avgArr[i] ):
                currentPos[i] = int(floor(10000/current_price))
            
            if (current_price * 1.05 >  avgArr[i]):
                currentPos[i] = - int(floor(10000/current_price))
    
    return currentPos