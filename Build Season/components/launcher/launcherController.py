from magicbot import StateMachine, timed_state, state

from components.launcher.launcher import Launcher, IntakeLevelPositions, IntakeRollerPosiitons, ShootingFlywheelPositions

class LauncherController(StateMachine):
    MODE_NAME = "Launcher Controller"
    DEFAULT = False

    launcher: Launcher

    move_changed: bool = False

    position = 0
    isEngaged = False

    '''
    STATE MACHINE DEFINITIONS
    '''
    def actuate(self):
        self.engage()

    @state(first= True, must_finish= True)
    def raise_intake(self):
        if self.launcher.IntakeLevelPosition != IntakeLevelPositions.RAISED:
            self.launcher.retractIntake()
        self.isEngaged = True
        self.next_state_now('spinup_launcher')
            
    @state(must_finish=True)
    def spinup_launcher(self):
        if self.launcher.ShootingFlywheelPosition != ShootingFlywheelPositions.READY:
            self.launcher.spinForward()
        else:
            self.next_state_now('shoot_note')

    @state()
    def shoot_note(self):
        self.next_state_now('dormant')
        self.isEngaged = False

    @state()    #Waits For Activation
    def dormant(self):
        pass