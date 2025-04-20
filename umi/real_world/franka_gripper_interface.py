import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(ROOT_DIR)
os.chdir(ROOT_DIR)

import numpy as np
import zerorpc

class FrankaGripperInterface:
    def __init__(self, ip='183.173.65.137', port=4241):
        self.server = zerorpc.Client(heartbeat=20)
        self.server.connect(f"tcp://{ip}:{port}")

    def get_state(self):
        state = self.server.get_state()
        return state
    
    def goto(self, width=0.08, speed=0.05, force=10.0, blocking=False):
        self.server.goto(width=width, speed=speed, force=force, blocking=blocking)


if __name__ == "__main__":
    robot = FrankaGripperInterface(ip='183.173.65.137', port=4241)
    print(robot.get_state())

    # robot.goto(width=0.08, speed=0.05, force=10.0, blocking=True)