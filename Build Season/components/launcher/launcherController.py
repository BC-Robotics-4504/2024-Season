from magicbot import StateMachine, timed_state, state

from components.swerveDrive.swerveDrive import SwerveDrive
from components.launcher.launcher import Launcher, IntakeLevelPositions, IntakeRollerPositions, ShootingFlywheelPositions
from components.vision.vision import Vision
from components.config import RobotConfig

class LauncherController(StateMachine):
    MODE_NAME = "Launcher Controller"
    DEFAULT = False

    Kp = -0.1
    min_command = 0.5

    RobotConfig: RobotConfig
    Launcher: Launcher
    Vision: Vision
    SwerveDrive: SwerveDrive

    move_changed: bool = False

    __actionLowerIntake__ = False
    __actionRaiseIntake__ = False
    __actionShootLauncher__ = False

    position = 0
    isEngaged = False

    def lowerIntake(self):
        self.__actionLowerIntake__ = True

    def raiseIntake(self):
        self.__actionRaiseIntake__ = True

    def shootLauncher(self):
        self.__actionShootLauncher__ = True


    def runLauncher(self):
        self.engage()

    '''
    STATE MACHINE DEFINITIONS ===================================
    '''

    @state(first=True)
    def __wait__(self):
        if self.__actionLowerIntake__:
            self.next_state('__lowerIntake__')

        elif self.__actionRaiseIntake__:
            self.next_state('__raiseIntake__')

        elif self.__actionShootLauncher__:
            self.next_state('__alignLauncher__')
            
    @state()
    def __raiseIntake__(self):
        self.Launcher.retractIntake()
        self.__actionRaiseIntake__ = False
        self.next_state('__spindownIntake__')
        
    @state()
    def __spindownIntake__(self):
        self.Launcher.spindownIntake()
        self.next_state('__wait__')

    @state()
    def __lowerIntake__(self):
        self.Launcher.lowerIntake()
        self.__actionLowerIntake__ = False
        self.next_state('__spinupIntake__')
        
    @state()
    def __spinupIntake__(self):
        self.Launcher.spinIntakeReverse()
        self.next_state('__wait__')

    @state(must_finish=True)
    def __alignLauncher__(self):
        # FIXME: add PID loop here? (https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-aiming-with-visual-servoing)
        target_angle = self.Vision.getTargetAngle()
        if abs(target_angle) > 1.0:
            self.SwerveDrive.goDistance(0, 0, target_angle/360)
        else:
            self.next_state('__spinupLauncher__')
            
    @state(must_finish=True)
    def __spinupLauncher__(self):
        if self.Launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.READY:
            # TODO: calculate correlation between target distance and shooter flywheel speed
            target_distance = self.Vision.getTargetDistance()
            shooter_speed = target_distance
            self.Launcher.spinIntakeForward(shooter_speed)
        else:
            self.next_state('__feedLauncher__')

    # @timed_state(duration=1, must_finish=True) #FIXME: Why doesn't @timed_state() work here?
    @state(must_finish=True)
    def __feedLauncher__(self):
        if self.Launcher.IntakeRollerPosition != IntakeRollerPositions.FORWARD:
            self.Launcher.spinIntakeForward()
        else:
            self.next_state('__spindownLauncher__')

    @state(must_finish=True)
    def __spindownLauncher__(self):
        self.Launcher.spindownShooter()
        self.next_state('__wait__')