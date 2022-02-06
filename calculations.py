import pandas
import matplotlib.pyplot as plt

f1 = pandas.read_csv("Modified_DelCp.csv", usecols=[0,1], index_col= 0)
Mv = sum(f1["Magnitude"])/len(f1["Magnitude"])
p = pow(10, (Mv/ + 4.05)/(-2.43)  + 1)
print(p)

