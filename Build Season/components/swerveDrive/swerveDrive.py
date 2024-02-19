import math
import rev
from components.config import RobotConfig

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 0.32
    kI = 1e-4
    kD = 1
    kIz = 0.30
    kFF = 0
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0

    smartMotionSlot=0

    def __init__(
        self,
        canID,
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        absolute_encoder=False,
        z_offset = 0
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.absolute = absolute_encoder
        self.gear_ratio = gear_ratio
        self.wheel_diameter = wheel_diameter
        self.zOffset = z_offset

        # Encoder parameters 
        # https://docs.reduxrobotics.com/canandcoder/spark-max
        # https://github.com/REVrobotics/MAXSwerve-Java-Template/blob/main/src/main/java/frc/robot/subsystems/MAXSwerveModule.java

        self.motor = rev.CANSparkMax(self.canID, rev.CANSparkMax.MotorType.kBrushless)  
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(not inverted)
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(25)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(inverted)
        self.encoder.setPositionConversionFactor(2*math.pi)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        
        self.SMcontroller.setFeedbackDevice(self.encoder)
        self.SMcontroller.setPositionPIDWrappingEnabled(True) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMinInput(0) #TODO: does this need to be removed?
        self.SMcontroller.setPositionPIDWrappingMaxInput(2*math.pi) #TODO: does this need to be removed?
        
        # PID parameters
        self.SMcontroller.setP(self.kP)
        self.SMcontroller.setI(self.kI)
        self.SMcontroller.setD(self.kD)
        self.SMcontroller.setIZone(self.kIz)
        self.SMcontroller.setFF(self.kFF)
        self.SMcontroller.setOutputRange(self.kMinOutput, self.kMaxOutput)

        # # Smart Motion Parameters
        # self.SMcontroller.setSmartMotionMaxVelocity(self.maxVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMinOutputVelocity(self.minVel, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionMaxAccel(self.maxAcc, self.smartMotionSlot)
        # self.SMcontroller.setSmartMotionAllowedClosedLoopError(self.allowedErr, self.smartMotionSlot)
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        self.SMcontroller.setReference(position-self.zOffset, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getAbsPosition(self):
        rotation = self.encoder.getPosition()
        return rotation

class SparkMaxDriving:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 1e-4
    kI = 1e-4
    kD = 1e-4
    kIz = 0
    kFF = 1
    kMaxOutput = 1
    kMinOutput = -1
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 2000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0
    
    targetDistance = 0
    tolerance = 0.01

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
        
        self.encoder.setPositionConversionFactor(0.1016)
        self.encoder.setVelocityConversionFactor(0.0008463260209216138)
        
        # PID parameters
        self.controller.setP(self.kP)
        self.controller.setI(self.kI)
        self.controller.setD(self.kD)
        self.controller.setFF(self.kFF)
        self.controller.setOutputRange(self.kMinOutput, self.kMaxOutput)
        self.distance_to_rotations = gear_ratio / (math.pi * self.wheel_diameter)
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
    
    def atDistance(self):
        currentDistance = self.encoder.getPosition()
        if abs(currentDistance-self.targetDistance) <= self.tolerance:
            return True
        return False
    
    def setDistance(self, targetDistance):
        self.targetDistance = targetDistance
        self.encoder.setPosition(0)
        self.controller.setReference(targetDistance, rev.CANSparkMax.ControlType.kPosition)
        return False

class SwerveDrive:
    RobotConfig: RobotConfig

    FrontLeftAngleMotor: SparkMaxTurning
    __frontLeftAngle__: float = 0
    
    FrontLeftSpeedMotor: SparkMaxDriving 
    __frontLeftSpeed__: float = 0
    __frontLeftDistance__: float = 0
    
    RearLeftAngleMotor: SparkMaxTurning
    __rearLeftAngle__: float = 0
    
    RearLeftSpeedMotor: SparkMaxDriving
    __rearleftSpeed__: float = 0
    __rearLeftDistance__: float = 0
    
    RearRightAngleMotor: SparkMaxTurning
    __rearRightAngle__: float = 0

    RearRightSpeedMotor: SparkMaxDriving
    __rearRightSpeed__: float = 0
    __rearRightDistance__: float = 0 
    
    FrontRightAngleMotor: SparkMaxTurning
    __frontRightAngle__: float = 0

    FrontRightSpeedMotor: SparkMaxDriving
    __frontRightSpeed__: float = 0
    __frontRightDistance__: float = 0
    move_changed: bool = False
    distance_changed: bool = False
    
    def clearFaults(self):
        self.FrontLeftAngleMotor.clearFaults()
        self.FrontLeftSpeedMotor.clearFaults()
        self.RearLeftAngleMotor.clearFaults()
        self.RearLeftSpeedMotor.clearFaults()
        self.RearRightAngleMotor.clearFaults()
        self.RearRightSpeedMotor.clearFaults()
        self.FrontRightAngleMotor.clearFaults()
        self.FrontRightSpeedMotor.clearFaults()
        return False

    def move(self, Lx, Ly, Rx): 

        # Check negatives and positives here for Lx, Ly, and Rx
        Vx0 = -Lx
        Vy0 = Ly
        w0 = -Rx
        
        Vxp = Vx0 + w0*math.pi*self.RobotConfig.chassis_length
        Vxn = Vx0 - w0*math.pi*self.RobotConfig.chassis_length
        Vyp = Vy0 + w0*math.pi*self.RobotConfig.chassis_width
        Vyn = Vy0 - w0*math.pi*self.RobotConfig.chassis_width

        self.__frontLeftAngle__ = math.atan2(Vyp, Vxp)
        self.__frontLeftSpeed__ = math.hypot(Vyp, Vxp)

        self.__rearLeftAngle__ = math.atan2(Vyp, Vxn)
        self.__rearLeftSpeed__ = math.hypot(Vyp, Vxn)

        self.__rearRightAngle__ = math.atan2(Vyn, Vxn)
        self.__rearRightSpeed__ = math.hypot(Vyn, Vxn)

        self.__frontRightAngle__ = math.atan2(Vyn, Vxp)
        self.__frontRightSpeed__ = math.hypot(Vyn, Vxp)

        self.move_changed = True
        
        return False
    
    def goDistance(self, target_distance, target_angle, target_rotations):
        
        Xp = target_distance * math.cos(target_angle) + math.pi * self.RobotConfig.chassis_length * target_rotations
        Xn = target_distance * math.cos(target_angle) - math.pi * self.RobotConfig.chassis_length * target_rotations
        Yp = target_distance * math.sin(target_angle) + math.pi * self.RobotConfig.chassis_width * target_rotations
        Yn = target_distance * math.sin(target_angle) - math.pi * self.RobotConfig.chassis_width * target_rotations

        self.__frontLeftAngle__ = math.atan2(Yp, Xp)
        self.__frontLeftDistance__ = math.hypot(Yp, Xp)

        self.__rearLeftAngle__ = math.atan2(Yp, Xn)
        self.__rearLeftDistance__ = math.hypot(Yp, Xn)

        self.__rearRightAngle__ = math.atan2(Yn, Xn)
        self.__rearRightDistance__ = math.hypot(Yn, Xn)

        self.__frontRightAngle__ = math.atan2(Yn, Xp)
        self.__frontRightDistance__ = math.hypot(Yn, Xp)
        
        self.distance_changed = True
        
    def clampSpeed(self):
        max_val = max([self.__frontLeftSpeed__, 
                        self.__frontRightSpeed__, 
                        self.__rearLeftSpeed__, 
                        self.__rearRightSpeed__])/self.RobotConfig.speed_clamp
        if abs(max_val) == 0:
            max_val = 1
        return max_val

    def atDistance(self):
        FL = self.FrontLeftSpeedMotor.atDistance()
        FR = self.FrontRightSpeedMotor.atDistance()
        RL = self.RearLeftSpeedMotor.atDistance()
        RR = self.RearRightSpeedMotor.atDistance()
        
        if FL and FR and RL and RR:
            return True
        
        return False
        
    def execute(self):
        if self.move_changed:

            max_val = self.clampSpeed()

            self.FrontLeftSpeedMotor.setSpeed(self.__frontLeftSpeed__/max_val) 
            self.FrontLeftAngleMotor.setAbsPosition(self.__frontLeftAngle__)

            self.RearLeftSpeedMotor.setSpeed(self.__rearLeftSpeed__/max_val) 
            self.RearLeftAngleMotor.setAbsPosition(self.__rearLeftAngle__)

            self.RearRightSpeedMotor.setSpeed(self.__rearRightSpeed__/max_val) 
            self.RearRightAngleMotor.setAbsPosition(self.__rearRightAngle__)

            self.FrontRightSpeedMotor.setSpeed(self.__frontRightSpeed__/max_val) 
            self.FrontRightAngleMotor.setAbsPosition(self.__frontRightAngle__)

            self.move_changed = False
            
        if self.distance_changed:

            self.FrontLeftSpeedMotor.setDistance(self.__frontLeftDistance__) 
            self.FrontLeftAngleMotor.setAbsPosition(self.__frontLeftAngle__)

            self.RearLeftSpeedMotor.setDistance(self.__rearLeftDistance__) 
            self.RearLeftAngleMotor.setAbsPosition(self.__rearLeftAngle__)

            self.RearRightSpeedMotor.setDistance(self.__rearRightDistance__) 
            self.RearRightAngleMotor.setAbsPosition(self.__rearRightAngle__)

            self.FrontRightSpeedMotor.setDistance(self.__frontRightDistance__) 
            self.FrontRightAngleMotor.setAbsPosition(self.__frontRightAngle__)

            self.distance_changed = False