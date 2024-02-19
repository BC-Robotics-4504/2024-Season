from magicbot import StateMachine, timed_state, state

from components.launcher.launcher import Launcher, IntakeLevelPositions, IntakeRollerPosiitons, ShootingFlywheelPositions

class LauncherController(StateMachine):
    MODE_NAME = "Launcher Controller"
    DEFAULT = False

    launcher: Launcher

    move_changed: bool = False

    __actionlowerIntake__ = False
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

    def run(self):
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
            
        pass

    @state(must_finish=True)
    def __raiseIntake__(self):
        if self.launcher.IntakeLevelPosition != IntakeLevelPositions.RAISED:
            self.launcher.retractIntake()
        else:
            self.next_state('__spindownIntake__')

    @state(must_finish=True)
    def __spindownIntake__(self):
        if self.launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.STOPPED:
            self.launcher.spindownIntake()
        else:
            self.next_state('__wait__')
            
    @state(must_finish=True)
    def __spinupLauncher__(self):
        if self.launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.READY:
            self.launcher.spinIntakeForward()
        else:
            self.next_state('__shootLauncher__')

    @state(timed_state=1.0, must_finish=True)
    def __feedLauncher__(self):
        if self.launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.FORWARD:
            self.launcher.spinIntakeForward()
        else:
            self.next_state('__spindownLauncher__')

    @state(must_finish=True)
    def __spindownLauncher__(self):
        if self.launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.STOPPED:
            self.launcher.spindownShooter()
        else:
            self.next_state('__wait__')

    @state(must_finish=True)
    def __lowerIntake__(self):
        if self.launcher.IntakeLevelPosition != IntakeLevelPositions.LOWERED:
            self.launcher.lowerIntake()
        # self.isEngaged = True
        else:
            self.next_state('__spinupIntake__')

    @state(must_finish=True)
    def __spinupIntake__(self):
        if self.launcher.IntakeRollerPosiiton != IntakeRollerPosiitons.REVERSE:
            self.launcher.spinIntakeReverse()
        else:
            self.next_state('__wait__')