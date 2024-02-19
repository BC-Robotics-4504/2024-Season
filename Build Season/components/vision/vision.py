from .limelight import *
from .limelight_calcs import *

from components.config import RobotConfig
class Vision:
    RobotConfig: RobotConfig

    limelight: Limelight

    target_distance = 0.0
    horizontal_offset = 0.0
    vertical_offset = 0.0

    def getPoise(self):
        return self.target_distance, self.horizontal_offset, self.vertical_offset

    def execute(self):

        # Check if targets exist in frame
        if self.limelight.valid_targets:
            self.target_distance = calc_distance(self.RobotConfig.camera_angle,
                                                 self.RobotConfig.camera_mount_height,
                                                 self.RobotConfig.apriltag_target_height,
                                                 self.limelight)
            
            self.horizontal_offset = self.limelight.horizontal_offset()
            self.vertical_offset = self.limelight.vertical_offset()

