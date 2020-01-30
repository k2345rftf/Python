from pandas import read_csv, DataFrame
import math
import statsmodels.api as sm
import matplotlib.pyplot as plt
import numpy as np

def lag_korr(t, X,Y):
	size_x = len(X)
	size_y = len(Y)
	if  size_x!= size_y:
		return -2
	if t > size_x:
		return -3

	if size_x == 0:
		return -4

	if t < 0:
		return -5
	rez = 0
	cor1 = 0
	cor2 = 0
	cor3 = 0
	size_n = size_x
	sum1 = 0
	sum2 = 0
	sum3 = 0
	sum4 = 0
	sum5 = 0
	sum6 = 0
	for i in range(size_n-t):
		sum1 = sum1 + X[i]*Y[i+t]
		sum2 = sum2 + X[i]*Y[i+t]
		sum3 = sum3 + X[i]
		sum4 = sum4 + Y[i+t]
		sum5 = sum5 + X[i]*X[i]
		sum6 = sum6 + Y[i]*Y[i]


	cor1 = (size_n-t)*sum1-sum3*sum4
	cor2 = (size_n-t)*sum5 - sum3*sum3
	cor3 = (size_n-t)*sum6 - sum4*sum4
	rez = cor1/(math.sqrt(cor2*cor3))
	return rez


data = read_csv('oil.csv', ",",index_col=['<DATE>'], parse_dates=['<DATE>'], dayfirst=True)
otg = data.CLOSE

data1 = read_csv('gazprom.csv', ",",index_col=['<DATE>'], parse_dates=['<DATE>'], dayfirst=True)
otg1 = data1.CLOSE

plt.figure(figsize=(12,5))
plt.title('Цены на момент закрытия компании Газпром и Brent')

ax1 = otg1.plot(color='blue', grid=True, label='Brent')
ax2 = otg.plot(color='red', grid=True, secondary_y=True, label='Газпром')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()

plt.legend(h1+h2, l1+l2, loc=1)
plt.show()
print("Коэффициент корреляции r: ",otg.dropna().corr(otg1.dropna()))
print("Коэффициент корреляции r после преобразований: ",otg.dropna().pct_change().corr(otg1.dropna().pct_change()))
plt.subplot(1, 2, 1)
plt.scatter(
    otg.dropna(),
    otg1.dropna());
plt.title('Correlation')

plt.subplot(1, 2, 2)
plt.scatter(
    otg.dropna().pct_change(),
    otg1.dropna().pct_change());
plt.title('Percent change correlation');
plt.show()

result = sm.OLS(otg, otg1).fit()

print(result.summary())