import matplotlib.pyplot as plt
import os


class Plot:
    def __init__(self, element=None):
        self.data = []
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
            plt.plot(data_i.time, data_i.theta, label=data_i.name)
        plt.xlabel('time [s]')
        plt.ylabel('theta [radians]')
        plt.legend()
        if not os.path.exists("plots"):
            os.mkdir("plots")
        plt.savefig("plots/t_theta.png")
        plt.show()

    def plot_t_energy(self):
        for i in range(self.size()):
            data_i = self.data[i]
            plt.plot(data_i.time, data_i.energy, label=data_i.name)
        plt.xlabel('time [s]')
        plt.ylabel('energy [J]')
        plt.legend()
        if not os.path.exists("plots"):
            os.mkdir("plots")
        plt.savefig("plots/t_energy.png")
        plt.show()

    def plot_theta_omega(self): # phase space plot
        for i in range(self.size()):
            data_i = self.data[i]
            plt.plot(data_i.theta, data_i.omega, label=data_i.name)
        plt.xlabel('theta [radians]')
        plt.ylabel('omega [radians/s]')
        plt.legend()
        if not os.path.exists("plots"):
            os.mkdir("plots")
        plt.savefig("plots/theta_omega.png")
        plt.show()

