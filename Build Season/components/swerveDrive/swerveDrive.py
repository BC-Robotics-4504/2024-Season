import math
from dataclasses import dataclass

import rev

# Drivetrain configuration parameters
@dataclass
class DriveConfig:
    ''' Drivetrain Configuration
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    REFERENCE: https://docs.python.org/3/library/dataclasses.html
    '''
    chasis_length: float
    chasis_width: float

    @property
    def ratio(self):
        return math.hypot(self.chasis_length, self.chasis_width)

class SparkMax:
    ''' Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    '''
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

    def __init__(self, canID, motorType="brushless", inverted=False, gear_ratio=1, wheel_diameter=1,
                 absolute_encoder=False):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.motorType = motorType
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter

        if motorType == "brushless":
            mtype = rev.CANSparkMax.MotorType.kBrushless
        else:
            mtype = rev.CANSparkMax.MotorType.kBrushed  # FIXME!: Is this right?

        self.motor = rev.CANSparkMax(canID, mtype)
        
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(inverted)
        self.controller, self.encoder = self.__configureEncoder__(self.motor, absolute_encoder=absolute_encoder)
        self.resetDistance()

    def __configureEncoder__(self, motor, smartMotionSlot=0, absolute_encoder=False):
        controller = motor.getPIDController()
        
        if absolute_encoder:
            encoder = motor.getAbsoluteEncoder()
        else:
            encoder = motor.getEncoder()

        # PID parameters
        controller.setP(self.kP)
        controller.setI(self.kI)
        controller.setD(self.kD)
        controller.setIZone(self.kIz)
        controller.setFF(self.kFF)
        controller.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # Smart Motion Parameters
        controller.setSmartMotionMaxVelocity(self.maxVel, smartMotionSlot)
        controller.setSmartMotionMinOutputVelocity(self.minVel, smartMotionSlot)
        controller.setSmartMotionMaxAccel(self.maxAcc, smartMotionSlot)
        controller.setSmartMotionAllowedClosedLoopError(
            self.allowedErr, smartMotionSlot
        )
        return controller, encoder

    def resetDistance(self):
        self.encoder.setPosition(0)
        return False

    def setPercent(self, value):
        self.motor.set(value)
        return False

    def setMaxAccel(self, value):
        self.maxAcc = value
        self.controller.setSmartMotionMaxAccel(self.maxAcc, 0)
        return False

    def getVelocity(self):
        vel = -self.encoder.getVelocity()  # rpm
        return vel

    def getDistance(self):
        distance =  self.getRotation() 
        distance *= self.wheel_diameter / self.gear_ratio
        return distance

    def getRotation(self):
        rotation = -self.encoder.getPosition()
        rotation *= 2*math.pi # Conver to radians
        return rotation

    def resetDistance(self):
        self.encoder.setPosition(0)
        return False

    def setDistance(self, distance):
        rotations = distance /(2*math.pi *self.wheel_diameter / self.gear_ratio)
        self.controller.setReference(
            -rotations, rev.CANSparkMax.ControlType.kSmartMotion
        )
        return False

class SwerveModule:
    angleMotor: SparkMax
    speedMotor: SparkMax

    CLAMP = 0.2

    def __init__(self):

        self.target_angle = 0
        self.target_speed = 0

        self.target_distance = 0
        self.tolerance = 0.001

        self.auto_lockout = 0

    def getEncoder(self):
        return 0.0

    def resetEncoder(self):
        return 0.0

    def getSpeedAngle(self):
        angle = self.angleMotor.getRotation()
        speed = self.speedMotor.getDistance()
        return speed, angle

    def move(self, speed, angle):
        self.angleMotor.setDistance(angle)
        self.speedMotor.setPercent(speed)
        return False

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

    @staticmethod
    def __calcAngleSpeed__(self, front_rear, right_left):
        """
        :param front_rear:
        :param right_left: 
        :returns: 
        """
        speed = math.hypot(front_rear, right_left)
        angle = math.degrees(math.atan2(front_rear, right_left))
        return speed, angle

    @property
    def isMoveChanged(self):
        return self.move_changed

    def move(self, Lx, Ly, Rx, Ry):
        """
        :param front_rear:
        :param right_left: 
        :returns: 
        """
        strafe = Lx
        fwd = Ly
        rcw = Rx

        # TODO: optimize this normalization routine
        movement_arr = [fwd, strafe, rcw]
        max_mag = max([abs(move_val) for move_val in movement_arr])
        if max_mag > 1:
            for i,_ in range(3):
                movement_arr[i] = movement_arr[i] / max_mag
        fwd, strafe, rcw = movement_arr

        frontX = strafe - rcw * self.DriveConfig.chasis_length / self.DriveConfig.ratio
        rearX = strafe + rcw * self.DriveConfig.chasis_length / self.DriveConfig.ratio
        leftY = fwd - rcw * self.DriveConfig.chasis_width / self.DriveConfig.ratio
        rightY = fwd + rcw * self.DriveConfig.chasis_width / self.DriveConfig.ratio

        self.front_left_speed, self.front_left_angle = self.__calcAngleSpeed__(frontX, rightY)
        self.front_right_speed, self.front_right_angle = self.__calcAngleSpeed__(frontX, leftY)
        self.rear_left_speed, self.rear_left_angle = self.__calcAngleSpeed__(rearX, rightY)
        self.rear_right_speed, self.rear_right_angle = self.__calcAngleSpeed__(rearX, leftY)
        self.move_changed = True
        return False

    def execute(self):
        if self.isMoveChanged():
            self.FrontLeft_SwerveModule.move(front_left_speed, front_left_angle)
            self.FrontRight_SwerveModule.move(front_right_speed, front_right_angle)
            self.RearLeft_SwerveModule.move(rear_left_speed, rear_left_angle)
            self.RearRight_SwerveModule.move(rear_right_speed, rear_right_angle)
            self.move_changed = False