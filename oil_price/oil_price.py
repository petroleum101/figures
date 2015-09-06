import pandas as pd
import numpy
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
#%matplotlib inline

data = pd.read_csv('oil_price.csv')
data.columns = ['date',
                'bp',
                'domestic',
                'landed_arabian',
                'arabian_ras',
                'brent',
                'wti',
                'imported_aquisition',
                'domestic_aquisition',
                'dubai']



fig = plt.figure(figsize=[7,5]);

#plt.plot(data.date,data.bp, color='olivedrab', label='BP')
plt.plot(data.date,data.domestic, label='US Domestic')
plt.plot(data.date,data.landed_arabian,label='U.S. Landed of Arabian Light')
plt.plot(data.date,data.arabian_ras,label='Arabian Light posted at Ras Tanura')
plt.plot(data.date,data.brent,label='Brent Crude')
plt.plot(data.date,data.brent,label='West Texas Intermediate Crude')
plt.plot(data.date,data.imported_aquisition,label='US Imported Crude')
plt.plot(data.date,data.domestic_aquisition,label='US Domestic Acquisition')
plt.plot(data.date,data.dubai,label='Dubai Crude ')

plt.legend(loc='best')
plt.grid('off')

#TODO: fix subplot and make pretty
ax = plt.subplot(111)
ax.grid('on')
ax.set_xlabel('Date (years)')
ax.set_ylabel('Annual Average Crude Oil Price (US $)')

plt.savefig('oil_price.png')
plt.savefig('oil_price.pdf')
plt.savefig('oil_price.svg')

plt.show()

