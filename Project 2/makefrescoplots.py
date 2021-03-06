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
def twodplot(x,y,title,xaxis,yaxis,fig=None,leg=None,log=False):
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
        ax2.legend(handles[::-1], labels[::-1])
    if log:
        ax2.set_yscale('log')
    return fig
di='C:\\Users\\Charles\\Documents\\frescoreactions\\reactions\\'
ProtonPoint5=GetCrossSectionData(di+"pointlikeNi58Coulomb5Mev\\fort.16")
ProtonPoint50=GetCrossSectionData(di+"pointlikeNi58CoulombEn50Mev\\fort.16")
Proton5=GetCrossSectionData(di+"Ni58CoulombEn5Mev\\fort.16")
Proton50=GetCrossSectionData(di+"Ni58CoulombEn50Mev\\fort.16")
ProtPlot=twodplot(Proton5[:,0],Proton5[:,1],"Proton-Ni58 Cross Sections for Pointlike and Non-pointlike Nuclei","Angle(degrees)","Differential Cross Section(relative to Rutherford)",leg="5MeV r=1.2")
twodplot(Proton50[:,0],Proton50[:,1],"Proton-Ni58 Cross Sections for Pointlike and Non-pointlike Nuclei","Angle(degrees)","Differential Cross Section(mbarn per radian",leg="50MeV r=1.2",fig=ProtPlot)
twodplot(ProtonPoint5[:,0],ProtonPoint5[:,1],"Proton-Ni58 Cross Sections for Pointlike and Non-pointlike Nuclei","Angle(degrees)","Differential Cross Section(mbarn per radian",leg="5MeV pointlike",fig=ProtPlot)
twodplot(ProtonPoint50[:,0],ProtonPoint50[:,1],"Proton-Ni58 Cross Sections for Pointlike and Non-pointlike Nuclei","Angle(degrees)","Differential Cross Section(mbarn per radian",leg="50MeV pointlike",fig=ProtPlot)

Neu50=GetCrossSectionData(di+"Ni58Neutron50MeV\\fort.16")
Neu5=GetCrossSectionData(di+"Ni58Neutron5MeV\\fort.16")
Neurad=GetCrossSectionData(di+"Neutronradius\\fort.16")
Neudiff=GetCrossSectionData(di+"Neutrondiffuse\\fort.16")
NeuWeakcs=GetCrossSectionData(di+"NeutronWeakImaginary5MeV\\fort.16")
NeuStrongcs=GetCrossSectionData(di+"NeutronStrongImaginary5MeV\\fort.16")
NeuWeaks=GetSMatData(di+"NeutronWeakImaginary5MeV\\fort.7")
NeuStrongs=GetSMatData(di+"NeutronStrongImaginary5MeV\\fort.7")
Neuen=twodplot(Neu5[:,0],Neu5[:,1],"Neutron-Nickel 58 Cross Section","Angle (Degrees)", "Differential Cross Section(mbarn per radian)",leg="5 MeV",log=True)
twodplot(Neu50[:,0],Neu50[:,1],"Neutron-Nickel 58 Cross Section for 50 MeV","Angle (Degrees)", "milibarn per radian",fig=Neuen,leg="50 MeV")
#twodplot(Neudiff[:,0],Neudiff[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with increased diffusiveness","Angle (Degrees)", "Differential Cross Section(relative to Rutherford",leg="hi")
#twodplot(Neurad[:,0],Neurad[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with increased radius","Angle (Degrees)", "Differential Cross Section(relative to Rutherford")
impots=twodplot(NeuStrongcs[:,0],NeuStrongcs[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with varied potentials","Angle (Degrees)", "Differential Cross Section(milibarns/rad)",leg="Strong Imaginary Potential")
twodplot(NeuWeakcs[:,0],NeuWeakcs[:,1],"Neutron-Nickel 58 Cross Section for 5 MeV with weak imaginary potential","Angle (Degrees)", "Differential Cross Section(relative to Rutherford",fig=impots,leg="Weak Imaginary Potential")
ims=twodplot(NeuStrongs[0],NeuStrongs[1],"Neutron-Nickel 58 SMatrix Moduli for 5 MeV","Angular Momentum", "SMatrix Moduli",leg="Strong Imaginary Potential")
twodplot(NeuWeaks[0],NeuWeaks[1],"Neutron-Nickel 58 SMatrix Moduli for 5 MeV with weak imaginary potential","Angular Momentum", "SMatrix Moduli",fig=ims,leg="Weak Imaginary Potential")

plt.show()
