import numpy as np
import matplotlib.pyplot as plt
import os


def GetCrossSectionData(f):
    arr=np.genfromtxt(f,skiprows=14,skip_footer=1)
    return arr
def GetSMatData(f):
    arr=np.genfromtxt(f,skip_footer=1)
    mods=np.abs(arr[:,0]+1j*arr[:,1])
    Ls=arr[:,2]
    return np.array([Ls,mods])
def twodplot(x,y,title,xaxis,yaxis):
    fig=plt.figure()
    ax2=fig.add_subplot(111)
    ax2.plot(x,y)
    plt.title(title)
    plt.xlabel(xaxis)
    plt.ylabel(yaxis)
di='C:\\Users\\Charles\\Documents\\frescoreactions\\reactions\\'
Neu50=GetCrossSectionData(di+"Ni58Neutron50MeV\\fort.16")
Neu5=GetCrossSectionData(di+"Ni58Neutron5MeV\\fort.16")
Neurad=GetCrossSectionData(di+"Neutronradius\\fort.16")
Neudiff=GetCrossSectionData(di+"Neutrondiffuse\\fort.16")
NeuWeakcs=GetCrossSectionData(di+"NeutronWeakImaginary5MeV\\fort.16")
NeuStrongcs=GetCrossSectionData(di+"NeutronStrongImaginary5MeV\\fort.16")
NeuWeaks=GetSMatData(di+"NeutronWeakImaginary5MeV\\fort.7")
NeuStrongs=GetSMatData(di+"NeutronStrongImaginary5MeV\\fort.7")
twodplot(Neu5[:,0],Neu5[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(Neu50[:,0],Neu50[:,1],"Neutron-Nickel 58 Cross Section for 50 MeV","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(Neudiff[:,0],Neudiff[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with increased diffusiveness","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(Neurad[:,0],Neurad[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with increased radius","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(NeuStrongcs[:,0],NeuStrongcs[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with strong imaginary potential","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(NeuWeakcs[:,0],NeuWeakcs[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with weak imaginary potential","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
twodplot(NeuStrongs[0],NeuStrongs[1],"Neutron-Nickel 58 SMatrix Moduli for 5 MeV with strong imaginary potential","Angular Momentum", "SMatrix Moduli")
twodplot(NeuWeaks[0],NeuWeaks[1],"Neutron-Nickel 58 SMatrix Moduli for 5 MeV with weak imaginary potential","Angular Momentum", "SMatrix Moduli")



plt.show()
