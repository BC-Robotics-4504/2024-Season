# import ctre
import rev
from wpimath.controller import PIDController
from wpilib import SmartDashboard

import math

# from componentsHMI_xbox import XboxHMI, HMIModule

# # from componentsHMI import FlightStickHMI, HMIModule
# # from componentsIMU import IMUModule
# from componentsElevator import ElevatorModule


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
        self.angle_changed = False

        self.target_speed = 0
        self.speed_changed = False

        self.target_distance = 0
        self.tolerance = 0.001

        self.auto_lockout = 0

    def angleChanged(self):
        return self.angle_changed

    def speedChanged(self):
        return self.speed_changed

    def setSwerve(self, Lx, Rx, Ly, Ry):
        fwd = Ly
        strafe = Lx
        rcw = math.atan2(Ry, Rx)
        frontX = strafe - rcw * (self.chasis_length / self.ratio)
        rearX = strafe + rcw * (self.chasis_length / self.ratio)
        leftY = fwd - rcw * (self.width / self.ratio)
        rightX = fwd + rcw * (self.chasis_width / self.ratio)

        return False

    def execute(self):
        # if not self.auto_lockout:
        # TODO: put code to run the swerve module here!!!

        if self.angleChanged() or self.speedChanged():
            return False
