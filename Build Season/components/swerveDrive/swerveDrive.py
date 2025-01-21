import math
import rev
from components.config import RobotConfig

from wpimath.filter import SlewRateLimiter

class SparkMaxTurning:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP = 0.25
    kI = 0
    kD = 0
    kIz = 0
    kFF = 0
    kMaxOutput = 2*math.pi
    kMinOutput = -2*math.pi
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
        self.motor.setSmartCurrentLimit(40)

        self.SMcontroller = self.motor.getPIDController()
        self.encoder = self.motor.getAbsoluteEncoder(rev.SparkMaxAbsoluteEncoder.Type.kDutyCycle)
        self.encoder.setInverted(inverted)
        self.encoder.setPositionConversionFactor(2*math.pi)
        self.encoder.setVelocityConversionFactor(.104719755119659771)
        self.encoder.setZeroOffset(z_offset)
        
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
        
        #self.controller.burnFlash()    
        self.clearFaults()
    
    def clearFaults(self):
        """SparkMaxTurning.clearFaults()
        
        Clears the faults of the turning SparkMax
        """
        self.motor.clearFaults()
    
    def setAbsPosition(self, position):
        """SparkMaxTurning.setAbsPosition()
        
        Sets the absoulute positon of the encoder"""
        self.SMcontroller.setReference(position, rev.CANSparkMax.ControlType.kPosition)
        return False
    
    def getAbsPosition(self):
        """SparkMaxTurning.getAbsPosition()
        
        Gets the absolute positon of the encoder
        """
        rotation = self.encoder.getPosition()
        return rotation

class SparkMaxDriving:
    """Swerve Drive SparkMax Class
    Custom class for configuring SparkMaxes used in Swerve Drive Drivetrain
    """
    
    # PID coefficients
    kP0 = 6e-5 
    kI0 = 0
    kD0 = 0
    kIz0 = 0
    kFF0 = 0.00015
    kMaxOutput0 = 5_000
    kMinOutput0 = -5_000
    
    kP1 = 1e-2
    kI1 = 1e-7
    kD1 = 0
    kIz1 = 0
    kFF1 = 0
    kMaxOutput1 = 3_000
    kMinOutput1 = -3_000  
     
    maxRPM = 5700

    # Smart Motion Coefficients
    maxVel = 5_000  # rpm
    maxAcc = 1000
    minVel = 0
    allowedErr = 0
    
    targetDistance = 5.5
    tolerance = 0.1

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
         
        self.controller = self.motor.getPIDController()
        self.encoder = self.motor.getEncoder()
        
        self.encoder.setPositionConversionFactor(1)
        self.encoder.setVelocityConversionFactor(1)
        self.encoder.setPosition(0)
        
        # PID parameters
        self.controller.setP(self.kP0, slotID=0)
        self.controller.setI(self.kI0, slotID=0)
        self.controller.setD(self.kD0, slotID=0)
        self.controller.setFF(self.kFF0, slotID=0)
        self.controller.setOutputRange(self.kMinOutput0, self.kMaxOutput0, slotID=0)
        
        self.controller.setP(self.kP1, slotID=1)
        self.controller.setI(self.kI1, slotID=1)
        self.controller.setD(self.kD1, slotID=1)
        self.controller.setFF(self.kFF1, slotID=1)
        self.controller.setOutputRange(self.kMinOutput1, self.kMaxOutput1, slotID=1)
        
        self.motor.setIdleMode(rev.CANSparkMax.IdleMode.kBrake)
        self.motor.setSmartCurrentLimit(60)
        
        self.clearFaults()

    def clearFaults(self):
        """SparkMaxDriving.clearFaults()
        
        Clears the faults of the speed SparkMax"""
        self.motor.clearFaults()
    
    def getSpeed(self):
        """SparkMaxDriving.getSpeed()
        
        Gets the current speed of the swerve modules
        """
        vel = -self.encoder.getVelocity()  # rpm
        return vel

    def setSpeed(self, speed):
        """
        SparkMaxDriving.setSpeed()
        
        Sets the speed of the swerve modules """
        # self.motor.set(speed)
        self.controller.setReference(speed, rev.CANSparkMax.ControlType.kVelocity, pidSlot=0) #NOTE: Changed this.
        return None
    
    def atDistance(self):
        """SparkMaxDriving.atDistance()
        
        Checks if the robot has travlled to the specfied distance"""
        currentDistance = self.encoder.getPosition()
        if abs(currentDistance-self.targetDistance) <= self.tolerance:
            return True
        
        return False

    def setDistance(self, targetDistance: float):
        """SparkMaxDriving.setDistance()
        
        Sets a distance for the robot to travel 
        
        ::params: 
        targetDistance: Distance for the robot to travel
        """
        self.targetDistance = targetDistance
        self.controller.setReference(targetDistance, rev.CANSparkMax.ControlType.kPosition, pidSlot=1)
        return False

    def resetEncoder(self):
        self.encoder.setPosition(0)
        return 0

class SwerveDrive:
    """ SwerveDrive Class 

    """
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

    LxSlewRateLimiter = SlewRateLimiter(0.5)
    LySlewRateLimiter = SlewRateLimiter(0.5)
    RxSlewRateLimiter = SlewRateLimiter(1)
    
    def clearFaults(self):
        """SwerveDrive.clearFaults()
        Clears faults on all of the SparkMax modules
        """
        self.FrontLeftAngleMotor.clearFaults()
        self.FrontLeftSpeedMotor.clearFaults()
        self.RearLeftAngleMotor.clearFaults()
        self.RearLeftSpeedMotor.clearFaults()
        self.RearRightAngleMotor.clearFaults()
        self.RearRightSpeedMotor.clearFaults()
        self.FrontRightAngleMotor.clearFaults()
        self.FrontRightSpeedMotor.clearFaults()
        return False

    def move(self, Lx: float, Ly: float, Rx: float): 
        """SwerveDrive.move(Lx: float, Ly: float, Rx: float)

        ::params::
        Lx: Magnitude to move in the x direction in range, negative is forward [-1, 1]
        Ly: Magnitude to move in the y direction in range, positive is left [-1, 1]
        Rx: Magnitude of rotational speed where counter-clockwise is positive [-1, 1]
        """
        # Rx = self.RxSlewRateLimiter.calculate(Rx)
        # Check negatives and positives here for Lx, Ly, and Rx
        Vx0 = -Lx*self.RobotConfig.max_driving_speed*self.RobotConfig.drive_wheel_diameter*math.pi
        Vy0 = Ly*self.RobotConfig.max_driving_speed*self.RobotConfig.drive_wheel_diameter*math.pi
        w0 = -Rx*RobotConfig.max_angular_speed*math.pi
        
        # Calculate component vectors for the swerve modeule
        Vxp = Vx0 + w0*self.RobotConfig.chassis_length
        Vxn = Vx0 - w0*self.RobotConfig.chassis_length
        Vyp = Vy0 + w0*self.RobotConfig.chassis_width
        Vyn = Vy0 - w0*self.RobotConfig.chassis_width

        # Calculate the speed and angle for each swerve motor
        self.__frontLeftAngle__ = math.atan2(Vyp, Vxp)
        self.__frontLeftSpeed__ = math.hypot(Vyp, Vxp)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__rearLeftAngle__ = math.atan2(Vyp, Vxn)
        self.__rearLeftSpeed__ = math.hypot(Vyp, Vxn)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__rearRightAngle__ = math.atan2(Vyn, Vxn)
        self.__rearRightSpeed__ = math.hypot(Vyn, Vxn)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__frontRightAngle__ = math.atan2(Vyn, Vxp)
        self.__frontRightSpeed__ = math.hypot(Vyn, Vxp)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        # Normalizes speed to maximum allowable speed for each wheel
        self.normalizeSpeeds()

        # Enable the move to be changed when "execute()" is run
        self.move_changed = True
        
        return False
    
    def goDistance(self, Rx0: float, Ry0: float, r0: float):
        """SwerveDrive.gotDistance(target_distance: float, target_angle: float, target_rotations: float)
        
        Calculates the angle and speed for a robot to move autonomusly a certain distance and at a target angle. 

        ::params::
        target_distance: The target distance the robot should travel autonomously range[0, 2*math.pi]
        target_angle: the target angle the robot should be at once the autonomous movement ends
        target_rotations: How many time should the robot spin before the autonomous movement ends.

        """
        Rx0 *= self.RobotConfig.drive_wheel_diameter*math.pi
        Ry0 *= self.RobotConfig.drive_wheel_diameter*math.pi
        r0 *= -math.pi
        
        # Calculate component vectors for the swerve modeule
        Xp = Rx0 + r0*self.RobotConfig.chassis_length
        Xn = Rx0 - r0*self.RobotConfig.chassis_length
        Yp = Ry0 + r0*self.RobotConfig.chassis_width
        Yn = Ry0 - r0*self.RobotConfig.chassis_width        
        
        self.__frontLeftAngle__ = math.atan2(Yp, Xp)+math.pi/2
        self.__frontLeftDistance__ = math.hypot(Yp, Xp)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__rearLeftAngle__ = math.atan2(Yp, Xn)+math.pi/2
        self.__rearLeftDistance__ = math.hypot(Yp, Xn)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__rearRightAngle__ = math.atan2(Yn, Xn)+math.pi/2
        self.__rearRightDistance__ = math.hypot(Yn, Xn)/(math.pi*self.RobotConfig.drive_wheel_diameter)

        self.__frontRightAngle__ = math.atan2(Yn, Xp)+math.pi/2
        self.__frontRightDistance__ = math.hypot(Yn, Xp)/(math.pi*self.RobotConfig.drive_wheel_diameter)
                
        self.distance_changed = True
        
    def resetEncoders(self):
        self.RearLeftSpeedMotor.resetEncoder()
        self.RearRightSpeedMotor.resetEncoder()
        self.FrontLeftSpeedMotor.resetEncoder()
        self.FrontRightSpeedMotor.resetEncoder()
        
    def clampSpeed(self):
        """SwerveDrive.clampSpeed()
        
        Clamps the speed of the swerve drive"""
        self.__frontLeftSpeed__ *= self.RobotConfig.speed_clamp
        self.__frontRightSpeed__ *= self.RobotConfig.speed_clamp
        self.__rearLeftSpeed__ *= self.RobotConfig.speed_clamp
        self.__rearRightSpeed__ *= self.RobotConfig.speed_clamp
        return None
    
    def normalizeSpeeds(self):
        """SwerveDrive.normalizeSpeeds()

        Normalizes the speed vectors for each wheel"""
        maxSpeed = max([self.__frontLeftSpeed__, self.__frontRightSpeed__,
                        self.__rearLeftSpeed__, self.__rearRightSpeed__])
        if maxSpeed > self.RobotConfig.max_driving_speed:
            scalar = self.RobotConfig.max_driving_speed/maxSpeed
            self.__frontLeftSpeed__ *= scalar
            self.__frontRightSpeed__ *= scalar
            self.__rearRightSpeed__ *= scalar
            self.__rearLeftSpeed__ *= scalar
            return True
        
        return False

    def atDistance(self):
        """SwerveDrive.atDistance()

        Checks if each wheel has traveled a specified distance"""
        FL = self.FrontLeftSpeedMotor.atDistance()
        FR = self.FrontRightSpeedMotor.atDistance()
        RL = self.RearLeftSpeedMotor.atDistance()
        RR = self.RearRightSpeedMotor.atDistance()

        if FL and FR and RL and RR:
            return True
        
        return False
    
    def closestAngle(current_angle: float, setpoint: float):
        """SwerveDrive.closestAngle()

        Calculates the shortest direction to turn from a current angle to a desired setpoint angle.
        
        ::params: 
        current_angle: The current angle of the swerve module.
        setpoint: The desired angle for the swerve module to move to.
        """
        #get direction
        two_pi = math.pi*2
        dir = setpoint%(two_pi) - current_angle%(two_pi)

        # convert from -2*pi to 2*pi to -pi to pi
        if abs(dir) > math.pi:
            dir = -math.copysign(two_pi, dir) + dir
        return dir
        
    def execute(self):

        """SwerveDrive.execute()
        Updates the postion of the absolute encoders and the speed of each swerve module"""

        if self.move_changed:

            # self.clampSpeed()

            self.FrontLeftAngleMotor.setAbsPosition(self.__frontLeftAngle__)
            self.FrontLeftSpeedMotor.setSpeed(self.__frontLeftSpeed__) 

            self.RearLeftAngleMotor.setAbsPosition(self.__rearLeftAngle__)
            self.RearLeftSpeedMotor.setSpeed(self.__rearLeftSpeed__) 

            self.RearRightAngleMotor.setAbsPosition(self.__rearRightAngle__)
            self.RearRightSpeedMotor.setSpeed(self.__rearRightSpeed__) 
            
            self.FrontRightAngleMotor.setAbsPosition(self.__frontRightAngle__)
            self.FrontRightSpeedMotor.setSpeed(self.__frontRightSpeed__) 

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