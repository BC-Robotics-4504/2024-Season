import wpilib
from magicbot import MagicRobot
import math
import rev
import math

# from components.swerveDrive.swerveDrive import SwerveModule, SwerveDrive, SparkMaxTurning, SparkMaxDriving, DriveConfig
from components.hmi.hmi import HMI

class MyRobot(MagicRobot):
    ''' MagicRobot Framework
    REFERENCE: https://robotpy.readthedocs.io/en/stable/frameworks/magicbot.html
    '''
    
    # # Swerve Drive Component Code
    # DriveConfig: DriveConfig = DriveConfig(1.0, 1.0)
    # SwerveDrive: SwerveDrive
    # FrontLeft_SwerveModule: SwerveModule
    # FrontRight_SwerveModule: SwerveModule
    # RearLeft_SwerveModule: SwerveModule
    # RearRight_SwerveModule: SwerveModule
    
    # Controller Component Code
    HMI: HMI

    # Launcher Component Code

    # Climber Component Code    

    def createObjects(self):
        # Swerve Drive Hardware Config
        # self.FrontLeft_SwerveModule_angleMotor = SparkMaxTurning(6, inverted=False, gear_ratio=1, wheel_diameter=1,
        #                                                   absolute_encoder=True)
        # self.FrontLeft_SwerveModule_speedMotor = SparkMaxDriving(5, inverted=False, gear_ratio=1, wheel_diameter=1)

        # self.FrontRight_SwerveModule_angleMotor = SparkMaxTurning(4, inverted=True, gear_ratio=1, wheel_diameter=1,
        #                                                   absolute_encoder=True)
        # self.FrontRight_SwerveModule_speedMotor = SparkMaxDriving(3, inverted=False, gear_ratio=1, wheel_diameter=1)

        # self.RearLeft_SwerveModule_angleMotor = SparkMaxTurning(8, inverted=True, gear_ratio=1, wheel_diameter=1,
        #                                                   absolute_encoder=True)
        # self.RearLeft_SwerveModule_speedMotor = SparkMaxDriving(7, inverted=False, gear_ratio=1, wheel_diameter=1)

        # self.RearRight_SwerveModule_angleMotor = SparkMaxTurning(2, inverted=True, gear_ratio=1, wheel_diameter=1,
        #                                                   absolute_encoder=True)
        # self.RearRight_SwerveModule_speedMotor = SparkMaxDriving(1, inverted=False, gear_ratio=1, wheel_diameter=1)

        # Launcher Hardware Config

        # Climber Hardware Config

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(6, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(False)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(True)
        # self.encoder.setAverageDepth(1)
        # self.encoder.setZeroOffset(0)
        # self.encoder.setInverted(False)
        # self.encoder.setPositionConversionFactor(1.0)
        # self.encoder.setVelocityConversionFactor(1.0)
        self.SMcontroller.setFeedbackDevice(self.encoder)
        
        self.encoder.setPositionConversionFactor(1.0)
        self.encoder.setVelocityConversionFactor(1.0)
        self.SMcontroller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(-1) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(1) #TODO: does this need to be removed?
        
        # PID parameters
        self.SMcontroller.setP(1)
        self.SMcontroller.setI(0)
        self.SMcontroller.setD(0)
        self.SMcontroller.setIZone(0)
        self.SMcontroller.setFF(0)
        self.SMcontroller.setOutputRange(-1, 1)

        # # Smart Motion Parameters
        # self.SMcontroller.setSmartMotionMaxVelocity(5600, 0)
        # self.SMcontroller.setSmartMotionMinOutputVelocity(0, 0)
        # self.SMcontroller.setSmartMotionMaxAccel(2700, 0)
        # self.SMcontroller.setSmartMotionAllowedClosedLoopError(0.005, 0)
        
        #self.controller.burnFlash()    
        # self.clearFaults()

        # HMI Hardware Config
        self.HMI_xbox = wpilib.XboxController(0)
        pass

    def disabledPeriodic(self):
        pass

    def teleopInit(self):
        # Define relationships between controller input events and what they're supposed to trigger
        # DO NOT PUT LEFT X/Y or RIGHT X/Y here--those will have to be updated using polling
        # self.SwerveDrive.clearFaults()
        pass

    def teleopPeriodic(self):
        # 1.) Poll position of Left X/Y and Right X/Y from controller
        Lx, Ly, Rx, Ry = self.HMI.getAnalogSticks()

        if Rx < 0:
            Rx += 1
        print(f'{Rx:0.3}, {self.encoder.getPosition():0.3f}')
        self.SMcontroller.setReference(Rx, rev.CANSparkMax.ControlType.kPosition)
        # 2.) Move drivetrain based on Left X/Y and Right X/Y controller inputs
        # self.SwerveDrive.move(Lx, Ly, Rx)


if __name__ == "__main__":
    wpilib.run(MyRobot)