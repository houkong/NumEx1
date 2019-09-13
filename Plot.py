import matplotlib.pyplot as plt
import matplotlib
import os
from matplotlib.pyplot import figure
figure(num=None, figsize=(8,8), dpi=80, facecolor='w', edgecolor='k')
font = {'size'   : 22}
matplotlib.rc('font', **font)

SHOW = False
WIDTH = 4


class Plot:
    def __init__(self, element=None):
        self.data = []
        self.title = None
        if element:
            self.add(element)

    def __add__(self, other):
        for i in range(other.size()):
            self.add(other.data[i])
        return self

    def add(self, element):
        self.data.append(element)

    def size(self):
        return len(self.data)

    def plot_t_theta(self):
        for i in range(self.size()):
            data_i = self.data[i]
            assert len(data_i.time) == len(data_i.theta)
            plt.plot(data_i.time, data_i.theta, label=data_i.name, linewidth=WIDTH)
        plt.xlabel('time [s]')
        plt.ylabel('theta [radians]')
        plt.legend()
        if self.title:
            plt.title(self.title)
        if not os.path.exists("plots"):
            os.mkdir("plots")
        path = "plots/t_theta_" + self.title if self.title else "plots/t_theta.png"
        plt.tight_layout()
        plt.savefig(path)
        if SHOW:
            plt.show()
        else:
            plt.clf()

    def plot_t_energy(self):
        for i in range(self.size()):
            data_i = self.data[i]
            assert len(data_i.time) == len(data_i.energy)
            plt.plot(data_i.time, data_i.energy, label=data_i.name, linewidth=WIDTH)
        plt.xlabel('time [s]')
        plt.ylabel('energy [J]')
        plt.legend()
        if self.title:
            plt.title(self.title)
        if not os.path.exists("plots"):
            os.mkdir("plots")
        path = "plots/t_energy_" + self.title if self.title else "plots/t_energy.png"
        plt.tight_layout()
        plt.savefig(path)
        if SHOW:
            plt.show()
        else:
            plt.clf()

    def plot_theta_omega(self): # phase space plot
        for i in range(self.size()):
            data_i = self.data[i]
            assert len(data_i.theta) == len(data_i.omega)
            plt.plot(data_i.theta, data_i.omega, label=data_i.name, linewidth=WIDTH)
        plt.xlabel('theta [radians]')
        plt.ylabel('omega [radians/s]')
        plt.legend()
        if self.title:
            plt.title(self.title)
        if not os.path.exists("plots"):
            os.mkdir("plots")
        path = "plots/theta_omega_" + self.title if self.title else "plots/theta_omega.png"
        plt.tight_layout()
        plt.savefig(path)
        if SHOW:
            plt.show()
        else:
            plt.clf()