from magicbot import AutonomousStateMachine, timed_state, state
import wpilib
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
import time
from components.launcher.launcherController import LauncherController

# this is one of your components

BACKUP_DISTANCE = 2.0 #Meters

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
       self.next_state('__driveBackwards__')

    @state()
    def __shoot__(self):
        self.LauncherController.shootSpeaker()
        if not self.LauncherController.currentlyShooting():
            self.next_state('__driveBackwards__')
        return False

    @state()
    def __driveBackwards__(self):
        self.SwerveDrive.goDistance(BACKUP_DISTANCE, 0, 0)
        self.SwerveDrive.execute()
        # print(f"[{time.time()}] ================================= I am moving =======================================")
        if self.SwerveDrive.atDistance():
            self.next_state('__stop__')
        return False
        
    @state()
    def __stop__(self):
        pass
        # print(f"[{time.time()}] ================================= Finished. =======================================")

        
        