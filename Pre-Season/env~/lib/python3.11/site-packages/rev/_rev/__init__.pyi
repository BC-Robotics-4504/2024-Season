from __future__ import annotations
import rev._rev
import typing
import wpilib._wpilib
import wpilib.interfaces._interfaces

__all__ = [
    "AbsoluteEncoder",
    "AnalogInput",
    "CANAnalog",
    "CANEncoder",
    "CANSensor",
    "CANSparkMax",
    "CANSparkMaxLowLevel",
    "CIEColor",
    "ColorMatch",
    "ColorSensorV3",
    "MotorFeedbackSensor",
    "REVLibError",
    "RelativeEncoder",
    "SparkMaxAbsoluteEncoder",
    "SparkMaxAlternateEncoder",
    "SparkMaxAnalogSensor",
    "SparkMaxLimitSwitch",
    "SparkMaxPIDController",
    "SparkMaxRelativeEncoder"
]


class CANSensor():
    def getInverted(self) -> bool: 
        """
        Get the phase of the CANSensor. This will just return false
        if the user tries to get the inversion of the hall effect.
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the CANSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders and analog sensors. This will throw an error
        if the user tries to set the inversion of the hall effect.
        """
    pass
class AnalogInput():
    """
    Get an instance of AnalogInput by using
    CANSparkMax::GetAnalog(SparkMaxAnalogSensor::Mode)}.
    """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. Returns value in the native unit
        of 'volt' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Position of the sensor in volts
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the current conversion factor for the position of the analog
        sensor.

        :returns: Analog position conversion factor
        """
    def getVoltage(self) -> float: 
        """
        Get the voltage of the analog sensor.

        :returns: Voltage of the sensor
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for the position of the analog sensor.
        By default, revolutions per volt is 1. Changing the position conversion
        factor will also change the position units.

        :param factor: The conversion factor which will be multiplied by volts

        :returns: REVLibError::kOk if successful
        """
    pass
class MotorFeedbackSensor(CANSensor):
    """
    A sensor that can be used to provide rotational feedback to a motor
    controller
    """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false if
        the user tries to get the inversion of the hall sensor.

        :returns: The phase of the sensor
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in phase
        with the motor itself. This only works for quadrature encoders and analog
        sensors. This will throw an error if the user tries to set the inversion
        of the hall sensor.

        :param inverted: The phase of the sensor

        :returns: REVLibError::kOk if successful
        """
    pass
class CANEncoder(MotorFeedbackSensor, CANSensor):
    class AlternateEncoderType():
        """
        Members:

          kQuadrature
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
        __members__: dict # value = {'kQuadrature': <AlternateEncoderType.kQuadrature: 0>}
        kQuadrature: rev._rev.CANEncoder.AlternateEncoderType # value = <AlternateEncoderType.kQuadrature: 0>
        pass
    class EncoderType():
        """
        Members:

          kNoSensor

          kHallSensor

          kQuadrature
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
        __members__: dict # value = {'kNoSensor': <EncoderType.kNoSensor: 0>, 'kHallSensor': <EncoderType.kHallSensor: 1>, 'kQuadrature': <EncoderType.kQuadrature: 2>}
        kHallSensor: rev._rev.CANEncoder.EncoderType # value = <EncoderType.kHallSensor: 1>
        kNoSensor: rev._rev.CANEncoder.EncoderType # value = <EncoderType.kNoSensor: 0>
        kQuadrature: rev._rev.CANEncoder.EncoderType # value = <EncoderType.kQuadrature: 2>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the average sampling depth for a quadrature encoder.

        :returns: The average sampling depth
        """
    def getCountsPerRevolution(self) -> int: 
        """
        Get the counts per revolution of the quadrature encoder.

        For a description on the difference between CPR, PPR, etc. go to
        https://www.cuidevices.com/blog/what-is-encoder-ppr-cpr-and-lpr

        :returns: Counts per revolution
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the number of samples for reading from a quadrature encoder. This
        value sets the number of samples in the average for velocity readings.

        :returns: Measurement period in microseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().

        :returns: Number the RPM of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the average sampling depth for a quadrature encoder. This value
        sets the number of samples in the average for velocity readings. This
        can be any value from 1 to 64.

        When the SparkMax controller is in Brushless mode, this
        will not change any behavior.

        :param depth: The average sampling depth between 1 and 64 (default)

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders. This will throw an error if the user tries to set
        inverted while the SparkMax is Brushless and using the hall
        effect sensor.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the measurement period for velocity measurements of a quadrature
        encoder. When the SparkMax controller is in Brushless mode, this will not
        change any behavior.

        The basic formula to calculate velocity is change in positon / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds. This number may be
                          between 1 and 100 (default).

        :returns: REVLibError::kOk if successful
        """
    def setPosition(self, position: float) -> REVLibError: 
        """
        Set the position of the encoder.

        :param position: Number of rotations of the motor

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    pass
class AbsoluteEncoder(MotorFeedbackSensor, CANSensor):
    def getAverageDepth(self) -> int: 
        """
        Get the average sampling depth for an absolute encoder

        :returns: The average sampling depth
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the AbsoluteEncoder

        :returns: The phase of the encoder
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'rotations per second' by default, and can be changed by a scale
        factor using setVelocityConversionFactor().

        :returns: Number of rotations per second of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def getZeroOffset(self) -> float: 
        """
        Gets the zero offset for an absolute encoder (the position that is
        reported as zero).

        The zero offset is specified as the reported position of the encoder in
        the desired zero position, if the zero offset was set to 0. It is
        influenced by the absolute encoder's position conversion factor, and
        whether it is inverted.

        :returns: The zero offset of the absolute encoder with the position
                  conversion factor applied
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the average sampling depth for an absolute encoder. This is a bit
        size and should be either 1, 2, 4, 8, 16, 32, 64, or 128

        :param depth: The average sampling depth of 1, 2, 4, 8, 16, 32, 64, or 128

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the AbsoluteEncoder so that it is set to be in phase
        with the motor itself

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setZeroOffset(self, offset: float) -> REVLibError: 
        """
        Sets the zero offset of an absolute encoder (the position that is
        reported as zero).

        The zero offset is specified as the reported position of the encoder in
        the desired zero position, if the zero offset was set to 0. It is
        influenced by the absolute encoder's position conversion factor, and
        whether it is inverted.

        Always call SetPositionConversionFactor() and SetInverted() before
        calling this function.

        :param offset: The zero offset with the position conversion factor applied

        :returns: REVLibError::kOk if successful
        """
    pass
class CANSparkMaxLowLevel(wpilib.interfaces._interfaces.MotorController):
    class ControlType():
        """
        Members:

          kDutyCycle

          kVelocity

          kVoltage

          kPosition

          kSmartMotion

          kCurrent

          kSmartVelocity
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
        __members__: dict # value = {'kDutyCycle': <ControlType.kDutyCycle: 0>, 'kVelocity': <ControlType.kVelocity: 1>, 'kVoltage': <ControlType.kVoltage: 2>, 'kPosition': <ControlType.kPosition: 3>, 'kSmartMotion': <ControlType.kSmartMotion: 4>, 'kCurrent': <ControlType.kCurrent: 5>, 'kSmartVelocity': <ControlType.kSmartVelocity: 6>}
        kCurrent: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kCurrent: 5>
        kDutyCycle: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kDutyCycle: 0>
        kPosition: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kPosition: 3>
        kSmartMotion: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kSmartMotion: 4>
        kSmartVelocity: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kSmartVelocity: 6>
        kVelocity: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kVelocity: 1>
        kVoltage: rev._rev.CANSparkMaxLowLevel.ControlType # value = <ControlType.kVoltage: 2>
        pass
    class MotorType():
        """
        Members:

          kBrushed

          kBrushless
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
        __members__: dict # value = {'kBrushed': <MotorType.kBrushed: 0>, 'kBrushless': <MotorType.kBrushless: 1>}
        kBrushed: rev._rev.CANSparkMaxLowLevel.MotorType # value = <MotorType.kBrushed: 0>
        kBrushless: rev._rev.CANSparkMaxLowLevel.MotorType # value = <MotorType.kBrushless: 1>
        pass
    class ParameterStatus():
        """
        Members:

          kOK

          kInvalidID

          kMismatchType

          kAccessMode

          kInvalid

          kNotImplementedDeprecated
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
        __members__: dict # value = {'kOK': <ParameterStatus.kOK: 0>, 'kInvalidID': <ParameterStatus.kInvalidID: 1>, 'kMismatchType': <ParameterStatus.kMismatchType: 2>, 'kAccessMode': <ParameterStatus.kAccessMode: 3>, 'kInvalid': <ParameterStatus.kInvalid: 4>, 'kNotImplementedDeprecated': <ParameterStatus.kNotImplementedDeprecated: 5>}
        kAccessMode: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kAccessMode: 3>
        kInvalid: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kInvalid: 4>
        kInvalidID: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kInvalidID: 1>
        kMismatchType: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kMismatchType: 2>
        kNotImplementedDeprecated: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kNotImplementedDeprecated: 5>
        kOK: rev._rev.CANSparkMaxLowLevel.ParameterStatus # value = <ParameterStatus.kOK: 0>
        pass
    class PeriodicFrame():
        """
        Members:

          kStatus0

          kStatus1

          kStatus2

          kStatus3

          kStatus4

          kStatus5

          kStatus6
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
        __members__: dict # value = {'kStatus0': <PeriodicFrame.kStatus0: 0>, 'kStatus1': <PeriodicFrame.kStatus1: 1>, 'kStatus2': <PeriodicFrame.kStatus2: 2>, 'kStatus3': <PeriodicFrame.kStatus3: 3>, 'kStatus4': <PeriodicFrame.kStatus4: 4>, 'kStatus5': <PeriodicFrame.kStatus5: 5>, 'kStatus6': <PeriodicFrame.kStatus6: 6>}
        kStatus0: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus0: 0>
        kStatus1: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus1: 1>
        kStatus2: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus2: 2>
        kStatus3: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus3: 3>
        kStatus4: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus4: 4>
        kStatus5: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus5: 5>
        kStatus6: rev._rev.CANSparkMaxLowLevel.PeriodicFrame # value = <PeriodicFrame.kStatus6: 6>
        pass
    class PeriodicStatus0():
        def __init__(self) -> None: ...
        @property
        def appliedOutput(self) -> float:
            """
            :type: float
            """
        @appliedOutput.setter
        def appliedOutput(self, arg0: float) -> None:
            pass
        @property
        def faults(self) -> int:
            """
            :type: int
            """
        @faults.setter
        def faults(self, arg0: int) -> None:
            pass
        @property
        def isFollower(self) -> bool:
            """
            :type: bool
            """
        @isFollower.setter
        def isFollower(self, arg0: bool) -> None:
            pass
        @property
        def isInverted(self) -> int:
            """
            :type: int
            """
        @isInverted.setter
        def isInverted(self, arg0: int) -> None:
            pass
        @property
        def lock(self) -> int:
            """
            :type: int
            """
        @lock.setter
        def lock(self, arg0: int) -> None:
            pass
        @property
        def motorType(self) -> CANSparkMaxLowLevel.MotorType:
            """
            :type: CANSparkMaxLowLevel.MotorType
            """
        @motorType.setter
        def motorType(self, arg0: CANSparkMaxLowLevel.MotorType) -> None:
            pass
        @property
        def roboRIO(self) -> int:
            """
            :type: int
            """
        @roboRIO.setter
        def roboRIO(self, arg0: int) -> None:
            pass
        @property
        def stickyFaults(self) -> int:
            """
            :type: int
            """
        @stickyFaults.setter
        def stickyFaults(self, arg0: int) -> None:
            pass
        @property
        def timestamp(self) -> int:
            """
            :type: int
            """
        @timestamp.setter
        def timestamp(self, arg0: int) -> None:
            pass
        pass
    class PeriodicStatus1():
        def __init__(self) -> None: ...
        @property
        def busVoltage(self) -> float:
            """
            :type: float
            """
        @busVoltage.setter
        def busVoltage(self, arg0: float) -> None:
            pass
        @property
        def motorTemperature(self) -> int:
            """
            :type: int
            """
        @motorTemperature.setter
        def motorTemperature(self, arg0: int) -> None:
            pass
        @property
        def outputCurrent(self) -> float:
            """
            :type: float
            """
        @outputCurrent.setter
        def outputCurrent(self, arg0: float) -> None:
            pass
        @property
        def sensorVelocity(self) -> float:
            """
            :type: float
            """
        @sensorVelocity.setter
        def sensorVelocity(self, arg0: float) -> None:
            pass
        @property
        def timestamp(self) -> int:
            """
            :type: int
            """
        @timestamp.setter
        def timestamp(self, arg0: int) -> None:
            pass
        pass
    class PeriodicStatus2():
        def __init__(self) -> None: ...
        @property
        def iAccum(self) -> float:
            """
            :type: float
            """
        @iAccum.setter
        def iAccum(self, arg0: float) -> None:
            pass
        @property
        def sensorPosition(self) -> float:
            """
            :type: float
            """
        @sensorPosition.setter
        def sensorPosition(self, arg0: float) -> None:
            pass
        @property
        def timestamp(self) -> int:
            """
            :type: int
            """
        @timestamp.setter
        def timestamp(self, arg0: int) -> None:
            pass
        pass
    class TelemetryID():
        """
        Members:

          kBusVoltage

          kOutputCurrent

          kVelocity

          kPosition

          kIAccum

          kAppliedOutput

          kMotorTemp

          kFaults

          kStickyFaults

          kAnalogVoltage

          kAnalogPosition

          kAnalogVelocity

          kAltEncPosition

          kAltEncVelocity

          kTotalStreams
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
        __members__: dict # value = {'kBusVoltage': <TelemetryID.kBusVoltage: 0>, 'kOutputCurrent': <TelemetryID.kOutputCurrent: 1>, 'kVelocity': <TelemetryID.kVelocity: 2>, 'kPosition': <TelemetryID.kPosition: 3>, 'kIAccum': <TelemetryID.kIAccum: 4>, 'kAppliedOutput': <TelemetryID.kAppliedOutput: 5>, 'kMotorTemp': <TelemetryID.kMotorTemp: 6>, 'kFaults': <TelemetryID.kFaults: 7>, 'kStickyFaults': <TelemetryID.kStickyFaults: 8>, 'kAnalogVoltage': <TelemetryID.kAnalogVoltage: 9>, 'kAnalogPosition': <TelemetryID.kAnalogPosition: 10>, 'kAnalogVelocity': <TelemetryID.kAnalogVelocity: 11>, 'kAltEncPosition': <TelemetryID.kAltEncPosition: 12>, 'kAltEncVelocity': <TelemetryID.kAltEncVelocity: 13>, 'kTotalStreams': <TelemetryID.kTotalStreams: 14>}
        kAltEncPosition: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAltEncPosition: 12>
        kAltEncVelocity: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAltEncVelocity: 13>
        kAnalogPosition: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAnalogPosition: 10>
        kAnalogVelocity: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAnalogVelocity: 11>
        kAnalogVoltage: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAnalogVoltage: 9>
        kAppliedOutput: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kAppliedOutput: 5>
        kBusVoltage: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kBusVoltage: 0>
        kFaults: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kFaults: 7>
        kIAccum: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kIAccum: 4>
        kMotorTemp: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kMotorTemp: 6>
        kOutputCurrent: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kOutputCurrent: 1>
        kPosition: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kPosition: 3>
        kStickyFaults: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kStickyFaults: 8>
        kTotalStreams: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kTotalStreams: 14>
        kVelocity: rev._rev.CANSparkMaxLowLevel.TelemetryID # value = <TelemetryID.kVelocity: 2>
        pass
    class TelemetryMessage():
        def __init__(self) -> None: ...
        @property
        def id(self) -> CANSparkMaxLowLevel.TelemetryID:
            """
            :type: CANSparkMaxLowLevel.TelemetryID
            """
        @id.setter
        def id(self, arg0: CANSparkMaxLowLevel.TelemetryID) -> None:
            pass
        @property
        def lowerBnd(self) -> float:
            """
            :type: float
            """
        @lowerBnd.setter
        def lowerBnd(self, arg0: float) -> None:
            pass
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def timestamp(self) -> int:
            """
            :type: int
            """
        @timestamp.setter
        def timestamp(self, arg0: int) -> None:
            pass
        @property
        def units(self) -> str:
            """
            :type: str
            """
        @property
        def upperBnd(self) -> float:
            """
            :type: float
            """
        @upperBnd.setter
        def upperBnd(self, arg0: float) -> None:
            pass
        @property
        def value(self) -> float:
            """
            :type: float
            """
        @value.setter
        def value(self, arg0: float) -> None:
            pass
        pass
    def _getPeriodicStatus0(self) -> CANSparkMaxLowLevel.PeriodicStatus0: ...
    def _getPeriodicStatus1(self) -> CANSparkMaxLowLevel.PeriodicStatus1: ...
    def _getPeriodicStatus2(self) -> CANSparkMaxLowLevel.PeriodicStatus2: ...
    def _getSafeFloat(self, f: float) -> float: ...
    @staticmethod
    def enableExternalUSBControl(enable: bool) -> None: 
        """
        Allow external controllers to recieve control commands over USB.
        For example, a configuration where the heartbeat (and enable/disable)
        is sent by the main controller, but control frames are sent by
        other CAN devices over USB.

        This is global for all controllers on the same bus.

        This does not disable sending control frames from this device. To prevent
        conflicts, do not enable this feature and also send Set() for
        SetReference() from the controllers you wish to control.

        :param enable: Enable or disable external control
        """
    def getDeviceId(self) -> int: 
        """
        Get the configured Device ID of the SPARK MAX.

        :returns: int device ID
        """
    def getFirmwareString(self) -> str: 
        """
        Get the firmware version of the SPARK MAX as a string.

        :returns: std::string Human readable firmware version string
        """
    def getFirmwareVersion(self) -> int: 
        """
        Get the firmware version of the SPARK MAX.

        :returns: uint32_t Firmware version integer. Value is represented as 4
                  bytes, Major.Minor.Build H.Build L
        """
    def getInitialMotorType(self) -> CANSparkMaxLowLevel.MotorType: 
        """
        Get the motor type setting from when the SparkMax was created.

        This does not use the Get Parameter API which means it does not read
        what motor type is stored on the SparkMax itself. Instead, it reads
        the stored motor type from when the SparkMax object was first created.

        :deprecated: Use GetMotorType() instead

        :returns: MotorType Motor type setting
        """
    def getMotorType(self) -> CANSparkMaxLowLevel.MotorType: 
        """
        Get the motor type setting for the SPARK MAX.

        :returns: MotorType Motor type setting
        """
    def getSerialNumber(self) -> typing.List[int]: 
        """
        Get the unique serial number of the SPARK MAX. Currently not implemented.

        :returns: std::vector<uint8_t> Vector of bytes representig the unique
                  serial number
        """
    def restoreFactoryDefaults(self, persist: bool = False) -> REVLibError: 
        """
        Restore motor controller parameters to factory default

        :param persist: If true, burn the flash with the factory default
                        parameters

        :returns: REVLibError::kOk if successful
        """
    def setControlFramePeriodMs(self, periodMs: int) -> None: 
        """
        Set the control frame send period for the native CAN Send thread. To
        disable periodic sends, set periodMs to 0.

        :param periodMs: The send period in milliseconds between 1ms and 100ms
                         or set to 0 to disable periodic sends. Note this is not updated until
                         the next call to Set() or SetReference().
        """
    @staticmethod
    def setEnable(enable: bool) -> None: 
        """
        Send enabled or disabled command to controllers. This is global for all
        controllers on the same bus, and will only work for non-roboRIO targets
        in non-competiton use. This function will also not work if a roboRIO is
        present on the CAN bus.

        This does not disable sending control frames from this device. To prevent
        conflicts, do not enable this feature and also send Set() for
        SetReference() from the controllers you wish to control.

        :param enable: Enable or disable external control
        """
    def setPeriodicFramePeriod(self, frame: CANSparkMaxLowLevel.PeriodicFrame, periodMs: int) -> REVLibError: 
        """
        Set the rate of transmission for periodic frames from the SPARK MAX

        Each motor controller sends back status frames with different
        data at set rates. Use this function to change the default rates.

        Defaults:
        Status0 - 10ms
        Status1 - 20ms
        Status2 - 20ms
        Status3 - 50ms
        Status4 - 20ms
        Status5 - 200ms
        Status6 - 200ms

        This value is not stored in the FLASH after calling burnFlash()
        and is reset on powerup.

        Refer to the SPARK MAX reference manual on details for how and when
        to configure this parameter.

        :param frame:    Which periodic frame to change the period of
        :param periodMs: The rate the controller sends the frame to the
                         controller.

        :returns: REVLibError::kOk if successful
        """
    kAPIBuildVersion = 3
    kAPIMajorVersion = 231
    kAPIMinorVersion = 1
    kAPIVersion = 132579587
    pass
class CANSparkMax(CANSparkMaxLowLevel, wpilib.interfaces._interfaces.MotorController):
    class ExternalFollower():
        def __init__(self) -> None: ...
        @property
        def arbId(self) -> int:
            """
            :type: int
            """
        @arbId.setter
        def arbId(self, arg0: int) -> None:
            pass
        @property
        def configId(self) -> int:
            """
            :type: int
            """
        @configId.setter
        def configId(self, arg0: int) -> None:
            pass
        pass
    class FaultID():
        """
        Members:

          kBrownout

          kOvercurrent

          kIWDTReset

          kMotorFault

          kSensorFault

          kStall

          kEEPROMCRC

          kCANTX

          kCANRX

          kHasReset

          kDRVFault

          kOtherFault

          kSoftLimitFwd

          kSoftLimitRev

          kHardLimitFwd

          kHardLimitRev
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
        __members__: dict # value = {'kBrownout': <FaultID.kBrownout: 0>, 'kOvercurrent': <FaultID.kOvercurrent: 1>, 'kIWDTReset': <FaultID.kIWDTReset: 2>, 'kMotorFault': <FaultID.kMotorFault: 3>, 'kSensorFault': <FaultID.kSensorFault: 4>, 'kStall': <FaultID.kStall: 5>, 'kEEPROMCRC': <FaultID.kEEPROMCRC: 6>, 'kCANTX': <FaultID.kCANTX: 7>, 'kCANRX': <FaultID.kCANRX: 8>, 'kHasReset': <FaultID.kHasReset: 9>, 'kDRVFault': <FaultID.kDRVFault: 10>, 'kOtherFault': <FaultID.kOtherFault: 11>, 'kSoftLimitFwd': <FaultID.kSoftLimitFwd: 12>, 'kSoftLimitRev': <FaultID.kSoftLimitRev: 13>, 'kHardLimitFwd': <FaultID.kHardLimitFwd: 14>, 'kHardLimitRev': <FaultID.kHardLimitRev: 15>}
        kBrownout: rev._rev.CANSparkMax.FaultID # value = <FaultID.kBrownout: 0>
        kCANRX: rev._rev.CANSparkMax.FaultID # value = <FaultID.kCANRX: 8>
        kCANTX: rev._rev.CANSparkMax.FaultID # value = <FaultID.kCANTX: 7>
        kDRVFault: rev._rev.CANSparkMax.FaultID # value = <FaultID.kDRVFault: 10>
        kEEPROMCRC: rev._rev.CANSparkMax.FaultID # value = <FaultID.kEEPROMCRC: 6>
        kHardLimitFwd: rev._rev.CANSparkMax.FaultID # value = <FaultID.kHardLimitFwd: 14>
        kHardLimitRev: rev._rev.CANSparkMax.FaultID # value = <FaultID.kHardLimitRev: 15>
        kHasReset: rev._rev.CANSparkMax.FaultID # value = <FaultID.kHasReset: 9>
        kIWDTReset: rev._rev.CANSparkMax.FaultID # value = <FaultID.kIWDTReset: 2>
        kMotorFault: rev._rev.CANSparkMax.FaultID # value = <FaultID.kMotorFault: 3>
        kOtherFault: rev._rev.CANSparkMax.FaultID # value = <FaultID.kOtherFault: 11>
        kOvercurrent: rev._rev.CANSparkMax.FaultID # value = <FaultID.kOvercurrent: 1>
        kSensorFault: rev._rev.CANSparkMax.FaultID # value = <FaultID.kSensorFault: 4>
        kSoftLimitFwd: rev._rev.CANSparkMax.FaultID # value = <FaultID.kSoftLimitFwd: 12>
        kSoftLimitRev: rev._rev.CANSparkMax.FaultID # value = <FaultID.kSoftLimitRev: 13>
        kStall: rev._rev.CANSparkMax.FaultID # value = <FaultID.kStall: 5>
        pass
    class IdleMode():
        """
        Members:

          kCoast

          kBrake
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
        __members__: dict # value = {'kCoast': <IdleMode.kCoast: 0>, 'kBrake': <IdleMode.kBrake: 1>}
        kBrake: rev._rev.CANSparkMax.IdleMode # value = <IdleMode.kBrake: 1>
        kCoast: rev._rev.CANSparkMax.IdleMode # value = <IdleMode.kCoast: 0>
        pass
    class SoftLimitDirection():
        """
        Members:

          kForward

          kReverse
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
        __members__: dict # value = {'kForward': <SoftLimitDirection.kForward: 0>, 'kReverse': <SoftLimitDirection.kReverse: 1>}
        kForward: rev._rev.CANSparkMax.SoftLimitDirection # value = <SoftLimitDirection.kForward: 0>
        kReverse: rev._rev.CANSparkMax.SoftLimitDirection # value = <SoftLimitDirection.kReverse: 1>
        pass
    def __init__(self, deviceID: int, type: CANSparkMaxLowLevel.MotorType) -> None: 
        """
        Create a new object to control a SPARK MAX motor Controller

        :param deviceID: The device ID.
        :param type:     The motor type connected to the controller. Brushless
                         motor wires must be connected to their matching colors,
                         and the hall sensor must be plugged in. Brushed motors must be connected
                         to the Red and Black terminals only.
        """
    def __repr__(self) -> str: ...
    def burnFlash(self) -> REVLibError: 
        """
        Writes all settings to flash.
        """
    def clearFaults(self) -> REVLibError: 
        """
        Clears all non-sticky faults.

        Sticky faults must be cleared by resetting the motor controller.
        """
    def disable(self) -> None: 
        """
        Common interface for disabling a motor.
        """
    def disableVoltageCompensation(self) -> REVLibError: 
        """
        Disables the voltage compensation setting for all modes on the SPARK MAX.

        :returns: REVLibError::kOk if successful
        """
    def enableSoftLimit(self, direction: CANSparkMax.SoftLimitDirection, enable: bool) -> REVLibError: 
        """
        Enable soft limits

        :param direction: the direction of motion to restrict
        :param enable:    set true to enable soft limits
        """
    def enableVoltageCompensation(self, nominalVoltage: float) -> REVLibError: 
        """
        Sets the voltage compensation setting for all modes on the SPARK MAX and
        enables voltage compensation.

        :param nominalVoltage: Nominal voltage to compensate output to

        :returns: REVLibError::kOk if successful
        """
    @typing.overload
    def follow(self, leader: CANSparkMax, invert: bool = False) -> REVLibError: 
        """
        Causes this controller's output to mirror the provided leader.

        Only voltage output is mirrored. Settings changed on the leader do not
        affect the follower.

        Following anything other than a CAN SPARK MAX is not officially
        supported.

        :param leader: The motor controller to follow.
        :param invert: Set the follower to output opposite of the leader

        Causes this controller's output to mirror the provided leader.

        Only voltage output is mirrored. Settings changed on the leader do not
        affect the follower.

        Following anything other than a CAN SPARK MAX is not officially
        supported.

        :param leader:   The type of motor controller to follow (Talon SRX, Spark
                         Max, etc.).
        :param deviceID: The CAN ID of the device to follow.
        :param invert:   Set the follower to output opposite of the leader
        """
    @typing.overload
    def follow(self, leader: CANSparkMax.ExternalFollower, deviceID: int, invert: bool = False) -> REVLibError: ...
    def get(self) -> float: 
        """
        Common interface for getting the current set speed of a speed controller.

        :returns: The current set speed.  Value is between -1.0 and 1.0.
        """
    def getAbsoluteEncoder(self, encoderType: SparkMaxAbsoluteEncoder.Type) -> SparkMaxAbsoluteEncoder: 
        """
        Returns an object for interfacing with a connected absolute encoder.
        """
    @typing.overload
    def getAlternateEncoder(self, countsPerRev: int) -> SparkMaxAlternateEncoder: 
        """
        Returns an object for interfacing with a quadrature encoder connected to
        the alternate encoder mode data port pins. These are defined as:

        Pin 4 (Forward Limit Switch): Index
        Pin 6 (Multi-function): Encoder A
        Pin 8 (Reverse Limit Switch): Encoder B

        This call will disable support for the limit switch inputs.

        Returns an object for interfacing with a quadrature encoder connected to
        the alternate encoder mode data port pins. These are defined as:

        Pin 4 (Forward Limit Switch): Index
        Pin 6 (Multi-function): Encoder A
        Pin 8 (Reverse Limit Switch): Encoder B

        This call will disable support for the limit switch inputs.
        """
    @typing.overload
    def getAlternateEncoder(self, encoderType: SparkMaxAlternateEncoder.Type, countsPerRev: int) -> SparkMaxAlternateEncoder: ...
    def getAnalog(self, mode: SparkMaxAnalogSensor.Mode = Mode.kAbsolute) -> SparkMaxAnalogSensor: 
        """
        Returns an object for interfacing with a connected analog sensor.
        By default, the mode is set to kAbsolute, thus treating the
        sensor as an absolute sensor.
        """
    def getAppliedOutput(self) -> float: 
        """
        Returns motor controller's output duty cycle.
        """
    def getBusVoltage(self) -> float: 
        """
        Returns the voltage fed into the motor controller.
        """
    def getClosedLoopRampRate(self) -> float: 
        """
        Get the configured closed loop ramp rate

        This is the maximum rate at which the motor controller's output
        is allowed to change.

        :returns: rampte rate time in seconds to go from 0 to full throttle.
        """
    def getEncoder(self, encoderType: SparkMaxRelativeEncoder.Type = Type.kHallSensor, countsPerRev: int = 42) -> SparkMaxRelativeEncoder: 
        """
        Returns an object for interfacing with the encoder connected to the
        encoder pins or front port of the SPARK MAX.

        The default encoder type is assumed to be the hall effect for brushless.
        This can be modified for brushed DC to use an quadrature encoder.
        """
    def getFault(self, faultID: CANSparkMax.FaultID) -> bool: 
        """
        Returns whether the fault with the given ID occurred.
        """
    def getFaults(self) -> int: 
        """
        Returns fault bits.
        """
    def getForwardLimitSwitch(self, switchType: SparkMaxLimitSwitch.Type) -> SparkMaxLimitSwitch: 
        """
        Returns an object for interfacing with the forward limit switch connected
        to the appropriate pins on the data port.

        This call will disable support for the alternate encoder.

        :param switchType: Whether the limit switch is normally open or normally
                           closed.
        """
    def getIdleMode(self) -> CANSparkMax.IdleMode: 
        """
        Gets the idle mode setting for the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :returns: IdleMode Idle mode setting
        """
    def getInverted(self) -> bool: 
        """
        Common interface for returning the inversion state of a speed controller.

        This call has no effect if the controller is a follower.

        :returns: isInverted The state of inversion, true is inverted.
        """
    def getLastError(self) -> REVLibError: 
        """
        All device errors are tracked on a per thread basis for all
        devices in that thread. This is meant to be called
        immediately following another call that has the possibility
        of throwing an error to validate if an  error has occurred.

        :returns: the last error that was generated.
        """
    def getMotorTemperature(self) -> float: 
        """
        Returns the motor temperature in Celsius.
        """
    def getOpenLoopRampRate(self) -> float: 
        """
        Get the configured open loop ramp rate

        This is the maximum rate at which the motor controller's output
        is allowed to change.

        :returns: rampte rate time in seconds to go from 0 to full throttle.
        """
    def getOutputCurrent(self) -> float: 
        """
        Returns motor controller's output current in Amps.
        """
    def getPIDController(self) -> SparkMaxPIDController: 
        """
        Returns an object for interfacing with the integrated PID controller.
        """
    def getReverseLimitSwitch(self, switchType: SparkMaxLimitSwitch.Type) -> SparkMaxLimitSwitch: 
        """
        Returns an object for interfacing with the reverse limit switch connected
        to the appropriate pins on the data port.

        This call will disable support for the alternate encoder.

        :param switchType: Whether the limit switch is normally open or normally
                           closed.
        """
    def getSoftLimit(self, direction: CANSparkMax.SoftLimitDirection) -> float: 
        """
        Get the soft limit setting in the controller

        :param direction: the direction of motion to restrict

        :returns: position soft limit setting of the controller
        """
    def getStickyFault(self, faultID: CANSparkMax.FaultID) -> bool: 
        """
        Returns whether the sticky fault with the given ID occurred.
        """
    def getStickyFaults(self) -> int: 
        """
        Returns sticky fault bits.
        """
    def getVoltageCompensationNominalVoltage(self) -> float: 
        """
        Get the configured voltage compensation nominal voltage value

        :returns: The nominal voltage for voltage compensation mode.
        """
    def isFollower(self) -> bool: 
        """
        Returns whether the controller is following another controller

        :returns: True if this device is following another controller
                  false otherwise
        """
    def isSoftLimitEnabled(self, direction: CANSparkMax.SoftLimitDirection) -> bool: 
        """
        Returns true if the soft limit is enabled.
        """
    def set(self, speed: float) -> None: 
        """
        Common interface for setting the speed of a speed controller.

        :param speed: The speed to set.  Value should be between -1.0 and 1.0.
        """
    def setCANTimeout(self, milliseconds: int) -> REVLibError: 
        """
        Sets timeout for sending CAN messages. A timeout of 0 also means that
        error handling will be done automatically by registering calls and
        waiting for responses, rather than needing to call GetLastError().

        :param milliseconds: The timeout in milliseconds.
        """
    def setClosedLoopRampRate(self, rate: float) -> REVLibError: 
        """
        Sets the ramp rate for closed loop control modes.

        This is the maximum rate at which the motor controller's output
        is allowed to change.

        :param rate: Time in seconds to go from 0 to full throttle.
        """
    def setIdleMode(self, mode: CANSparkMax.IdleMode) -> REVLibError: 
        """
        Sets the idle mode setting for the SPARK MAX.

        :param mode: Idle mode (coast or brake).
        """
    def setInverted(self, isInverted: bool) -> None: 
        """
        Common interface for inverting direction of a speed controller.

        This call has no effect if the controller is a follower. To invert
        a follower, see the follow() method.

        :param isInverted: The state of inversion, true is inverted.
        """
    def setOpenLoopRampRate(self, rate: float) -> REVLibError: 
        """
        Sets the ramp rate for open loop control modes.

        This is the maximum rate at which the motor controller's output
        is allowed to change.

        :param rate: Time in seconds to go from 0 to full throttle.
        """
    def setSecondaryCurrentLimit(self, limit: float, limitCycles: int = 0) -> REVLibError: 
        """
        Sets the secondary current limit in Amps.

        The motor controller will disable the output of the controller briefly
        if the current limit is exceeded to reduce the current. This limit is
        a simplified 'on/off' controller. This limit is enabled by default
        but is set higher than the default Smart Current Limit.

        The time the controller is off after the current limit is reached
        is determined by the parameter limitCycles, which is the number of
        PWM cycles (20kHz). The recommended value is the default of 0 which
        is the minimum time and is part of a PWM cycle from when the over
        current is detected. This allows the controller to regulate the current
        close to the limit value.

        The total time is set by the equation

        ::

          t = (50us - t0) + 50us * limitCycles
          t = total off time after over current
          t0 = time from the start of the PWM cycle until over current is detected

        :param limit:       The current limit in Amps.
        :param limitCycles: The number of additional PWM cycles to turn
                            the driver off after overcurrent is detected.
        """
    @typing.overload
    def setSmartCurrentLimit(self, limit: int) -> REVLibError: 
        """
        Sets the current limit in Amps.

        The motor controller will reduce the controller voltage output to avoid
        surpassing this limit. This limit is enabled by default and used for
        brushless only. This limit is highly recommended when using the NEO
        brushless motor.

        The NEO Brushless Motor has a low internal resistance, which
        can mean large current spikes that could be enough to cause damage to
        the motor and controller. This current limit provides a smarter
        strategy to deal with high current draws and keep the motor and
        controller operating in a safe region.

        :param limit: The current limit in Amps.

        Sets the current limit in Amps.

        The motor controller will reduce the controller voltage output to avoid
        surpassing this limit. This limit is enabled by default and used for
        brushless only. This limit is highly recommended when using the NEO
        brushless motor.

        The NEO Brushless Motor has a low internal resistance, which
        can mean large current spikes that could be enough to cause damage to
        the motor and controller. This current limit provides a smarter
        strategy to deal with high current draws and keep the motor and
        controller operating in a safe region.

        The controller can also limit the current based on the RPM of the motor
        in a linear fashion to help with controllability in closed loop control.
        For a response that is linear the entire RPM range leave limit RPM at 0.

        :param stallLimit: The current limit in Amps at 0 RPM.
        :param freeLimit:  The current limit at free speed (5700RPM for NEO).
        :param limitRPM:   RPM less than this value will be set to the stallLimit,
                           RPM values greater than limitRPM will scale linearly to freeLimit
        """
    @typing.overload
    def setSmartCurrentLimit(self, stallLimit: int, freeLimit: int, limitRPM: int = 20000) -> REVLibError: ...
    def setSoftLimit(self, direction: CANSparkMax.SoftLimitDirection, limit: float) -> REVLibError: 
        """
        Set the soft limit based on position. The default unit is
        rotations, but will match the unit scaling set by the user.

        Note that this value is not scaled internally so care must
        be taken to make sure these units match the desired conversion

        :param direction: the direction of motion to restrict
        :param limit:     position soft limit of the controller
        """
    def setVoltage(self, output: volts) -> None: 
        """
        Sets the voltage output of the SpeedController.  This is equivalent to
        a call to SetReference(output, CANSparkMax::ControlType::kVoltage). The
        behavior of this call differs slightly from the WPILib documentation for
        this call since the device internally sets the desired voltage (not a
        compensation value). That means that this *can* be a 'set-and-forget'
        call.

        :param output: The voltage to output.
        """
    def stopMotor(self) -> None: 
        """
        Common interface to stop the motor until Set is called again.
        """
    kAPIVersion = 132579587
    pass
class CIEColor():
    def __init__(self, X: float, Y: float, Z: float) -> None: ...
    def getX(self) -> float: 
        """
        Get the X component of the color

        :returns: CIE X
        """
    def getY(self) -> float: 
        """
        Get the Y component of the color

        :returns: CIE Y
        """
    def getYx(self) -> float: 
        """
        Get the x calculated coordinate
        of the CIE 19313 color space

        https://en.wikipedia.org/wiki/CIE_1931_color_space

        :returns: CIE Yx
        """
    def getYy(self) -> float: 
        """
        Get the y calculated coordinate
        of the CIE 19313 color space

        https://en.wikipedia.org/wiki/CIE_1931_color_space

        :returns: CIE Yy
        """
    def getZ(self) -> float: 
        """
        Get the Z component of the color

        :returns: CIE Z
        """
    pass
class ColorMatch():
    """
    REV Robotics Color Sensor V3.

    This class allows access to a REV Robotics color sensor V3 on an I2C bus.
    """
    def __init__(self) -> None: ...
    def addColorMatch(self, color: wpilib._wpilib.Color) -> None: 
        """
        Add color to match object

        :param color: color to add to matching
        """
    def matchClosestColor(self, colorToMatch: wpilib._wpilib.Color) -> typing.Tuple[wpilib._wpilib.Color, float]: 
        """
        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values

        :param colorToMatch: color to compare against stored colors
        :param confidence:   The confidence value for this match, this is
                             simply 1 - euclidean distance of the two color vectors

        :returns: Closest matching color
        """
    @typing.overload
    def matchColor(self, colorToMatch: wpilib._wpilib.Color) -> typing.Tuple[typing.Optional[wpilib._wpilib.Color], float]: 
        """
        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values

        :param colorToMatch: color to compare against stored colors

        :returns: Matched color if detected

        MatchColor uses euclidean distance to compare a given normalized RGB
        vector against stored values

        :param colorToMatch: color to compare against stored colors
        :param confidence:   The confidence value for this match, this is
                             simply 1 - euclidean distance of the two color vectors

        :returns: Matched color if detected
        """
    @typing.overload
    def matchColor(self, colorToMatch: wpilib._wpilib.Color) -> typing.Optional[wpilib._wpilib.Color]: ...
    def setConfidenceThreshold(self, confidence: float) -> None: 
        """
        Set the confidence interval for determining color. Defaults to 0.95

        :param confidence: A value between 0 and 1
        """
    pass
class ColorSensorV3():
    """
    REV Robotics Color Sensor V3.

    This class allows access to a REV Robotics color sensor V3 on an I2C bus.
    """
    class ColorMeasurementRate():
        """
        Members:

          k25ms

          k50ms

          k100ms

          k200ms

          k500ms

          k1000ms

          k2000ms
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
        __members__: dict # value = {'k25ms': <ColorMeasurementRate.k25ms: 0>, 'k50ms': <ColorMeasurementRate.k50ms: 1>, 'k100ms': <ColorMeasurementRate.k100ms: 2>, 'k200ms': <ColorMeasurementRate.k200ms: 3>, 'k500ms': <ColorMeasurementRate.k500ms: 4>, 'k1000ms': <ColorMeasurementRate.k1000ms: 5>, 'k2000ms': <ColorMeasurementRate.k2000ms: 7>}
        k1000ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k1000ms: 5>
        k100ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k100ms: 2>
        k2000ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k2000ms: 7>
        k200ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k200ms: 3>
        k25ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k25ms: 0>
        k500ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k500ms: 4>
        k50ms: rev._rev.ColorSensorV3.ColorMeasurementRate # value = <ColorMeasurementRate.k50ms: 1>
        pass
    class ColorResolution():
        """
        Members:

          k20bit

          k19bit

          k18bit

          k17bit

          k16bit

          k13bit
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
        __members__: dict # value = {'k20bit': <ColorResolution.k20bit: 0>, 'k19bit': <ColorResolution.k19bit: 16>, 'k18bit': <ColorResolution.k18bit: 32>, 'k17bit': <ColorResolution.k17bit: 48>, 'k16bit': <ColorResolution.k16bit: 64>, 'k13bit': <ColorResolution.k13bit: 80>}
        k13bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k13bit: 80>
        k16bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k16bit: 64>
        k17bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k17bit: 48>
        k18bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k18bit: 32>
        k19bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k19bit: 16>
        k20bit: rev._rev.ColorSensorV3.ColorResolution # value = <ColorResolution.k20bit: 0>
        pass
    class GainFactor():
        """
        Members:

          k1x

          k3x

          k6x

          k9x

          k18x
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
        __members__: dict # value = {'k1x': <GainFactor.k1x: 0>, 'k3x': <GainFactor.k3x: 1>, 'k6x': <GainFactor.k6x: 2>, 'k9x': <GainFactor.k9x: 3>, 'k18x': <GainFactor.k18x: 4>}
        k18x: rev._rev.ColorSensorV3.GainFactor # value = <GainFactor.k18x: 4>
        k1x: rev._rev.ColorSensorV3.GainFactor # value = <GainFactor.k1x: 0>
        k3x: rev._rev.ColorSensorV3.GainFactor # value = <GainFactor.k3x: 1>
        k6x: rev._rev.ColorSensorV3.GainFactor # value = <GainFactor.k6x: 2>
        k9x: rev._rev.ColorSensorV3.GainFactor # value = <GainFactor.k9x: 3>
        pass
    class LEDCurrent():
        """
        Members:

          kPulse2mA

          kPulse5mA

          kPulse10mA

          kPulse25mA

          kPulse50mA

          kPulse75mA

          kPulse100mA

          kPulse125mA
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
        __members__: dict # value = {'kPulse2mA': <LEDCurrent.kPulse2mA: 0>, 'kPulse5mA': <LEDCurrent.kPulse5mA: 1>, 'kPulse10mA': <LEDCurrent.kPulse10mA: 2>, 'kPulse25mA': <LEDCurrent.kPulse25mA: 3>, 'kPulse50mA': <LEDCurrent.kPulse50mA: 4>, 'kPulse75mA': <LEDCurrent.kPulse75mA: 5>, 'kPulse100mA': <LEDCurrent.kPulse100mA: 6>, 'kPulse125mA': <LEDCurrent.kPulse125mA: 7>}
        kPulse100mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse100mA: 6>
        kPulse10mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse10mA: 2>
        kPulse125mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse125mA: 7>
        kPulse25mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse25mA: 3>
        kPulse2mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse2mA: 0>
        kPulse50mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse50mA: 4>
        kPulse5mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse5mA: 1>
        kPulse75mA: rev._rev.ColorSensorV3.LEDCurrent # value = <LEDCurrent.kPulse75mA: 5>
        pass
    class LEDPulseFrequency():
        """
        Members:

          k60kHz

          k70kHz

          k80kHz

          k90kHz

          k100kHz
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
        __members__: dict # value = {'k60kHz': <LEDPulseFrequency.k60kHz: 24>, 'k70kHz': <LEDPulseFrequency.k70kHz: 64>, 'k80kHz': <LEDPulseFrequency.k80kHz: 40>, 'k90kHz': <LEDPulseFrequency.k90kHz: 48>, 'k100kHz': <LEDPulseFrequency.k100kHz: 56>}
        k100kHz: rev._rev.ColorSensorV3.LEDPulseFrequency # value = <LEDPulseFrequency.k100kHz: 56>
        k60kHz: rev._rev.ColorSensorV3.LEDPulseFrequency # value = <LEDPulseFrequency.k60kHz: 24>
        k70kHz: rev._rev.ColorSensorV3.LEDPulseFrequency # value = <LEDPulseFrequency.k70kHz: 64>
        k80kHz: rev._rev.ColorSensorV3.LEDPulseFrequency # value = <LEDPulseFrequency.k80kHz: 40>
        k90kHz: rev._rev.ColorSensorV3.LEDPulseFrequency # value = <LEDPulseFrequency.k90kHz: 48>
        pass
    class ProximityMeasurementRate():
        """
        Members:

          k6ms

          k12ms

          k25ms

          k50ms

          k100ms

          k200ms

          k400ms
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
        __members__: dict # value = {'k6ms': <ProximityMeasurementRate.k6ms: 1>, 'k12ms': <ProximityMeasurementRate.k12ms: 2>, 'k25ms': <ProximityMeasurementRate.k25ms: 3>, 'k50ms': <ProximityMeasurementRate.k50ms: 4>, 'k100ms': <ProximityMeasurementRate.k100ms: 5>, 'k200ms': <ProximityMeasurementRate.k200ms: 6>, 'k400ms': <ProximityMeasurementRate.k400ms: 7>}
        k100ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k100ms: 5>
        k12ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k12ms: 2>
        k200ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k200ms: 6>
        k25ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k25ms: 3>
        k400ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k400ms: 7>
        k50ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k50ms: 4>
        k6ms: rev._rev.ColorSensorV3.ProximityMeasurementRate # value = <ProximityMeasurementRate.k6ms: 1>
        pass
    class ProximityResolution():
        """
        Members:

          k8bit

          k9bit

          k10bit

          k11bit
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
        __members__: dict # value = {'k8bit': <ProximityResolution.k8bit: 0>, 'k9bit': <ProximityResolution.k9bit: 8>, 'k10bit': <ProximityResolution.k10bit: 16>, 'k11bit': <ProximityResolution.k11bit: 24>}
        k10bit: rev._rev.ColorSensorV3.ProximityResolution # value = <ProximityResolution.k10bit: 16>
        k11bit: rev._rev.ColorSensorV3.ProximityResolution # value = <ProximityResolution.k11bit: 24>
        k8bit: rev._rev.ColorSensorV3.ProximityResolution # value = <ProximityResolution.k8bit: 0>
        k9bit: rev._rev.ColorSensorV3.ProximityResolution # value = <ProximityResolution.k9bit: 8>
        pass
    class RawColor():
        def __init__(self, r: int, g: int, b: int, _ir: int) -> None: ...
        @property
        def blue(self) -> int:
            """
            :type: int
            """
        @blue.setter
        def blue(self, arg0: int) -> None:
            pass
        @property
        def green(self) -> int:
            """
            :type: int
            """
        @green.setter
        def green(self, arg0: int) -> None:
            pass
        @property
        def ir(self) -> int:
            """
            :type: int
            """
        @ir.setter
        def ir(self, arg0: int) -> None:
            pass
        @property
        def red(self) -> int:
            """
            :type: int
            """
        @red.setter
        def red(self, arg0: int) -> None:
            pass
        pass
    def __init__(self, port: wpilib._wpilib.I2C.Port) -> None: 
        """
        Constructs a ColorSensorV3.

        Note that the REV Color Sensor is really two devices in one package:
        a color sensor providing red, green, blue and IR values, and a proximity
        sensor.

        :param port: The I2C port the color sensor is attached to
        """
    def configureColorSensor(self, res: ColorSensorV3.ColorResolution, rate: ColorSensorV3.ColorMeasurementRate) -> None: 
        """
        Configure the color sensor.

        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        color sensor measurements.

        :param res:  Bit resolution output by the respective light sensor ADCs
        :param rate: Measurement rate of the light sensor
        """
    def configureProximitySensor(self, res: ColorSensorV3.ProximityResolution, rate: ColorSensorV3.ProximityMeasurementRate) -> None: 
        """
        Configure the proximity sensor.

        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        proximity sensor measurements.

        :param res:  Bit resolution output by the proximity sensor ADC.
        :param rate: Measurement rate of the proximity sensor
        """
    def configureProximitySensorLED(self, freq: ColorSensorV3.LEDPulseFrequency, current: ColorSensorV3.LEDCurrent, pulses: int) -> None: 
        """
        Configure the the IR LED used by the proximity sensor.

        These settings are only needed for advanced users, the defaults
        will work fine for most teams. Consult the APDS-9151 for more
        information on these configuration settings and how they will affect
        proximity sensor measurements.

        :param freq:   The pulse modulation frequency for the proximity
                       sensor LED
        :param curr:   The pulse current for the proximity sensor LED
        :param pulses: The number of pulses per measurement of the
                       proximity sensor LED
        """
    def getCIEColor(self) -> CIEColor: 
        """
        Get the color converted to CIE XYZ color space using factory
        calibrated constants.

        https://en.wikipedia.org/wiki/CIE_1931_color_space

        :returns: CIEColor value from sensor
        """
    def getColor(self) -> wpilib._wpilib.Color: 
        """
        Get the normalized RGB color from the sensor (normalized based on
        total R + G + B)

        :returns: frc::Color class with normalized sRGB values
        """
    def getIR(self) -> float: 
        """
        Get the normalzied IR value from the sensor. Works best when within 2
        inches and perpendicular to surface of interest.

        :returns: Color class with normalized values
        """
    def getProximity(self) -> int: 
        """
        Get the raw proximity value from the sensor ADC. This value is largest
        when an object is close to the sensor and smallest when
        far away.

        :returns: Proximity measurement value, ranging from 0 to 2047 in
                  default configuration
        """
    def getRawColor(self) -> ColorSensorV3.RawColor: 
        """
        Get the raw color value from the sensor.

        :returns: Raw color values from sensopr
        """
    def hasReset(self) -> bool: 
        """
        Indicates if the device reset. Based on the power on status flag in the
        status register. Per the datasheet:

        Part went through a power-up event, either because the part was turned
        on or because there was power supply voltage disturbance (default at
        first register read).

        This flag is self clearing

        :returns: true if the device was reset
        """
    def isConnected(self) -> bool: 
        """
        Indicates if the device can currently be communicated with.

        :returns: true if the device is currently connected and responsive
        """
    def setGain(self, gain: ColorSensorV3.GainFactor) -> None: 
        """
        Set the gain factor applied to color ADC measurements.

        By default, the gain is set to 3x.

        :param gain: Gain factor applied to color ADC measurements
                     measurements
        """
    pass
class CANAnalog(MotorFeedbackSensor, CANSensor):
    class AnalogMode():
        """
        Members:

          kAbsolute

          kRelative
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
        __members__: dict # value = {'kAbsolute': <AnalogMode.kAbsolute: 0>, 'kRelative': <AnalogMode.kRelative: 1>}
        kAbsolute: rev._rev.CANAnalog.AnalogMode # value = <AnalogMode.kAbsolute: 0>
        kRelative: rev._rev.CANAnalog.AnalogMode # value = <AnalogMode.kRelative: 1>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the number of samples included in the average for velocity readings.

        :returns: The average sampling depth
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the measurement period used for velocity calculation.

        :returns: Measurement period in microseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the sensor. Returns value in the native unit
        of 'volt' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Position of the sensor in volts
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the current conversion factor for the position of the analog
        sensor.

        :returns: Analog position conversion factor
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the sensor. Returns value in the native units of
        'volts per second' by default, and can be changed by a
        scale factor using setVelocityConversionFactor().

        :returns: Velocity of the sensor in volts per second
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the current conversion factor for the velocity of the analog
        sensor.

        :returns: Analog velocity conversion factor
        """
    def getVoltage(self) -> float: 
        """
        Get the voltage of the analog sensor.

        :returns: Voltage of the sensor
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the number of samples in the average for velocity readings. This
        can be any value from 1 to 64.

        When the SparkMax controller is in Brushless mode, this
        will not change any behavior.

        :param depth: The average sampling depth between 1 and 64 (default)

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders. This will throw an error if the user tries to set
        inverted while the SparkMax is Brushless and using the hall
        effect sensor.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the measurement period for velocity calculations.

        The basic formula to calculate velocity is change in position / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds. This number may be
                          between 1 and 100 (default).

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for the position of the analog sensor.
        By default, revolutions per volt is 1. Changing the position conversion
        factor will also change the position units.

        :param factor: The conversion factor which will be multiplied by volts

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for the velocity of the analog sensor.
        By default, revolutions per volt second is 1. Changing the velocity
        conversion factor will also change the velocity units.

        :param factor: The conversion factor which will be multipled by volts per
                       second

        :returns: REVLibError::kOk if successful
        """
    pass
class REVLibError():
    """
    Members:

      kOk

      kError

      kTimeout

      kNotImplemented

      kHALError

      kCantFindFirmware

      kFirmwareTooOld

      kFirmwareTooNew

      kParamInvalidID

      kParamMismatchType

      kParamAccessMode

      kParamInvalid

      kParamNotImplementedDeprecated

      kFollowConfigMismatch

      kInvalid

      kSetpointOutOfRange

      kUnknown

      kCANDisconnected

      kDuplicateCANId

      kInvalidCANId

      kSparkMaxDataPortAlreadyConfiguredDifferently
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
    __members__: dict # value = {'kOk': <REVLibError.kOk: 0>, 'kError': <REVLibError.kError: 1>, 'kTimeout': <REVLibError.kTimeout: 2>, 'kNotImplemented': <REVLibError.kNotImplemented: 3>, 'kHALError': <REVLibError.kHALError: 4>, 'kCantFindFirmware': <REVLibError.kCantFindFirmware: 5>, 'kFirmwareTooOld': <REVLibError.kFirmwareTooOld: 6>, 'kFirmwareTooNew': <REVLibError.kFirmwareTooNew: 7>, 'kParamInvalidID': <REVLibError.kParamInvalidID: 8>, 'kParamMismatchType': <REVLibError.kParamMismatchType: 9>, 'kParamAccessMode': <REVLibError.kParamAccessMode: 10>, 'kParamInvalid': <REVLibError.kParamInvalid: 11>, 'kParamNotImplementedDeprecated': <REVLibError.kParamNotImplementedDeprecated: 12>, 'kFollowConfigMismatch': <REVLibError.kFollowConfigMismatch: 13>, 'kInvalid': <REVLibError.kInvalid: 14>, 'kSetpointOutOfRange': <REVLibError.kSetpointOutOfRange: 15>, 'kUnknown': <REVLibError.kUnknown: 16>, 'kCANDisconnected': <REVLibError.kCANDisconnected: 17>, 'kDuplicateCANId': <REVLibError.kDuplicateCANId: 18>, 'kInvalidCANId': <REVLibError.kInvalidCANId: 19>, 'kSparkMaxDataPortAlreadyConfiguredDifferently': <REVLibError.kSparkMaxDataPortAlreadyConfiguredDifferently: 20>}
    kCANDisconnected: rev._rev.REVLibError # value = <REVLibError.kCANDisconnected: 17>
    kCantFindFirmware: rev._rev.REVLibError # value = <REVLibError.kCantFindFirmware: 5>
    kDuplicateCANId: rev._rev.REVLibError # value = <REVLibError.kDuplicateCANId: 18>
    kError: rev._rev.REVLibError # value = <REVLibError.kError: 1>
    kFirmwareTooNew: rev._rev.REVLibError # value = <REVLibError.kFirmwareTooNew: 7>
    kFirmwareTooOld: rev._rev.REVLibError # value = <REVLibError.kFirmwareTooOld: 6>
    kFollowConfigMismatch: rev._rev.REVLibError # value = <REVLibError.kFollowConfigMismatch: 13>
    kHALError: rev._rev.REVLibError # value = <REVLibError.kHALError: 4>
    kInvalid: rev._rev.REVLibError # value = <REVLibError.kInvalid: 14>
    kInvalidCANId: rev._rev.REVLibError # value = <REVLibError.kInvalidCANId: 19>
    kNotImplemented: rev._rev.REVLibError # value = <REVLibError.kNotImplemented: 3>
    kOk: rev._rev.REVLibError # value = <REVLibError.kOk: 0>
    kParamAccessMode: rev._rev.REVLibError # value = <REVLibError.kParamAccessMode: 10>
    kParamInvalid: rev._rev.REVLibError # value = <REVLibError.kParamInvalid: 11>
    kParamInvalidID: rev._rev.REVLibError # value = <REVLibError.kParamInvalidID: 8>
    kParamMismatchType: rev._rev.REVLibError # value = <REVLibError.kParamMismatchType: 9>
    kParamNotImplementedDeprecated: rev._rev.REVLibError # value = <REVLibError.kParamNotImplementedDeprecated: 12>
    kSetpointOutOfRange: rev._rev.REVLibError # value = <REVLibError.kSetpointOutOfRange: 15>
    kSparkMaxDataPortAlreadyConfiguredDifferently: rev._rev.REVLibError # value = <REVLibError.kSparkMaxDataPortAlreadyConfiguredDifferently: 20>
    kTimeout: rev._rev.REVLibError # value = <REVLibError.kTimeout: 2>
    kUnknown: rev._rev.REVLibError # value = <REVLibError.kUnknown: 16>
    pass
class RelativeEncoder(CANEncoder, MotorFeedbackSensor, CANSensor):
    def getAverageDepth(self) -> int: 
        """
        Get the velocity calculation process's sampling depth for a quadrature or
        hall sensor encoder.

        :returns: The velocity calculation averaging process's sampling depth
        """
    def getCountsPerRevolution(self) -> int: 
        """
        Get the counts per revolution of the quadrature encoder.

        For a description on the difference between CPR, PPR, etc. go to
        https://www.cuidevices.com/blog/what-is-encoder-ppr-cpr-and-lpr

        :returns: Counts per revolution
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the position measurement period used to calculate the velocity of a
        quadrature or hall sensor encoder.

        :returns: Measurement period in milliseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().

        :returns: Number the RPM of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the sampling depth of the velocity calculation process for a
        quadrature or hall sensor encoder. This value sets the number of samples
        in the average for velocity readings. For a quadrature encoder, this can
        be any value from 1 to 64 (default). For a hall sensor, it must be either
        1, 2, 4, or 8 (default).

        :param depth: The velocity calculation process's sampling depth

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders. This will throw an error if the user tries to set
        inverted while the SparkMax is Brushless and using the hall
        effect sensor.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the position measurement period used to calculate the velocity of a
        quadrature or hall sensor encoder. For a quadrature encoder, this number
        may be between 1 and 100 (default). For a hall sensor, this number may be
        between 8 and 64. The default for a hall sensor is 32ms.

        The basic formula to calculate velocity is change in position / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds

        :returns: REVLibError::kOk if successful
        """
    def setPosition(self, position: float) -> REVLibError: 
        """
        Set the position of the encoder.

        :param position: Number of rotations of the motor

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    pass
class SparkMaxAbsoluteEncoder(AbsoluteEncoder, MotorFeedbackSensor, CANSensor):
    """
    Get an instance of this class by using CANSparkMax::GetEncoder() or
    CANSparkMax::GetEncoder(SparkMaxRelativeEncoder::Type, int).
    """
    class Type():
        """
        The type of encoder connected to a SPARK MAX

        Members:

          kDutyCycle
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
        __members__: dict # value = {'kDutyCycle': <Type.kDutyCycle: 0>}
        kDutyCycle: rev._rev.SparkMaxAbsoluteEncoder.Type # value = <Type.kDutyCycle: 0>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the average sampling depth for an absolute encoder

        :returns: The average sampling depth
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the AbsoluteEncoder

        :returns: The phase of the encoder
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'rotations per second' by default, and can be changed by a scale
        factor using setVelocityConversionFactor().

        :returns: Number of rotations per second of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def getZeroOffset(self) -> float: 
        """
        Gets the zero offset for an absolute encoder (the position that is
        reported as zero).

        The zero offset is specified as the reported position of the encoder in
        the desired zero position, if the zero offset was set to 0. It is
        influenced by the absolute encoder's position conversion factor, and
        whether it is inverted.

        :returns: The zero offset of the absolute encoder with the position
                  conversion factor applied
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the average sampling depth for an absolute encoder. This is a bit
        size and should be either 1, 2, 4, 8, 16, 32, 64, or 128

        :param depth: The average sampling depth of 1, 2, 4, 8, 16, 32, 64, or 128

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the AbsoluteEncoder so that it is set to be in phase
        with the motor itself

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setZeroOffset(self, offset: float) -> REVLibError: 
        """
        Sets the zero offset of an absolute encoder (the position that is
        reported as zero).

        The zero offset is specified as the reported position of the encoder in
        the desired zero position, if the zero offset was set to 0. It is
        influenced by the absolute encoder's position conversion factor, and
        whether it is inverted.

        Always call SetPositionConversionFactor() and SetInverted() before
        calling this function.

        :param offset: The zero offset with the position conversion factor applied

        :returns: REVLibError::kOk if successful
        """
    pass
class SparkMaxAlternateEncoder(RelativeEncoder, CANEncoder, MotorFeedbackSensor, CANSensor):
    """
    Get an instance of this class by using CANSparkMax::GetEncoder() or
    CANSparkMax::GetEncoder(CANSparkMax::EncoderType, int).
    """
    class Type():
        """
        The type of encoder wired as an Alternate Encoder on a SPARK MAX

        Members:

          kQuadrature
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
        __members__: dict # value = {'kQuadrature': <Type.kQuadrature: 0>}
        kQuadrature: rev._rev.SparkMaxAlternateEncoder.Type # value = <Type.kQuadrature: 0>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the average sampling depth for a quadrature encoder.

        :returns: The average sampling depth
        """
    def getCountsPerRevolution(self) -> int: 
        """
        Get the counts per revolution of the quadrature encoder.

        For a description on the difference between CPR, PPR, etc. go to
        https://www.cuidevices.com/blog/what-is-encoder-ppr-cpr-and-lpr

        :returns: Counts per revolution
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the number of samples for reading from a quadrature encoder. This
        value sets the number of samples in the average for velocity readings.

        :returns: Measurement period in microseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().

        :returns: Number the RPM of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the average sampling depth for a quadrature encoder. This value
        sets the number of samples in the average for velocity readings. This
        can be any value from 1 to 64.

        :param depth: The average sampling depth between 1 and 64 (default)

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the measurement period for velocity measurements of a quadrature
        encoder.

        The basic formula to calculate velocity is change in position / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds. This number may be
                          between 1 and 100 (default).

        :returns: REVLibError::kOk if successful
        """
    def setPosition(self, position: float) -> REVLibError: 
        """
        Set the position of the encoder.

        :param position: Number of rotations of the motor

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    pass
class SparkMaxAnalogSensor(AnalogInput, CANAnalog, MotorFeedbackSensor, CANSensor):
    class Mode():
        """
        Analog sensors have the ability to either be absolute or relative.
        By default, CANSparkMax::GetAnalog() will return an absolute analog
        sensor, but it can also be configured to be a relative sensor instead.

        Members:

          kAbsolute

          kRelative
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
        __members__: dict # value = {'kAbsolute': <Mode.kAbsolute: 0>, 'kRelative': <Mode.kRelative: 1>}
        kAbsolute: rev._rev.SparkMaxAnalogSensor.Mode # value = <Mode.kAbsolute: 0>
        kRelative: rev._rev.SparkMaxAnalogSensor.Mode # value = <Mode.kRelative: 1>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the number of samples included in the average for velocity readings.

        :returns: The average sampling depth
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the measurement period used for velocity readings.

        :returns: Measurement period in microseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the sensor. Returns value in the native unit
        of 'volt' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Position of the sensor in volts
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the current conversion factor for the position of the analog
        sensor.

        :returns: Analog position conversion factor
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the sensor. Returns value in the native units of
        'volts per second' by default, and can be changed by a
        scale factor using setVelocityConversionFactor().

        :returns: Velocity of the sensor in volts per second
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the current conversion factor for the velocity of the analog
        sensor.

        :returns: Analog velocity conversion factor
        """
    def getVoltage(self) -> float: 
        """
        Get the voltage of the analog sensor.

        :returns: Voltage of the sensor
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the number of samples in the average for velocity readings. This
        can be any value from 1 to 64.

        When the SparkMax controller is in Brushless mode, this
        will not change any behavior.

        :param depth: The average sampling depth between 1 and 64 (default)

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders. This will throw an error if the user tries to set
        inverted while the SparkMax is Brushless and using the hall
        effect sensor.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the measurement period for velocity readings.

        The basic formula to calculate velocity is change in position / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds. This number may be
                          between 1 and 100 (default).

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for the position of the analog sensor.
        By default, revolutions per volt is 1. Changing the position conversion
        factor will also change the position units.

        :param factor: The conversion factor which will be multiplied by volts

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for the velocity of the analog sensor.
        By default, revolutions per volt second is 1. Changing the velocity
        conversion factor will also change the velocity units.

        :param factor: The conversion factor which will be multipled by volts per
                       second

        :returns: REVLibError::kOk is successful
        """
    pass
class SparkMaxLimitSwitch():
    class Type():
        """
        Represents whether the circuit is open or closed when the switch is not
        being pressed

        Members:

          kNormallyOpen

          kNormallyClosed
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
        __members__: dict # value = {'kNormallyOpen': <Type.kNormallyOpen: 0>, 'kNormallyClosed': <Type.kNormallyClosed: 1>}
        kNormallyClosed: rev._rev.SparkMaxLimitSwitch.Type # value = <Type.kNormallyClosed: 1>
        kNormallyOpen: rev._rev.SparkMaxLimitSwitch.Type # value = <Type.kNormallyOpen: 0>
        pass
    def enableLimitSwitch(self, enable: bool) -> REVLibError: 
        """
        Enables or disables controller shutdown based on limit switch.
        """
    def get(self) -> bool: 
        """
        Get the state of the limit switch, whether or not it is enabled
        (limiting the rotation of the motor).
        """
    def isLimitSwitchEnabled(self) -> bool: 
        """
        Returns true if limit switch is enabled.
        """
    pass
class SparkMaxPIDController():
    class AccelStrategy():
        """
        Acceleration strategy used by Smart Motion

        Members:

          kTrapezoidal

          kSCurve
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
        __members__: dict # value = {'kTrapezoidal': <AccelStrategy.kTrapezoidal: 0>, 'kSCurve': <AccelStrategy.kSCurve: 1>}
        kSCurve: rev._rev.SparkMaxPIDController.AccelStrategy # value = <AccelStrategy.kSCurve: 1>
        kTrapezoidal: rev._rev.SparkMaxPIDController.AccelStrategy # value = <AccelStrategy.kTrapezoidal: 0>
        pass
    class ArbFFUnits():
        """
        Units for arbitrary feed-forward

        Members:

          kVoltage

          kPercentOut
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
        __members__: dict # value = {'kVoltage': <ArbFFUnits.kVoltage: 0>, 'kPercentOut': <ArbFFUnits.kPercentOut: 1>}
        kPercentOut: rev._rev.SparkMaxPIDController.ArbFFUnits # value = <ArbFFUnits.kPercentOut: 1>
        kVoltage: rev._rev.SparkMaxPIDController.ArbFFUnits # value = <ArbFFUnits.kVoltage: 0>
        pass
    def getD(self, slotID: int = 0) -> float: 
        """
        Get the Derivative Gain constant of the PIDF controller on the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double D Gain value
        """
    def getDFilter(self, slotID: int = 0) -> float: 
        """
        Get the Derivative Filter constant of the PIDF controller on the SPARK
        MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double D Filter value
        """
    def getFF(self, slotID: int = 0) -> float: 
        """
        Get the Feed-forward Gain constant of the PIDF controller on the SPARK
        MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double F Gain value
        """
    def getI(self, slotID: int = 0) -> float: 
        """
        Get the Integral Gain constant of the PIDF controller on the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double I Gain value
        """
    def getIAccum(self) -> float: 
        """
        Get the I accumulator of the PID controller. This is useful when wishing
        to see what the I accumulator value is to help with PID tuning

        :returns: The value of the I accumulator
        """
    def getIMaxAccum(self, slotID: int = 0) -> float: 
        """
        Get the maximum I accumulator of the PID controller. This value is used
        to constrain the I accumulator to help manage integral wind-up

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The max value to contrain the I accumulator to
        """
    def getIZone(self, slotID: int = 0) -> float: 
        """
        Get the IZone constant of the PIDF controller on the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double IZone value
        """
    def getOutputMax(self, slotID: int = 0) -> float: 
        """
        Get the max output of the PIDF controller on the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double max value
        """
    def getOutputMin(self, slotID: int = 0) -> float: 
        """
        Get the min output of the PIDF controller on the SPARK MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double min value
        """
    def getP(self, slotID: int = 0) -> float: 
        """
        Get the Proportional Gain constant of the PIDF controller on the SPARK
        MAX.

        This uses the Get Parameter API and should be used infrequently. This
        function uses a non-blocking call and will return a cached value if the
        parameter is not returned by the timeout. The timeout can be changed by
        calling SetCANTimeout(int milliseconds)

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: double P Gain value
        """
    def getPositionPIDWrappingEnabled(self) -> bool: 
        """
        Get whether or not PID Wrapping for position closed loop control is
        enabled

        :returns: true if PID Wrapping is enabled
        """
    def getPositionPIDWrappingMaxInput(self) -> float: 
        """
        Get the maximum input value for PID Wrapping with position closed loop
        control

        :returns: the maximum input value
        """
    def getPositionPIDWrappingMinInput(self) -> float: 
        """
        Get the minimum input value for PID Wrapping with position closed loop
        control

        :returns: the minimum in put value
        """
    def getSmartMotionAccelStrategy(self, slotID: int = 0) -> SparkMaxPIDController.AccelStrategy: 
        """
        Get the acceleration strategy used to control acceleration on the motor.
        The current strategy is trapezoidal motion profiling.

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The acceleration strategy to use for the automatically generated
                  motion profile
        """
    def getSmartMotionAllowedClosedLoopError(self, slotID: int = 0) -> float: 
        """
        Get the allowed closed loop error of SmartMotion mode. This value is how
        much deviation from your setpoint is tolerated and is useful in
        preventing oscillation around your setpoint.

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The allowed deviation for your setpoint vs actual position in
                  rotations
        """
    def getSmartMotionMaxAccel(self, slotID: int = 0) -> float: 
        """
        Get the maximum acceleration of the SmartMotion mode. This is the
        accleration that the motor velocity will increase at until the max
        velocity is reached

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The maxmimum acceleration for the motion profile in RPM per
                  second
        """
    def getSmartMotionMaxVelocity(self, slotID: int = 0) -> float: 
        """
        Get the maximum velocity of the SmartMotion mode. This is the velocity
        that is reached in the middle of the profile and is what the motor should
        spend most of its time at

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The maxmimum cruise velocity for the motion profile in RPM
        """
    def getSmartMotionMinOutputVelocity(self, slotID: int = 0) -> float: 
        """
        Get the mimimum velocity of the SmartMotion mode. Any requested
        velocities below this value will be set to 0.

        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: The minimum velocity for the motion profile in RPM
        """
    def setD(self, gain: float, slotID: int = 0) -> REVLibError: 
        """
        Set the Derivative Gain constant of the PIDF controller on the SPARK MAX.
        This uses the Set Parameter API and should be used infrequently. The
        parameter does not presist unless burnFlash() is called.  The recommended
        method to configure this parameter is use to SPARK MAX GUI to tune and
        save parameters.

        :param gain:   The derivative gain value, must be positive
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setDFilter(self, gain: float, slotID: int = 0) -> REVLibError: 
        """
        Set the Derivative Filter constant of the PIDF controller on the SPARK
        MAX. This uses the Set Parameter API and should be used infrequently. The
        parameter does not presist unless burnFlash() is called.

        :param gain:   The derivative filter value, must be a positive number
                       between 0 and 1
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setFF(self, gain: float, slotID: int = 0) -> REVLibError: 
        """
        Set the Feed-forward Gain constant of the PIDF controller on the SPARK
        MAX. This uses the Set Parameter API and should be used infrequently. The
        parameter does not presist unless burnFlash() is called.  The recommended
        method to configure this parameter is use to SPARK MAX GUI to tune and
        save parameters.

        :param gain:   The feed-forward gain value
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setFeedbackDevice(self, sensor: CANSensor) -> REVLibError: 
        """
        Set the controller's feedback device.

        The default feedback device is assumed to be the integrated encoder.
        This is used to changed to another feedback device for the controller,
        such as an analog sensor.

        If there is a limited range on the feedback sensor that should be
        observed by the PIDController, it can be set by calling
        SetFeedbackSensorRange() on the sensor object.

        :param sensor: The sensor to be used as a feedback device

        :returns: REVLibError::kOk if successful
        """
    def setI(self, gain: float, slotID: int = 0) -> REVLibError: 
        """
        Set the Integral Gain constant of the PIDF controller on the SPARK MAX.
        This uses the Set Parameter API and should be used infrequently. The
        parameter does not presist unless burnFlash() is called.  The recommended
        method to configure this parameter is use to SPARK MAX GUI to tune and
        save parameters.

        :param gain:   The integral gain value, must be positive
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setIAccum(self, iAccum: float) -> REVLibError: 
        """
        Set the I accumulator of the PID controller. This is useful when wishing
        to force a reset on the I accumulator of the PID controller. You can also
        preset values to see how it will respond to certain I characteristics

        To use this function, the controller must be in a closed loop control
        mode by calling setReference()

        :param iAccum: The value to set the I accumulator to

        :returns: REVLibError::kOk if successful
        """
    def setIMaxAccum(self, iMaxAccum: float, slotID: int = 0) -> REVLibError: 
        """
        Configure the maximum I accumulator of the PID controller. This value is
        used to constrain the I accumulator to help manage integral wind-up

        :param iMaxAccum: The max value to contrain the I accumulator to
        :param slotID:    Is the gain schedule slot, the value is a number
                          between 0 and 3. Each slot has its own set of gain values and
                          can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setIZone(self, IZone: float, slotID: int = 0) -> REVLibError: 
        """
        Set the IZone range of the PIDF controller on the SPARK MAX. This value
        specifies the range the :math:`|error|` must be within for the integral constant
        to take effect.

        This uses the Set Parameter API and should be used infrequently.
        The parameter does not presist unless :meth:`.burnFlash` is called.
        The recommended method to configure this parameter is to use the
        SPARK MAX GUI to tune and save parameters.

        :param IZone:  The IZone value, must be positive. Set to 0 to disable
        :param slotID: Is the gain schedule slot, the value is a number
             between 0 and 3. Each slot has its own set of gain values and
             can be changed in each control frame using :meth:`setReference`.

        :returns: REVLibError.kOk if successful
        """
    def setOutputRange(self, min: float, max: float, slotID: int = 0) -> REVLibError: 
        """
        Set the min amd max output for the closed loop mode.

        This uses the Set Parameter API and should be used infrequently.
        The parameter does not presist unless burnFlash() is called.
        The recommended method to configure this parameter is to use the
        SPARK MAX GUI to tune and save parameters.

        :param min:    Reverse power minimum to allow the controller to output
        :param max:    Forward power maximum to allow the controller to output
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setP(self, gain: float, slotID: int = 0) -> REVLibError: 
        """
        Set the Proportional Gain constant of the PIDF controller on the SPARK
        MAX. This uses the Set Parameter API and should be used infrequently. The
        parameter does not presist unless burnFlash() is called.  The recommended
        method to configure this parameter is use to SPARK MAX GUI to tune and
        save parameters.

        :param gain:   The proportional gain value, must be positive
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setPositionPIDWrappingEnabled(self, enable: bool) -> REVLibError: 
        """
        Enable or disable PID Wrapping for position closed loop control

        :param enable: Whether position PID wrapping should be enabled

        :returns: REVLibError::kOk if successful
        """
    def setPositionPIDWrappingMaxInput(self, value: float) -> REVLibError: 
        """
        Set the maximum input value for PID Wrapping with position closed loop
        control

        :param value: The maximum input value

        :returns: REVLibError::kOk if successful
        """
    def setPositionPIDWrappingMinInput(self, value: float) -> REVLibError: 
        """
        Set the minimum input value for PID Wrapping with position closed loop
        control

        :param value: The minimum input value

        :returns: REVLibError::kOk if successful
        """
    def setReference(self, value: float, ctrl: CANSparkMaxLowLevel.ControlType, pidSlot: int = 0, arbFeedforward: float = 0, arbFFUnits: SparkMaxPIDController.ArbFFUnits = ArbFFUnits.kVoltage) -> REVLibError: 
        """
        Set the controller reference value based on the selected control mode.

        :param value:          The value to set depending on the control mode. For basic
                               duty cycle control this should be a value between -1 and 1
                               Otherwise: Voltage Control: Voltage (volts) Velocity Control: Velocity
                               (RPM) Position Control: Position (Rotations) Current Control: Current
                               (Amps). The units can be changed for position and velocity by a scale
                               factor using setPositionConversionFactor().
        :param ctrl:           Is the control type
        :param pidSlot:        for this command
        :param arbFeedforward: A value from -32.0 to 32.0 which is a voltage
                               applied to the motor after the result of the specified control mode. The
                               units for the parameter is Volts. This value is set after the control
                               mode, but before any current limits or ramp rates.

        :returns: REVLibError::kOk if successful
        """
    def setSmartMotionAccelStrategy(self, accelStrategy: SparkMaxPIDController.AccelStrategy, slotID: int = 0) -> REVLibError: 
        """
        NOTE: As of the 2022 FRC season, the firmware only supports the
        trapezoidal motion profiling acceleration strategy.

        Configure the acceleration strategy used to control acceleration on the
        motor.

        :param accelStrategy: The acceleration strategy to use for the
                              automatically generated motion profile
        :param slotID:        Is the gain schedule slot, the value is a number
                              between 0 and 3. Each slot has its own set of gain values and
                              can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setSmartMotionAllowedClosedLoopError(self, allowedErr: float, slotID: int = 0) -> REVLibError: 
        """
        Configure the allowed closed loop error of SmartMotion mode. This value
        is how much deviation from your setpoint is tolerated and is useful in
        preventing oscillation around your setpoint.

        :param allowedErr: The allowed deviation for your setpoint vs actual
                           position in rotations
        :param slotID:     Is the gain schedule slot, the value is a number
                           between 0 and 3. Each slot has its own set of gain values and
                           can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setSmartMotionMaxAccel(self, maxAccel: float, slotID: int = 0) -> REVLibError: 
        """
        Configure the maximum acceleration of the SmartMotion mode. This is the
        accleration that the motor velocity will increase at until the max
        velocity is reached

        :param maxAccel: The maxmimum acceleration for the motion profile in RPM
                         per second
        :param slotID:   Is the gain schedule slot, the value is a number
                         between 0 and 3. Each slot has its own set of gain values and
                         can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setSmartMotionMaxVelocity(self, maxVel: float, slotID: int = 0) -> REVLibError: 
        """
        Configure the maximum velocity of the SmartMotion mode. This is the
        velocity that is reached in the middle of the profile and is what the
        motor should spend most of its time at

        :param maxVel: The maxmimum cruise velocity for the motion profile in RPM
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    def setSmartMotionMinOutputVelocity(self, minVel: float, slotID: int = 0) -> REVLibError: 
        """
        Configure the mimimum velocity of the SmartMotion mode. Any requested
        velocities below this value will be set to 0.

        :param minVel: The minimum velocity for the motion profile in RPM
        :param slotID: Is the gain schedule slot, the value is a number
                       between 0 and 3. Each slot has its own set of gain values and
                       can be changed in each control frame using SetReference().

        :returns: REVLibError::kOk if successful
        """
    pass
class SparkMaxRelativeEncoder(RelativeEncoder, CANEncoder, MotorFeedbackSensor, CANSensor):
    """
    Get an instance of this class by using CANSparkMax::GetEncoder() or
    CANSparkMax::GetEncoder(SparkMaxRelativeEncoder::Type, int).
    """
    class Type():
        """
        The type of encoder connected to a SPARK MAX

        Members:

          kNoSensor

          kHallSensor

          kQuadrature
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
        __members__: dict # value = {'kNoSensor': <Type.kNoSensor: 0>, 'kHallSensor': <Type.kHallSensor: 1>, 'kQuadrature': <Type.kQuadrature: 2>}
        kHallSensor: rev._rev.SparkMaxRelativeEncoder.Type # value = <Type.kHallSensor: 1>
        kNoSensor: rev._rev.SparkMaxRelativeEncoder.Type # value = <Type.kNoSensor: 0>
        kQuadrature: rev._rev.SparkMaxRelativeEncoder.Type # value = <Type.kQuadrature: 2>
        pass
    def getAverageDepth(self) -> int: 
        """
        Get the velocity calculation process's sampling depth for a quadrature or
        hall sensor encoder.

        :returns: The velocity calculation averaging process's sampling depth
        """
    def getCountsPerRevolution(self) -> int: 
        """
        Get the counts per revolution of the quadrature encoder.

        For a description on the difference between CPR, PPR, etc. go to
        https://www.cuidevices.com/blog/what-is-encoder-ppr-cpr-and-lpr

        :returns: Counts per revolution
        """
    def getInverted(self) -> bool: 
        """
        Get the phase of the MotorFeedbackSensor. This will just return false
        if the user tries to get inverted while the SparkMax is
        Brushless and using the hall effect sensor.

        :returns: The phase of the encoder
        """
    def getMeasurementPeriod(self) -> int: 
        """
        Get the position measurement period used to calculate the velocity of a
        quadrature or hall sensor encoder.

        :returns: Measurement period in milliseconds
        """
    def getPosition(self) -> float: 
        """
        Get the position of the motor. This returns the native units
        of 'rotations' by default, and can be changed by a scale factor
        using setPositionConversionFactor().

        :returns: Number of rotations of the motor
        """
    def getPositionConversionFactor(self) -> float: 
        """
        Get the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :returns: The conversion factor for position
        """
    def getVelocity(self) -> float: 
        """
        Get the velocity of the motor. This returns the native units
        of 'RPM' by default, and can be changed by a scale factor
        using setVelocityConversionFactor().

        :returns: Number the RPM of the motor
        """
    def getVelocityConversionFactor(self) -> float: 
        """
        Get the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :returns: The conversion factor for velocity
        """
    def setAverageDepth(self, depth: int) -> REVLibError: 
        """
        Set the sampling depth of the velocity calculation process for a
        quadrature or hall sensor encoder. This value sets the number of samples
        in the average for velocity readings. For a quadrature encoder, this can
        be any value from 1 to 64 (default). For a hall sensor, it must be either
        1, 2, 4, or 8 (default).

        :param depth: The velocity calculation process's sampling depth

        :returns: REVLibError::kOk if successful
        """
    def setInverted(self, inverted: bool) -> REVLibError: 
        """
        Set the phase of the MotorFeedbackSensor so that it is set to be in
        phase with the motor itself. This only works for quadrature
        encoders. This will throw an error if the user tries to set
        inverted while the SparkMax is Brushless and using the hall
        effect sensor.

        :param inverted: The phase of the encoder

        :returns: REVLibError::kOk if successful
        """
    def setMeasurementPeriod(self, period_ms: int) -> REVLibError: 
        """
        Set the position measurement period used to calculate the velocity of a
        quadrature or hall sensor encoder. For a quadrature encoder, this number
        may be between 1 and 100 (default). For a hall sensor, this number may be
        between 8 and 64. The default for a hall sensor is 32ms.

        The basic formula to calculate velocity is change in position / change in
        time. This parameter sets the change in time for measurement.

        :param period_ms: Measurement period in milliseconds

        :returns: REVLibError::kOk if successful
        """
    def setPosition(self, position: float) -> REVLibError: 
        """
        Set the position of the encoder.

        :param position: Number of rotations of the motor

        :returns: REVLibError::kOk if successful
        """
    def setPositionConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for position of the encoder. Multiplied by the
        native output units to give you position

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    def setVelocityConversionFactor(self, factor: float) -> REVLibError: 
        """
        Set the conversion factor for velocity of the encoder. Multiplied by the
        native output units to give you velocity

        :param factor: The conversion factor to multiply the native units by

        :returns: REVLibError::kOk if successful
        """
    pass
