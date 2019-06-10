import csv
import operator
from collections import OrderedDict

def main():

    file_name = "megamillions.csv"

    startYear = input("Enter a Start year from 2003 to 2019: ")
    
    #READ IN VALUES FROM CSV FILE
    values_List = Read_In_Values(file_name, startYear)
    
    #TRANSFORM VALUES INTO A DICTIONARY
    valuesDict = AnalyzeValues(values_List)

    winningNumbers = valuesDict[0]
    powerNumber = valuesDict[1]


    #RETURN MOST FREQUENT VALUES
    BestValues = findBestValues(winningNumbers, powerNumber, startYear)
    return


def Read_In_Values(file_name, startYear):
    data = [];
    with open(file_name, 'r') as f:
        r = csv.reader(f, delimiter=',');
        for row in r:
            curYear = row[3]
            if(curYear >= startYear):
                data.append(row)
        return data


def AnalyzeValues(values_List):
    LotteryValues = []
    PowerNumber = []
    freqLotteryValues = {}
    freqPowerNumber = {}

    #GO THOUGH OUR DATA PICK OUT WHAT WE NEED     
    for day in values_List:
        #DISCECT REGULAR WINNING NUMBERS
        for numbers in range(4,8):
            # print(day[numbers])
            LotteryValues.append(day[numbers])
        
        #DISECT POWERBALL WINNNG NUcBMERS
        PowerNumber.append(day[9])



    #ADD LotteryValues TO A DICTIONARY WITH VALUES OF FREQUENCY
    for item in LotteryValues: 
        if (item in freqLotteryValues): 
            freqLotteryValues[item] += 1
        else: 
            freqLotteryValues[item] = 1

    # print("\nWINNING NUMBERS AND FREQUENCY: \n")
    # for key, value in freqLotteryValues.items(): 
    #     print (key, value) 


    #ADD PowerValues TO A DICTIONARY WITH VALUES OF FREQUENCY
    for item in PowerNumber: 
        if (item in freqPowerNumber): 
            freqPowerNumber[item] += 1
        else: 
            freqPowerNumber[item] = 1

    return freqLotteryValues, freqPowerNumber


def findBestValues(winningNumbers, powerNumber, startYear):

    sorted_winning_numbers = dict(sorted(winningNumbers.items(),key=operator.itemgetter(1), reverse=True))
    print("\nSORTED WINNING NUMBERS\n\n(number)   ==>     (frequency)\n")
    
    for key, value in sorted_winning_numbers.items():
        print(f'{key:10} ==> {value:10d}')
   
    sorted_power_numbers = dict(sorted(powerNumber.items(), key=operator.itemgetter(1),reverse=True))
    print("\nSORTED POWER NUMBERS\n")

    for key, value in sorted_power_numbers.items():
        print(f'{key:10} ==> {value:10d}')


    print("\nANALYSIS OF BEST POSSIBLE LOTTERY TICKET: \n\nStart Year: ", startYear)
    winningNumbers = list(map(int, sorted_winning_numbers))[0:5]
    winningNumbers.sort()
    print("Most Frequent winning numbers: ", winningNumbers)

    winningPowerNumbers = list(map(int,sorted_power_numbers))[0:1]
    print("Most Frequent winning power number: ",winningPowerNumbers)    

    

    return
main()
