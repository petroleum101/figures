import pandas as pd
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#%matplotlib inline #uncomment if using ipython notebook

data = pd.read_csv('bp_review_gobal_production.csv')
data = data[20:]
data.columns = ['date', 'production']

#Polynomial fitting function of arbitrary degree.
def _polynomial(x, *p):
    poly = 0.
    for i, n in enumerate(p):
        poly += n * x**i
    return poly
 
x = data.date
y = data.production

# p0 is the initial guess for the fitting coefficients, set the length
# of this to be the order of the polynomial you want to fit.
# you can try different values and look at the plot for fit
p0 = numpy.ones(2,)

coeff, var_matrix = curve_fit(_polynomial, x, y, p0=p0)
yfit = [_polynomial(xx, *tuple(coeff)) for xx in x]

fig = plt.figure(figsize=[7,5]);

plt.plot(data.date,data.production, color='olivedrab', label='production post shale boom')
plt.plot(data.date[:-5],data.production[:-5],color='lawngreen', label='historic production data')
plt.plot(x, yfit, '--',color='darkgreen',label='curve-fitted production')
plt.legend(loc='best' )
plt.grid('off')

#TODO: fix subplot and make pretty
ax = plt.subplot(111)
ax.grid('on')
ax.set_xlabel('Date (years)')
ax.set_ylabel('Crude Oil Production (million barrels/day)')

plt.savefig('global_production.png')
plt.savefig('global_production.pdf')
plt.show()
