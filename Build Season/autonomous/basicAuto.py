import math
from magicbot import AutonomousStateMachine, timed_state, state
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
from components.launcher.launcherController import LauncherController

# this is one of your components
def distance_to_rotation(distance, wheel_diamter=0.114):
    return distance / (math.pi*wheel_diamter)
    
DISTANCE1 = 3 # m
DISTANCE2 = 5 # m
class DefaultAuto(AutonomousStateMachine):
     
    SwerveDrive : SwerveDrive
    LauncherController: LauncherController
    MODE_NAME = "Default Auto"
    DEFAULT = True

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
        print(self.SwerveDrive.FrontLeftSpeedMotor.encoder.getPosition(), DISTANCE1)
        if self.SwerveDrive.atDistance():
            self.next_state('__startLauncher__')     
        
    @state()
    def __startLauncher__(self):
        self.LauncherController.shootSpeaker()
        self.LauncherController.runLauncher()
        self.next_state('__shoot__')

    @state()
    def __shoot__(self):
        self.LauncherController.runLauncher()
        print("IMHERE++++++++=======================")
        if not self.LauncherController.currentlyShooting():
            self.SwerveDrive.resetEncoders()
            self.next_state('__driveBackwards2__')
    
   
    @state()
    def __driveBackwards2__(self):
        self.SwerveDrive.goDistance(distance_to_rotation(DISTANCE2), 0, 0)
        self.SwerveDrive.execute()
        self.next_state('__atDistance__') 
        # print(f"[{time.time()}] ================================= I am moving =======================================")

        return False

    @state()
    def __atDistance__(self):
        self.SwerveDrive.execute()
        if self.SwerveDrive.atDistance():
            self.next_state('__stop__')        
        
    @state()
    def __stop__(self):
        pass
        # print(f"[{time.time()}] ================================= Finished. =======================================")

        
        