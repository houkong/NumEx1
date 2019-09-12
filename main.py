from solvers import*
from Plot import*


THETA0 = 0.2
OMEGA0 = 0
START = 0
STOP = 10
STEP = 0.1


_simple_euler = simple_euler(THETA0, OMEGA0, start=START, stop=STOP, step=STEP)
_euler_cromer = euler_cromer(THETA0, OMEGA0, start=START, stop=STOP, step=STEP)
_analytic = analytic(THETA0, OMEGA0, stop=STOP, step=STEP)
_runge_kutta = rk4(THETA0, OMEGA0, start=START, stop=STOP, step=STEP)


plot = Plot(_simple_euler) + Plot(_euler_cromer) + Plot(_analytic) + Plot(_runge_kutta)
plot.title = "t-theta"
plot.plot_t_theta()
plot.title = "t-energy"
plot.plot_t_energy()
plot.title = "theta_omega"
plot.plot_theta_omega()

_1 = simple_euler(THETA0, OMEGA0, step=0.5, name="STEP=0.5")
_2 = simple_euler(THETA0, OMEGA0, step=0.1, name="STEP=0.1")
_3 = simple_euler(THETA0, OMEGA0, step=0.05, name="STEP=0.05")
plot2 = Plot(_1) + Plot(_2) + Plot(_3)
plot2.title = "Numerical solutions using runge-kutta4"
plot2.plot_theta_omega()