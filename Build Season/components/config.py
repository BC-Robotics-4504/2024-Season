from dataclasses import dataclass  # * Why do we need this import statement?

# Drivetrain configuration parameters
@dataclass
class RobotConfig:
    """Drivetrain Configuration
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    """

    # Robot Geometry Parameters
    chasis_length: float = 1.0
    chasis_width: float = 1.0

    # Swerve Drive Parameters
    speed_clamp: float = 0.25

    # Launcher Parameters
    shooting_flywheel_speed: float = 0.25
    intake_forward_rolling_speed: float = 0.1
    intake_reverse_rolling_speed: float = -0.1
    intake_lowered_position: float = 0.15
    intake_raised_position: float = 0.0
