import matplotlib.pyplot as plt
import numpy as np
#x = phi2s
#y = phi2r
x = np.linspace(0.01, 0.4, 100)
ms = [[3,4],[5,6]]
ns= [10,25,50,100]
fig, axs = plt.subplots(2,2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        for n in ns:
            y = ((-((0.495*x**2)+x*(1+0.304*(ms[i][j]/n)*((1/ms[i][j])-0.5))+np.log(1-x))/(0.304*(x**(1/3))*(ms[i][j]/n)*(1-2/ms[i][j])))**(3/2))
            z = y/x
            axs[i,j].plot(y,z, label= "m="+str(ms[i][j])+", n="+str(n))

ax1 = axs[0,0]
ax2 = axs[0,1]
ax3 = axs[1,0]
ax4 = axs[1,1]
ax1.set_title(r'$\phi_{2,r}$ vs $\phi_{2,r}$/$\phi_{2,s}$ for m = 3')
ax2.set_title(r'$\phi_{2,r}$ vs $\phi_{2,r}$/$\phi_{2,s}$ for m = 4')
ax3.set_title(r'$\phi_{2,r}$ vs $\phi_{2,r}$/$\phi_{2,s}$ for m = 5')
ax4.set_title(r'$\phi_{2,r}$ vs $\phi_{2,r}$/$\phi_{2,s}$ for m = 6')
ax1.legend(fontsize =8)
ax2.legend(fontsize =8)
ax3.legend(fontsize =8)
ax4.legend(fontsize =8)
# the function, which is y = x^2 here
# setting the axes at the centre
ax1.set_xlabel(r'$\phi_{2,r}$')
ax1.set_ylabel(r'$\phi_{2,r}$/$\phi_{2,s}$')
ax2.set_xlabel(r'$\phi_{2,r}$')
ax2.set_ylabel(r'$\phi_{2,r}$/$\phi_{2,s}$')
ax3.set_xlabel(r'$\phi_{2,r}$')
ax3.set_ylabel(r'$\phi_{2,r}$/$\phi_{2,s}$')
ax4.set_xlabel(r'$\phi_{2,r}$')
ax4.set_ylabel(r'$\phi_{2,r}$/$\phi_{2,s}$')
plt.tight_layout()
# plot the function
plt.xlim(0,.4)
plt.ylim(0,3)
# show the plot
plt.show()