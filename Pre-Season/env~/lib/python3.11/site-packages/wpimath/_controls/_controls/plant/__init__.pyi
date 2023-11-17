from __future__ import annotations
import wpimath._controls._controls.plant
import typing
import wpimath._controls._controls.system

__all__ = [
    "DCMotor",
    "LinearSystemId"
]


class DCMotor():
    """
    Holds the constants for a DC motor.
    """
    @staticmethod
    def CIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of CIM.
        """
    @staticmethod
    def NEO(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO brushless motor.
        """
    @staticmethod
    def NEO550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO 550 brushless motor.
        """
    @staticmethod
    def RS775_125(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark RS 775-125.
        """
    def __init__(self, nominalVoltage: volts, stallTorque: newton_meters, stallCurrent: amperes, freeCurrent: amperes, freeSpeed: radians_per_second, numMotors: int = 1) -> None: 
        """
        Constructs a DC motor.

        :param nominalVoltage: Voltage at which the motor constants were measured.
        :param stallTorque:    Torque when stalled.
        :param stallCurrent:   Current draw when stalled.
        :param freeCurrent:    Current draw under no load.
        :param freeSpeed:      Angular velocity under no load.
        :param numMotors:      Number of motors in a gearbox.
        """
    @staticmethod
    def andymark9015(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark 9015.
        """
    @staticmethod
    def bag(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Bag motor.
        """
    @staticmethod
    def banebotsRS550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 550.
        """
    @staticmethod
    def banebotsRS775(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 775.
        """
    def current(self, speed: radians_per_second, inputVoltage: volts) -> amperes: 
        """
        Returns current drawn by motor with given speed and input voltage.

        :param speed:        The current angular velocity of the motor.
        :param inputVoltage: The voltage being applied to the motor.
        """
    @staticmethod
    def falcon500(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Falcon 500 brushless motor.
        """
    @staticmethod
    def miniCIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of MiniCIM.
        """
    @staticmethod
    def romiBuiltIn(numMotors: int = 1) -> DCMotor: 
        """
        Return a gearbox of Romi/TI_RSLK MAX motors.
        """
    def speed(self, torque: newton_meters, inputVoltage: volts) -> radians_per_second: 
        """
        Returns the speed produced by the motor at a given torque and input
        voltage.

        :param torque:       The torque produced by the motor.
        :param inputVoltage: The input voltage provided to the motor.
        """
    def torque(self, current: amperes) -> newton_meters: 
        """
        Returns torque produced by the motor with a given current.

        :param current: The current drawn by the motor.
        """
    @staticmethod
    def vex775Pro(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Vex 775 Pro.
        """
    def voltage(self, torque: newton_meters, speed: radians_per_second) -> volts: 
        """
        Returns the voltage provided to the motor for a given torque and
        angular velocity.

        :param torque: The torque produced by the motor.
        :param speed:  The current angular velocity of the motor.
        """
    def withReduction(self, gearboxReduction: float) -> DCMotor: 
        """
        Returns a copy of this motor with the given gearbox reduction applied.

        :param gearboxReduction: The gearbox reduction.
        """
    @property
    def Kt(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @property
    def Kv(self) -> radians_per_second_per_volt:
        """
        :type: radians_per_second_per_volt
        """
    @property
    def R(self) -> ohms:
        """
        :type: ohms
        """
    @property
    def freeCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def freeSpeed(self) -> radians_per_second:
        """
        :type: radians_per_second
        """
    @property
    def nominalVoltage(self) -> volts:
        """
        :type: volts
        """
    @property
    def stallCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def stallTorque(self) -> newton_meters:
        """
        :type: newton_meters
        """
    pass
class LinearSystemId():
    @staticmethod
    def DCMotorSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_2: 
        """
        Create a state-space model of a DC motor system. The states of the system
        are [angular position, angular velocity], inputs are [voltage], and outputs
        are [angular position, angular velocity].

        :param motor: The motor (or gearbox) attached to the system.
        :param J:     the moment of inertia J of the DC motor.
        :param G:     Gear ratio from motor to output.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    def __init__(self) -> None: ...
    @staticmethod
    def drivetrainVelocitySystem(motor: DCMotor, mass: kilograms, r: meters, rb: meters, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_2_2: 
        """
        Create a state-space model of differential drive drivetrain. In this model,
        the states are [left velocity, right velocity], the inputs are [left
        voltage, right voltage], and the outputs are [left velocity, right
        velocity]

        :param motor: The motor (or gearbox) driving the drivetrain.
        :param mass:  The mass of the robot in kilograms.
        :param r:     The radius of the wheels in meters.
        :param rb:    The radius of the base (half of the track width), in meters.
        :param J:     The moment of inertia of the robot.
        :param G:     Gear ratio from motor to wheel.
                      @throws std::domain_error if mass <= 0, r <= 0, rb <= 0, J <= 0, or
                      G <= 0.
        """
    @staticmethod
    def elevatorSystem(motor: DCMotor, mass: kilograms, radius: meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Create a state-space model of the elevator system. The states of the system
        are [position, velocity], inputs are [voltage], and outputs are [position].

        :param motor:  The motor (or gearbox) attached to the carriage.
        :param mass:   The mass of the elevator carriage, in kilograms.
        :param radius: The radius of the elevator's driving drum, in meters.
        :param G:      Gear ratio from motor to carriage.
                       @throws std::domain_error if mass <= 0, radius <= 0, or G <= 0.
        """
    @staticmethod
    def flywheelSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_1_1_1: 
        """
        Create a state-space model of a flywheel system, the states of the system
        are [angular velocity], inputs are [voltage], and outputs are [angular
        velocity].

        :param motor: The motor (or gearbox) attached to the flywheel.
        :param J:     The moment of inertia J of the flywheel.
        :param G:     Gear ratio from motor to flywheel.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    @staticmethod
    @typing.overload
    def identifyDrivetrainSystem(kVLinear: volt_seconds_per_meter, kALinear: volt_seconds_squared_per_meter, kVAngular: volt_seconds_per_meter, kAAngular: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_2_2_2: 
        """
        Identify a differential drive drivetrain given the drivetrain's kV and kA
        in both linear {(volts/(meter/sec), (volts/(meter/sec²))} and angular
        {(volts/(radian/sec), (volts/(radian/sec²))} cases. These constants can be
        found using SysId.

        States: [[left velocity], [right velocity]]
        Inputs: [[left voltage], [right voltage]]
        Outputs: [[left velocity], [right velocity]]

        :param kVLinear:  The linear velocity gain in volts per (meters per second).
        :param kALinear:  The linear acceleration gain in volts per (meters per
                          second squared).
        :param kVAngular: The angular velocity gain in volts per (meters per
                          second).
        :param kAAngular: The angular acceleration gain in volts per (meters per
                          second squared).
                          @throws domain_error if kVLinear <= 0, kALinear <= 0, kVAngular <= 0,
                          or kAAngular <= 0.

        Identify a differential drive drivetrain given the drivetrain's kV and kA
        in both linear {(volts/(meter/sec)), (volts/(meter/sec²))} and angular
        {(volts/(radian/sec)), (volts/(radian/sec²))} cases. This can be found
        using SysId.

        States: [[left velocity], [right velocity]]
        Inputs: [[left voltage], [right voltage]]
        Outputs: [[left velocity], [right velocity]]

        :param kVLinear:   The linear velocity gain in volts per (meters per
                           second).
        :param kALinear:   The linear acceleration gain in volts per (meters per
                           second squared).
        :param kVAngular:  The angular velocity gain in volts per (radians per
                           second).
        :param kAAngular:  The angular acceleration gain in volts per (radians per
                           second squared).
        :param trackwidth: The distance between the differential drive's left and
                           right wheels, in meters.
                           @throws domain_error if kVLinear <= 0, kALinear <= 0, kVAngular <= 0,
                           kAAngular <= 0, or trackwidth <= 0.
        """
    @staticmethod
    @typing.overload
    def identifyDrivetrainSystem(kVLinear: volt_seconds_per_meter, kALinear: volt_seconds_squared_per_meter, kVAngular: volt_seconds_per_radian, kAAngular: volt_seconds_squared_per_radian, trackwidth: meters) -> wpimath._controls._controls.system.LinearSystem_2_2_2: ...
    @staticmethod
    def identifyPositionSystemMeters(kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Create a state-space model for a 1 DOF position system from its kV
        (volts/(unit/sec)) and kA (volts/(unit/sec²)). These constants can be
        found using SysId. the states of the system are [position, velocity],
        inputs are [voltage], and outputs are [position].

        You MUST use an SI unit (i.e. meters or radians) for the Distance template
        argument. You may still use non-SI units (such as feet or inches) for the
        actual method arguments; they will automatically be converted to SI
        internally.

        The parameters provided by the user are from this feedforward model:

        u = K_v v + K_a a

        @throws std::domain_error if kV <= 0 or kA <= 0.

        :param kV: The velocity gain, in volts/(unit/sec).
        :param kA: The acceleration gain, in volts/(unit/sec²).
        """
    @staticmethod
    def identifyPositionSystemRadians(kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian) -> wpimath._controls._controls.system.LinearSystem_2_1_1: ...
    @staticmethod
    def identifyVelocitySystemMeters(kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter) -> wpimath._controls._controls.system.LinearSystem_1_1_1: 
        """
        Create a state-space model for a 1 DOF velocity system from its kV
        (volts/(unit/sec)) and kA (volts/(unit/sec²)). These constants can be
        found using SysId. The states of the system are [velocity], inputs are
        [voltage], and outputs are [velocity].

        You MUST use an SI unit (i.e. meters or radians) for the Distance template
        argument. You may still use non-SI units (such as feet or inches) for the
        actual method arguments; they will automatically be converted to SI
        internally.

        The parameters provided by the user are from this feedforward model:

        u = K_v v + K_a a

        :param kV: The velocity gain, in volts/(unit/sec).
        :param kA: The acceleration gain, in volts/(unit/sec²).
                   @throws std::domain_error if kV <= 0 or kA <= 0.
        """
    @staticmethod
    def identifyVelocitySystemRadians(kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian) -> wpimath._controls._controls.system.LinearSystem_1_1_1: ...
    @staticmethod
    def singleJointedArmSystem(motor: DCMotor, J: kilogram_square_meters, G: float) -> wpimath._controls._controls.system.LinearSystem_2_1_1: 
        """
        Create a state-space model of a single-jointed arm system.The states of the
        system are [angle, angular velocity], inputs are [voltage], and outputs are
        [angle].

        :param motor: The motor (or gearbox) attached to the arm.
        :param J:     The moment of inertia J of the arm.
        :param G:     Gear ratio from motor to arm.
                      @throws std::domain_error if J <= 0 or G <= 0.
        """
    pass
