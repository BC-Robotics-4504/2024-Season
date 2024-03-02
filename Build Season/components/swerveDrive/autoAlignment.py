from enum import Enum
import math

from wpimath.controller import PIDController

from components.swerveDrive.swerveDrive import SwerveDrive
from components.launcher.launcher import Launcher
from components.vision.vision import Vision
from components.config import RobotConfig

class AutoAlignment:
    
    Kp = 1e-4
    Ki = 0
    Kd = 0

    RobotConfig: RobotConfig
    Vision: Vision
    SwerveDrive: SwerveDrive
    
    controller = PIDController(Kp, Ki, Kd)
    
    do_alignment = False
    
    setpoint_found = False
    
    def __init__(self):
        self.controller.setSetpoint(0.0)
        
    def align(self):
        self.do_alignment = True
        return None

    def pidIteration(self):
        target_angle = self.Vision.getTargetAngle()
        pid_output = self.controller.calculate(target_angle)/360*2*math.pi
        
        if self.controller.atSetpoint():
            return True

        self.SwerveDrive.goDistance(0, 0, pid_output)
        return False
        
    def execute(self):
        if self.do_alignment and self.Vision.valid_target:
            self.pidIteration()
            self.do_alignment = False