import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#%matplotlib inline # uncomment if using ipython notebook

data = pd.read_csv('eia_US_annual_field_production_oil_MCRFPUS1.csv')
data.columns = ['date', 'production']

#Polynomial fitting function of arbitrary degree.
def _polynomial(x, *p):
    poly = 0.
    for i, n in enumerate(p):
        poly += n * x**i
    return poly

x = data.date[:-5]
y = data.production[:-5]

# p0 is the initial guess for the fitting coefficients, set the length
# of this to be the order of the polynomial you want to fit.
# you can try differnt values and look at the plot for fit
p0 = numpy.ones(4,)

coeff, var_matrix = curve_fit(_polynomial, x, y, p0=p0)

yfit = [_polynomial(xx, *tuple(coeff)) for xx in x]

#Can play with colors following the link
#http://stackoverflow.com/questions/22408237/named-colors-in-matplotlib
fig = plt.figure(figsize=[7,5]);
plt.plot(data.date,data.production, color='olivedrab', label='production post shale boom')
plt.plot(data.date[:-6],data.production[:-6],color='lawngreen', label='historic production data')
plt.plot(x[10:], yfit[10:], '--',color='darkgreen',label='curve-fitted production')
plt.legend(loc='best' )
plt.grid('off')

#TODO: Make graph pretty with subplot
ax = plt.subplot(111)
ax.grid('on')
ax.set_xlabel('Date (years)')
ax.set_ylabel('Crude Oil Production (billion barrels/year)')
plt.savefig('us_production.png')
plt.savefig('us_production.pdf')

plt.show()
