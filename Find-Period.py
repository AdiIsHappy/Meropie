import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


sgn = lambda x : x/abs(x) if x!= 0 else 0
# [2437860:]
# x = pd.read_csv("Modified2_Eta-Aql.csv", usecols=[1,2], index_col= 0)
x = pd.read_csv("Modified2_DelCp.csv", usecols=[1,2], index_col=0)

f1 = pd.DataFrame({"Magnitude":x["Magnitude"][2437860:]}) 
f1["diff"] = f1["Magnitude"].diff()
f1.reset_index(level=0, inplace=True)

print(f1["diff"])
print(f1.dtypes)
n = np.array([0]*len(f1["diff"]))
for i in range(2,len(f1["diff"])):
    a = sgn(f1["diff"][i-1])
    b = sgn(f1["diff"][i])
    if (a != b) and b < 0:
        n[i] = f1["JD"][i] - f1["JD"][i-1]
print(sum(n[n!= 0])/len(n[n!=0]))
print(n[n!= 0])
# lastWasMax = True



# for i in f1["Magnitude"][2437860:]:
    
