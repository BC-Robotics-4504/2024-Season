import math
import rev

class MySparkMax:
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
        motorType="brushless",
        inverted=False,
        gear_ratio=1,
        wheel_diameter=1,
        chasis_width=1,
        chasis_length=1,
    ):
        self.canID = canID
        self.gear_ratio = gear_ratio
        self.inverted = inverted
        self.motorType = motorType
        self.gear_ratio = gear_ratio
        self.chasis_length = chasis_length
        self.chasis_width = chasis_width
        self.wheel_diameter = wheel_diameter
        self.distance_to_rotations = gear_ratio / (math.pi * wheel_diameter)
        self.ratio = math.hypot(chasis_length, chasis_width)

        if motorType == "brushless":
            mtype = rev.CANSparkMax.MotorType.kBrushless
        else:
            mtype = rev.CANSparkMax.MotorType.kBrushed  # FIXME!: Is this right?

        self.motor = rev.CANSparkMax(canID, mtype)
        self.motor.restoreFactoryDefaults()
        self.motor.setInverted(inverted)
        self.controller, self.encoder = self.__configureEncoder__(self.motor)
        self.resetDistance()

    def __configureEncoder__(self, motor, smartMotionSlot=0):
        controller = motor.getPIDController()
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
        pos = -self.encoder.getPosition() / self.distance_to_rotations
        return pos

    def resetDistance(self):
        self.encoder.setPosition(0)
        return False

    def setDistance(self, distance):
        rotations = distance * self.distance_to_rotations
        self.controller.setReference(
            -rotations, rev.CANSparkMax.ControlType.kSmartMotion
        )
        return False

class SwerveModule:
    angleMotor: MySparkMax
    speedMotor: MySparkMax

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

    def move(self, speed, angle):
        self.angleMotor.setDistance(angle)
        self.speedMotor.setPercent(speed)
        return False

class SwerveDrive:
    frontLeftModule: SwerveModule
    frontRightModule: SwerveModule
    rearLeftModule: SwerveModule
    rearRightModule: SwerveModule

    front_left_speed: float = 0
    front_left_angle: float = 0
    front_right_speed: float = 0
    front_right_angle: float = 0
    rear_left_speed: float = 0
    rear_left_angle: float = 0
    rear_right_speed: float = 0
    rear_right_angle: float = 0

    movement_changed: bool = False

    def setup(self):

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
        rcw = math.atan2(Ry, Rx)

        # TODO: optimize this normalization routine
        movement_arr = [fwd, strafe, rcw]
        max_mag = max([abs(move_val) for move_val in movement_arr]])
        if max_mag > 1:
            for i,_ in range(len(move_vals):
                movement_arr[i] = movement_arr[i] / max_mag
        fwd, strafe, rcw = movement_arr

        frontX = strafe - rcw * self.chasis_length / self.ratio
        rearX = strafe + rcw * self.chasis_length / self.ratio
        leftY = fwd - rcw * self.chasis_width / self.ratio
        rightY = fwd + rcw * self.chasis_width / self.ratio

        self.front_left_speed, self.front_left_angle = self.__calcAngleSpeed__(frontX, rightY)
        self.front_right_speed, self.front_right_angle = self.__calcAngleSpeed__(frontX, leftY)
        self.rear_left_speed, self.rear_left_angle = self.__calcAngleSpeed__(rearX, rightY)
        self.rear_right_speed, self.rear_right_angle = self.__calcAngleSpeed__(rearX, leftY)
        self.move_changed = True
        return False

    def execute(self):

        if self.isMoveChanged():
            self.frontLeftModule.move(front_left_speed, front_left_angle)
            self.frontRightModule.move(front_right_speed, front_right_angle)
            self.rearLeftModule.move(rear_left_speed, rear_left_angle)
            self.rearRightModule.move(rear_right_speed, rear_right_angle)