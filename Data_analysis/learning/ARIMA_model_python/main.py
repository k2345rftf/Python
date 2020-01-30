from pandas import read_csv, DataFrame
import statsmodels.api as sm
from statsmodels.iolib.table import SimpleTable
from sklearn.metrics import r2_score
import ml_metrics as metrics
import matplotlib.pyplot as plt
import numpy as np


def addufler_test(data):
	test = sm.tsa.adfuller(data)
	print ('adf: ', test[0] )
	print ('p-value: ', test[1])
	print('Critical values: ', test[4])
	if test[0]> test[4]['5%']: 
	    print ('есть единичные корни, ряд не стационарен')
	else:
	    print ('единичных корней нет, ряд стационарен')

# 1) Загрузка и обработка данных
data = read_csv('data1.csv', ";",index_col=['DATE'], parse_dates=['DATE'], dayfirst=True)
otg = data.CLOSE

otg = otg.resample('M').mean()
# otg.plot()
# Гистограмма частоты
itog = otg.describe()
# otg.hist()
print(itog)
print ('Коэфф. вариации = {}'.format(itog['std']/itog['mean']))

# тест Харки — Бера 
row =  [u'JB', u'p-value', u'skew', u'kurtosis']
jb_test = sm.stats.stattools.jarque_bera(otg)
a = np.vstack([jb_test])
itog = SimpleTable(a, row)
print(itog)


 # обобщенный тест Дикки-Фуллера
addufler_test(otg)
# определние порядока интегрированного ряда
otg1diff = otg.diff(periods=1).dropna()
 # обобщенный тест Дикки-Фуллера
addufler_test(otg1diff)
m = otg1diff.index[len(otg1diff.index)//2+1]
r1 = sm.stats.DescrStatsW(otg1diff[m:])
r2 = sm.stats.DescrStatsW(otg1diff[:m])
print ('p-value: ', sm.stats.CompareMeans(r1,r2).ttest_ind()[1])

# otg1diff.plot(figsize=(12,6))
# Определяем p и q
# fig = plt.figure(figsize=(12,8))
# ax1 = fig.add_subplot(211)
# fig = sm.graphics.tsa.plot_acf(otg1diff.values.squeeze(), lags=25, ax=ax1)
# ax2 = fig.add_subplot(212)
# fig = sm.graphics.tsa.plot_pacf(otg1diff, lags=25, ax=ax2)

p=1
q=1
d=1
# прогноз(Построение ARIMA модели)
dat = '2018-11-30'
src_data_model = otg[:dat]
model = sm.tsa.ARIMA(src_data_model, order=(p,d,q), freq='M').fit(disp=0)
print(model.summary())
# остатки модели и построение для них ACF
q_test = sm.tsa.stattools.acf(model.resid, qstat=True) #свойство resid, хранит остатки модели, qstat=True, означает что применяем указынный тест к коэф-ам
#Расчет коэффициента детерминации R^2
pred = model.predict(dat,'2018-12-31', typ='levels')
trn = otg[dat:'2018-11-30']
l = len(trn)+1
r2 = r2_score(trn, pred[1:l])
print ('R^2: %1.2f' % r2)
print("Среднеквадратичное отклонение нашей модели:")
print(metrics.rmse(trn,pred[1:l]))
print("Средняя абсолютная ошибка прогноза:")
print(metrics.mae(trn,pred[1:l]))

otg.plot()
pred.plot(style='r--')
plt.show()