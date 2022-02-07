import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
from math import log10

# this func do's all the calcualtions
def calculate(case : int):
    # if-else used to do calculations for both the datas seperatley; read data accordingly from diff file
    if case == 0 :
        csvReadData = pd.read_csv("Modified2_Eta-Aql.csv", usecols=[1,2], index_col= 0)
    elif case==1 :
        csvReadData = pd.read_csv("Modified2_DelCp.csv", usecols=[1,2], index_col=0)
    else : return
    #stripped the data to a part which was more good to analyise
    StrippedData = pd.DataFrame({"Magnitude":csvReadData["Magnitude"][2437860:]}) 

    # mad a column diff. it stores the diff of current element and previous element for each elemnt present
    StrippedData["diff"] = StrippedData["Magnitude"].diff()
    StrippedData.reset_index(level=0, inplace=True) 

    # this array will store all expected  time period values
    timePriodsMin = np.array([0]*len(StrippedData["diff"]))
    timePriodsMax = np.array([0]*len(StrippedData["diff"]))

    for i in range(2,len(StrippedData["diff"])):
        PreviousM = sgn(StrippedData["diff"][i-1])
        currentM = sgn(StrippedData["diff"][i])

        #stores data to timePriods array is current point is min and privous one was max.
        if (PreviousM != currentM) and currentM < 0:
            timePriodsMin[i] = StrippedData["JD"][i] - StrippedData["JD"][i-1]
        if (PreviousM != currentM) and currentM > 0:
            timePriodsMax[i] = StrippedData["JD"][i] - StrippedData["JD"][i-1]

    #find final time period by taking avregae of non zero values
    PeriodMin =sum(timePriodsMax[timePriodsMax!= 0])/len(timePriodsMax[timePriodsMax!=0])
    PeriodMax =sum(timePriodsMin[timePriodsMin!= 0])/len(timePriodsMin[timePriodsMin!=0])

    #apperent Magnitude is just average of all magnitudes given
    apperentMagnitude = sum(csvReadData["Magnitude"])/len(csvReadData["Magnitude"])

    #absolute Magnitude. this calculation is done on the basis of info available in wikipidea
    # https://en.wikipedia.org/wiki/Period-luminosity_relation#:~:text=In%20astronomy%2C%20a%20period%2Dluminosity,sometimes%20called%20the%20Leavitt%20law
    absoluteMagnitudeMax = (-2.43)*(log10(PeriodMax) - 1) - 4.05
    absoluteMagnitudeMin = (-2.43)*(log10(PeriodMin) - 1) - 4.05

    #distance of star is calulated based following fomula 
    #distnace =  10^((m-M+5)/5) parsecs 
    # it is taken from https://www.atnf.csiro.au/outreach/education/senior/astrophysics/variable_cepheids.html
    distanceMax = pow(10, (apperentMagnitude-absoluteMagnitudeMax +5)/5) * 3.26156
    distanceMin = pow(10, (apperentMagnitude-absoluteMagnitudeMin+5)/5) * 3.26156

    #all prinint work
    print(f"Case {case + 1} :")
    print("\tEta Aquilae") if case == 0 else print("\tDelta Cephei")
    print(f"\tcalculated period for this case is {(PeriodMax+PeriodMin)/2 : .2f}days and calculated distance is {(distanceMax+ distanceMin)/2:.2f} light yeras")

if __name__ == "__main__":
    sgn = lambda x : x/abs(x) if x!= 0 else 0
    calculate(0)
    calculate(1)

