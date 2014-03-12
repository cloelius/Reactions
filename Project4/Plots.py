import numpy as np
import matplotlib.pyplot as plt
import os

def GetCrossSectionData(f):
    arr=np.genfromtxt(f,skiprows=6,skip_footer=32)
    return arr
def GetSMatData(f):
    arr=np.genfromtxt(f,skip_footer=1)
    mods=np.abs(arr[:,0]+1j*arr[:,1])
    Ls=arr[:,2]
    return np.array([Ls,mods])
def twodplot(x,y,title="",xaxis="",yaxis="",fig=None,leg=None,log=False):
    if(fig==None):
        fig=plt.figure()
        ax2=fig.add_subplot(111)
        plt.title(title)
        plt.xlabel(xaxis)
        plt.ylabel(yaxis)
    else :
        ax2=fig.gca()
    if leg != None:
            ax2.plot(x,y,label=leg)
    else:
            ax2.plot(x,y)
    handles, labels = ax2.get_legend_handles_labels()
    if any(labels):
        ax2.legend(handles[::-1], labels[::-1],loc=2)
    if log:
        ax2.set_yscale('log')
    return fig
    
SpinOrbit="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\SpinOrbit\\fort.16"
SpinOrbitAll="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\SpinOrbitAll\\fort.16"
SurfcaeLimited="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\Surface\\fort.16"
SurfAll="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\SufaceImVolumeReal\\fort.16"
VolumeRealStrength="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\VolumeRealStrength\\fort.16"
VolumeReal="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\VolumeRealOnly\\fort.16"
VolumeAll="C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\VolumeAll\\fort.16"

data=GetCrossSectionData(SpinOrbitAll)
fig=twodplot(data[:,0],data[:,1],"Fresco Cross Sections for Ni 58 +p scattering at 16 MeV", "Angle(theta)", "Cross Section(mb/sr)",leg="Spin Orbit With All Terms Varied")
spinorbdat=GetCrossSectionData(SpinOrbit)
twodplot(spinorbdat[:,0],spinorbdat[:,1],fig=fig,leg="Spin Orbit Terms Added, Strength and r varied")
surflim=GetCrossSectionData(SurfcaeLimited)
surfall=GetCrossSectionData(SurfAll)
twodplot(surfall[:,0],surfall[:,1],fig=fig,leg="Surface and Volume All Strength and R terms varied)")
twodplot(surflim[:,0],surflim[:,1],fig=fig,leg="Surface Imaginary Potential, Volume Real Terms varied")
volall=GetCrossSectionData(VolumeAll)

volstreng=GetCrossSectionData(VolumeRealStrength)
twodplot(volall[:,0],volall[:,1],fig=fig,leg="Volume Real and Imaginary Strength and Radius varied")

volreal=GetCrossSectionData(VolumeReal)
twodplot(volreal[:,0],volreal[:,1],fig=fig,leg="Volume Real Strength and Radius varied")

twodplot(volstreng[:,0],volstreng[:,1],fig=fig,leg="Volume Real Strength Term Varied")

ActualData=np.loadtxt("C:\\Users\\Charles\\Documents\\Assignment4\\Ni58ActualValuesWithModifyingPotentials\\Data\\Data.txt")
axes=fig.gca()
axes.scatter(ActualData[:,0],ActualData[:,1],label="Actual Data")
handles, labels = axes.get_legend_handles_labels()
if any(labels):
        axes.legend(handles[::-1], labels[::-1],loc=2)
#axes.set_yscale('log')

fig1=twodplot(volall[:,0],volall[:,1],"Comparison of Effects of Imaginary Term of Fresco Cross Sections for Ni 58 +p scattering at 16 MeV", "Angle(theta)", "Cross Section(mb/sr)",leg="Volume Imaginary")
twodplot(surflim[:,0],surflim[:,1],fig=fig1,leg="Surface Imaginary Term")
fig2=plt.figure()
axes2=fig2.gca()
axes2.scatter(ActualData[:,0],ActualData[:,1])
plt.title("Differential Cross Section Data for Ni-58+p at 16 MeV")
plt.ylabel("Differential Cross Section mb/sr")
plt.xlabel("Angle(Degrees)")
plt.show()