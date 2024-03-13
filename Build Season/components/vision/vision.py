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
    inRange = False
    
    def getTargetDistance(self):
        """getTargetDistance() -> float or None
        
        Get the distance to the target. If there is no target, return None."""
        if self.valid_target:
            return self.target_distance
        else:
            return None
        
    def getTargetHeight(self):
        """getTargetHeight() -> float or None
        
        Get the height of the target. If there is no target, return None."""
        if self.valid_target:
            return self.vertical_offset
        
    def getTargetAngle(self):
        """getTargetAngle() -> float or None
        
        Get the angle to the target. If there is no target, return None."""
        if self.valid_target:
            return self.horizontal_offset
        else:
            return None
        
    def getTargetID(self):
        """getTargetID() -> int or None
        
        Get the ID of the target. If there is no target, return None."""
        return self.valid_target
    
    def enableFrontCamera(self):
        """enableFrontCamera() -> None
        
        Enable the front LimeLight."""
        self.front_camera_active = True
        
    def disableFrontCamera(self):
        """disableFrontCamera() -> None
        
        Disable the front LimeLight."""
        self.front_camera_active = False
        
    def checkSpeakerRange(self):
        """checkSpeakerRange() -> None
        Check if the target is in range of the speakers. If it is, turn on the LimeLight LEDs. If it is not, turn off the LimeLight LED's."""
        
        if self.target_distance is None:
            return False
        
        if self.target_distance >= self.RobotConfig.min_target_range and self.target_distance <=self.RobotConfig.max_target_range:
            self.LimeLight.light(LEDState.ON)
            self.LimeLightFront.light(LEDState.ON)
            self.inRange = True

        else:
            self.LimeLight.light(LEDState.OFF)
            self.LimeLightFront.light(LEDState.OFF)
            self.inRange = True        

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
                
                self.checkSpeakerRange()
                

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