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

ratio_arr = np.zeros(25000).reshape(100, 250)

def getMyPosition (prcSoFar):
    global currentPos
    global current_first_stock, current_second_stock
    global ratio_arr
    # Build your function body here
    
    # Creating the correlation 
    cor = np.corrcoef(prcSoFar)
    np.fill_diagonal(cor, 0)

    # Initialising the array to store the average prices
    avgArr = np.zeros(nInst)
    for i in range(100):
        avgArr[i] = np.average(prcSoFar[i][-10:])
    
    # simple moving average 
    for i in range(100):

        vol_index[i] = np.std(prcSoFar[i])

        if len(prcSoFar[1]) > 3 and vol_index[i] < 0.46:
            current_price = prcSoFar[i][-1]

            if (current_price * 0.8 < avgArr[i] ):
                currentPos[i] = int(floor(10000/current_price))
        
            if (current_price *  1.2 >  avgArr[i] ):
                currentPos[i] = - int(floor(10000/current_price))
    
    index_pos = np.where(cor > 0.92)
    index_neg = np.where(cor < -0.93)

    #print(index_pos)
    # Transferring the indicies of correlation
    # for i in range(len(index_pos[0])):
    #     first_el[i] = index_pos[0][i]
    #     second_el[i] = index_pos[1][i]
    
    # for i in range(50): 

    #     # Storing the stock pairs to detect any changes
    #     first_stock_arr[i] = int(first_el[i])
    #     second_stock_arr[i] = int(second_el[i]) 

    #     first_stock = int(first_el[i])
    #     second_stock = int(second_el[i]) 

    #     # Index correlation is subject to change, this will reset the ratio_arr array if a change is detected
    #     if current_first_stock[i] != first_stock_arr[i] or current_second_stock[i] != second_stock_arr[i]:
    #         ratio_arr[i] = np.zeros(250)

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

    #     ratio_diff = ratio / average_ratio
      
    #     #print(list[0][0])
    #     #print(first_stock_arr, second_stock_arr, prcSoFar[first_stock_arr][-1], prcSoFar[second_stock_arr][-1])
    #     if ratio_diff > 1.045:

    #         # if (prcSoFar[first_stock][-1] > avgArr[first_stock] * 1.045):

    #         #     currentPos[first_stock] = -int(floor(10000/prcSoFar[first_stock][-1]))

    #         # elif (prcSoFar[second_stock][-1] < avgArr[second_stock] * 0.955):

    #         #     currentPos[second_stock] = int(floor(10000/prcSoFar[second_stock][-1]))
            
    #         # else:
    #         currentPos[first_stock] = -int(floor(10000/prcSoFar[first_stock][-1]))
    #         currentPos[second_stock] = int(floor(10000/prcSoFar[second_stock][-1]))

    #         print("upper")
        
    #     if ratio_diff < 0.955:

    #         # if (prcSoFar[first_stock][-1] < avgArr[first_stock] * 0.955):
    #         #     currentPos[first_stock] = int(floor(10000/prcSoFar[first_stock][-1]))

    #         # elif (prcSoFar[first_stock][-1] < avgArr[first_stock] * 1.045):
    #         #     currentPos[second_stock] = - int(floor(10000/prcSoFar[second_stock][-1]))
            
    #         # else:
    #         currentPos[first_stock] = int(floor(10000/prcSoFar[first_stock][-1]))
    #         currentPos[second_stock] = -int(floor(10000/prcSoFar[second_stock][-1]))

    #         print("lower")
    
    # ratio_arr[0][0] = 1123
    #print(avgArr[0], currentPos[0], len(prcSoFar[1]))
    #print(index_neg)
    
        #print(ratio_arr, ratio_diff)
    # for i in range(sizeof(index_pos)):
    #     price_dif = 

    #print for troubleshooting
    # print("Therefore, change position sizes by:")
    # print(changeNeeded)

    #return changes needed to be made to our position
    return currentPos


    
