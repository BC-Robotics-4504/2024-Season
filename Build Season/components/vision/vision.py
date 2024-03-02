from .limelight import *
from .limelight_calcs import *

from components.config import RobotConfig
class Vision:
    RobotConfig: RobotConfig

    LimeLight: Limelight

    target_distance = 0.0
    horizontal_offset = 0.0
    vertical_offset = 0.0
    valid_target = False
    
    def getTargetDistance(self):
        if self.valid_target:
            return self.target_distance
        else:
            return None
        
    def getTargetHeight(self):
        if self.valid_target:
            return self.vertical_offset
        
    def getTargetAngle(self):
        if self.valid_target:
            return self.horizontal_offset
        else:
            return None
        
    def getTargetID(self):
        return self.valid_target

    def execute(self):
        self.valid_target = self.LimeLight.valid_targets
        if self.valid_target:
            self.LimeLight.light(LEDState.ON)
            self.target_distance = calc_distance(self.RobotConfig.camera_angle,
                                                 self.RobotConfig.camera_mount_height,
                                                 self.RobotConfig.apriltag_target_height,
                                                 self.LimeLight)
            
            self.horizontal_offset = self.LimeLight.horizontal_offset
            self.vertical_offset = self.LimeLight.vertical_offset
            
        else:
            self.LimeLight.light(LEDState.OFF)

