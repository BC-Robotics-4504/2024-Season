from magicbot import StateMachine, state
from enum import Enum
from wpilib import Timer

from components.swerveDrive.swerveDrive import SwerveDrive
from components.launcher.launcher import Launcher
from components.vision.vision import Vision
from components.config import RobotConfig

class LauncherActions(Enum):
    RAISE_INTAKE = 1
    LOWER_INTAKE = 2
    SHOOT_SPEAKER = 3
    SHOOT_AMP = 4
    WAIT = 5

class LauncherController(StateMachine):
    MODE_NAME = "Launcher Controller"
    DEFAULT = False
    
    target_action = LauncherActions.WAIT

    Kp = -0.1

    RobotConfig: RobotConfig
    Launcher: Launcher

    isEngaged = False
    
    timer = Timer()
    timer.start()

    def lowerIntake(self):
        self.target_action = LauncherActions.LOWER_INTAKE

    def raiseIntake(self):
        self.target_action = LauncherActions.RAISE_INTAKE
        
    def raiseIntakeAmp(self):
        self.target_action = LauncherActions.SHOOT_AMP

    def shootSpeaker(self):
        self.target_action = LauncherActions.SHOOT_SPEAKER

    def runLauncher(self):
        self.engage()

    '''
    STATE MACHINE DEFINITIONS ===================================
    '''

    @state(first=True)
    def __wait__(self):       
        if self.Launcher.isNoteInIntake():
            self.next_state_now('__raiseIntake__')
        
        if self.target_action == LauncherActions.RAISE_INTAKE:
            self.next_state('__raiseIntake__')

        if self.target_action == LauncherActions.LOWER_INTAKE:
            self.next_state('__lowerIntake__')
            
        if self.target_action == LauncherActions.SHOOT_SPEAKER:
            self.next_state('__spinupLauncher__')
            
        if self.target_action == LauncherActions.SHOOT_AMP:
            self.next_state('__ampIntake__')
            
        self.target_action = LauncherActions.WAIT
           
    @state()
    def __lowerIntake__(self):
        self.Launcher.lowerIntake()
        self.Launcher.spinIntakeIn()
        self.next_state('__wait__')
            
    @state()
    def __spinupLauncher__(self):
        self.Launcher.spinupShooter()
        if self.Launcher.isLauncherAtSpeed():
            self.timer.restart()
            self.next_state_now('__launchNoteSpeaker__')
            
    
    @state()
    def __launchNoteSpeaker__(self):
        self.Launcher.feedShooterSpeaker()
        if self.timer.hasElapsed(self.RobotConfig.intake_feed_delay):
            self.timer.stop()
            self.next_state('__spindownLauncher__')
            
    @state()
    def __spindownLauncher__(self):
        self.Launcher.spindownLauncher()
        self.Launcher.spindownIntake()
        self.next_state('__wait__')
            
    @state()
    def __raiseIntake__(self):
        self.Launcher.raiseIntake()
        self.Launcher.spindownIntake()
        self.next_state('__wait__')
    
    @state()
    def __ampIntake__(self):
        self.Launcher.ampIntake()
        if self.Launcher.isPositionedIntake():
            self.timer.restart()
            self.next_state('__launchNoteAmp__')
        
    @state()
    def __launchNoteAmp__(self):
        self.Launcher.feedShooterAmp()
        if self.timer.hasElapsed(self.RobotConfig.intake_feed_delay):
            self.timer.stop()
            self.next_state('__raiseIntake__')            
        

    # @state(must_finish=True)
    # def __alignLauncher__(self):
    #     # FIXME: add PID loop here? (https://docs.limelightvision.io/docs/docs-limelight/tutorials/tutorial-aiming-with-visual-servoing)
    #     target_angle = self.Vision.getTargetAngle()
    #     if abs(target_angle) > 1.0:
    #         self.SwerveDrive.goDistance(0, 0, target_angle/360)
    #     else:
    #         self.next_state('__spinupLauncher__')