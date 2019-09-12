import numpy as np
from Solution import*
g = 1
l = 1
m = 1


def analytic(theta0, omega0, step=0.1, stop=10, name="analytic"):
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
    return Solution(t, theta, omega, e, name=name)


def simple_euler(theta0, omega0, step=0.1, stop=10, start=0, name="simple_euler"):
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
    return Solution(t, theta, omega, e, name=name)


def euler_cromer(theta0, omega0, step=0.1, stop=10, start=0, name="euler_cromer"):
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
    return Solution(t, theta, omega, e, name=name)


def rk4(theta0, omega0, step=0.1, stop=10, start=0, name="runge_kutta"):
    def omega_prime(theta):
        """
        :return: derivative of omega with respect to time at some point theta
        """
        return -(g / l) * theta

    def theta_prime(omega):
        """
        :return: derivative of theta with respect to time at some point omega
        """
        return omega
    t = np.arange(start, stop, step)
    n = int((stop - start)/step)
    omega = np.zeros(n)
    theta = np.zeros(n)
    omega[0], theta[0] = omega0, theta0
    for i in range(n-1):
        # calculate next omega
        o1 = omega_prime(theta[i])
        o2 = omega_prime(theta[i] + o1 * step / 2)
        o3 = omega_prime(theta[i] + o2 * step / 2)
        o4 = omega_prime(theta[i] + o3 * step)
        omega[i + 1] = omega[i] + (step/6)*(o1 + 2*o2 + 2*o3 + o4)

        # calculate next theta
        t1 = theta_prime(omega[i])
        t2 = theta_prime(omega[i] + t1 * step / 2)
        t3 = theta_prime(omega[i] + t2 * step / 2)
        t4 = theta_prime(omega[i] + t3 * step)
        theta[i + 1] = theta[i] + (step/6)*(t1 + 2 * t2 + 2 * t3 + t4)

    # calculate energy
    e = 0.5*m*l*l*(omega**2 + (g/l)*theta**2)
    return Solution(t, theta, omega, e, name=name)