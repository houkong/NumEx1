import numpy as np
from Solution import*
g = 1
l = 1
m = 1

def analytic(theta0, omega0, step=0.1, stop=10):
    """
    :param theta0: initial value for theta
    :param omega0: initial value for omega
    :param step: time increment
    :param stop: terminal time value
    :return: solution object with time, theta, energy
    """
    O = np.sqrt(g/l)
    phi = np.arccos(omega0/(O*theta0))
    t = np.arange(0, stop, step)
    theta = theta0*np.sin(O*t + phi)
    omega = theta0*O*np.cos(O*t + phi)
    e = 0.5 * m * l * l * (omega ** 2 + (g / l) * theta ** 2)
    return Solution(time=t, theta=theta, energy=e,  name="analytic")

def simple_euler(theta0, omega0, step=0.1, stop=10, start=0):
    """
    :param theta0: initial value for theta
    :param omega0: initial value for omega
    :param step: time increment
    :param stop: terminal time value
    :param start: initial time value
    :return: solution object with time, theta, energy
    """
    t = np.arange(start, stop, step)
    n = int((stop - start)/step)
    omega = np.zeros(n)
    theta = np.zeros(n)
    omega[0], theta[0] = omega0, theta0
    for i in range(n - 1):
        omega[i + 1] = omega[i] - (g/l)*theta[i]*step
        theta[i + 1] = theta[i] + omega[i]*step

    e = 0.5*m*l*l*(omega**2 + (g/l)*theta**2)
    return Solution(time=t, theta=theta, energy=e, name="simple_euler")


def euler_cromer(theta0, omega0, step=0.1, stop=10, start=0):
    """
    :param theta0: initial value for theta
    :param omega0: initial value for omega
    :param step: time increment
    :param stop: terminal time value
    :param start: initial time value
    :return: solution object with time, theta, energy
    """
    t = np.arange(start, stop, step)
    n = int((stop - start)/step)
    omega = np.zeros(n)
    theta = np.zeros(n)
    omega[0], theta[0] = omega0, theta0
    for i in range(n - 1):
        omega[i + 1] = omega[i] - (g/l)*theta[i]*step
        theta[i + 1] = theta[i] + omega[i+1]*step
    e = 0.5*m*l*l*(omega**2 + (g/l)*theta**2)
    return Solution(time=t, theta=theta, energy=e, name="euler_cromer")

def runge_kutta(_):
    pass