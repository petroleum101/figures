import pandas as pd
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#%matplotlib inline #uncomment if using ipython notebook

data = pd.read_csv('bp_outlook_2035_gas_production.csv')
data.columns = ['date',
                'north_america',
                'south_central_america',
                'europe_euroasia',
                'middle_east',
                'africa',
                'asia_pacific',
                'total']

fig = plt.figure(figsize=[7,6]);
plt.plot(data.date,data.north_america, label='North Ameria')
plt.plot(data.date,data.south_central_america, label='South and Central America')
plt.plot(data.date,data.europe_euroasia, label='Europe and Eurasia')
plt.plot(data.date,data.middle_east, label='Middle East')
plt.plot(data.date,data.africa, label='Africa')
plt.plot(data.date,data.asia_pacific, label='Asia Pacific')
plt.plot(data.date,data.total, label='Total Oil Production')
plt.legend(loc='best' )
plt.grid('off')

ax = plt.subplot(111)
#ax.grid('on')
ax.set_xlabel('Date (years)')
ax.set_ylabel('Projected Natural Gas Production (million tonnes of oil equivalent)')
plt.savefig('gas_outlook_2035.png')
plt.savefig('gas_outlook_2035.pdf')
plt.savefig('gas_outlook_2035.svg')
plt.show()
