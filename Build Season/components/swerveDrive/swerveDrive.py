import math
from dataclasses import dataclass  # * Why do we need this import statement?

import rev

# Drivetrain configuration parameters
@dataclass
class DriveConfig:
    """Drivetrain Configuration
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    """

    chasis_length: float
    chasis_width: float
    speed_clamp: float = 0.1

    @property
    def ratio(self):
        return math.hypot(self.chasis_length, self.chasis_width)

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 5e-5
    kI = 1e-6
    kD = 0
    kIz = 0
    kFF = 0.000156
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
         
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.controller = self.motor.getPIDController()
        self.controller.setFeedbackDevice(self.encoder)
        
        self.encoder.setPositionConversionFactor(1.0)
        self.encoder.setVelocityConversionFactor(1.0)
        self.encoder.setInverted(inverted)
        self.controller.setPositionPIDWrappingEnabled(True)
        self.controller.setPositionPIDWrappingMinInput(0.0)
        self.controller.setPositionPIDWrappingMaxInput(2*math.pi)
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        self.motor.setSmartCurrentLimit(40)
        
        #self.controller.burnFlash()    

        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        self.controller.setReference(position, rev.CANSparkMax.ControlType.kDutyCycle)
        return False
    
    def getAbsPosition(self):
        rotation = self.encoder.getPosition()
        return rotation

class SparkMaxDriving:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 5e-5
    kI = 1e-6
    kD = 0
    kIz = 0
    kFF = 0.000156
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
         
        self.encoder = self.motor.getEncoder()
        self.controller = self.motor.getPIDController()
        self.controller.setFeedbackDevice(self.encoder)
        
        self.encoder.setPositionConversionFactor(1.0)
        self.encoder.setVelocityConversionFactor(1.0)
        
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kCoast)
        self.motor.setSmartCurrentLimit(40)
        
        #self.controller.burnFlash()    

        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def getSpeed(self):
        vel = -self.encoder.getVelocity()  # rpm
        return vel

    def setSpeed(self, speed):
        self.motor.set(speed)
        return None
        
        
        
class SwerveModule:
    angleMotor: SparkMaxTurning
    speedMotor: SparkMaxDriving


    def __init__(self):
        self.target_angle = 0
        self.target_speed = 0

        self.target_distance = 0
        self.tolerance = 0.001

        self.auto_lockout = 0
    
    def clearFaults(self):
        self.angleMotor.clearFaults()
        self.speedMotor.clearFaults()
        return False

    def getSpeedAngle(self):
        angle = self.angleMotor.getAbsPosition()
        speed = self.speedMotor.getSpeed()
        return speed, angle

    def move(self, speed, angle):
        self.target_speed = speed
        self.target_angle = angle
        return False
    
    def execute(self):
        #print(f'speed:{self.target_speed}    angle:{self.target_angle}')
        self.angleMotor.setAbsPosition(self.target_angle)
        self.speedMotor.setSpeed(self.target_speed) 
        speed, angle = self.getSpeedAngle()
        print(speed, angle)
               


class SwerveDrive:
    DriveConfig: DriveConfig
    FrontLeft_SwerveModule: SwerveModule
    FrontRight_SwerveModule: SwerveModule
    RearLeft_SwerveModule: SwerveModule
    RearRight_SwerveModule: SwerveModule

    front_left_speed: float = 0
    front_left_angle: float = 0
    front_right_speed: float = 0
    front_right_angle: float = 0
    rear_left_speed: float = 0
    rear_left_angle: float = 0
    rear_right_speed: float = 0
    rear_right_angle: float = 0

    movement_changed: bool = False

    # @staticmethod
    def __calcAngleSpeed__(self, front_rear, right_left):
        """
        :param front_rear:
        :param right_left:
        :returns:
        """
        speed = math.hypot(front_rear, right_left)
        angle = math.atan2(front_rear, right_left)
        return speed, angle

    # @property
    def isMoveChanged(self):
        return self.move_changed
    
    def clearFaults(self):
        self.RearLeft_SwerveModule.clearFaults()
        self.RearRight_SwerveModule.clearFaults()
        self.FrontLeft_SwerveModule.clearFaults()
        self.FrontRight_SwerveModule.clearFaults()
        return False

    def move(self, Lx, Ly, Rx, Ry, rateLimit = False): 
        """
        :param front_rear:
        :param right_left:
        :returns:
        """
        strafe = Lx
        fwd = Ly
        rcw = Rx

        # translationDir = math.atan2(Ly, Lx)
        # translationMag = math.sqrt(math.pow(Lx, 2) + math.pow(Ly, 2))
        # directionSlewRate:
        # if (translationMag != 0.0): directionSlewRate = math.abs(driveConstants.kDirectionSlewRate / translationMag):
        # else:
        #     directionSlewRate = 500.0
        
        # currentTime = WPIUtilJNI.now() * 1e-6
        # elapsedTime = currentTime - prevTime
        
        
        
            
        
        
        
        # FIXME: check the logic, how to unit test(potentualy) 

        frontX = strafe - rcw * self.DriveConfig.chasis_length / self.DriveConfig.ratio
        rearX = strafe + rcw * self.DriveConfig.chasis_length / self.DriveConfig.ratio
        leftY = fwd - rcw * self.DriveConfig.chasis_width / self.DriveConfig.ratio
        rightY = fwd + rcw * self.DriveConfig.chasis_width / self.DriveConfig.ratio

        self.front_left_speed, self.front_left_angle = self.__calcAngleSpeed__(frontX, leftY)
        self.front_right_speed, self.front_right_angle = self.__calcAngleSpeed__(frontX, rightY)
        self.rear_left_speed, self.rear_left_angle = self.__calcAngleSpeed__(rearX, leftY)
        self.rear_right_speed, self.rear_right_angle = self.__calcAngleSpeed__(rearX, rightY)
        self.move_changed = True
        return False


    def execute(self):
        if self.isMoveChanged():
            self.FrontLeft_SwerveModule.move(
                self.DriveConfig.speed_clamp*self.front_left_speed, self.front_left_angle
            )
            self.FrontRight_SwerveModule.move(
                self.DriveConfig.speed_clamp*self.front_right_speed, self.front_right_angle
            )
            self.RearLeft_SwerveModule.move(
                self.DriveConfig.speed_clamp*self.rear_left_speed, self.rear_left_angle
            )
            self.RearRight_SwerveModule.move(
                self.DriveConfig.speed_clamp*self.rear_right_speed, self.rear_right_angle
            )
            self.move_changed = False