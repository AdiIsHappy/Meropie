import pandas
import matplotlib.pyplot as plt

f1 = pandas.read_csv("Modified_Eta-Aql.csv", usecols=[0,1], index_col= 0)
f1["Smooth"] = f1["Magnitude"].rolling(500).mean()
f1["Magnitude"][2437860:].plot()
plt.show()
# f1 = pandas.read_csv("Modified_DelCp.csv", usecols=[0,1], index_col= 0)
# f1["Smooth"] = f1["Magnitude"].rolling(500).mean()
# f1["Magnitude"][2437860:].plot()
# plt.show()