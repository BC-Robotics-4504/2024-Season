from .limelight import *
from .limelight_calcs import *

from components.config import RobotConfig
class Vision:
    RobotConfig: RobotConfig

    LimeLight: Limelight
    LimeLightFront: Limelight

    target_distance = 0.0
    horizontal_offset = 0.0
    vertical_offset = 0.0
    valid_target = False
    
    front_camera_active = False
    
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
    
    def enableFrontCamera(self):
        self.front_camera_active = True
        
    def disableFrontCamera(self):
        self.front_camera_active = False

    def execute(self):
        if not self.front_camera_active:
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
                
        else:
            
            self.valid_target = self.LimeLightFront.valid_targets
            if self.valid_target:
                self.LimeLightFront.light(LEDState.ON)
                self.target_distance = calc_distance(self.RobotConfig.front_camera_angle,
                                                    self.RobotConfig.front_camera_mount_height,
                                                    self.RobotConfig.front_apriltag_target_height,
                                                    self.LimeLightFront)
                
                self.horizontal_offset = self.LimeLightFront.horizontal_offset
                self.vertical_offset = self.LimeLightFront.vertical_offset  
            
            else:
                self.LimeLightFront.light(LEDState.OFF)
