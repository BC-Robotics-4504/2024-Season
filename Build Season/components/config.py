from dataclasses import dataclass  # * Why do we need this import statement?

# Drivetrain configuration parameters
@dataclass
class RobotConfig:
    """Drivetrain Configuration
    Custom class for configuring values that are repeatedly in the robot code
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    """

    # Targeting Distance
    max_target_range: float = 3.37
    min_target_range: float = 2.60

    # Robot Geometry Parameters
    chassis_length: float = 0.7366 # 29 in to m
    chassis_width: float = 0.7366 # 29 in to m

    # Swerve Drive Parameters
    speed_clamp: float = 0.65
    max_driving_speed = 5000 #rpm
    max_angular_speed = 600 #rpm
    movement_deadzone = 0.02
    drive_wheel_diameter: float = 0.114 #m

    # Launcher Parameters
    shooting_flywheel_speed: float = 1.0
    shooting_flywheel_threshold_speed: float = 550.0
    shooting_flywheel_tolerance = 3.0
    shooting_abort_delay = 2.0
    
    shooting_max_distance: float = 10.0
    intake_forward_rolling_speed: float = 0.2
    intake_reverse_rolling_speed: float = -0.2
    intake_feed_speaker_speed: float = 0.35
    intake_feed_delay: float = 0.5
    
    intake_lowered_position: float = 0.58
    intake_raised_position: float = 1.32
    intake_tolerance: float = 0.03
    intake_amp_position: float = 1.09
    intake_amp_shooting_speed: float = 0.24
    intake_launch_rolling_speed: float = 1.0
    

    # Climber Parameters
    climbing_m_per_rot: float = (0.039878/25)
    climbing_max_distance: float = 0.0254
    climbing_min_distance: float = 0
    climber_position_raised: float = 0
    climber_position_low: float = 0.135 # Meters
    climber_position_locked : float = 0.17 # Meters

    # Vision Parameters
    camera_angle: float = 0
    camera_mount_height: float = 0.25
    apriltag_target_height: float = 1.25
    
    front_camera_angle: float = 0
    front_camera_mount_height: float = 0.25
    front_apriltag_target_height: float = 1.25
    
    
