class Solution:
    def __init__(self, time, theta = None, energy = None):
        self.time = time
        self.theta = theta
        self.energy = energy
    
    def __call__(self, theta = None, energy = None):
