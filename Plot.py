import matplotlib.pyplot as plt


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
        plt.show()

    def plot_t_energy(self):
        pass
