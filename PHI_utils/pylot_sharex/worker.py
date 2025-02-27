import numpy as np
import matplotlib.pyplot as plt
import warnings
# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/shared_axis_demo.html


warnings.filterwarnings("ignore") # no idea does not work. Do python -W "ignore" xxx.py

if __name__ == "__main__":

    wb97x = {"excitation_energy": [np.loadtxt("defect/struct1/wb97x/excitation_energy.dat"),
                                  np.loadtxt("defect/struct2/wb97x/excitation_energy.dat"),
                                  np.loadtxt("defect/struct3/wb97x/excitation_energy.dat")],
            "oscillator_strength": [np.loadtxt("defect/struct1/wb97x/oscillator_strength.dat"),
                                    np.loadtxt("defect/struct2/wb97x/oscillator_strength.dat"),
                                    np.loadtxt("defect/struct3/wb97x/oscillator_strength.dat")]}

    # nstates = 50
    for i in range(len(wb97x["excitation_energy"])):
        wb97x["excitation_energy"][i] = np.concatenate((wb97x["excitation_energy"][i], [3.5]))
    for i in range(len(wb97x["oscillator_strength"])):
        wb97x["oscillator_strength"][i] = np.concatenate((wb97x["oscillator_strength"][i], [0.]))


    ## wb97x
    ax1 = plt.subplot(311)
    plt.stem(wb97x["excitation_energy"][0], wb97x["oscillator_strength"][0], basefmt=" ", linefmt="-,m", markerfmt='')
    plt.tick_params('x', labelbottom=False)
    plt.ylim((0,0.2))
    plt.yticks(fontsize=14)
    plt.legend(['struct1\n$\omega$b97x'])

    ax2 = plt.subplot(312,sharex=ax1)
    plt.stem(wb97x["excitation_energy"][1], wb97x["oscillator_strength"][1], basefmt=' ',linefmt='--,b',markerfmt='')
    plt.tick_params('x',labelbottom=False)
    plt.ylabel("Oscillator strength [a.u.]", fontsize=16)
    plt.ylim((0,0.2))
    plt.yticks(fontsize=14)
    plt.legend([r'$\omega$b97x \nstruct2'])

    ax3 = plt.subplot(313,sharex=ax1)
    plt.stem(wb97x["excitation_energy"][2], wb97x["oscillator_strength"][2], basefmt=' ',linefmt=':,g',markerfmt='')
    plt.tick_params('x',labelbottom=True)
    plt.xlabel("Excitation energy [eV]", fontsize=16)
    plt.yticks(fontsize=14)
    plt.xticks(fontsize=14)
    plt.ylim((0,0.2))
    plt.legend([r'$\omega$b97x \nstruct3'])

    plt.tight_layout()
    # plt.savefig("KPHI_monolayer_withoutwater_defected_stem_wb97x.svg")
    plt.show()

