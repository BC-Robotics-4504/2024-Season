from dataclasses import dataclass  # * Why do we need this import statement?

# Drivetrain configuration parameters
@dataclass
class RobotConfig:
    """Drivetrain Configuration
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    """

    # Robot Geometry Parameters
    chassis_length: float = 0.7366 # 29 in to m
    chassis_width: float = 0.7366 # 29 in to m

    # Swerve Drive Parameters
    speed_clamp: float = 0.25

    # Launcher Parameters
    shooting_flywheel_speed: float = 1.0
    shooting_flywheel_threshold_speed: float = 540.0
    shooting_flywheel_tolerance = 3.0
    
    shooting_max_distance: float = 10.0
    intake_forward_rolling_speed: float = 0.2
    intake_reverse_rolling_speed: float = -0.2
    intake_feed_speaker_speed: float = 0.35
    intake_feed_delay: float = 1.0
    
    
    intake_lowered_position: float = 0.58
    intake_raised_position: float = 1.3
    intake_tolerance: float = 0.03
    intake_amp_position: float = 1.1
    intake_amp_shooting_speed: float = 0.35
    intake_launch_rolling_speed: float = 1.0
    

    # Climber Parameters
    climbing_max_distance: float = 0.5

    # Vision Parameters
    camera_angle: float = 0.0
    camera_mount_height: float = 0.0
    apriltag_target_height: float = 0.0
    
    
