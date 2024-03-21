import math
from magicbot import AutonomousStateMachine, timed_state, state
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
from components.launcher.launcherController import LauncherController
from components.launcher.launcher import Launcher
from components.config import RobotConfig
from wpilib import Timer
# this is one of your components
def distance_to_rotation(distance, wheel_diamter=0.114):
    return distance / (math.pi*wheel_diamter)
    
DISTANCE1 = 3 # m
DISTANCE2 = 5 # m

class DefaultAuto(AutonomousStateMachine):
     
    SwerveDrive : SwerveDrive
    LauncherController: LauncherController
    Launcher : Launcher
    RobotConfig : RobotConfig
    MODE_NAME = "Default Auto"
    DEFAULT = True
    timer = Timer()
    timer.start()

    # Injected from the definition in robot.py

    @state(first=True)
    def start(self):
       self.engage()
       self.SwerveDrive.resetEncoders()
       self.next_state('__driveBackwards1__')
        
    @state()
    def __driveBackwards1__(self):
        self.SwerveDrive.goDistance(distance_to_rotation(DISTANCE1), 0, 0)
        self.SwerveDrive.execute()
        self.next_state('__atDistance1__') 
    
    @state()
    def __atDistance1__(self):
        self.SwerveDrive.execute()
        self.Launcher.spinupShooter()
        print(self.SwerveDrive.FrontLeftSpeedMotor.encoder.getPosition(), DISTANCE1)
        if self.SwerveDrive.atDistance():
            self.timer.restart()
            self.next_state('__spinupLauncher__')     
    @state()
    def __spinupLauncher__(self):
        if self.Launcher.isLauncherAtSpeed() or self.timer.hasElapsed(self.RobotConfig.shooting_abort_delay):
            self.timer.restart()
            self.next_state_now('__launchNoteSpeaker__')
            
    @state()
    def __launchNoteSpeaker__(self):
        self.Launcher.feedShooterSpeaker()
        if self.timer.hasElapsed(self.RobotConfig.intake_feed_delay):
            self.timer.stop()
            self.isShooting = False
            self.next_state('__spindownLauncher__')

    @state()
    def __spindownLauncher__(self):
        self.Launcher.spindownLauncher()
        self.Launcher.spindownIntake()
        self.next_state('__driveBackwards2__')
        
    # @state()
    # def __shoot__(self):
    #     self.LauncherController.runLauncher()
    #     print("IMHERE++++++++=======================")
    #     if not self.LauncherController.currentlyShooting():
    #         self.SwerveDrive.resetEncoders()
    #         self.next_state('__driveBackwards2__')
    
   
    @state()
    def __driveBackwards2__(self):
        self.SwerveDrive.goDistance(distance_to_rotation(DISTANCE2), 0, 0)
        self.SwerveDrive.execute()
        self.next_state('__stop__')
        # print(f"[{time.time()}] ================================= I am moving =======================================")

        return False
               
        
    @state()
    def __stop__(self):
        pass
        # print(f"[{time.time()}] ================================= Finished. =======================================")

        
        