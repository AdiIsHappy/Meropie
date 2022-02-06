import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


sgn = lambda x : x/abs(x) if x!= 0 else 0
# [2437860:]
f1 = pd.read_csv("Modified_Eta-Aql.csv", usecols=[0,1])
f1["diff"] = f1["Magnitude"].diff()
print(f1["diff"])
x = np.array([0]*len(f1["diff"]))
for i in range(2,len(f1["diff"])):
    a = sgn(f1["diff"][i-1])
    b = sgn(f1["diff"][i])
    if a != b:
        x[i] = f1["JD"][i] - f1["JD"][i-1]
print(sum(x[x!= 0])/len(x[x!=0]))
lastWasMax = True
# for i in f1["Magnitude"][2437860:]:
    
