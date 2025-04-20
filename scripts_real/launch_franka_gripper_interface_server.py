import zerorpc
from polymetis import GripperInterface
import scipy.spatial.transform as st
import numpy as np
import torch

class FrankaGripperInterface:
    def __init__(self):
        self.robot = GripperInterface()

    def get_state(self):
        return self.robot.get_state()
    
    def goto(self, width=0.08, speed=0.05, force=10.0, blocking=False):
        self.robot.goto(width=width, speed=speed, force=force, blocking=blocking)

# if __name__ == "__main__":
#     robot =  FrankaGripperInterface() 
#     print(robot.get_joint_positions())

s = zerorpc.Server(FrankaGripperInterface())
s.bind("tcp://0.0.0.0:4241")
s.run()