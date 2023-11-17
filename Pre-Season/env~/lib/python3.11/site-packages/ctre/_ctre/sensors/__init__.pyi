from __future__ import annotations
import ctre._ctre.sensors
import typing
import ctre._ctre
import wpilib.interfaces._interfaces
import wpimath.geometry._geometry
import wpiutil._wpiutil

__all__ = [
    "AbsoluteSensorRange",
    "AxisDirection",
    "BasePigeon",
    "BasePigeonConfigUtils",
    "BasePigeonConfiguration",
    "BasePigeonSimCollection",
    "CANCoder",
    "CANCoderConfigUtils",
    "CANCoderConfiguration",
    "CANCoderFaults",
    "CANCoderSimCollection",
    "CANCoderStatusFrame",
    "CANCoderStickyFaults",
    "MagnetFieldStrength",
    "Pigeon2",
    "Pigeon2ConfigUtils",
    "Pigeon2Configuration",
    "Pigeon2_Faults",
    "Pigeon2_StickyFaults",
    "PigeonIMU",
    "PigeonIMUConfigUtils",
    "PigeonIMUConfiguration",
    "PigeonIMU_ControlFrame",
    "PigeonIMU_Faults",
    "PigeonIMU_StatusFrame",
    "PigeonIMU_StickyFaults",
    "SensorInitializationStrategy",
    "SensorTimeBase",
    "SensorVelocityMeasPeriod",
    "WPI_CANCoder",
    "WPI_Pigeon2",
    "WPI_PigeonIMU"
]


class AbsoluteSensorRange():
    """
    Enum for how to range the absolute sensor position.

    Members:

      Unsigned_0_to_360 : Express the absolute position as an unsigned value.
    E.g. [0,+1) rotations or [0,360) deg.

      Signed_PlusMinus180 : Express the absolute position as an signed value.
    E.g. [-0.5,+0.5) rotations or [-180,+180) deg.
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Signed_PlusMinus180: ctre._ctre.sensors.AbsoluteSensorRange # value = <AbsoluteSensorRange.Signed_PlusMinus180: 1>
    Unsigned_0_to_360: ctre._ctre.sensors.AbsoluteSensorRange # value = <AbsoluteSensorRange.Unsigned_0_to_360: 0>
    __members__: dict # value = {'Unsigned_0_to_360': <AbsoluteSensorRange.Unsigned_0_to_360: 0>, 'Signed_PlusMinus180': <AbsoluteSensorRange.Signed_PlusMinus180: 1>}
    pass
class AxisDirection():
    """
    Enumerations for what primary axis to talk about
    Positive indicates in n the direction, negative indicates in the opposite direction

    Members:

      PositiveZ

      PositiveY

      PositiveX

      NegativeZ

      NegativeY

      NegativeX
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    NegativeX: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.NegativeX: 5>
    NegativeY: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.NegativeY: 4>
    NegativeZ: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.NegativeZ: 3>
    PositiveX: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.PositiveX: 2>
    PositiveY: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.PositiveY: 1>
    PositiveZ: ctre._ctre.sensors.AxisDirection # value = <AxisDirection.PositiveZ: 0>
    __members__: dict # value = {'PositiveZ': <AxisDirection.PositiveZ: 0>, 'PositiveY': <AxisDirection.PositiveY: 1>, 'PositiveX': <AxisDirection.PositiveX: 2>, 'NegativeZ': <AxisDirection.NegativeZ: 3>, 'NegativeY': <AxisDirection.NegativeY: 4>, 'NegativeX': <AxisDirection.NegativeX: 5>}
    pass
class BasePigeon(ctre._ctre.CANBusAddressable):
    """
    Pigeon IMU Class.
    Class supports communicating over CANbus and over ribbon-cable (CAN Talon SRX).
    """
    def __init__(self, deviceNumber: int, version: str, canbus: str = '') -> None: 
        """
        Create a Pigeon object that communicates with Pigeon on CAN Bus.

        :param deviceNumber: CAN Device Id of Pigeon [0,62]
        :param canbus:       Name of the CANbus; can be a SocketCAN interface (on Linux),
                             or a CANivore device name or serial number
        """
    def addYaw(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Atomically add to the Yaw register.

        :param angleDeg:  Degrees to add to the Yaw register.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def clearStickyFaults(self, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Clears the Sticky Faults

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configAllSettings(self, allConfigs: BasePigeonConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configFactoryDefault(self, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings to defaults.

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configGetCustomParam(self, paramIndex: int, timeoutMs: int = 0) -> int: 
        """
        Gets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/declination/offset
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param paramIndex: Index of custom parameter. [0-1]
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Value of the custom param.
        """
    @typing.overload
    def configGetParameter(self, param: ctre._ctre.ParamEnum, ordinal: int, timeoutMs: int = 0) -> float: 
        """
        Gets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:     Parameter enumeration.
        :param ordinal:   Ordinal of parameter.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Value of parameter.

        Gets a parameter by passing an int by reference

        :param param:         Parameter enumeration
        :param valueToSend:   Value to send to parameter
        :param valueReceived: Reference to integer to receive
        :param subValue:      SubValue of parameter
        :param ordinal:       Ordinal of parameter
        :param timeoutMs:     Timeout value in ms. If nonzero, function will wait for
                              config success and report an error if it times out.
                              If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    @typing.overload
    def configGetParameter(self, param: ctre._ctre.ParamEnum, valueToSend: int, ordinal: int, timeoutMs: int) -> typing.Tuple[ctre._ctre.ErrorCode, int, int]: ...
    def configSetCustomParam(self, newValue: int, paramIndex: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/declination/offset
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param newValue:   Value for custom parameter.
        :param paramIndex: Index of custom parameter. [0-1]
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSetParameter(self, param: ctre._ctre.ParamEnum, value: float, subValue: int, ordinal: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:     Parameter enumeration.
        :param value:     Value of parameter.
        :param subValue:  Subvalue for parameter. Maximum value of 255.
        :param ordinal:   Ordinal of parameter.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    @staticmethod
    def destroyAllBasePigeons() -> None: 
        """
        Destructs all pigeon objects
        """
    def get6dQuaternion(self) -> typing.Tuple[ctre._ctre.ErrorCode, typing.List[float[4]]]: 
        """
        Get 6d Quaternion data.

        :param wxyz: Array to fill with quaternion data w[0], x[1], y[2], z[3]

        :returns: The last ErrorCode generated.
        """
    def getAbsoluteCompassHeading(self) -> float: 
        """
        Get the absolute compass heading.

        :returns: compass heading [0,360) degrees.
        """
    def getAccumGyro(self) -> typing.Tuple[int, typing.List[float[3]]]: 
        """
        Get AccumGyro data.
        AccumGyro is the integrated gyro value on each axis.

        :param xyz_deg: Array to fill with x[0], y[1], and z[2] AccumGyro data

        :returns: The last ErrorCode generated.
        """
    def getAllConfigs(self, allConfigs: BasePigeonConfiguration, timeoutMs: int = 50) -> None: 
        """
        Gets all persistant settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.
        """
    def getBiasedAccelerometer(self) -> typing.Tuple[int, typing.List[int[3]]]: 
        """
        Get Biased Accelerometer data.

        :param ba_xyz: Array to fill with x[0], y[1], and z[2] data.
                       These are in fixed point notation Q2.14.  eg. 16384 = 1G

        :returns: The last ErrorCode generated.
        """
    def getBiasedMagnetometer(self) -> typing.Tuple[int, typing.List[int[3]]]: 
        """
        Get Biased Magnetometer data.

        :param bm_xyz: Array to fill with x[0], y[1], and z[2] data
                       Number is equal to 0.6 microTeslas per unit.

        :returns: The last ErrorCode generated.
        """
    def getCompassFieldStrength(self) -> float: 
        """
        Gets the compass' measured magnetic field strength.

        :returns: field strength in Microteslas (uT).
        """
    def getCompassHeading(self) -> float: 
        """
        Get the continuous compass heading.

        :returns: continuous compass heading [-23040, 23040) degrees. Use
                  SetCompassHeading to modify the wrap-around portion.
        """
    def getFirmVers(self) -> int: 
        """
        :returns: firmware version of Pigeon
        """
    def getFirmwareVersion(self) -> int: 
        """
        Gets the firmware version of the device.

        :returns: param holds the firmware version of the device. Device must be powered
                  cycled at least once.
        """
    def getLastError(self) -> ctre._ctre.ErrorCode: 
        """
        Call GetLastError() generated by this object.
        Not all functions return an error code but can
        potentially report errors.

        This function can be used to retrieve those error codes.

        :returns: The last ErrorCode generated.
        """
    def getLowLevelHandle(self) -> capsule: 
        """
        :returns: Pigeon resource handle.
        """
    def getPitch(self) -> float: 
        """
        Get the pitch from the Pigeon

        :returns: Pitch
        """
    def getRawGyro(self) -> typing.Tuple[int, typing.List[float[3]]]: 
        """
        Get Raw Gyro data.

        :param xyz_dps: Array to fill with x[0], y[1], and z[2] data in degrees per second.

        :returns: The last ErrorCode generated.
        """
    def getRawMagnetometer(self) -> typing.Tuple[int, typing.List[int[3]]]: 
        """
        Get Raw Magnetometer data.

        :param rm_xyz: Array to fill with x[0], y[1], and z[2] data
                       Number is equal to 0.6 microTeslas per unit.

        :returns: The last ErrorCode generated.
        """
    def getResetCount(self) -> int: 
        """
        :returns: number of times Pigeon Reset
        """
    def getResetFlags(self) -> int: 
        """
        :returns: Reset flags for Pigeon
        """
    def getRoll(self) -> float: 
        """
        Get the roll from the Pigeon

        :returns: Roll
        """
    def getSimCollection(self) -> BasePigeonSimCollection: 
        """
        :returns: object that can set simulation inputs.
        """
    def getStatusFramePeriod(self, frame: PigeonIMU_StatusFrame, timeoutMs: int = 0) -> int: 
        """
        Gets the period of the given status frame.

        :param frame:     Frame to get the period of.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Period of the given status frame.
        """
    def getTemp(self) -> float: 
        """
        Gets the temperature of the pigeon.

        :returns: Temperature in ('C)
        """
    def getUpTime(self) -> int: 
        """
        Gets the current Pigeon uptime.

        :returns: How long has Pigeon been running in whole seconds. Value caps at
                  255.
        """
    def getYaw(self) -> float: 
        """
        Get the yaw from the Pigeon

        :returns: Yaw
        """
    def getYawPitchRoll(self) -> typing.Tuple[ctre._ctre.ErrorCode, typing.List[float[3]]]: 
        """
        Get Yaw, Pitch, and Roll data.

        :param ypr: Array to fill with yaw[0], pitch[1], and roll[2] data.
                    *                                   Yaw is within [-368,640, +368,640] degrees.
                    *                                   Pitch is within [-90,+90] degrees.
                    *                                   Roll is within [-90,+90] degrees.

        :returns: The last ErrorCode generated.
        """
    def hasResetOccurred(self) -> bool: 
        """
        :returns: true iff a reset has occurred since last call.
        """
    def setAccumZAngle(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Sets the AccumZAngle.

        :param angleDeg:  Degrees to set AccumZAngle to.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setControlFramePeriod(self, frame: PigeonIMU_ControlFrame, periodMs: int) -> ctre._ctre.ErrorCode: 
        """
        Sets the period of the given control frame.

        :param frame:    Frame whose period is to be changed.
        :param periodMs: Period in ms for the given frame.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setStatusFramePeriod(self, statusFrame: PigeonIMU_StatusFrame, periodMs: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the period of the given status frame.

        :param statusFrame: Frame whose period is to be changed.
        :param periodMs:    Period in ms for the given frame.
        :param timeoutMs:   Timeout value in ms. If nonzero, function will wait for
                            config success and report an error if it times out.
                            If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setYaw(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Sets the Yaw register to the specified value.

        :param angleDeg:  Degree of Yaw  [+/- 368,640 degrees]
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setYawToCompass(self, timeoutMs: int = 0) -> int: 
        """
        Sets the Yaw register to match the current compass value.

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    pass
class BasePigeonConfigUtils():
    """
    Util class to help with Pigeon configurations
    """
    def __init__(self) -> None: ...
    @staticmethod
    def customParam0Different(settings: BasePigeonConfiguration) -> bool: 
        """
        Determine if specified value is different from default

        :param settings: settings to compare against

        :returns: if specified value is different from default
                  @{
        """
    @staticmethod
    def customParam1Different(settings: BasePigeonConfiguration) -> bool: ...
    pass
class BasePigeonConfiguration(ctre._ctre.CustomParamConfiguration):
    """
    Configurables available to Pigeon
    """
    def __init__(self) -> None: ...
    @typing.overload
    def toString(self) -> str: 
        """
        :returns: String representation of configs



        :param prependString: String to prepend to configs

        :returns: String representation of configs
        """
    @typing.overload
    def toString(self, prependString: str) -> str: ...
    pass
class BasePigeonSimCollection():
    """
    Collection of simulation functions available to a Pigeon IMU.
    Use the getSimCollection() function in your BasePigeon object to create the respective sim collection.
    """
    def __init__(self, pigeon: BasePigeon, isRibbonCable: bool) -> None: 
        """
        :param pigeon: Pigeon IMU to connect so sim collection
        """
    def addHeading(self, dHeading: float) -> ctre._ctre.ErrorCode: 
        """
        Adds to the simulated heading of the Pigeon IMU

        :param dHeading: the change in heading in degrees

        :returns: error code
        """
    def setRawHeading(self, newHeading: float) -> ctre._ctre.ErrorCode: 
        """
        Sets the simulated input heading position of the Pigeon IMU.

        The Pigeon IMU integrates the delta between each new raw heading value and uses
        this to calculate the true reported yaw and fused heading.

        When using the WPI Sim GUI, you will notice a readonly 'yaw' and
        settable 'RawHeading'.  The readonly signal is the emulated yaw
        which will match self-test in Tuner and the hardware API.  Changes to
        'RawHeading' will be integrated into the emulated yaw.  This way
        a simulator can modify the heading without overriding your
        hardware API calls for home-ing your sensor.

        Inputs to this function over time should be continuous,
        as user calls of setYaw() or setFusedHeading()
        will be accounted for in the calculation.

        :param newHeading: the new input heading in degrees

        :returns: error code
        """
    pass
class CANCoder(ctre._ctre.CANBusAddressable):
    """
    CTRE CANCoder.

    ::

      {@code
      // Example usage of a CANCoder
      CANCoder cancoder{0}; // creates a new CANCoder with ID 0
      
      CANCoderConfiguration config;
      // set units of the CANCoder to radians, with velocity being radians per second
      config.sensorCoefficient = 2 * M_PI / 4096.0;
      config.unitString = "rad";
      config.sensorTimeBase = SensorTimeBase::PerSecond;
      cancoder.ConfigAllSettings(config);
      
      std::cout << cancoder.GetPosition() << std::endl; // prints the position of the CANCoder
      std::cout << cancoder.GetVelocity() << std::endl; // prints the velocity recorded by the CANCoder
      
      ErrorCode error = cancoder.GetLastError(); // gets the last error generated by the CANCoder
      CANCoderFaults faults;
      ErrorCode faultsError = cancoder.GetFaults(faults); // fills faults with the current CANCoder faults; returns the last error generated
      
      cancoder.SetStatusFramePeriod(CANCoderStatusFrame_SensorData, 10); // changes the period of the sensor data frame to 10ms
      }
    """
    def __init__(self, deviceNumber: int, canbus: str = '') -> None: 
        """
        Constructor.

        :param deviceNumber: The CAN Device ID of the CANCoder.
        :param canbus:       Name of the CANbus; can be a SocketCAN interface (on Linux),
                             or a CANivore device name or serial number
        """
    def clearStickyFaults(self, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Clears the Sticky Faults

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configAbsoluteSensorRange(self, absoluteSensorRange: AbsoluteSensorRange, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the signage and range of the "Absolute Position" signal.
        Choose unsigned for an absolute range of [0,+1) rotations, [0,360) deg, etc...
        Choose signed for an absolute range of [-0.5,+0.5) rotations, [-180,+180) deg, etc...

        :param absoluteSensorRange: Desired Sign/Range for the absolute position register.
        :param timeoutMs:           Timeout value in ms. If nonzero, function will wait for
                                    config success and report an error if it times out.
                                    If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configAllSettings(self, allConfigs: CANCoderConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configFactoryDefault(self, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings to defaults (overloaded so timeoutMs is 50 ms).

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configFeedbackCoefficient(self, sensorCoefficient: float, unitString: str, sensortimeBase: SensorTimeBase, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Choose what units you want the API to get/set.  This also impacts the units displayed in Self-Test in Tuner.
        Depending on your mechanism, you may want to scale rotational units (deg, radians, rotations), or scale to a distance (inches, centimeters).

        :param sensorCoefficient: Scalar to multiply the CANCoder's native 12-bit resolute sensor. Defaults to 0.087890625 to produce degrees.
        :param unitString:        String holding the unit to report in.  This impacts all routines (except for ConfigMagnetOffset) and the self-test in Tuner.
                                  The string value itself is arbitrary.  The max number of letters will depend on firmware versioning, but generally CANCoder
                                  supports up to eight letters.  However, common units such as "centimeters" are supported explicitly despite exceeding the eight-letter limit.
                                  *                       Default is "deg"
        :param sensortimeBase:    Desired denominator to report velocity in.  This impacts GetVelocity and the reported velocity in self-test in Tuner.
                                  Default is "Per Second".
        :param timeoutMs:         Timeout value in ms. If nonzero, function will wait for
                                  config success and report an error if it times out.
                                  If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configGetCustomParam(self, paramIndex: int, timeoutMs: int = 0) -> int: 
        """
        Gets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/duty cycle/output
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param paramIndex: Index of custom parameter. [0-1]
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Value of the custom param.
        """
    @typing.overload
    def configGetParameter(self, param: ctre._ctre.ParamEnum, ordinal: int, timeoutMs: int = 0) -> float: 
        """
        Gets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:     Parameter enumeration.
        :param ordinal:   Ordinal of parameter.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Value of parameter.

        Gets a parameter by passing an int by reference

        :param param:         Parameter enumeration
        :param valueToSend:   Value to send to parameter
        :param valueReceived: Reference to integer to receive
        :param subValue:      SubValue of parameter
        :param ordinal:       Ordinal of parameter
        :param timeoutMs:     Timeout value in ms. If nonzero, function will wait for
                              config success and report an error if it times out.
                              If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    @typing.overload
    def configGetParameter(self, param: ctre._ctre.ParamEnum, valueToSend: int, ordinal: int, timeoutMs: int) -> typing.Tuple[ctre._ctre.ErrorCode, int, int]: ...
    def configMagnetOffset(self, offsetDegrees: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Adjusts the zero point for the absolute position register.
        The absolute position of the sensor will always have a discontinuity (360 -> 0 deg) or (+180 -> -180)
        and a hard-limited mechanism may have such a discontinuity in its functional range.
        In which case use this config to move the discontinuity outside of the function range.

        :param offsetDegrees: Offset in degrees (unit string and coefficient DO NOT apply for this config).
        :param timeoutMs:     Timeout value in ms. If nonzero, function will wait for
                              config success and report an error if it times out.
                              If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSensorDirection(self, bSensorDirection: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Choose which direction is interpreted as positive displacement.
        This affects both "Position" and "Absolute Position".

        :param bSensorDirection: False (default) means positive rotation occurs when magnet
                                 is spun counter-clockwise when observer is facing the LED side of CANCoder.
        :param timeoutMs:        Timeout value in ms. If nonzero, function will wait for
                                 config success and report an error if it times out.
                                 If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSensorInitializationStrategy(self, initializationStrategy: SensorInitializationStrategy, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Pick the strategy on how to initialize the CANCoder's "Position" register.  Depending on the mechanism,
        it may be desirable to auto set the Position register to match the Absolute Position (swerve for example).
        Or it may be desired to zero the sensor on boot (drivetrain translation sensor or a relative servo).

        TIP: Tuner's self-test feature will report what the boot sensor value will be in the event the CANCoder is reset.

        :param initializationStrategy: The sensor initialization strategy to use.  This will impact the behavior the next time CANCoder boots up.
        :param timeoutMs:              Timeout value in ms. If nonzero, function will wait for
                                       config success and report an error if it times out.
                                       If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSetCustomParam(self, newValue: int, paramIndex: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/duty cycle/output
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param newValue:   Value for custom parameter.
        :param paramIndex: Index of custom parameter. [0-1]
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSetParameter(self, param: ctre._ctre.ParamEnum, value: float, subValue: int, ordinal: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets a parameter. Generally this is not used.
        This can be utilized in
        - Using new features without updating API installation.
        - Errata workarounds to circumvent API implementation.
        - Allows for rapid testing / unit testing of firmware.

        :param param:     Parameter enumeration.
        :param value:     Value of parameter.
        :param subValue:  Subvalue for parameter. Maximum value of 255.
        :param ordinal:   Ordinal of parameter.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configVelocityMeasurementPeriod(self, period: SensorVelocityMeasPeriod, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configures the period of each velocity sample.
        Every 1ms a position value is sampled, and the delta between that sample
        and the position sampled kPeriod ms ago is inserted into a filter.
        kPeriod is configured with this function.

        :param period:    Desired period for the velocity measurement.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configVelocityMeasurementWindow(self, windowSize: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the number of velocity samples used in the rolling average velocity
        measurement.

        :param windowSize: Number of samples in the rolling average of velocity
                           measurement. Valid values are 1,2,4,8,16,32. If another
                           value is specified, it will truncate to nearest support value.
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    @staticmethod
    def destroyAllCANCoders() -> None: 
        """
        Destructs all CANCoder objects
        """
    def getAbsolutePosition(self) -> float: 
        """
        Gets the absolute position of the sensor.
        The absolute position may be unsigned (for example: [0,360) deg), or signed (for example: [-180,+180) deg).  This is determined by a configuration.  The default selection is unsigned.
        The units are determined by the coefficient and unit-string configuration params, default is degrees.
        Note: this signal is not affected by calls to SetPosition().

        :returns: The position of the sensor.
        """
    def getAllConfigs(self, allConfigs: CANCoderConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Gets all persistant settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getBusVoltage(self) -> float: 
        """
        Gets the bus voltage seen by the device.

        :returns: The bus voltage value (in volts).
        """
    def getFaults(self, toFill: CANCoderFaults) -> ctre._ctre.ErrorCode: 
        """
        Gets the CANCoder fault status

        :param toFill: Container for fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getFirmwareVersion(self) -> int: 
        """
        Gets the firmware version of the device.

        :returns: Firmware version of device.
        """
    def getLastError(self) -> ctre._ctre.ErrorCode: 
        """
        Call GetLastError() generated by this object.
        Not all functions return an error code but can
        potentially report errors.

        This function can be used to retrieve those error codes.

        :returns: The last ErrorCode generated.
        """
    def getLastTimestamp(self) -> float: 
        """
        *Get the timestamp of the CAN frame retrieved in the last called get routine.
        """
    def getLastUnitString(self) -> str: 
        """
        Get the units for the signal retrieved in the last called get routine.
        """
    def getMagnetFieldStrength(self) -> MagnetFieldStrength: 
        """
        Gets the magnet's health.

        :returns: The magnet health code (red/orange/green).
        """
    def getPosition(self) -> float: 
        """
        Gets the position of the sensor.  This may be relative or absolute depending on configuration.
        The units are determined by the coefficient and unit-string configuration params, default is degrees.

        :returns: The position of the sensor.
        """
    def getSimCollection(self) -> CANCoderSimCollection: 
        """
        :returns: object that can set simulation inputs.
        """
    def getStatusFramePeriod(self, frame: CANCoderStatusFrame, timeoutMs: int = 0) -> int: 
        """
        Gets the period of the given status frame.

        :param frame:     Frame to get the period of.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Period of the given status frame.
        """
    def getStickyFaults(self, toFill: CANCoderStickyFaults) -> ctre._ctre.ErrorCode: 
        """
        Gets the CANCoder sticky fault status

        :param toFill: Container for sticky fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getVelocity(self) -> float: 
        """
        Sets the position of the sensor.
        The units are determined by the coefficient and unit-string configuration params, default is degrees.

        :param newPosition: 

        :returns: ErrorCode generated by function. 0 indicates no error.
        """
    def hasResetOccurred(self) -> bool: 
        """
        Returns true if the device has reset since last call.

        :returns: Has a Device Reset Occurred?
        """
    def setPosition(self, newPosition: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the position of the sensor.
        The units are determined by the coefficient and unit-string configuration params, default is degrees.

        :param newPosition: 

        :returns: ErrorCode generated by function. 0 indicates no error.
        """
    def setPositionToAbsolute(self, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the position of the sensor to match the magnet's "Absolute Sensor".
        The units are determined by the coefficient and unit-string configuration params, default is degrees.

        :returns: ErrorCode generated by function. 0 indicates no error.
        """
    def setStatusFramePeriod(self, statusFrame: CANCoderStatusFrame, periodMs: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the period of the given status frame.

        :param statusFrame: Frame whose period is to be changed.
        :param periodMs:    Period in ms for the given frame.
        :param timeoutMs:   Timeout value in ms. If nonzero, function will wait for
                            config success and report an error if it times out.
                            If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    pass
class CANCoderConfigUtils(ctre._ctre.CustomParamConfigUtil):
    """
    Util class to help with configuring CANCoder
    """
    def __init__(self) -> None: ...
    @staticmethod
    def absoluteSensorRangeDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def initializationStrategyDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def magnetOffsetDegreesDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def sensorCoefficientDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def sensorDirectionDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def sensorTimeBaseDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def unitStringDifferent(settings: CANCoderConfiguration) -> bool: ...
    @staticmethod
    def velocityMeasurementPeriodDifferent(settings: CANCoderConfiguration) -> bool: 
        """
        Determine if specified value is different from default

        :param settings: settings to compare against

        :returns: if specified value is different from default
                  @{
        """
    @staticmethod
    def velocityMeasurementWindowDifferent(settings: CANCoderConfiguration) -> bool: ...
    pass
class CANCoderConfiguration(ctre._ctre.CustomParamConfiguration):
    """
    Configurables available to CANCoder
    """
    def __init__(self) -> None: 
        """
        Constructor
        """
    def __str__(self) -> str: 
        """
        :returns: String representation of configs
        """
    def toString(self, prependString: str) -> str: 
        """
        :param prependString: String to prepend to configs

        :returns: String representation of configs
        """
    @property
    def absoluteSensorRange(self) -> AbsoluteSensorRange:
        """
        Desired Sign / Range for the absolute position register.
        Choose unsigned for an absolute range of[0, +1) rotations, [0, 360) deg, etc.
        Choose signed for an absolute range of[-0.5, +0.5) rotations, [-180, +180) deg, etc.

        :type: AbsoluteSensorRange
        """
    @absoluteSensorRange.setter
    def absoluteSensorRange(self, arg0: AbsoluteSensorRange) -> None:
        """
        Desired Sign / Range for the absolute position register.
        Choose unsigned for an absolute range of[0, +1) rotations, [0, 360) deg, etc.
        Choose signed for an absolute range of[-0.5, +0.5) rotations, [-180, +180) deg, etc.
        """
    @property
    def initializationStrategy(self) -> SensorInitializationStrategy:
        """
        The sensor initialization strategy to use.This will impact the behavior the next time CANCoder boots up.

        Pick the strategy on how to initialize the CANCoder's "Position" register.  Depending on the mechanism,
        it may be desirable to auto set the Position register to match the Absolute Position(swerve for example).
        Or it may be desired to zero the sensor on boot(drivetrain translation sensor or a relative servo).

        TIP: Tuner's self-test feature will report what the boot sensor value will be in the event the CANCoder is reset.

        :type: SensorInitializationStrategy
        """
    @initializationStrategy.setter
    def initializationStrategy(self, arg0: SensorInitializationStrategy) -> None:
        """
        The sensor initialization strategy to use.This will impact the behavior the next time CANCoder boots up.

        Pick the strategy on how to initialize the CANCoder's "Position" register.  Depending on the mechanism,
        it may be desirable to auto set the Position register to match the Absolute Position(swerve for example).
        Or it may be desired to zero the sensor on boot(drivetrain translation sensor or a relative servo).

        TIP: Tuner's self-test feature will report what the boot sensor value will be in the event the CANCoder is reset.
        """
    @property
    def magnetOffsetDegrees(self) -> float:
        """
        Adjusts the zero point for the absolute position register.
        The absolute position of the sensor will always have a discontinuity (360 -> 0 deg) or (+180 -> -180)
        and a hard-limited mechanism may have such a discontinuity in its functional range.
        In which case use this config to move the discontinuity outside of the function range.

        :type: float
        """
    @magnetOffsetDegrees.setter
    def magnetOffsetDegrees(self, arg0: float) -> None:
        """
        Adjusts the zero point for the absolute position register.
        The absolute position of the sensor will always have a discontinuity (360 -> 0 deg) or (+180 -> -180)
        and a hard-limited mechanism may have such a discontinuity in its functional range.
        In which case use this config to move the discontinuity outside of the function range.
        """
    @property
    def sensorCoefficient(self) -> float:
        """
        Scalar to multiply the CANCoder's native 12-bit resolute sensor. Defaults to 0.087890625 to produce degrees.

        :type: float
        """
    @sensorCoefficient.setter
    def sensorCoefficient(self, arg0: float) -> None:
        """
        Scalar to multiply the CANCoder's native 12-bit resolute sensor. Defaults to 0.087890625 to produce degrees.
        """
    @property
    def sensorDirection(self) -> bool:
        """
        Choose which direction is interpreted as positive displacement.
        This affects both "Position"and "Absolute Position".
        False(default) means positive rotation occurs when magnet
        is spun counter - clockwise when observer is facing the LED side of CANCoder.

        :type: bool
        """
    @sensorDirection.setter
    def sensorDirection(self, arg0: bool) -> None:
        """
        Choose which direction is interpreted as positive displacement.
        This affects both "Position"and "Absolute Position".
        False(default) means positive rotation occurs when magnet
        is spun counter - clockwise when observer is facing the LED side of CANCoder.
        """
    @property
    def sensorTimeBase(self) -> SensorTimeBase:
        """
        Desired denominator to report velocity in. This impacts GetVelocityand the reported velocity in self-test in Tuner.
        Default is "Per Second".

        :type: SensorTimeBase
        """
    @sensorTimeBase.setter
    def sensorTimeBase(self, arg0: SensorTimeBase) -> None:
        """
        Desired denominator to report velocity in. This impacts GetVelocityand the reported velocity in self-test in Tuner.
        Default is "Per Second".
        """
    @property
    def unitString(self) -> str:
        """
        String holding the unit to report in.  This impacts all routines(except for ConfigMagnetOffset) and the self-test in Tuner.
        The string value itself is arbitrary.The max number of letters will depend on firmware versioning, but generally CANCoder
        supports up to eight letters.However, common units such as "centimeters" are supported explicitly despite exceeding the eight-letter limit.
        Default is "deg"

        :type: str
        """
    @unitString.setter
    def unitString(self, arg0: str) -> None:
        """
        String holding the unit to report in.  This impacts all routines(except for ConfigMagnetOffset) and the self-test in Tuner.
        The string value itself is arbitrary.The max number of letters will depend on firmware versioning, but generally CANCoder
        supports up to eight letters.However, common units such as "centimeters" are supported explicitly despite exceeding the eight-letter limit.
        Default is "deg"
        """
    @property
    def velocityMeasurementPeriod(self) -> SensorVelocityMeasPeriod:
        """
        Velocity measurement period to use

        :type: SensorVelocityMeasPeriod
        """
    @velocityMeasurementPeriod.setter
    def velocityMeasurementPeriod(self, arg0: SensorVelocityMeasPeriod) -> None:
        """
        Velocity measurement period to use
        """
    @property
    def velocityMeasurementWindow(self) -> int:
        """
        Velocity measurement window to use

        :type: int
        """
    @velocityMeasurementWindow.setter
    def velocityMeasurementWindow(self, arg0: int) -> None:
        """
        Velocity measurement window to use
        """
    pass
class CANCoderFaults():
    """
    Faults available to CANCoderFaults
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @property
    def APIError(self) -> bool:
        """
        API error detected.  Make sure API and firmware versions are compatible.

        :type: bool
        """
    @APIError.setter
    def APIError(self, arg0: bool) -> None:
        """
        API error detected.  Make sure API and firmware versions are compatible.
        """
    @property
    def HardwareFault(self) -> bool:
        """
        Device detects hardware failure

        :type: bool
        """
    @HardwareFault.setter
    def HardwareFault(self, arg0: bool) -> None:
        """
        Device detects hardware failure
        """
    @property
    def MagnetTooWeak(self) -> bool:
        """
        Magnet strength is too weak to provide reliable results
        Make sure CANCoder is close to the magnet being used

        :type: bool
        """
    @MagnetTooWeak.setter
    def MagnetTooWeak(self, arg0: bool) -> None:
        """
        Magnet strength is too weak to provide reliable results
        Make sure CANCoder is close to the magnet being used
        """
    @property
    def ResetDuringEn(self) -> bool:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.

        :type: bool
        """
    @ResetDuringEn.setter
    def ResetDuringEn(self, arg0: bool) -> None:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.
        """
    @property
    def UnderVoltage(self) -> bool:
        """
        Device is under 6.5V

        :type: bool
        """
    @UnderVoltage.setter
    def UnderVoltage(self, arg0: bool) -> None:
        """
        Device is under 6.5V
        """
    pass
class CANCoderSimCollection():
    """
    Collection of simulation functions available to a CANCoder.

    Use the getSimCollection() function in your CANCoder object to create the respective sim collection.
    """
    def __init__(self, canCoder: CANCoder) -> None: 
        """
        Constructor for CANCoderSimCollection

        :param canCoder: CANCoder to connect Collection to
        """
    def addPosition(self, dPos: int) -> ctre._ctre.ErrorCode: 
        """
        Adds to the simulated position of the CANCoder.

        :param dPos: the change in position in native units

        :returns: error code
        """
    def setBusVoltage(self, vbat: float) -> ctre._ctre.ErrorCode: 
        """
        Sets the simulated bus voltage of the CANCoder.

        The minimum allowed bus voltage is 4 V - values
        below this will be promoted to 4 V.

        :param vbat: the bus voltage in volts

        :returns: error code
        """
    def setRawPosition(self, newPos: int) -> ctre._ctre.ErrorCode: 
        """
        Sets the simulated raw position of the CANCoder.

        The CANCoder integrates this to calculate the true reported position.

        When using the WPI Sim GUI, you will notice a readonly 'position' and
        settable 'rawPositionInput'.  The readonly signal is the emulated position
        which will match self-test in Tuner and the hardware API.  Changes to
        'rawPositionInput' will be integrated into the emulated position.  This way
        a simulator can modify the position without overriding your
        hardware API calls for home-ing your sensor.

        Inputs to this function over time should be continuous, as user calls
        of setPosition() will be accounted for in the calculation.

        :param newPos: the new raw position in native units

        :returns: error code
        """
    def setVelocity(self, newVel: int) -> ctre._ctre.ErrorCode: 
        """
        Sets the simulated velocity of the CANCoder.

        :param newVel: the new velocity in native units per 100ms

        :returns: error code
        """
    pass
class CANCoderStatusFrame():
    """
    Enumerated type for status frame types.

    Members:

      SensorData

      VbatAndFaults
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    SensorData: ctre._ctre.sensors.CANCoderStatusFrame # value = <CANCoderStatusFrame.SensorData: 267264>
    VbatAndFaults: ctre._ctre.sensors.CANCoderStatusFrame # value = <CANCoderStatusFrame.VbatAndFaults: 267328>
    __members__: dict # value = {'SensorData': <CANCoderStatusFrame.SensorData: 267264>, 'VbatAndFaults': <CANCoderStatusFrame.VbatAndFaults: 267328>}
    pass
class CANCoderStickyFaults():
    """
    Sticky Faults for CANCoder (Currently has none)
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @property
    def APIError(self) -> bool:
        """
        API error detected.  Make sure API and firmware versions are compatible.

        :type: bool
        """
    @APIError.setter
    def APIError(self, arg0: bool) -> None:
        """
        API error detected.  Make sure API and firmware versions are compatible.
        """
    @property
    def HardwareFault(self) -> bool:
        """
        Device detects hardware failure

        :type: bool
        """
    @HardwareFault.setter
    def HardwareFault(self, arg0: bool) -> None:
        """
        Device detects hardware failure
        """
    @property
    def MagnetTooWeak(self) -> bool:
        """
        Magnet strength is too weak to provide reliable results
        Make sure CANCoder is close to the magnet being used

        :type: bool
        """
    @MagnetTooWeak.setter
    def MagnetTooWeak(self, arg0: bool) -> None:
        """
        Magnet strength is too weak to provide reliable results
        Make sure CANCoder is close to the magnet being used
        """
    @property
    def ResetDuringEn(self) -> bool:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.

        :type: bool
        """
    @ResetDuringEn.setter
    def ResetDuringEn(self, arg0: bool) -> None:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.
        """
    @property
    def UnderVoltage(self) -> bool:
        """
        Device is under 6.5V

        :type: bool
        """
    @UnderVoltage.setter
    def UnderVoltage(self, arg0: bool) -> None:
        """
        Device is under 6.5V
        """
    pass
class MagnetFieldStrength():
    """
    Indicates the magnet field strength of a magnet-based sensor

    Members:

      Invalid_Unknown : Magnet Field strength cannot be determined

      BadRange_RedLED : Magnet field is far too low (too far) or far too high (too close).

      Adequate_OrangeLED : Magnet field is adequate, sensor can be used in this range with slightly reduced accuracy.

      Good_GreenLED : Magnet field is ideal
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Adequate_OrangeLED: ctre._ctre.sensors.MagnetFieldStrength # value = <MagnetFieldStrength.Adequate_OrangeLED: 2>
    BadRange_RedLED: ctre._ctre.sensors.MagnetFieldStrength # value = <MagnetFieldStrength.BadRange_RedLED: 1>
    Good_GreenLED: ctre._ctre.sensors.MagnetFieldStrength # value = <MagnetFieldStrength.Good_GreenLED: 3>
    Invalid_Unknown: ctre._ctre.sensors.MagnetFieldStrength # value = <MagnetFieldStrength.Invalid_Unknown: 0>
    __members__: dict # value = {'Invalid_Unknown': <MagnetFieldStrength.Invalid_Unknown: 0>, 'BadRange_RedLED': <MagnetFieldStrength.BadRange_RedLED: 1>, 'Adequate_OrangeLED': <MagnetFieldStrength.Adequate_OrangeLED: 2>, 'Good_GreenLED': <MagnetFieldStrength.Good_GreenLED: 3>}
    pass
class Pigeon2(BasePigeon, ctre._ctre.CANBusAddressable):
    """
    Pigeon 2 Class. Class supports communicating over CANbus.

    ::

      {@code
      // Example usage of a Pigeon 2
      Pigeon2 pigeon{0}; // creates a new Pigeon2 with ID 0
      
      Pigeon2Configuration config;
      // set mount pose as rolled 90 degrees counter-clockwise
      config.MountPoseYaw = 0;
      config.MountPosePitch = 0;
      config.MountPoseRoll = 90;
      pigeon.ConfigAllSettings(config);
      
      std::cout << pigeon.GetYaw() << std::endl; // prints the yaw of the Pigeon
      std::cout << pigeon.GetPitch() << std::endl; // prints the pitch of the Pigeon
      std::cout << pigeon.GetRoll() << std::endl; // prints the roll of the Pigeon
      
      double gravityVec[3];
      pigeon.GetGravityVector(gravityVec); // gets the gravity vector of the Pigeon 2
      
      ErrorCode error = pigeon.GetLastError(); // gets the last error generated by the Pigeon
      Pigeon2_Faults faults;
      ErrorCode faultsError = pigeon.GetFaults(faults); // fills faults with the current Pigeon 2 faults; returns the last error generated
      }
    """
    def __init__(self, deviceNumber: int, canbus: str = '') -> None: 
        """
        Create a Pigeon object that communicates with Pigeon on CAN Bus.

        :param deviceNumber: CAN Device Id of Pigeon [0,62]
        :param canbus:       Name of the CANbus; can be a SocketCAN interface (on Linux),
                             or a CANivore device name or serial number
        """
    def configAllSettings(self, settings: Pigeon2Configuration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configDisableNoMotionCalibration(self, disable: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Disables the no-motion calibration from Pigeon2

        :param disable:   Boolean to disable/enable no-motion calibration
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: ErrorCode Status of the config response
        """
    def configDisableTemperatureCompensation(self, disable: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Disables temperature compensation from Pigeon2.

        :param disable:   Boolean to disable/enable temperature compensation
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: ErrorCode Status of the config response
        """
    def configEnableCompass(self, enable: bool, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Enables the magnetometer fusion for Pigeon2. This is **not** recommended for FRC use

        :param enable:    Boolean to enable/disable magnetometer fusion
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: ErrorCode Status of the config response
        """
    @typing.overload
    def configMountPose(self, forward: AxisDirection, up: AxisDirection, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configure the Mount Pose using the primary axis.
        This is useful if the Pigeon 2.0 is mounted straight, and you only
        need to describe what axis is forward and what axis is up.

        :param forward:   Axis that points forward from the robot
        :param up:        Axis that points up from the robot
        :param timeoutMs: Config timeout in milliseconds.

        :returns: OK if successful, InvalidParamValue if both forward and up are of the same primary axis, otherwise config return.

        Configure the mounting pose of the Pigeon2.
        This is the Yaw-Pitch-Roll the Pigeon2 underwent to get to its current
        orientation, referenced from the robot's point of view.
        This is only necessary if the Pigeon2 is mounted at an exotic angle
        near the gimbal lock point or not forward.
        If the pigeon is relatively flat and pointed forward, this is not needed.

        Examples:
        If the Pigeon2 is pointed directly right, that corresponds to a -90 yaw,
        0 pitch, and 0 roll, as it yaw'd 90 degrees clockwise.
        If the Pigeon2 points upwards, that's a 0 yaw, -90 pitch, 0 roll, as it
        pitched 90 degrees clockwise.

        :param yaw:       Yaw angle needed to reach the current orientation in degrees.
        :param pitch:     Pitch angle needed to reach the current orientation in degrees.
        :param roll:      Roll angle needed to reach the current orientation in degrees.
        :param timeoutMs: Config timeout in milliseconds.

        :returns: Worst error code of all config sets.
        """
    @typing.overload
    def configMountPose(self, yaw: float, pitch: float, roll: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: ...
    def configMountPosePitch(self, pitch: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configure the mounting pose Pitch of the Pigeon2.
        See :meth:`.configMountPose`

        :param pitch:     Pitch angle needed to reach the current orientation in degrees.
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode of configSet
        """
    def configMountPoseRoll(self, roll: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configure the mounting pose Roll of the Pigeon2.
        See :meth:`.configMountPose`

        :param roll:      Roll angle needed to reach the current orientation in degrees.
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode of configSet
        """
    def configMountPoseYaw(self, yaw: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configure the mounting pose Yaw of the Pigeon2.
        See :meth:`.configMountPose`

        :param yaw:       Yaw angle needed to reach the current orientation in degrees.
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode of configSet
        """
    def configXAxisGyroError(self, err: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configures the X Axis Gyroscope Error for 1 rotation

        :param err:       Degrees that Pigeon 2.0 overshot after 1 rotation (i.e. overshot 1 degree is 1; undershot by 3 degrees is -3)
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode fo configSet
        """
    def configYAxisGyroError(self, err: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configures the Y Axis Gyroscope Error for 1 rotation

        :param err:       Degrees that Pigeon 2.0 overshot after 1 rotation (i.e. overshot 1 degree is 1; undershot by 3 degrees is -3)
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode fo configSet
        """
    def configZAxisGyroError(self, err: float, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Configures the Z Axis Gyroscope Error for 1 rotation

        :param err:       Degrees that Pigeon 2.0 overshot after 1 rotation (i.e. overshot 1 degree is 1; undershot by 3 degrees is -3)
        :param timeoutMs: Config timeout in milliseconds.

        :returns: ErrorCode fo configSet
        """
    def getAllConfigs(self, allConfigs: Pigeon2Configuration, timeoutMs: int = 50) -> None: 
        """
        Gets all persistant settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.
        """
    def getFaults(self, toFill: Pigeon2_Faults) -> ctre._ctre.ErrorCode: 
        """
        Gets the fault status

        :param toFill: Container for fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getGravityVector(self) -> typing.Tuple[ctre._ctre.ErrorCode, typing.List[float[3]]]: 
        """
        Get the Gravity Vector.

        This provides a vector that points toward ground. This is useful for applications like
        an arm, where the z-value of the gravity vector corresponds to the feed-forward needed
        to hold the arm steady.
        The gravity vector is calculated after the mount pose, so if the pigeon is where it was
        mounted, the gravity vector is {0, 0, 1}.

        :param gravVector: Pass in a double array of size 3 to get the gravity vector

        :returns: Errorcode of getter
        """
    def getStickyFaults(self, toFill: Pigeon2_StickyFaults) -> ctre._ctre.ErrorCode: 
        """
        Gets the sticky fault status

        :param toFill: Container for sticky fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def zeroGyroBiasNow(self, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Performs an offset calibration on gyro bias

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: ErrorCode Status of the config response
        """
    pass
class Pigeon2ConfigUtils():
    """
    Util class to help with Pigeon configurations
    """
    @staticmethod
    def XAxisGyroErrorDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def YAxisGyroErrorDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def ZAxisGyroErrorDifferent(settings: Pigeon2Configuration) -> bool: ...
    def __init__(self) -> None: ...
    @staticmethod
    def customParam0Different(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def customParam1Different(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def disableNoMotionCalibrationDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def disableTemperatureCompensationDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def enableCompassDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def mountPosePitchDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def mountPoseRollDifferent(settings: Pigeon2Configuration) -> bool: ...
    @staticmethod
    def mountPoseYawDifferent(settings: Pigeon2Configuration) -> bool: 
        """
        Determine if specified value is different from default

        :param settings: settings to compare against

        :returns: if specified value is different from default
                  @{
        """
    pass
class Pigeon2Configuration(ctre._ctre.CustomParamConfiguration):
    """
    Configurables available to Pigeon
    """
    def __init__(self) -> None: ...
    @typing.overload
    def toString(self) -> str: 
        """
        :returns: String representation of configs



        :param prependString: String to prepend to configs

        :returns: String representation of configs
        """
    @typing.overload
    def toString(self, prependString: str) -> str: ...
    pass
class Pigeon2_Faults():
    """
    Sticky faults available to Pigeon
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @property
    def APIError(self) -> bool:
        """
        API error detected.  Make sure API and firmware versions are compatible.

        :type: bool
        """
    @APIError.setter
    def APIError(self, arg0: bool) -> None:
        """
        API error detected.  Make sure API and firmware versions are compatible.
        """
    @property
    def AccelFault(self) -> bool:
        """
        The Accelerometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large impact.

        :type: bool
        """
    @AccelFault.setter
    def AccelFault(self, arg0: bool) -> None:
        """
        The Accelerometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large impact.
        """
    @property
    def BootIntoMotion(self) -> bool:
        """
        The Pigeon saw motion as soon as it booted, and didn't
        attempt to self-test its features.
        This isn't an issue, but to prevent this don't turn the
        robot on while moving it.

        :type: bool
        """
    @BootIntoMotion.setter
    def BootIntoMotion(self, arg0: bool) -> None:
        """
        The Pigeon saw motion as soon as it booted, and didn't
        attempt to self-test its features.
        This isn't an issue, but to prevent this don't turn the
        robot on while moving it.
        """
    @property
    def GyroFault(self) -> bool:
        """
        The gyro failed its self-test.
        This is likely due to hardware damage.

        :type: bool
        """
    @GyroFault.setter
    def GyroFault(self, arg0: bool) -> None:
        """
        The gyro failed its self-test.
        This is likely due to hardware damage.
        """
    @property
    def HardwareFault(self) -> bool:
        """
        Device detects hardware failure

        :type: bool
        """
    @HardwareFault.setter
    def HardwareFault(self, arg0: bool) -> None:
        """
        Device detects hardware failure
        """
    @property
    def MagnetometerFault(self) -> bool:
        """
        The magnetometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large magnetic field.

        :type: bool
        """
    @MagnetometerFault.setter
    def MagnetometerFault(self, arg0: bool) -> None:
        """
        The magnetometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large magnetic field.
        """
    @property
    def ResetDuringEn(self) -> bool:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.

        :type: bool
        """
    @ResetDuringEn.setter
    def ResetDuringEn(self, arg0: bool) -> None:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.
        """
    @property
    def SaturatedAccel(self) -> bool:
        """
        The device saw an acceleration that exceeded its maximum.
        Increase the range or avoid high-g events.

        :type: bool
        """
    @SaturatedAccel.setter
    def SaturatedAccel(self, arg0: bool) -> None:
        """
        The device saw an acceleration that exceeded its maximum.
        Increase the range or avoid high-g events.
        """
    @property
    def SaturatedMag(self) -> bool:
        """
        The device saw a magnetic field that exceeded its maximum.
        Keep the device far from strong magnetic fields.

        :type: bool
        """
    @SaturatedMag.setter
    def SaturatedMag(self, arg0: bool) -> None:
        """
        The device saw a magnetic field that exceeded its maximum.
        Keep the device far from strong magnetic fields.
        """
    @property
    def SaturatedRotVelocity(self) -> bool:
        """
        The device rotated at a rate that exceeded its maximum.
        Increase the range or slow the rate of rotation.

        :type: bool
        """
    @SaturatedRotVelocity.setter
    def SaturatedRotVelocity(self, arg0: bool) -> None:
        """
        The device rotated at a rate that exceeded its maximum.
        Increase the range or slow the rate of rotation.
        """
    @property
    def UnderVoltage(self) -> bool:
        """
        Device is under 6.5V

        :type: bool
        """
    @UnderVoltage.setter
    def UnderVoltage(self, arg0: bool) -> None:
        """
        Device is under 6.5V
        """
    pass
class Pigeon2_StickyFaults():
    """
    Sticky faults available to Pigeon
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @property
    def APIError(self) -> bool:
        """
        API error detected.  Make sure API and firmware versions are compatible.

        :type: bool
        """
    @APIError.setter
    def APIError(self, arg0: bool) -> None:
        """
        API error detected.  Make sure API and firmware versions are compatible.
        """
    @property
    def AccelFault(self) -> bool:
        """
        The Accelerometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large impact.

        :type: bool
        """
    @AccelFault.setter
    def AccelFault(self, arg0: bool) -> None:
        """
        The Accelerometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large impact.
        """
    @property
    def BootIntoMotion(self) -> bool:
        """
        The Pigeon saw motion as soon as it booted, and didn't
        attempt to self-test its features.
        This isn't an issue, but to prevent this don't turn the
        robot on while moving it.

        :type: bool
        """
    @BootIntoMotion.setter
    def BootIntoMotion(self, arg0: bool) -> None:
        """
        The Pigeon saw motion as soon as it booted, and didn't
        attempt to self-test its features.
        This isn't an issue, but to prevent this don't turn the
        robot on while moving it.
        """
    @property
    def GyroFault(self) -> bool:
        """
        The gyro failed its self-test.
        This is likely due to hardware damage.

        :type: bool
        """
    @GyroFault.setter
    def GyroFault(self, arg0: bool) -> None:
        """
        The gyro failed its self-test.
        This is likely due to hardware damage.
        """
    @property
    def HardwareFault(self) -> bool:
        """
        Device detects hardware failure

        :type: bool
        """
    @HardwareFault.setter
    def HardwareFault(self, arg0: bool) -> None:
        """
        Device detects hardware failure
        """
    @property
    def MagnetometerFault(self) -> bool:
        """
        The magnetometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large magnetic field.

        :type: bool
        """
    @MagnetometerFault.setter
    def MagnetometerFault(self, arg0: bool) -> None:
        """
        The magnetometer failed its self-test.
        This is likely due to hardware damage, oftentimes from
        exposing the Pigeon to a very large magnetic field.
        """
    @property
    def ResetDuringEn(self) -> bool:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.

        :type: bool
        """
    @ResetDuringEn.setter
    def ResetDuringEn(self, arg0: bool) -> None:
        """
        Device was powered-on or reset while robot is enabled.
        Check your breakers and wiring.
        """
    @property
    def SaturatedAccel(self) -> bool:
        """
        The device saw an acceleration that exceeded its maximum.
        Increase the range or avoid high-g events.

        :type: bool
        """
    @SaturatedAccel.setter
    def SaturatedAccel(self, arg0: bool) -> None:
        """
        The device saw an acceleration that exceeded its maximum.
        Increase the range or avoid high-g events.
        """
    @property
    def SaturatedMag(self) -> bool:
        """
        The device saw a magnetic field that exceeded its maximum.
        Keep the device far from strong magnetic fields.

        :type: bool
        """
    @SaturatedMag.setter
    def SaturatedMag(self, arg0: bool) -> None:
        """
        The device saw a magnetic field that exceeded its maximum.
        Keep the device far from strong magnetic fields.
        """
    @property
    def SaturatedRotVelocity(self) -> bool:
        """
        The device rotated at a rate that exceeded its maximum.
        Increase the range or slow the rate of rotation.

        :type: bool
        """
    @SaturatedRotVelocity.setter
    def SaturatedRotVelocity(self, arg0: bool) -> None:
        """
        The device rotated at a rate that exceeded its maximum.
        Increase the range or slow the rate of rotation.
        """
    @property
    def UnderVoltage(self) -> bool:
        """
        Device is under 6.5V

        :type: bool
        """
    @UnderVoltage.setter
    def UnderVoltage(self, arg0: bool) -> None:
        """
        Device is under 6.5V
        """
    pass
class PigeonIMU(BasePigeon, ctre._ctre.CANBusAddressable):
    """
    Pigeon IMU Class.
    Class supports communicating over CANbus and over ribbon-cable (CAN Talon SRX).
    """
    class CalibrationMode():
        """
        Various calibration modes supported by Pigeon.

        Note that you can instead use Phoenix Tuner to accomplish certain calibrations.

        Members:

          BootTareGyroAccel : Boot-Calibrate the pigeon

          Temperature : Temperature-Calibrate the pigeon

          Magnetometer12Pt : Magnetometer-Calibrate the pigeon using the 12pt process

          Magnetometer360 : Magnetometer-Calibrate the pigeon using 360 turns

          Accelerometer : Calibrate the pigeon accelerometer
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        Accelerometer: ctre._ctre.sensors.PigeonIMU.CalibrationMode # value = <CalibrationMode.Accelerometer: 5>
        BootTareGyroAccel: ctre._ctre.sensors.PigeonIMU.CalibrationMode # value = <CalibrationMode.BootTareGyroAccel: 0>
        Magnetometer12Pt: ctre._ctre.sensors.PigeonIMU.CalibrationMode # value = <CalibrationMode.Magnetometer12Pt: 2>
        Magnetometer360: ctre._ctre.sensors.PigeonIMU.CalibrationMode # value = <CalibrationMode.Magnetometer360: 3>
        Temperature: ctre._ctre.sensors.PigeonIMU.CalibrationMode # value = <CalibrationMode.Temperature: 1>
        __members__: dict # value = {'BootTareGyroAccel': <CalibrationMode.BootTareGyroAccel: 0>, 'Temperature': <CalibrationMode.Temperature: 1>, 'Magnetometer12Pt': <CalibrationMode.Magnetometer12Pt: 2>, 'Magnetometer360': <CalibrationMode.Magnetometer360: 3>, 'Accelerometer': <CalibrationMode.Accelerometer: 5>}
        pass
    class FusionStatus():
        """
        Data object for holding fusion information.
        """
        def __init__(self) -> None: ...
        @property
        def bIsFusing(self) -> bool:
            """
            Whether the pigeon is fusing

            :type: bool
            """
        @bIsFusing.setter
        def bIsFusing(self, arg0: bool) -> None:
            """
            Whether the pigeon is fusing
            """
        @property
        def bIsValid(self) -> bool:
            """
            Whether the fusion is valid

            :type: bool
            """
        @bIsValid.setter
        def bIsValid(self, arg0: bool) -> None:
            """
            Whether the fusion is valid
            """
        @property
        def description(self) -> str:
            """
            Description of fusion status

            :type: str
            """
        @description.setter
        def description(self, arg0: str) -> None:
            """
            Description of fusion status
            """
        @property
        def heading(self) -> float:
            """
            Fused Heading

            :type: float
            """
        @heading.setter
        def heading(self, arg0: float) -> None:
            """
            Fused Heading
            """
        @property
        def lastError(self) -> int:
            """
            Same as GetLastError()

            :type: int
            """
        @lastError.setter
        def lastError(self, arg0: int) -> None:
            """
            Same as GetLastError()
            """
        pass
    class GeneralStatus():
        """
        Data object for status on current calibration and general status.

        Pigeon has many calibration modes supported for a variety of uses.
        The modes generally collects and saves persistently information that makes
        the Pigeon signals more accurate.  This includes collecting temperature, gyro, accelerometer,
        and compass information.

        For FRC use-cases, typically compass and temperature calibration is not required.

        Additionally when motion driver software in the Pigeon boots, it will perform a fast boot calibration
        to initially bias gyro and setup accelerometer.

        These modes can be enabled with the EnterCalibration mode.

        When a calibration mode is entered, caller can expect...

        - PigeonState to reset to Initializing and bCalIsBooting is set to true.  Pigeon LEDs will blink the boot pattern.
        This is similar to the normal boot cal, however it can an additional ~30 seconds since calibration generally
        requires more information.
        currentMode will reflect the user's selected calibration mode.

        - PigeonState will eventually settle to UserCalibration and Pigeon LEDs will show cal specific blink patterns.
        bCalIsBooting is now false.

        - Follow the instructions in the Pigeon User Manual to meet the calibration specific requirements.
        When finished calibrationError will update with the result.
        Pigeon will solid-fill LEDs with red (for failure) or green (for success) for ~5 seconds.
        Pigeon then perform boot-cal to cleanly apply the newly saved calibration data.
        """
        def __init__(self) -> None: ...
        @property
        def bCalIsBooting(self) -> bool:
            """
            After caller requests a calibration mode, pigeon will perform a boot-cal before
            entering the requested mode.  During this period, this flag is set to true.

            :type: bool
            """
        @bCalIsBooting.setter
        def bCalIsBooting(self, arg0: bool) -> None:
            """
            After caller requests a calibration mode, pigeon will perform a boot-cal before
            entering the requested mode.  During this period, this flag is set to true.
            """
        @property
        def calibrationError(self) -> int:
            """
            The error code for the last calibration mode.
            Zero represents a successful cal (with solid green LEDs at end of cal)
            and nonzero is a failed calibration (with solid red LEDs at end of cal).
            Different calibration

            :type: int
            """
        @calibrationError.setter
        def calibrationError(self, arg0: int) -> None:
            """
            The error code for the last calibration mode.
            Zero represents a successful cal (with solid green LEDs at end of cal)
            and nonzero is a failed calibration (with solid red LEDs at end of cal).
            Different calibration
            """
        @property
        def currentMode(self) -> PigeonIMU.CalibrationMode:
            """
            The currently applied calibration mode if state is in UserCalibration or if bCalIsBooting is true.
            Otherwise it holds the last selected calibration mode (when calibrationError was updated).

            :type: PigeonIMU.CalibrationMode
            """
        @currentMode.setter
        def currentMode(self, arg0: PigeonIMU.CalibrationMode) -> None:
            """
            The currently applied calibration mode if state is in UserCalibration or if bCalIsBooting is true.
            Otherwise it holds the last selected calibration mode (when calibrationError was updated).
            """
        @property
        def description(self) -> str:
            """
            general string description of current status

            :type: str
            """
        @description.setter
        def description(self, arg0: str) -> None:
            """
            general string description of current status
            """
        @property
        def lastError(self) -> int:
            """
            Same as GetLastError()

            :type: int
            """
        @lastError.setter
        def lastError(self, arg0: int) -> None:
            """
            Same as GetLastError()
            """
        @property
        def noMotionBiasCount(self) -> int:
            """
            Number of times the Pigeon has automatically rebiased the gyro.
            This counter overflows from 15 -> 0 with no cap.

            :type: int
            """
        @noMotionBiasCount.setter
        def noMotionBiasCount(self, arg0: int) -> None:
            """
            Number of times the Pigeon has automatically rebiased the gyro.
            This counter overflows from 15 -> 0 with no cap.
            """
        @property
        def state(self) -> PigeonIMU.PigeonState:
            """
            The current state of the motion driver.  This reflects if the sensor signals are accurate.
            Most calibration modes will force Pigeon to reinit the motion driver.

            :type: PigeonIMU.PigeonState
            """
        @state.setter
        def state(self, arg0: PigeonIMU.PigeonState) -> None:
            """
            The current state of the motion driver.  This reflects if the sensor signals are accurate.
            Most calibration modes will force Pigeon to reinit the motion driver.
            """
        @property
        def tempC(self) -> float:
            """
            Temperature in Celsius

            :type: float
            """
        @tempC.setter
        def tempC(self, arg0: float) -> None:
            """
            Temperature in Celsius
            """
        @property
        def tempCompensationCount(self) -> int:
            """
            Number of times the Pigeon has temperature compensated the various signals.
            This counter overflows from 15 -> 0 with no cap.

            :type: int
            """
        @tempCompensationCount.setter
        def tempCompensationCount(self, arg0: int) -> None:
            """
            Number of times the Pigeon has temperature compensated the various signals.
            This counter overflows from 15 -> 0 with no cap.
            """
        @property
        def upTimeSec(self) -> int:
            """
            Number of seconds Pigeon has been up (since boot).
            This register is reset on power boot or processor reset.
            Register is capped at 255 seconds with no wrap around.

            :type: int
            """
        @upTimeSec.setter
        def upTimeSec(self, arg0: int) -> None:
            """
            Number of seconds Pigeon has been up (since boot).
            This register is reset on power boot or processor reset.
            Register is capped at 255 seconds with no wrap around.
            """
        pass
    class PigeonState():
        """
        Overall state of the Pigeon.

        Members:

          NoComm : No communications with Pigeon

          Initializing : Pigeon is initializing

          Ready : Pigeon is ready

          UserCalibration : Pigeon is calibrating due to user
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        Initializing: ctre._ctre.sensors.PigeonIMU.PigeonState # value = <PigeonState.Initializing: 1>
        NoComm: ctre._ctre.sensors.PigeonIMU.PigeonState # value = <PigeonState.NoComm: 0>
        Ready: ctre._ctre.sensors.PigeonIMU.PigeonState # value = <PigeonState.Ready: 2>
        UserCalibration: ctre._ctre.sensors.PigeonIMU.PigeonState # value = <PigeonState.UserCalibration: 3>
        __members__: dict # value = {'NoComm': <PigeonState.NoComm: 0>, 'Initializing': <PigeonState.Initializing: 1>, 'Ready': <PigeonState.Ready: 2>, 'UserCalibration': <PigeonState.UserCalibration: 3>}
        pass
    @typing.overload
    def __init__(self, deviceNumber: int) -> None: 
        """
        Create a Pigeon object that communicates with Pigeon on CAN Bus.

        :param deviceNumber: CAN Device Id of Pigeon [0,62]

        Create a Pigeon object that communciates with Pigeon through the
        Gadgeteer ribbon cable connected to a Talon on CAN Bus.

        :param talonSrx: Object for the TalonSRX connected via ribbon cable.
        """
    @typing.overload
    def __init__(self, talonSrx: ctre._ctre.TalonSRX) -> None: ...
    def addFusedHeading(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Atomically add to the Fused Heading register.

        :param angleDeg:  Degrees to add to the Fused Heading register.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def clearStickyFaults(self, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Clears the Sticky Faults

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configAllSettings(self, allConfigs: PigeonIMUConfiguration, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configFactoryDefault(self, timeoutMs: int = 50) -> ctre._ctre.ErrorCode: 
        """
        Configures all persistent settings to defaults.

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def configSetCustomParam(self, newValue: int, paramIndex: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the value of a custom parameter. This is for arbitrary use.

        Sometimes it is necessary to save calibration/declination/offset
        information in the device. Particularly if the
        device is part of a subsystem that can be replaced.

        :param newValue:   Value for custom parameter.
        :param paramIndex: Index of custom parameter. [0-1]
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def enterCalibrationMode(self, calMode: PigeonIMU.CalibrationMode, timeoutMs: int = 0) -> int: 
        """
        Enters the Calbration mode.  See the Pigeon IMU documentation for More
        information on Calibration.

        Note that you can instead use Phoenix Tuner to accomplish this.
        Note you should NOT be calling this during normal robot operation.

        :param calMode:   Calibration to execute
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getAccelerometerAngles(self) -> typing.Tuple[int, typing.List[float[3]]]: 
        """
        Get Accelerometer tilt angles.

        :param tiltAngles: Array to fill with x[0], y[1], and z[2] angles in degrees.

        :returns: The last ErrorCode generated.
        """
    def getAllConfigs(self, allConfigs: PigeonIMUConfiguration, timeoutMs: int = 50) -> None: 
        """
        Gets all persistant settings.

        :param allConfigs: Object with all of the persistant settings
        :param timeoutMs:  Timeout value in ms. If nonzero, function will wait for
                           config success and report an error if it times out.
                           If zero, no blocking or checking is performed.
        """
    def getFaults(self, toFill: PigeonIMU_Faults) -> ctre._ctre.ErrorCode: 
        """
        Gets the fault status

        :param toFill: Container for fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getFirmwareVersion(self) -> int: 
        """
        Gets the firmware version of the device.

        :returns: param holds the firmware version of the device. Device must be powered
                  cycled at least once.
        """
    @typing.overload
    def getFusedHeading(self) -> float: 
        """
        Get the current Fusion Status (including fused heading)

        :param status: object reference to fill with fusion status flags.
                       *                                        Caller may pass null if flags are not needed.

        :returns: The fused heading in degrees.

        Gets the Fused Heading

        :returns: The fused heading in degrees.
        """
    @typing.overload
    def getFusedHeading(self, status: PigeonIMU.FusionStatus) -> float: ...
    def getGeneralStatus(self, statusToFill: PigeonIMU.GeneralStatus) -> int: 
        """
        Get the status of the current (or previousley complete) calibration.

        :param out: statusToFill Container for the status information.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def getResetCount(self) -> int: 
        """
        :returns: number of times Pigeon Reset
        """
    def getResetFlags(self) -> int: 
        """
        :returns: Reset flags for Pigeon
        """
    def getState(self) -> PigeonIMU.PigeonState: 
        """
        Gets the current Pigeon state

        :returns: PigeonState enum
        """
    def getStatusFramePeriod(self, frame: PigeonIMU_StatusFrame, timeoutMs: int = 0) -> int: 
        """
        Gets the period of the given status frame.

        :param frame:     Frame to get the period of.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Period of the given status frame.
        """
    def getStickyFaults(self, toFill: PigeonIMU_StickyFaults) -> ctre._ctre.ErrorCode: 
        """
        Gets the sticky fault status

        :param toFill: Container for sticky fault statuses.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setCompassAngle(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Sets the compass angle. Although compass is absolute [0,360) degrees, the
        continuous compass register holds the wrap-arounds.

        :param angleDeg:  Degrees to set continuous compass angle to.
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setCompassDeclination(self, angleDegOffset: float, timeoutMs: int = 0) -> int: 
        """
        Set the declination for compass. Declination is the difference between
        Earth Magnetic north, and the geographic "True North".

        :param angleDegOffset: Degrees to set Compass Declination to.
        :param timeoutMs:      Timeout value in ms. If nonzero, function will wait for
                               config success and report an error if it times out.
                               If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setControlFramePeriod(self, frame: PigeonIMU_ControlFrame, periodMs: int) -> ctre._ctre.ErrorCode: 
        """
        Sets the period of the given control frame.

        :param frame:    Frame whose period is to be changed.
        :param periodMs: Period in ms for the given frame.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setFusedHeading(self, angleDeg: float, timeoutMs: int = 0) -> int: 
        """
        Sets the Fused Heading to the specified value.

        :param angleDeg:  New fused-heading in degrees [+/- 23,040 degrees]
        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setFusedHeadingToCompass(self, timeoutMs: int = 0) -> int: 
        """
        Sets the Fused Heading register to match the current compass value.

        :param timeoutMs: Timeout value in ms. If nonzero, function will wait for
                          config success and report an error if it times out.
                          If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setStatusFramePeriod(self, statusFrame: PigeonIMU_StatusFrame, periodMs: int, timeoutMs: int = 0) -> ctre._ctre.ErrorCode: 
        """
        Sets the period of the given status frame.

        :param statusFrame: Frame whose period is to be changed.
        :param periodMs:    Period in ms for the given frame.
        :param timeoutMs:   Timeout value in ms. If nonzero, function will wait for
                            config success and report an error if it times out.
                            If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    def setTemperatureCompensationDisable(self, bTempCompDisable: bool, timeoutMs: int = 0) -> int: 
        """
        Disable/Enable Temp compensation. Pigeon has this on/False at boot.

        :param bTempCompDisable: Set to "False" to enable temperature compensation.
        :param timeoutMs:        Timeout value in ms. If nonzero, function will wait for
                                 config success and report an error if it times out.
                                 If zero, no blocking or checking is performed.

        :returns: Error Code generated by function. 0 indicates no error.
        """
    @staticmethod
    @typing.overload
    def toString(cm: PigeonIMU.CalibrationMode) -> str: 
        """
        Gets the string representation of a PigeonState

        :param state: PigeonState to get the string representation of

        :returns: string representation of specified PigeonState

        Gets the string representation of a CalibrationMode

        :param cm: CalibrationMode to get the string representation of

        :returns: string representation of specified CalibrationMode
        """
    @staticmethod
    @typing.overload
    def toString(state: PigeonIMU.PigeonState) -> str: ...
    pass
class PigeonIMUConfigUtils(BasePigeonConfigUtils):
    """
    Util class to help with Pigeon configurations
    """
    def __init__(self) -> None: ...
    pass
class PigeonIMUConfiguration(BasePigeonConfiguration, ctre._ctre.CustomParamConfiguration):
    """
    Configurables available to Pigeon
    """
    def __init__(self) -> None: ...
    def __str__(self) -> str: 
        """
        :returns: String representation of configs
        """
    def toString(self, prependString: str) -> str: 
        """
        :param prependString: String to prepend to configs

        :returns: String representation of configs
        """
    pass
class PigeonIMU_ControlFrame():
    """
    Enumerated type for status frame types.

    Members:

      PigeonIMU_CondStatus_Control_1
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    PigeonIMU_CondStatus_Control_1: ctre._ctre.sensors.PigeonIMU_ControlFrame # value = <PigeonIMU_ControlFrame.PigeonIMU_CondStatus_Control_1: 272384>
    __members__: dict # value = {'PigeonIMU_CondStatus_Control_1': <PigeonIMU_ControlFrame.PigeonIMU_CondStatus_Control_1: 272384>}
    pass
class PigeonIMU_Faults():
    """
    Sticky faults available to Pigeon
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    pass
class PigeonIMU_StatusFrame():
    """
    Enumerated type for status frame types.

    Members:

      PigeonIMU_CondStatus_1_General

      PigeonIMU_CondStatus_9_SixDeg_YPR

      PigeonIMU_CondStatus_6_SensorFusion

      PigeonIMU_CondStatus_11_GyroAccum

      PigeonIMU_CondStatus_2_GeneralCompass

      PigeonIMU_CondStatus_3_GeneralAccel

      PigeonIMU_CondStatus_10_SixDeg_Quat

      PigeonIMU_RawStatus_4_Mag

      PigeonIMU_BiasedStatus_2_Gyro

      PigeonIMU_BiasedStatus_4_Mag

      PigeonIMU_BiasedStatus_6_Accel
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    PigeonIMU_BiasedStatus_2_Gyro: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_2_Gyro: 269376>
    PigeonIMU_BiasedStatus_4_Mag: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag: 269504>
    PigeonIMU_BiasedStatus_6_Accel: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_6_Accel: 269632>
    PigeonIMU_CondStatus_10_SixDeg_Quat: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_10_SixDeg_Quat: 270912>
    PigeonIMU_CondStatus_11_GyroAccum: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_11_GyroAccum: 270976>
    PigeonIMU_CondStatus_1_General: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_1_General: 270336>
    PigeonIMU_CondStatus_2_GeneralCompass: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_2_GeneralCompass: 270400>
    PigeonIMU_CondStatus_3_GeneralAccel: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_3_GeneralAccel: 270464>
    PigeonIMU_CondStatus_6_SensorFusion: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_6_SensorFusion: 270656>
    PigeonIMU_CondStatus_9_SixDeg_YPR: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_9_SixDeg_YPR: 270848>
    PigeonIMU_RawStatus_4_Mag: ctre._ctre.sensors.PigeonIMU_StatusFrame # value = <PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag: 269504>
    __members__: dict # value = {'PigeonIMU_CondStatus_1_General': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_1_General: 270336>, 'PigeonIMU_CondStatus_9_SixDeg_YPR': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_9_SixDeg_YPR: 270848>, 'PigeonIMU_CondStatus_6_SensorFusion': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_6_SensorFusion: 270656>, 'PigeonIMU_CondStatus_11_GyroAccum': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_11_GyroAccum: 270976>, 'PigeonIMU_CondStatus_2_GeneralCompass': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_2_GeneralCompass: 270400>, 'PigeonIMU_CondStatus_3_GeneralAccel': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_3_GeneralAccel: 270464>, 'PigeonIMU_CondStatus_10_SixDeg_Quat': <PigeonIMU_StatusFrame.PigeonIMU_CondStatus_10_SixDeg_Quat: 270912>, 'PigeonIMU_RawStatus_4_Mag': <PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag: 269504>, 'PigeonIMU_BiasedStatus_2_Gyro': <PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_2_Gyro: 269376>, 'PigeonIMU_BiasedStatus_4_Mag': <PigeonIMU_StatusFrame.PigeonIMU_RawStatus_4_Mag: 269504>, 'PigeonIMU_BiasedStatus_6_Accel': <PigeonIMU_StatusFrame.PigeonIMU_BiasedStatus_6_Accel: 269632>}
    pass
class PigeonIMU_StickyFaults():
    """
    Sticky faults available to Pigeon
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    @typing.overload
    def __init__(self, bits: int) -> None: ...
    def hasAnyFault(self) -> bool: 
        """
        :returns: true if any faults are tripped
        """
    def toBitfield(self) -> int: 
        """
        :returns: Current fault list as a bit field
        """
    def update(self, bits: int) -> None: 
        """
        Updates current fault list with specified bit field of faults

        :param bits: bit field of faults to update with
        """
    pass
class SensorInitializationStrategy():
    """
    Enum for how CANCoder should initialize its position register on boot.

    Members:

      BootToZero : On boot up, set position to zero.

      BootToAbsolutePosition : On boot up, sync to the Absolute Position signal.  The Absolute position signal will be signed according to the selected Absolute Sensor Range.
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    BootToAbsolutePosition: ctre._ctre.sensors.SensorInitializationStrategy # value = <SensorInitializationStrategy.BootToAbsolutePosition: 1>
    BootToZero: ctre._ctre.sensors.SensorInitializationStrategy # value = <SensorInitializationStrategy.BootToZero: 0>
    __members__: dict # value = {'BootToZero': <SensorInitializationStrategy.BootToZero: 0>, 'BootToAbsolutePosition': <SensorInitializationStrategy.BootToAbsolutePosition: 1>}
    pass
class SensorTimeBase():
    """
    Velocity Measurement Periods

    Members:

      Per100Ms_Legacy : Legacy Mode

      PerSecond : Per-Second Velocities

      PerMinute : Per-Minute Velocities
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Per100Ms_Legacy: ctre._ctre.sensors.SensorTimeBase # value = <SensorTimeBase.Per100Ms_Legacy: 0>
    PerMinute: ctre._ctre.sensors.SensorTimeBase # value = <SensorTimeBase.PerMinute: 2>
    PerSecond: ctre._ctre.sensors.SensorTimeBase # value = <SensorTimeBase.PerSecond: 1>
    __members__: dict # value = {'Per100Ms_Legacy': <SensorTimeBase.Per100Ms_Legacy: 0>, 'PerSecond': <SensorTimeBase.PerSecond: 1>, 'PerMinute': <SensorTimeBase.PerMinute: 2>}
    pass
class SensorVelocityMeasPeriod():
    """
    Enumerate filter periods for any sensor that measures velocity.

    Members:

      Period_1Ms : 1ms velocity measurement period

      Period_2Ms : 2ms velocity measurement period

      Period_5Ms : 5ms velocity measurement period

      Period_10Ms : 10ms velocity measurement period

      Period_20Ms : 20ms velocity measurement period

      Period_25Ms : 25ms velocity measurement period

      Period_50Ms : 50ms velocity measurement period

      Period_100Ms : 100ms velocity measurement period
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Period_100Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_100Ms: 100>
    Period_10Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_10Ms: 10>
    Period_1Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_1Ms: 1>
    Period_20Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_20Ms: 20>
    Period_25Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_25Ms: 25>
    Period_2Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_2Ms: 2>
    Period_50Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_50Ms: 50>
    Period_5Ms: ctre._ctre.sensors.SensorVelocityMeasPeriod # value = <SensorVelocityMeasPeriod.Period_5Ms: 5>
    __members__: dict # value = {'Period_1Ms': <SensorVelocityMeasPeriod.Period_1Ms: 1>, 'Period_2Ms': <SensorVelocityMeasPeriod.Period_2Ms: 2>, 'Period_5Ms': <SensorVelocityMeasPeriod.Period_5Ms: 5>, 'Period_10Ms': <SensorVelocityMeasPeriod.Period_10Ms: 10>, 'Period_20Ms': <SensorVelocityMeasPeriod.Period_20Ms: 20>, 'Period_25Ms': <SensorVelocityMeasPeriod.Period_25Ms: 25>, 'Period_50Ms': <SensorVelocityMeasPeriod.Period_50Ms: 50>, 'Period_100Ms': <SensorVelocityMeasPeriod.Period_100Ms: 100>}
    pass
class WPI_CANCoder(CANCoder, ctre._ctre.CANBusAddressable, wpiutil._wpiutil.Sendable):
    def __init__(self, deviceNumber: int, canbus: str = '') -> None: 
        """
        Construtor for CANCoder.

        :param deviceNumber: CAN Device ID of the CANCoder.
        :param canbus:       Name of the CANbus; can be a CANivore device name or serial number.
                             Pass in nothing or "rio" to use the roboRIO.
        """
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    pass
class WPI_Pigeon2(Pigeon2, BasePigeon, ctre._ctre.CANBusAddressable, wpilib.interfaces._interfaces.Gyro, wpiutil._wpiutil.Sendable):
    def __init__(self, deviceNumber: int, canbus: str = '') -> None: 
        """
        Construtor for WPI_Pigeon2.

        :param deviceNumber: CAN Device ID of the Pigeon 2.
        :param canbus:       Name of the CANbus; can be a CANivore device name or serial number.
                             Pass in nothing or "rio" to use the roboRIO.
        """
    def calibrate(self) -> None: ...
    def getAngle(self) -> float: ...
    def getRate(self) -> float: ...
    def getRotation2d(self) -> wpimath.geometry._geometry.Rotation2d: ...
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def reset(self) -> None: ...
    pass
class WPI_PigeonIMU(PigeonIMU, BasePigeon, ctre._ctre.CANBusAddressable, wpilib.interfaces._interfaces.Gyro, wpiutil._wpiutil.Sendable):
    @typing.overload
    def __init__(self, deviceNumber: int) -> None: 
        """
        Construtor for WPI_PigeonIMU.

        :param deviceNumber: CAN Device ID of the Pigeon IMU.

        Construtor for WPI_PigeonIMU.

        :param talon: The Talon SRX ribbon-cabled to Pigeon.
        """
    @typing.overload
    def __init__(self, talon: ctre._ctre.TalonSRX) -> None: ...
    def calibrate(self) -> None: ...
    def getAngle(self) -> float: ...
    def getRate(self) -> float: ...
    def getRotation2d(self) -> wpimath.geometry._geometry.Rotation2d: ...
    def initSendable(self, builder: wpiutil._wpiutil.SendableBuilder) -> None: ...
    def reset(self) -> None: ...
    pass
