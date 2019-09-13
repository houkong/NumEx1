from solvers import*
from Plot import*


THETA0 = 0.2
OMEGA0 = 0
START = 0
STOP = 20
STEP = 0.1


def format_name(step):
    return "∆t = " + str(step) + "s"


_simple_euler1 = Plot(simple_euler(THETA0, OMEGA0, start=START, stop=STOP, step=0.02, name=format_name(0.02)))
_simple_euler2 = Plot(simple_euler(THETA0, OMEGA0, start=START, stop=STOP, step=0.2, name=format_name(0.2)))
_simple_euler3 = Plot(simple_euler(THETA0, OMEGA0, start=START, stop=STOP, step=0.4, name=format_name(0.4)))
_analytic = Plot(analytic(THETA0, OMEGA0, stop=STOP, step=STEP))

plot1 = _simple_euler1 + _simple_euler2 + _simple_euler3 + _analytic
plot1.title = "simple_euler"
plot1.plot_t_theta()
plot1.plot_t_energy()


_simple_euler = Plot(simple_euler(THETA0, OMEGA0, start=START, stop=STOP, step=STEP))
_euler_cromer = Plot(euler_cromer(THETA0, OMEGA0, start=START, stop=STOP, step=STEP))
_analytic = Plot(analytic(THETA0, OMEGA0, stop=STOP, step=STEP))
_runge_kutta = Plot(rk4(THETA0, OMEGA0, start=START, stop=STOP, step=STEP))

plot2 = _simple_euler + _euler_cromer + _analytic + _runge_kutta
plot2.title = "num_met"
plot2.plot_t_theta()
plot2.plot_t_energy()
plot2.plot_theta_omega()


_runge_kutta1 = Plot(rk4(THETA0, OMEGA0, start=START, stop=STOP, step=0.1, name=format_name(0.1)))
_runge_kutta2 = Plot(rk4(THETA0, OMEGA0, start=START, stop=STOP, step=0.01, name=format_name(0.01)))
_runge_kutta3 = Plot(rk4(THETA0, OMEGA0, start=START, stop=STOP, step=0.04, name=format_name(0.04)))
_analytic = Plot(analytic(THETA0, OMEGA0, stop=STOP, step=STEP))

plot3 = _runge_kutta1 + _runge_kutta2 + _runge_kutta3 + _analytic
plot3.title = "rk4"
plot3.plot_t_theta()

_euler_cromer1 = Plot(euler_cromer(THETA0, OMEGA0, start=START, stop=STOP, step=0.2, name=format_name(0.2)))
_euler_cromer2 = Plot(euler_cromer(THETA0, OMEGA0, start=START, stop=STOP, step=0.8, name=format_name(0.8)))
_euler_cromer3 = Plot(euler_cromer(THETA0, OMEGA0, start=START, stop=STOP, step=1, name=format_name(1)))
_analytic = Plot(analytic(THETA0, OMEGA0, stop=STOP, step=STEP))


plot4 = _euler_cromer1 + _euler_cromer2 + _euler_cromer3 + _analytic
plot4.title = "euler_cromer"
plot4.plot_t_theta()