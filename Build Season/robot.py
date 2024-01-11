import wpilib
import rev
from magicbot import MagicRobot
from networktables import NetworkTables

import swerveDrive.swervedrive
import swervemodule


# Get the config preset from the swervemodule
ModuleConfig = swervemodule.ModuleConfig


class MyRobot(MagicRobot):
    """
    After creating low-level components like "shooter", use component's name and an underscore

    e.g.
    Using variable annotation like "shooter_beltMotor: ctre.WPI_VictorSPX" decleares the type of the variable.
    When beltMotor is called from the shooter component, it's going to be a VictorSPX object.

    Using equal sign for variable decleration like "shooter_beltMotor = ctre.WPI_VictorSPX(11)" creates the actual object.
    When beltMotor is called from the shooter component, it's going to be a VictorSPX at the can port 11.

    Use the equal sign (mostly) in the #createObjects function, so they can be correctly injected to their parent components.

    For more info refer to https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    """

    # Create low-level object
    drive: swervedrive.SwerveDrive

    frontLeftModule: swervemodule.SwerveModule
    frontRightModule: swervemodule.SwerveModule
    rearLeftModule: swervemodule.SwerveModule
    rearRightModule: swervemodule.SwerveModule

    # Create configs for each module. This is before #createObjects because modules need these configs to be
    # initialized.
    frontLeftModule_cfg = ModuleConfig(
        sd_prefix="FrontLeft_Module", zero=2.97, inverted=True, allow_reverse=True
    )
    frontRightModule_cfg = ModuleConfig(
        sd_prefix="FrontRight_Module", zero=2.69, inverted=False, allow_reverse=True
    )
    rearLeftModule_cfg = ModuleConfig(
        sd_prefix="RearLeft_Module", zero=0.18, inverted=True, allow_reverse=True
    )
    rearRightModule_cfg = ModuleConfig(
        sd_prefix="RearRight_Module", zero=4.76, inverted=False, allow_reverse=True
    )

    # Declare motors for the shooter component

    # *Still need to be created

    # Create common components

    # *Still need to be created

    def createObjects(self):
        """
        This is where all the components are actually created with "=" sign.
        Components with a parent prefix like "shooter_" will be injected.
        """
        # SmartDashboard
        self.sd = NetworkTables.getTable("SmartDashboard")

        # Gamepad
        self.xbox = wpilib.XboxController(0)

        # Drive Motors
        self.frontLeftModule_driveMotor = rev.CANSparkMax(
            deviceID=1, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.frontRightModule_driveMotor = rev.CANSparkMax(
            deviceID=3, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.rearLeftModule_driveMotor = rev.CANSparkMax(
            deviceID=5, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.rearRightModule_driveMotor = rev.CANSparkMax(
            deviceID=7, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )

        # Rotate Motors
        self.frontLeftModule_rotateMotor = rev.CANSparkMax(
            deviceID=2, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.frontRightModule_rotateMotor = rev.CANSparkMax(
            deviceID=4, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.rearLeftModule_rotateMotor = rev.CANSparkMax(
            deviceID=6, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )
        self.rearRightModule_rotateMotor = rev.CANSparkMax(
            deviceID=8, type=rev.CANSparkLowLevel.MotorType.kBrushless
        )

        # ! Encoders (Probably needs fixed) and/or is not needed
        self.frontLeftModule_encoder = wpilib.AnalogInput(0)
        self.frontRightModule_encoder = wpilib.AnalogInput(3)
        self.rearLeftModule_encoder = wpilib.AnalogInput(1)
        self.rearRightModule_encoder = wpilib.AnalogInput(2)

        # Limit Switch
        self.switch = wpilib.DigitalInput(0)

        # # PDP #? Not sure if this is right
        self.pdp = wpilib.PowerDistribution(
            module=9, moduleType=wpilib.PowerDistribution.ModuleType.kRev
        )

    def disabledPeriodic(self):
        # Update the dashboard, even when the robot is disabled.
        self.update_sd()

    # def autonomousInit(self):
    #     # Reset the drive when the auto starts.
    #     self.drive.flush()
    #     self.drive.threshold_input_vectors = True

    # def autonomous(self):
    #     # For auto, use MagicBot's auto mode.
    #     # This will load the ./autonomous folder.
    #     super().autonomous()

    def teleopInit(self):
        # Reset the drive when the teleop starts.
        self.drive.flush()
        self.drive.squared_inputs = True
        self.drive.threshold_input_vectors = True

    def move(self, x, y, rcw):
        """
        This function is ment to be used by the teleOp.
        :param x: Velocity in x-axis [-1, 1]
        :param y: Velocity in y-axis [-1, 1]
        :param rcw: Velocity in z axis [-1, 1]
        """

        if self.xbox.getLeftBumper():
            # If the button is pressed, lower the rotate speed.
            rcw *= 0.7

        self.drive.move(x, y, rcw)

    def teleopPeriodic(self):
        # Drive
        self.move(
            self.xbox.getRawAxis(5),  # Right stick Y-axis
            self.xbox.getRawAxis(4),  # Right stick X-axis
            self.xbox.getRawAxis(0),  # Left stick X-axis
        )

        # Lock
        if self.xbox.getRawButton(1):  # A button
            self.drive.request_wheel_lock = True

        # Vectoral Button Drive
        if self.xbox.getRawAxis(1) < 0:  # Left stick up
            self.drive.set_raw_fwd(-0.35)
        elif self.xbox.getRawAxis(1) > 0:  # Left stick down
            self.drive.set_raw_fwd(0.35)
        elif self.xbox.getRawAxis(0) > 0:  # Left stick right
            self.drive.set_raw_strafe(0.35)
        elif self.xbox.getRawAxis(0) < 0:  # Left stick left
            self.drive.set_raw_strafe(-0.35)

    # def update_sd(self):
    #     """
    #     Calls each component's own update function
    #     and puts data to the smartdashboard.
    #     """
    #     self.sd.putNumber("Climb_Current_Draw", self.pdp.getCurrent(10))

    #     self.drive.update_smartdash()
    #     # self.colorSensor.updateSD()  # Decleare motors for the shooter component


if __name__ == "__main__":
    wpilib.run(MyRobot)
