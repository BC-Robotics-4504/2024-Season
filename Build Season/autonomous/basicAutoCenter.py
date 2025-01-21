import math
from magicbot import AutonomousStateMachine, timed_state, state
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
from components.launcher.launcher import Launcher
from components.config import RobotConfig
from components.climber.climber import Climber
from wpilib import Timer
# this is one of your components
def distance_to_rotation(distance, wheel_diamter=0.114):
    return distance / (math.pi*wheel_diamter)
    
DISTANCE1 = 5 # m
DISTANCE2 = 20 # m

class DefaultAuto(AutonomousStateMachine):
     
    SwerveDrive : SwerveDrive
    # LauncherController: LauncherController
    Launcher : Launcher
    Climber : Climber
    RobotConfig : RobotConfig
    MODE_NAME = "Default Auto"
    DEFAULT = True
    timer = Timer()
    timer.start()

    # Injected from the definition in robot.py

    @state(first=True)
    def start(self):
       self.engage()
       self.next_state('__setup__')
       
    @state(must_finish=True)
    def __setup__(self):
    #    self.Climber.lowerClimber()
       self.SwerveDrive.resetEncoders()
       self.timer.reset()
       self.next_state('__driveBackwards1__')
        
    @state(must_finish= True)
    def __driveBackwards1__(self):
        self.SwerveDrive.goDistance(distance_to_rotation(DISTANCE1), 0, 0)
        self.SwerveDrive.execute()
        self.next_state('__atDistance1__') 
    
    @state(must_finish= True)
    def __atDistance1__(self):
        self.SwerveDrive.execute()
        self.Launcher.spinupShooter()
        if self.SwerveDrive.atDistance() or self.timer.hasElapsed(2.0):
            self.timer.restart()
            self.next_state('__spinupLauncher__')  
               
    @state(must_finish= True)
    def __spinupLauncher__(self):
        if self.Launcher.isLauncherAtSpeed() or self.timer.hasElapsed(2.0):
            self.timer.restart()
            self.next_state_now('__launchNoteSpeaker__')
            
    @state(must_finish= True)
    def __launchNoteSpeaker__(self):
        self.Launcher.feedShooterSpeaker()
        if self.timer.hasElapsed(self.RobotConfig.intake_feed_delay):
            self.timer.stop()
            self.isShooting = False
            self.next_state('__spindownLauncher__')

    @state(must_finish= True)
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
    
   
    @state(must_finish= True)
    def __driveBackwards2__(self):
        self.SwerveDrive.resetEncoders()
        self.SwerveDrive.goDistance(distance_to_rotation(DISTANCE2), 0, 0)
        self.SwerveDrive.execute()
        self.timer.restart()
        self.next_state('__ismoving2__')
        # print(f"[{time.time()}] ================================= I am moving =======================================")

        return False
               
    @state(must_finish=True)   
    def __ismoving2__(self):
        self.SwerveDrive.execute()
        if self.timer.hasElapsed(5.0):
            self.next_state('__stop__')

    @state()
    def __stop__(self):
        pass
        # print(f"[{time.time()}] ================================= Finished. =======================================")

        
        