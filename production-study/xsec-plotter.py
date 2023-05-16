import numpy as np
import matplotlib.pyplot as plt

basedir="./MG5_aMC_v2_9_15/wh/Events/"

## import data files
data1 = np.loadtxt(basedir+'scan_run_0[1-9].txt', skiprows=1, usecols=(1,2))
#data2 = np.loadtxt('scan_mgo14TeV[-_scan_07].txt', skiprows=1, usecols=(1,2))

## define the variables for the x and y axes
mh=data1[:,0]
xsec1=data1[:,1]
#xsec2=data2[:,1]

## setup a plot
plt.plot(mh,xsec1,'-or',label='WH')
#plt.plot(mh,xsec2*10**6,'--or',label='$\sqrt{s}=14$TeV')
xlab=r'$m_{Higgs}$ [GeV]'
ylab=r'$\sigma(pp \rightarrow H + X)$ [pb]'
xlimrange=[10,100]
ylimrange=[10**-1,50**2]
savepdf='xsec_scan.pdf'

## setup the details
plt.yscale('log')
plt.xlim(xlimrange)
plt.ylim(ylimrange)
plt.title("Higgs Production in LHC")
plt.xlabel(xlab, fontsize=16)
plt.ylabel(ylab, fontsize=16)
plt.legend()
plt.grid()
plt.gca().xaxis.set_tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)
plt.gca().yaxis.set_tick_params(which='both', direction='in',bottom=True, top=True, left=True, right=True)

## output
plt.savefig(savepdf, format='pdf', bbox_inches='tight')
plt.show()
