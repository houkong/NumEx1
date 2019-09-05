from solvers import*
from Plot import*


THETA0 = 0.2
OMEGA0 = 0
STEP = 0.1

_simple_euler = simple_euler(THETA0, OMEGA0, step=STEP)
_euler_cromer = euler_cromer(THETA0, OMEGA0, step=STEP)
_analytic = analytic(THETA0, OMEGA0, step=STEP)

plot = Plot(_simple_euler) + Plot(_euler_cromer) + Plot(_analytic)
plot.plot_t_theta()
plot.plot_t_energy()
plot.plot_theta_omega()