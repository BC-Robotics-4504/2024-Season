from __future__ import annotations
import wpimath.geometry._geometry
import typing

__all__ = [
    "CoordinateAxis",
    "CoordinateSystem",
    "Pose2d",
    "Pose3d",
    "Quaternion",
    "Rotation2d",
    "Rotation3d",
    "Transform2d",
    "Transform3d",
    "Translation2d",
    "Translation3d",
    "Twist2d",
    "Twist3d"
]


class CoordinateAxis():
    """
    A class representing a coordinate system axis within the NWU coordinate
    system.
    """
    @staticmethod
    def D() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to -Z in the NWU coordinate system.
        """
    @staticmethod
    def E() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to -Y in the NWU coordinate system.
        """
    @staticmethod
    def N() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to +X in the NWU coordinate system.
        """
    @staticmethod
    def S() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to -X in the NWU coordinate system.
        """
    @staticmethod
    def U() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to +Z in the NWU coordinate system.
        """
    @staticmethod
    def W() -> CoordinateAxis: 
        """
        Returns a coordinate axis corresponding to +Y in the NWU coordinate system.
        """
    def __init__(self, x: float, y: float, z: float) -> None: 
        """
        Constructs a coordinate system axis within the NWU coordinate system and
        normalizes it.

        :param x: The x component.
        :param y: The y component.
        :param z: The z component.
        """
    pass
class CoordinateSystem():
    """
    A helper class that converts Pose3d objects between different standard
    coordinate frames.
    """
    @staticmethod
    def EDN() -> CoordinateSystem: 
        """
        Returns an instance of the East-Down-North (EDN) coordinate system.

        The +X axis is east, the +Y axis is down, and the +Z axis is north.
        """
    @staticmethod
    def NED() -> CoordinateSystem: 
        """
        Returns an instance of the NED coordinate system.

        The +X axis is north, the +Y axis is east, and the +Z axis is down.
        """
    @staticmethod
    def NWU() -> CoordinateSystem: 
        """
        Returns an instance of the North-West-Up (NWU) coordinate system.

        The +X axis is north, the +Y axis is west, and the +Z axis is up.
        """
    def __init__(self, positiveX: CoordinateAxis, positiveY: CoordinateAxis, positiveZ: CoordinateAxis) -> None: 
        """
        Constructs a coordinate system with the given cardinal directions for each
        axis.

        :param positiveX: The cardinal direction of the positive x-axis.
        :param positiveY: The cardinal direction of the positive y-axis.
        :param positiveZ: The cardinal direction of the positive z-axis.
                          @throws std::domain_error if the coordinate system isn't special orthogonal
        """
    @staticmethod
    @typing.overload
    def convert(pose: Pose3d, from_: CoordinateSystem, to: CoordinateSystem) -> Pose3d: 
        """
        Converts the given translation from one coordinate system to another.

        :param translation: The translation to convert.
        :param from_:       The coordinate system the translation starts in.
        :param to:          The coordinate system to which to convert.

        :returns: The given translation in the desired coordinate system.

        Converts the given rotation from one coordinate system to another.

        :param rotation: The rotation to convert.
        :param from_:    The coordinate system the rotation starts in.
        :param to:       The coordinate system to which to convert.

        :returns: The given rotation in the desired coordinate system.

        Converts the given pose from one coordinate system to another.

        :param pose:  The pose to convert.
        :param from_: The coordinate system the pose starts in.
        :param to:    The coordinate system to which to convert.

        :returns: The given pose in the desired coordinate system.

        Converts the given transform from one coordinate system to another.

        :param transform: The transform to convert.
        :param from_:     The coordinate system the transform starts in.
        :param to:        The coordinate system to which to convert.

        :returns: The given transform in the desired coordinate system.
        """
    @staticmethod
    @typing.overload
    def convert(rotation: Rotation3d, from_: CoordinateSystem, to: CoordinateSystem) -> Rotation3d: ...
    @staticmethod
    @typing.overload
    def convert(transform: Transform3d, from_: CoordinateSystem, to: CoordinateSystem) -> Transform3d: ...
    @staticmethod
    @typing.overload
    def convert(translation: Translation3d, from_: CoordinateSystem, to: CoordinateSystem) -> Translation3d: ...
    pass
class Pose2d():
    """
    Represents a 2D pose containing translational and rotational elements.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the pose's translation.

        :returns: The x component of the pose's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the pose's translation.

        :returns: The y component of the pose's translation.
        """
    def __add__(self, arg0: Transform2d) -> Pose2d: 
        """
        Transforms the pose by the given transformation and returns the new
        transformed pose.

        ::

          [x_new]    [cos, -sin, 0][transform.x]
          [y_new] += [sin,  cos, 0][transform.y]
          [t_new]    [  0,    0, 1][transform.t]

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def __eq__(self, arg0: Pose2d) -> bool: 
        """
        Checks equality between this Pose2d and another object.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a pose at the origin facing toward the positive X axis.

        Constructs a pose with the specified translation and rotation.

        :param translation: The translational component of the pose.
        :param rotation:    The rotational component of the pose.

        Constructs a pose with x and y translations instead of a separate
        Translation2d.

        :param x:        The x component of the translational component of the pose.
        :param y:        The y component of the translational component of the pose.
        :param rotation: The rotational component of the pose.
        """
    @typing.overload
    def __init__(self, translation: Translation2d, rotation: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, angle: radians) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, rotation: Rotation2d) -> None: ...
    def __mul__(self, arg0: float) -> Pose2d: 
        """
        Multiplies the current pose by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Pose2d.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Pose2d) -> Transform2d: 
        """
        Returns the Transform2d that maps the one pose to another.

        :param other: The initial pose of the transformation.

        :returns: The transform that maps the other pose to the current pose.
        """
    def __truediv__(self, arg0: float) -> Pose2d: 
        """
        Divides the current pose by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Pose2d.
        """
    def exp(self, twist: Twist2d) -> Pose2d: 
        """
        Obtain a new Pose2d from a (constant curvature) velocity.

        See https://file.tavsys.net/control/controls-engineering-in-frc.pdf section
        10.2 "Pose exponential" for a derivation.

        The twist is a change in pose in the robot's coordinate frame since the
        previous pose update. When the user runs exp() on the previous known
        field-relative pose with the argument being the twist, the user will
        receive the new field-relative pose.

        "Exp" represents the pose exponential, which is solving a differential
        equation moving the pose forward in time.

        :param twist: The change in pose in the robot's coordinate frame since the
                      previous pose update. For example, if a non-holonomic robot moves forward
                      0.01 meters and changes angle by 0.5 degrees since the previous pose
                      update, the twist would be Twist2d{0.01_m, 0_m, 0.5_deg}.

        :returns: The new pose of the robot.
        """
    @staticmethod
    @typing.overload
    def fromFeet(x: feet, y: feet, angle: radians) -> Pose2d: ...
    @staticmethod
    @typing.overload
    def fromFeet(x: feet, y: feet, r: Rotation2d) -> Pose2d: ...
    def log(self, end: Pose2d) -> Twist2d: 
        """
        Returns a Twist2d that maps this pose to the end pose. If c is the output
        of a.Log(b), then a.Exp(c) would yield b.

        :param end: The end pose for the transformation.

        :returns: The twist that maps this to end.
        """
    def nearest(self, poses: typing.List[Pose2d]) -> Pose2d: 
        """
        Returns the nearest Pose2d from a collection of poses

        :param poses: The collection of poses.

        :returns: The nearest Pose2d from the collection.
        """
    def relativeTo(self, other: Pose2d) -> Pose2d: 
        """
        Returns the current pose relative to the given pose.

        This function can often be used for trajectory tracking or pose
        stabilization algorithms to get the error between the reference and the
        current pose.

        :param other: The pose that is the origin of the new coordinate frame that
                      the current pose will be converted into.

        :returns: The current pose relative to the new origin pose.
        """
    def rotation(self) -> Rotation2d: 
        """
        Returns the underlying rotation.

        :returns: Reference to the rotational component of the pose.
        """
    def transformBy(self, other: Transform2d) -> Pose2d: 
        """
        Transforms the pose by the given transformation and returns the new pose.
        See + operator for the matrix multiplication performed.

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def translation(self) -> Translation2d: 
        """
        Returns the underlying translation.

        :returns: Reference to the translational component of the pose.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Pose3d():
    """
    Represents a 3D pose containing translational and rotational elements.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the pose's translation.

        :returns: The x component of the pose's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the pose's translation.

        :returns: The y component of the pose's translation.
        """
    def Z(self) -> meters: 
        """
        Returns the Z component of the pose's translation.

        :returns: The z component of the pose's translation.
        """
    def __add__(self, arg0: Transform3d) -> Pose3d: 
        """
        Transforms the pose by the given transformation and returns the new
        transformed pose.

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def __eq__(self, arg0: Pose3d) -> bool: 
        """
        Checks equality between this Pose3d and another object.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a pose at the origin facing toward the positive X axis.

        Constructs a pose with the specified translation and rotation.

        :param translation: The translational component of the pose.
        :param rotation:    The rotational component of the pose.

        Constructs a pose with x, y, and z translations instead of a separate
        Translation3d.

        :param x:        The x component of the translational component of the pose.
        :param y:        The y component of the translational component of the pose.
        :param z:        The z component of the translational component of the pose.
        :param rotation: The rotational component of the pose.

        Constructs a 3D pose from a 2D pose in the X-Y plane.

        :param pose: The 2D pose.
        """
    @typing.overload
    def __init__(self, pose: Pose2d) -> None: ...
    @typing.overload
    def __init__(self, translation: Translation3d, rotation: Rotation3d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, z: meters, rotation: Rotation3d) -> None: ...
    def __mul__(self, arg0: float) -> Pose3d: 
        """
        Multiplies the current pose by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Pose2d.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Pose3d) -> Transform3d: 
        """
        Returns the Transform3d that maps the one pose to another.

        :param other: The initial pose of the transformation.

        :returns: The transform that maps the other pose to the current pose.
        """
    def __truediv__(self, arg0: float) -> Pose3d: 
        """
        Divides the current pose by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Pose2d.
        """
    def exp(self, twist: Twist3d) -> Pose3d: 
        """
        Obtain a new Pose3d from a (constant curvature) velocity.

        The twist is a change in pose in the robot's coordinate frame since the
        previous pose update. When the user runs exp() on the previous known
        field-relative pose with the argument being the twist, the user will
        receive the new field-relative pose.

        "Exp" represents the pose exponential, which is solving a differential
        equation moving the pose forward in time.

        :param twist: The change in pose in the robot's coordinate frame since the
                      previous pose update. For example, if a non-holonomic robot moves forward
                      0.01 meters and changes angle by 0.5 degrees since the previous pose
                      update, the twist would be Twist3d{0.01_m, 0_m, 0_m, Rotation3d{0.0, 0.0,
                      0.5_deg}}.

        :returns: The new pose of the robot.
        """
    @staticmethod
    def fromFeet(x: feet, y: feet, z: feet, r: Rotation3d) -> Pose3d: ...
    def log(self, end: Pose3d) -> Twist3d: 
        """
        Returns a Twist3d that maps this pose to the end pose. If c is the output
        of a.Log(b), then a.Exp(c) would yield b.

        :param end: The end pose for the transformation.

        :returns: The twist that maps this to end.
        """
    def relativeTo(self, other: Pose3d) -> Pose3d: 
        """
        Returns the current pose relative to the given pose.

        This function can often be used for trajectory tracking or pose
        stabilization algorithms to get the error between the reference and the
        current pose.

        :param other: The pose that is the origin of the new coordinate frame that
                      the current pose will be converted into.

        :returns: The current pose relative to the new origin pose.
        """
    def rotation(self) -> Rotation3d: 
        """
        Returns the underlying rotation.

        :returns: Reference to the rotational component of the pose.
        """
    def toPose2d(self) -> Pose2d: 
        """
        Returns a Pose2d representing this Pose3d projected into the X-Y plane.
        """
    def transformBy(self, other: Transform3d) -> Pose3d: 
        """
        Transforms the pose by the given transformation and returns the new pose.
        See + operator for the matrix multiplication performed.

        :param other: The transform to transform the pose by.

        :returns: The transformed pose.
        """
    def translation(self) -> Translation3d: 
        """
        Returns the underlying translation.

        :returns: Reference to the translational component of the pose.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def z(self) -> meters:
        """
        :type: meters
        """
    @property
    def z_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Quaternion():
    def W(self) -> float: 
        """
        Returns W component of the quaternion.
        """
    def X(self) -> float: 
        """
        Returns X component of the quaternion.
        """
    def Y(self) -> float: 
        """
        Returns Y component of the quaternion.
        """
    def Z(self) -> float: 
        """
        Returns Z component of the quaternion.
        """
    def __eq__(self, arg0: Quaternion) -> bool: 
        """
        Checks equality between this Quaternion and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a quaternion with a default angle of 0 degrees.

        Constructs a quaternion with the given components.

        :param w: W component of the quaternion.
        :param x: X component of the quaternion.
        :param y: Y component of the quaternion.
        :param z: Z component of the quaternion.
        """
    @typing.overload
    def __init__(self, w: float, x: float, y: float, z: float) -> None: ...
    def __mul__(self, arg0: Quaternion) -> Quaternion: 
        """
        Multiply with another quaternion.

        :param other: The other quaternion.
        """
    def __repr__(self) -> str: ...
    def inverse(self) -> Quaternion: 
        """
        Returns the inverse of the quaternion.
        """
    def normalize(self) -> Quaternion: 
        """
        Normalizes the quaternion.
        """
    def toRotationVector(self) -> numpy.ndarray[numpy.float64, _Shape[3, 1]]: 
        """
        Returns the rotation vector representation of this quaternion.

        This is also the log operator of SO(3).
        """
    __hash__ = None
    pass
class Rotation2d():
    """
    A rotation in a 2D coordinate frame represented by a point on the unit circle
    (cosine and sine).

    The angle is continuous, that is if a Rotation2d is constructed with 361
    degrees, it will return 361 degrees. This allows algorithms that wouldn't
    want to see a discontinuity in the rotations as it sweeps past from 360 to 0
    on the second time around.
    """
    def __add__(self, arg0: Rotation2d) -> Rotation2d: 
        """
        Adds two rotations together, with the result being bounded between -pi and
        pi.

        For example, <code>Rotation2d{30_deg} + Rotation2d{60_deg}</code> equals
        <code>Rotation2d{units::radian_t{std::numbers::pi/2.0}}</code>

        :param other: The rotation to add.

        :returns: The sum of the two rotations.
        """
    def __eq__(self, arg0: Rotation2d) -> bool: 
        """
        Checks equality between this Rotation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Rotation2d with a default angle of 0 degrees.

        Constructs a Rotation2d with the given radian value.

        :param value: The value of the angle in radians.

        Constructs a Rotation2d with the given x and y (cosine and sine)
        components. The x and y don't have to be normalized.

        :param x: The x component or cosine of the rotation.
        :param y: The y component or sine of the rotation.
        """
    @typing.overload
    def __init__(self, value: radians) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float) -> None: ...
    def __mul__(self, arg0: float) -> Rotation2d: 
        """
        Multiplies the current rotation by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Rotation2d.
        """
    def __neg__(self) -> Rotation2d: 
        """
        Takes the inverse of the current rotation. This is simply the negative of
        the current angular value.

        :returns: The inverse of the current rotation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Rotation2d) -> Rotation2d: 
        """
        Subtracts the new rotation from the current rotation and returns the new
        rotation.

        For example, <code>Rotation2d{10_deg} - Rotation2d{100_deg}</code> equals
        <code>Rotation2d{units::radian_t{-std::numbers::pi/2.0}}</code>

        :param other: The rotation to subtract.

        :returns: The difference between the two rotations.
        """
    def __truediv__(self, arg0: float) -> Rotation2d: 
        """
        Divides the current rotation by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Rotation2d.
        """
    def cos(self) -> float: 
        """
        Returns the cosine of the rotation.

        :returns: The cosine of the rotation.
        """
    def degrees(self) -> degrees: 
        """
        Returns the degree value of the rotation.

        :returns: The degree value of the rotation.
                  @see InputModulus to constrain the angle within (-180, 180]
        """
    @staticmethod
    def fromDegrees(value: degrees) -> Rotation2d: ...
    def radians(self) -> radians: 
        """
        Returns the radian value of the rotation.

        :returns: The radian value of the rotation.
                  @see AngleModulus to constrain the angle within (-pi, pi]
        """
    def rotateBy(self, other: Rotation2d) -> Rotation2d: 
        """
        Adds the new rotation to the current rotation using a rotation matrix.

        ::

          [cos_new]   [other.cos, -other.sin][cos]
          [sin_new] = [other.sin,  other.cos][sin]
          value_new = std::atan2(sin_new, cos_new)

        :param other: The rotation to rotate by.

        :returns: The new rotated Rotation2d.
        """
    def sin(self) -> float: 
        """
        Returns the sine of the rotation.

        :returns: The sine of the rotation.
        """
    def tan(self) -> float: 
        """
        Returns the tangent of the rotation.

        :returns: The tangent of the rotation.
        """
    __hash__ = None
    pass
class Rotation3d():
    """
    A rotation in a 3D coordinate frame represented by a quaternion.
    """
    def X(self) -> radians: 
        """
        Returns the counterclockwise rotation angle around the X axis (roll).
        """
    def Y(self) -> radians: 
        """
        Returns the counterclockwise rotation angle around the Y axis (pitch).
        """
    def Z(self) -> radians: 
        """
        Returns the counterclockwise rotation angle around the Z axis (yaw).
        """
    def __add__(self, arg0: Rotation3d) -> Rotation3d: 
        """
        Adds two rotations together.

        :param other: The rotation to add.

        :returns: The sum of the two rotations.
        """
    def __eq__(self, arg0: Rotation3d) -> bool: 
        """
        Checks equality between this Rotation3d and another object.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Rotation3d with a default angle of 0 degrees.

        Constructs a Rotation3d from a quaternion.

        :param q: The quaternion.

        Constructs a Rotation3d from extrinsic roll, pitch, and yaw.

        Extrinsic rotations occur in that order around the axes in the fixed global
        frame rather than the body frame.

        Angles are measured counterclockwise with the rotation axis pointing "out
        of the page". If you point your right thumb along the positive axis
        direction, your fingers curl in the direction of positive rotation.

        :param roll:  The counterclockwise rotation angle around the X axis (roll).
        :param pitch: The counterclockwise rotation angle around the Y axis (pitch).
        :param yaw:   The counterclockwise rotation angle around the Z axis (yaw).

        Constructs a Rotation3d with the given axis-angle representation. The axis
        doesn't have to be normalized.

        :param axis:  The rotation axis.
        :param angle: The rotation around the axis.

        Constructs a Rotation3d with the given rotation vector representation. This
        representation is equivalent to axis-angle, where the normalized axis is
        multiplied by the rotation around the axis in radians.

        :param rvec: The rotation vector.

        Constructs a Rotation3d from a rotation matrix.

        :param rotationMatrix: The rotation matrix.
                               @throws std::domain_error if the rotation matrix isn't special orthogonal.

        Constructs a Rotation3d that rotates the initial vector onto the final
        vector.

        This is useful for turning a 3D vector (final) into an orientation relative
        to a coordinate system vector (initial).

        :param initial: The initial vector.
        :param final:   The final vector.
        """
    @typing.overload
    def __init__(self, axis: numpy.ndarray[numpy.float64, _Shape[3, 1]], angle: radians) -> None: ...
    @typing.overload
    def __init__(self, initial: numpy.ndarray[numpy.float64, _Shape[3, 1]], final: numpy.ndarray[numpy.float64, _Shape[3, 1]]) -> None: ...
    @typing.overload
    def __init__(self, q: Quaternion) -> None: ...
    @typing.overload
    def __init__(self, roll: radians, pitch: radians, yaw: radians) -> None: ...
    @typing.overload
    def __init__(self, rotationMatrix: numpy.ndarray[numpy.float64, _Shape[3, 3]]) -> None: ...
    @typing.overload
    def __init__(self, rvec: numpy.ndarray[numpy.float64, _Shape[3, 1]]) -> None: ...
    def __mul__(self, arg0: float) -> Rotation3d: 
        """
        Multiplies the current rotation by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Rotation3d.
        """
    def __neg__(self) -> Rotation3d: 
        """
        Takes the inverse of the current rotation.

        :returns: The inverse of the current rotation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Rotation3d) -> Rotation3d: 
        """
        Subtracts the new rotation from the current rotation and returns the new
        rotation.

        :param other: The rotation to subtract.

        :returns: The difference between the two rotations.
        """
    def __truediv__(self, arg0: float) -> Rotation3d: 
        """
        Divides the current rotation by a scalar.

        :param scalar: The scalar.

        :returns: The new scaled Rotation3d.
        """
    def axis(self) -> numpy.ndarray[numpy.float64, _Shape[3, 1]]: 
        """
        Returns the axis in the axis-angle representation of this rotation.
        """
    @staticmethod
    def fromDegrees(roll: degrees, pitch: degrees, yaw: degrees) -> Rotation3d: ...
    def getQuaternion(self) -> Quaternion: 
        """
        Returns the quaternion representation of the Rotation3d.
        """
    def rotateBy(self, other: Rotation3d) -> Rotation3d: 
        """
        Adds the new rotation to the current rotation.

        :param other: The rotation to rotate by.

        :returns: The new rotated Rotation3d.
        """
    def toRotation2d(self) -> Rotation2d: 
        """
        Returns a Rotation2d representing this Rotation3d projected into the X-Y
        plane.
        """
    @property
    def angle(self) -> radians:
        """
        :type: radians
        """
    @property
    def angle_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @property
    def x(self) -> radians:
        """
        :type: radians
        """
    @property
    def x_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @property
    def y(self) -> radians:
        """
        :type: radians
        """
    @property
    def y_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @property
    def z(self) -> radians:
        """
        :type: radians
        """
    @property
    def z_degrees(self) -> degrees:
        """
        :type: degrees
        """
    __hash__ = None
    pass
class Transform2d():
    """
    Represents a transformation for a Pose2d.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the transformation's translation.

        :returns: The x component of the transformation's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the transformation's translation.

        :returns: The y component of the transformation's translation.
        """
    def __add__(self, arg0: Transform2d) -> Transform2d: 
        """
        Composes two transformations.

        :param other: The transform to compose with this one.

        :returns: The composition of the two transformations.
        """
    def __eq__(self, arg0: Transform2d) -> bool: 
        """
        Checks equality between this Transform2d and another object.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs the transform that maps the initial pose to the final pose.

        :param initial: The initial pose for the transformation.
        :param final:   The final pose for the transformation.

        Constructs a transform with the given translation and rotation components.

        :param translation: Translational component of the transform.
        :param rotation:    Rotational component of the transform.

        Constructs the identity transform -- maps an initial pose to itself.
        """
    @typing.overload
    def __init__(self, initial: Pose2d, final: Pose2d) -> None: ...
    @typing.overload
    def __init__(self, translation: Translation2d, rotation: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, angle: radians) -> None: ...
    def __mul__(self, arg0: float) -> Transform2d: 
        """
        Multiplies the transform by the scalar.

        :param scalar: The scalar.

        :returns: The scaled Transform2d.
        """
    def __repr__(self) -> str: ...
    def __truediv__(self, arg0: float) -> Transform2d: 
        """
        Divides the transform by the scalar.

        :param scalar: The scalar.

        :returns: The scaled Transform2d.
        """
    @staticmethod
    def fromFeet(x: feet, y: feet, angle: radians) -> Transform2d: ...
    def inverse(self) -> Transform2d: 
        """
        Invert the transformation. This is useful for undoing a transformation.

        :returns: The inverted transformation.
        """
    def rotation(self) -> Rotation2d: 
        """
        Returns the rotational component of the transformation.

        :returns: Reference to the rotational component of the transform.
        """
    def translation(self) -> Translation2d: 
        """
        Returns the translation component of the transformation.

        :returns: Reference to the translational component of the transform.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Transform3d():
    """
    Represents a transformation for a Pose3d.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the transformation's translation.

        :returns: The x component of the transformation's translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the transformation's translation.

        :returns: The y component of the transformation's translation.
        """
    def Z(self) -> meters: 
        """
        Returns the Z component of the transformation's translation.

        :returns: The z component of the transformation's translation.
        """
    def __add__(self, arg0: Transform3d) -> Transform3d: 
        """
        Composes two transformations.

        :param other: The transform to compose with this one.

        :returns: The composition of the two transformations.
        """
    def __eq__(self, arg0: Transform3d) -> bool: 
        """
        Checks equality between this Transform3d and another object.
        """
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs the transform that maps the initial pose to the final pose.

        :param initial: The initial pose for the transformation.
        :param final:   The final pose for the transformation.

        Constructs a transform with the given translation and rotation components.

        :param translation: Translational component of the transform.
        :param rotation:    Rotational component of the transform.

        Constructs the identity transform -- maps an initial pose to itself.
        """
    @typing.overload
    def __init__(self, initial: Pose3d, final: Pose3d) -> None: ...
    @typing.overload
    def __init__(self, translation: Translation3d, rotation: Rotation3d) -> None: ...
    def __mul__(self, arg0: float) -> Transform3d: 
        """
        Multiplies the transform by the scalar.

        :param scalar: The scalar.

        :returns: The scaled Transform3d.
        """
    def __repr__(self) -> str: ...
    def __truediv__(self, arg0: float) -> Transform3d: 
        """
        Divides the transform by the scalar.

        :param scalar: The scalar.

        :returns: The scaled Transform3d.
        """
    def inverse(self) -> Transform3d: 
        """
        Invert the transformation. This is useful for undoing a transformation.

        :returns: The inverted transformation.
        """
    def rotation(self) -> Rotation3d: 
        """
        Returns the rotational component of the transformation.

        :returns: Reference to the rotational component of the transform.
        """
    def translation(self) -> Translation3d: 
        """
        Returns the translation component of the transformation.

        :returns: Reference to the translational component of the transform.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def z(self) -> meters:
        """
        :type: meters
        """
    @property
    def z_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Translation2d():
    """
    Represents a translation in 2D space.
    This object can be used to represent a point or a vector.

    This assumes that you are using conventional mathematical axes.
    When the robot is at the origin facing in the positive X direction, forward
    is positive X and left is positive Y.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the translation.

        :returns: The X component of the translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the translation.

        :returns: The Y component of the translation.
        """
    def __abs__(self) -> meters: ...
    def __add__(self, arg0: Translation2d) -> Translation2d: 
        """
        Returns the sum of two translations in 2D space.

        For example, Translation3d{1.0, 2.5} + Translation3d{2.0, 5.5} =
        Translation3d{3.0, 8.0}.

        :param other: The translation to add.

        :returns: The sum of the translations.
        """
    def __eq__(self, arg0: Translation2d) -> bool: 
        """
        Checks equality between this Translation2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __getitem__(self, arg0: int) -> meters: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Translation2d with X and Y components equal to zero.

        Constructs a Translation2d with the X and Y components equal to the
        provided values.

        :param x: The x component of the translation.
        :param y: The y component of the translation.

        Constructs a Translation2d with the provided distance and angle. This is
        essentially converting from polar coordinates to Cartesian coordinates.

        :param distance: The distance from the origin to the end of the translation.
        :param angle:    The angle between the x-axis and the translation vector.
        """
    @typing.overload
    def __init__(self, distance: meters, angle: Rotation2d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters) -> None: ...
    def __len__(self) -> int: ...
    def __mul__(self, arg0: float) -> Translation2d: 
        """
        Returns the translation multiplied by a scalar.

        For example, Translation2d{2.0, 2.5} * 2 = Translation2d{4.0, 5.0}.

        :param scalar: The scalar to multiply by.

        :returns: The scaled translation.
        """
    def __neg__(self) -> Translation2d: 
        """
        Returns the inverse of the current translation. This is equivalent to
        rotating by 180 degrees, flipping the point over both axes, or negating all
        components of the translation.

        :returns: The inverse of the current translation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Translation2d) -> Translation2d: 
        """
        Returns the difference between two translations.

        For example, Translation2d{5.0, 4.0} - Translation2d{1.0, 2.0} =
        Translation2d{4.0, 2.0}.

        :param other: The translation to subtract.

        :returns: The difference between the two translations.
        """
    def __truediv__(self, arg0: float) -> Translation2d: 
        """
        Returns the translation divided by a scalar.

        For example, Translation2d{2.0, 2.5} / 2 = Translation2d{1.0, 1.25}.

        :param scalar: The scalar to divide by.

        :returns: The scaled translation.
        """
    def angle(self) -> Rotation2d: 
        """
        Returns the angle this translation forms with the positive X axis.

        :returns: The angle of the translation
        """
    def distance(self, other: Translation2d) -> meters: 
        """
        Calculates the distance between two translations in 2D space.

        The distance between translations is defined as √((x₂−x₁)²+(y₂−y₁)²).

        :param other: The translation to compute the distance to.

        :returns: The distance between the two translations.
        """
    def distanceFeet(self, arg0: Translation2d) -> feet: ...
    @staticmethod
    def fromFeet(x: feet, y: feet) -> Translation2d: ...
    def nearest(self, translations: typing.List[Translation2d]) -> Translation2d: 
        """
        Returns the nearest Translation2d from a collection of translations

        :param translations: The collection of translations.

        :returns: The nearest Translation2d from the collection.
        """
    def norm(self) -> meters: 
        """
        Returns the norm, or distance from the origin to the translation.

        :returns: The norm of the translation.
        """
    def normFeet(self) -> feet: ...
    def rotateBy(self, other: Rotation2d) -> Translation2d: 
        """
        Applies a rotation to the translation in 2D space.

        This multiplies the translation vector by a counterclockwise rotation
        matrix of the given angle.

        ::

          [x_new]   [other.cos, -other.sin][x]
          [y_new] = [other.sin,  other.cos][y]

        For example, rotating a Translation2d of &lt;2, 0&gt; by 90 degrees will
        return a Translation2d of &lt;0, 2&gt;.

        :param other: The rotation to rotate the translation by.

        :returns: The new rotated translation.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Translation3d():
    """
    Represents a translation in 3D space.
    This object can be used to represent a point or a vector.

    This assumes that you are using conventional mathematical axes. When the
    robot is at the origin facing in the positive X direction, forward is
    positive X, left is positive Y, and up is positive Z.
    """
    def X(self) -> meters: 
        """
        Returns the X component of the translation.

        :returns: The Z component of the translation.
        """
    def Y(self) -> meters: 
        """
        Returns the Y component of the translation.

        :returns: The Y component of the translation.
        """
    def Z(self) -> meters: 
        """
        Returns the Z component of the translation.

        :returns: The Z component of the translation.
        """
    def __abs__(self) -> meters: ...
    def __add__(self, arg0: Translation3d) -> Translation3d: 
        """
        Returns the sum of two translations in 3D space.

        For example, Translation3d{1.0, 2.5, 3.5} + Translation3d{2.0, 5.5, 7.5} =
        Translation3d{3.0, 8.0, 11.0}.

        :param other: The translation to add.

        :returns: The sum of the translations.
        """
    def __eq__(self, arg0: Translation3d) -> bool: 
        """
        Checks equality between this Translation3d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __getitem__(self, arg0: int) -> meters: ...
    @typing.overload
    def __init__(self) -> None: 
        """
        Constructs a Translation3d with X, Y, and Z components equal to zero.

        Constructs a Translation3d with the X, Y, and Z components equal to the
        provided values.

        :param x: The x component of the translation.
        :param y: The y component of the translation.
        :param z: The z component of the translation.

        Constructs a Translation3d with the provided distance and angle. This is
        essentially converting from polar coordinates to Cartesian coordinates.

        :param distance: The distance from the origin to the end of the translation.
        :param angle:    The angle between the x-axis and the translation vector.
        """
    @typing.overload
    def __init__(self, distance: meters, angle: Rotation3d) -> None: ...
    @typing.overload
    def __init__(self, x: meters, y: meters, z: meters) -> None: ...
    def __len__(self) -> int: ...
    def __mul__(self, arg0: float) -> Translation3d: 
        """
        Returns the translation multiplied by a scalar.

        For example, Translation3d{2.0, 2.5, 4.5} * 2 = Translation3d{4.0, 5.0,
        9.0}.

        :param scalar: The scalar to multiply by.

        :returns: The scaled translation.
        """
    def __neg__(self) -> Translation3d: 
        """
        Returns the inverse of the current translation. This is equivalent to
        negating all components of the translation.

        :returns: The inverse of the current translation.
        """
    def __repr__(self) -> str: ...
    def __sub__(self, arg0: Translation3d) -> Translation3d: 
        """
        Returns the difference between two translations.

        For example, Translation3d{5.0, 4.0, 3.0} - Translation3d{1.0, 2.0, 3.0} =
        Translation3d{4.0, 2.0, 0.0}.

        :param other: The translation to subtract.

        :returns: The difference between the two translations.
        """
    def __truediv__(self, arg0: float) -> Translation3d: 
        """
        Returns the translation divided by a scalar.

        For example, Translation3d{2.0, 2.5, 4.5} / 2 = Translation3d{1.0, 1.25,
        2.25}.

        :param scalar: The scalar to divide by.

        :returns: The scaled translation.
        """
    def distance(self, other: Translation3d) -> meters: 
        """
        Calculates the distance between two translations in 3D space.

        The distance between translations is defined as
        √((x₂−x₁)²+(y₂−y₁)²+(z₂−z₁)²).

        :param other: The translation to compute the distance to.

        :returns: The distance between the two translations.
        """
    def distanceFeet(self, arg0: Translation3d) -> feet: ...
    @staticmethod
    def fromFeet(x: feet, y: feet, z: feet) -> Translation3d: ...
    def norm(self) -> meters: 
        """
        Returns the norm, or distance from the origin to the translation.

        :returns: The norm of the translation.
        """
    def normFeet(self) -> feet: ...
    def rotateBy(self, other: Rotation3d) -> Translation3d: 
        """
        Applies a rotation to the translation in 3D space.

        For example, rotating a Translation3d of &lt;2, 0, 0&gt; by 90 degrees
        around the Z axis will return a Translation3d of &lt;0, 2, 0&gt;.

        :param other: The rotation to rotate the translation by.

        :returns: The new rotated translation.
        """
    def toTranslation2d(self) -> Translation2d: 
        """
        Returns a Translation2d representing this Translation3d projected into the
        X-Y plane.
        """
    @property
    def x(self) -> meters:
        """
        :type: meters
        """
    @property
    def x_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def y(self) -> meters:
        """
        :type: meters
        """
    @property
    def y_feet(self) -> feet:
        """
        :type: feet
        """
    @property
    def z(self) -> meters:
        """
        :type: meters
        """
    @property
    def z_feet(self) -> feet:
        """
        :type: feet
        """
    __hash__ = None
    pass
class Twist2d():
    """
    A change in distance along a 2D arc since the last pose update. We can use
    ideas from differential calculus to create new Pose2ds from a Twist2d and
    vice versa.

    A Twist can be used to represent a difference between two poses.
    """
    def __eq__(self, arg0: Twist2d) -> bool: 
        """
        Checks equality between this Twist2d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __init__(self, dx: meters = 0, dy: meters = 0, dtheta: radians = 0) -> None: ...
    def __mul__(self, arg0: float) -> Twist2d: 
        """
        Scale this by a given factor.

        :param factor: The factor by which to scale.

        :returns: The scaled Twist2d.
        """
    def __repr__(self) -> str: ...
    @staticmethod
    def fromFeet(dx: feet = 0, dy: feet = 0, dtheta: radians = 0) -> Twist2d: ...
    @property
    def dtheta(self) -> radians:
        """
        Angular "dtheta" component (radians)

        :type: radians
        """
    @dtheta.setter
    def dtheta(self, arg0: radians) -> None:
        """
        Angular "dtheta" component (radians)
        """
    @property
    def dtheta_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @dtheta_degrees.setter
    def dtheta_degrees(self, arg1: degrees) -> None:
        pass
    @property
    def dx(self) -> meters:
        """
        Linear "dx" component

        :type: meters
        """
    @dx.setter
    def dx(self, arg0: meters) -> None:
        """
        Linear "dx" component
        """
    @property
    def dx_feet(self) -> feet:
        """
        :type: feet
        """
    @dx_feet.setter
    def dx_feet(self, arg1: feet) -> None:
        pass
    @property
    def dy(self) -> meters:
        """
        Linear "dy" component

        :type: meters
        """
    @dy.setter
    def dy(self, arg0: meters) -> None:
        """
        Linear "dy" component
        """
    @property
    def dy_feet(self) -> feet:
        """
        :type: feet
        """
    @dy_feet.setter
    def dy_feet(self, arg1: feet) -> None:
        pass
    __hash__ = None
    pass
class Twist3d():
    """
    A change in distance along a 3D arc since the last pose update. We can use
    ideas from differential calculus to create new Pose3ds from a Twist3d and
    vice versa.

    A Twist can be used to represent a difference between two poses.
    """
    def __eq__(self, arg0: Twist3d) -> bool: 
        """
        Checks equality between this Twist3d and another object.

        :param other: The other object.

        :returns: Whether the two objects are equal.
        """
    def __init__(self, dx: meters = 0, dy: meters = 0, dz: meters = 0, rx: radians = 0, ry: radians = 0, rz: radians = 0) -> None: ...
    def __mul__(self, arg0: float) -> Twist3d: 
        """
        Scale this by a given factor.

        :param factor: The factor by which to scale.

        :returns: The scaled Twist3d.
        """
    def __repr__(self) -> str: ...
    @staticmethod
    def fromFeet(dx: feet = 0, dy: feet = 0, dz: feet = 0, rx: radians = 0, ry: radians = 0, rz: radians = 0) -> Twist3d: ...
    @property
    def dx(self) -> meters:
        """
        Linear "dx" component

        :type: meters
        """
    @dx.setter
    def dx(self, arg0: meters) -> None:
        """
        Linear "dx" component
        """
    @property
    def dx_feet(self) -> feet:
        """
        :type: feet
        """
    @dx_feet.setter
    def dx_feet(self, arg1: feet) -> None:
        pass
    @property
    def dy(self) -> meters:
        """
        Linear "dy" component

        :type: meters
        """
    @dy.setter
    def dy(self, arg0: meters) -> None:
        """
        Linear "dy" component
        """
    @property
    def dy_feet(self) -> feet:
        """
        :type: feet
        """
    @dy_feet.setter
    def dy_feet(self, arg1: feet) -> None:
        pass
    @property
    def dz(self) -> meters:
        """
        Linear "dz" component

        :type: meters
        """
    @dz.setter
    def dz(self, arg0: meters) -> None:
        """
        Linear "dz" component
        """
    @property
    def dz_feet(self) -> feet:
        """
        :type: feet
        """
    @dz_feet.setter
    def dz_feet(self, arg1: feet) -> None:
        pass
    @property
    def rx(self) -> radians:
        """
        Rotation vector x component.

        :type: radians
        """
    @rx.setter
    def rx(self, arg0: radians) -> None:
        """
        Rotation vector x component.
        """
    @property
    def rx_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @rx_degrees.setter
    def rx_degrees(self, arg1: degrees) -> None:
        pass
    @property
    def ry(self) -> radians:
        """
        Rotation vector y component.

        :type: radians
        """
    @ry.setter
    def ry(self, arg0: radians) -> None:
        """
        Rotation vector y component.
        """
    @property
    def ry_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @ry_degrees.setter
    def ry_degrees(self, arg1: degrees) -> None:
        pass
    @property
    def rz(self) -> radians:
        """
        Rotation vector z component.

        :type: radians
        """
    @rz.setter
    def rz(self, arg0: radians) -> None:
        """
        Rotation vector z component.
        """
    @property
    def rz_degrees(self) -> degrees:
        """
        :type: degrees
        """
    @rz_degrees.setter
    def rz_degrees(self, arg1: degrees) -> None:
        pass
    __hash__ = None
    pass
