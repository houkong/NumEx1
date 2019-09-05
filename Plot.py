import matplotlib.pyplot as plt


class Plot:
    def __init__(self, Data):
        '''
        :param Data: data of type Solution
        '''
        self.Data = Data


    def theta_energy(self, title=""):
        f, ax1 = plt.subplots()
        color = 'tab:red'
        ax1.set_xlabel('time (s)')
        ax1.set_ylabel('theta [radians]', color=color)
        ax1.plot(self.Data.time, self.Data.theta, color = color)
        ax1.tick_params(axis='y', labelcolor=color)
        ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
        color = 'tab:blue'
        ax2.set_ylabel('Energy [J]', color=color)
        ax2.plot(self.Data.time, self.Data.energy, color=color)
        ax2.tick_params(axis='y', labelcolor=color)
        ax1.set_title(title)
        plt.show()

    def theta(self):
        plt.plot(self.Data.time, self.Data.theta)
        plt.xlabel('time (s)')
        plt.ylabel('theta [radians]')
        plt.show()

    def energy(self):
        pass
