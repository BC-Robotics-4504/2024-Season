from magicbot import StateMachine, timed_state, state

from components.launcher.launcher import Launcher, IntakeLevelPositions, IntakeRollerPosiitons, ShootingFlywheelPositions

class LauncherController(StateMachine):
    MODE_NAME = "Launcher Controller"
    DEFAULT = False

    Launcher: Launcher

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
            self.next_state('__spinupLauncher__')
            
    @state(must_finish=True)
    def __raiseIntake__(self):
        if self.Launcher.IntakeLevelPosition != IntakeLevelPositions.RAISED:
            self.Launcher.retractIntake()
        else:
            self.next_state('__spindownIntake__')

    @state(must_finish=True)
    def __spindownIntake__(self):
        if self.Launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.STOPPED:
            self.Launcher.spindownIntake()
        else:
            self.next_state('__wait__')
            
    @state(must_finish=True)
    def __spinupLauncher__(self):
        if self.Launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.READY:
            self.Launcher.spinIntakeForward()
        else:
            self.next_state('__shootLauncher__')

    # @timed_state(duration=1, must_finish=True) #FIXME: Why doesn't @timed_state() work here?
    @state(must_finish=True)
    def __feedLauncher__(self):
        if self.Launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.FORWARD:
            self.Launcher.spinIntakeForward()
        else:
            self.next_state('__spindownLauncher__')

    @state(must_finish=True)
    def __spindownLauncher__(self):
        if self.Launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.STOPPED:
            self.Launcher.spindownShooter()
        else:
            self.next_state('__wait__')

    @state(must_finish=True)
    def __lowerIntake__(self):
        if self.Launcher.IntakeLevelPosition != IntakeLevelPositions.LOWERED:
            self.Launcher.lowerIntake()
        # self.isEngaged = True
        else:
            self.next_state('__spinupIntake__')

    @state(must_finish=True)
    def __spinupIntake__(self):
        if self.Launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.REVERSE:
            self.Launcher.spinIntakeReverse()
        else:
            self.next_state('__wait__')