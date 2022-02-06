import pandas
import matplotlib.pyplot as plt

f1 = pandas.read_csv("Modified_DelCp.csv", usecols=[0,1], index_col= 0)
print(f1.dtypes)
f1.plot()
plt.show()

