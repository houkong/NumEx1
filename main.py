from solvers import*
from Plot import*

_simple_euler = simple_euler(0.2, 0, step=0.01)
_analytic = analytic(0.2, 0, step=0.01)



Plot(_simple_euler).theta_energy()
Plot(_analytic).theta()