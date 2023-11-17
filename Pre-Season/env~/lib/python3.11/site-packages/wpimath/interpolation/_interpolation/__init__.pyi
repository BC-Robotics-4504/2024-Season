from __future__ import annotations
import wpimath.interpolation._interpolation
import typing
import wpimath.geometry._geometry

__all__ = [
    "TimeInterpolatableFloatBuffer",
    "TimeInterpolatablePose2dBuffer",
    "TimeInterpolatableRotation2dBuffer"
]


class TimeInterpolatableFloatBuffer():
    """
    The TimeInterpolatableBuffer provides an easy way to estimate past
    measurements. One application might be in conjunction with the
    DifferentialDrivePoseEstimator, where knowledge of the robot pose at the time
    when vision or other global measurement were recorded is necessary, or for
    recording the past angles of mechanisms as measured by encoders.

    When sampling this buffer, a user-provided function or wpi::Lerp can be
    used. For Pose2ds, we use Twists.

    @tparam T The type stored in this buffer.
    """
    @typing.overload
    def __init__(self, historySize: seconds) -> None: 
        """
        Create a new TimeInterpolatableBuffer.

        :param historySize: The history size of the buffer.
        :param func:        The function used to interpolate between values.

        Create a new TimeInterpolatableBuffer. By default, the interpolation
        function is wpi::Lerp except for Pose2d, which uses the pose exponential.

        :param historySize: The history size of the buffer.
        """
    @typing.overload
    def __init__(self, historySize: seconds, func: typing.Callable[[float, float, float], float]) -> None: ...
    def addSample(self, time: seconds, sample: float) -> None: 
        """
        Add a sample to the buffer.

        :param time:   The timestamp of the sample.
        :param sample: The sample object.
        """
    def clear(self) -> None: 
        """
        Clear all old samples.
        """
    def getInternalBuffer(self) -> typing.List[typing.Tuple[seconds, float]]: 
        """
        Grant access to the internal sample buffer. Used in Pose Estimation to
        replay odometry inputs stored within this buffer.
        """
    def sample(self, time: seconds) -> typing.Optional[float]: 
        """
        Sample the buffer at the given time. If the buffer is empty, an empty
        optional is returned.

        :param time: The time at which to sample the buffer.
        """
    pass
class TimeInterpolatablePose2dBuffer():
    """
    The TimeInterpolatableBuffer provides an easy way to estimate past
    measurements. One application might be in conjunction with the
    DifferentialDrivePoseEstimator, where knowledge of the robot pose at the time
    when vision or other global measurement were recorded is necessary, or for
    recording the past angles of mechanisms as measured by encoders.

    When sampling this buffer, a user-provided function or wpi::Lerp can be
    used. For Pose2ds, we use Twists.

    @tparam T The type stored in this buffer.
    """
    @typing.overload
    def __init__(self, historySize: seconds) -> None: 
        """
        Create a new TimeInterpolatableBuffer.

        :param historySize: The history size of the buffer.
        :param func:        The function used to interpolate between values.

        Create a new TimeInterpolatableBuffer. By default, the interpolation
        function is wpi::Lerp except for Pose2d, which uses the pose exponential.

        :param historySize: The history size of the buffer.
        """
    @typing.overload
    def __init__(self, historySize: seconds, func: typing.Callable[[wpimath.geometry._geometry.Pose2d, wpimath.geometry._geometry.Pose2d, float], wpimath.geometry._geometry.Pose2d]) -> None: ...
    def addSample(self, time: seconds, sample: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Add a sample to the buffer.

        :param time:   The timestamp of the sample.
        :param sample: The sample object.
        """
    def clear(self) -> None: 
        """
        Clear all old samples.
        """
    def getInternalBuffer(self) -> typing.List[typing.Tuple[seconds, wpimath.geometry._geometry.Pose2d]]: 
        """
        Grant access to the internal sample buffer. Used in Pose Estimation to
        replay odometry inputs stored within this buffer.
        """
    def sample(self, time: seconds) -> typing.Optional[wpimath.geometry._geometry.Pose2d]: 
        """
        Sample the buffer at the given time. If the buffer is empty, an empty
        optional is returned.

        :param time: The time at which to sample the buffer.
        """
    pass
class TimeInterpolatableRotation2dBuffer():
    """
    The TimeInterpolatableBuffer provides an easy way to estimate past
    measurements. One application might be in conjunction with the
    DifferentialDrivePoseEstimator, where knowledge of the robot pose at the time
    when vision or other global measurement were recorded is necessary, or for
    recording the past angles of mechanisms as measured by encoders.

    When sampling this buffer, a user-provided function or wpi::Lerp can be
    used. For Pose2ds, we use Twists.

    @tparam T The type stored in this buffer.
    """
    @typing.overload
    def __init__(self, historySize: seconds) -> None: 
        """
        Create a new TimeInterpolatableBuffer.

        :param historySize: The history size of the buffer.
        :param func:        The function used to interpolate between values.

        Create a new TimeInterpolatableBuffer. By default, the interpolation
        function is wpi::Lerp except for Pose2d, which uses the pose exponential.

        :param historySize: The history size of the buffer.
        """
    @typing.overload
    def __init__(self, historySize: seconds, func: typing.Callable[[wpimath.geometry._geometry.Rotation2d, wpimath.geometry._geometry.Rotation2d, float], wpimath.geometry._geometry.Rotation2d]) -> None: ...
    def addSample(self, time: seconds, sample: wpimath.geometry._geometry.Rotation2d) -> None: 
        """
        Add a sample to the buffer.

        :param time:   The timestamp of the sample.
        :param sample: The sample object.
        """
    def clear(self) -> None: 
        """
        Clear all old samples.
        """
    def getInternalBuffer(self) -> typing.List[typing.Tuple[seconds, wpimath.geometry._geometry.Rotation2d]]: 
        """
        Grant access to the internal sample buffer. Used in Pose Estimation to
        replay odometry inputs stored within this buffer.
        """
    def sample(self, time: seconds) -> typing.Optional[wpimath.geometry._geometry.Rotation2d]: 
        """
        Sample the buffer at the given time. If the buffer is empty, an empty
        optional is returned.

        :param time: The time at which to sample the buffer.
        """
    pass
