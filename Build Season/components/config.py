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
    shooting_flywheel_speed: float = 0.25
    intake_forward_rolling_speed: float = 0.1
    intake_reverse_rolling_speed: float = -0.1
    intake_lowered_position: float = 0.15
    intake_raised_position: float = 0.0

    # Climber Parameters
    climbing_max_distance: float = 0.5

    # Vision Parameters
    camera_angle: float = 0.0
    camera_mount_height: float = 0.0
    apriltag_target_height: float = 0.0
    
