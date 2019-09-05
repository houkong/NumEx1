from solvers import*
from Plot import*

_simple_euler = simple_euler(0.2, 0, step=0.01)
_euler_cromer = euler_cromer(0.2, 0, step=0.01)
_analytic = analytic(0.2, 0, step=0.01)
_runge_kutta = runge_kutta(_)



Plot(_simple_euler).theta_energy()
Plot(_euler_cromer).theta_energy()
Plot(_analytic).theta()