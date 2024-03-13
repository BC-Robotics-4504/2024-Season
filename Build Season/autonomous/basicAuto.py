from magicbot import AutonomousStateMachine, timed_state, state
import wpilib
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
import time
from components.launcher.launcherController import LauncherController

# this is one of your components

BACKUP_DISTANCE = 2.75844

class DefaultAuto(AutonomousStateMachine):
     
    SwerveDrive : SwerveDrive
    LauncherController: LauncherController
    MODE_NAME = "Default Auto"
    DEFAULT = True

    # Injected from the definition in robot.py

    @state(first=True, must_finish=True)
    def start(self):
       self.engage()
       self.next_state('__shoot__')

    @state(must_finish=True)
    def __shoot__(self):
        self.LauncherController.shootSpeaker()
        if not self.LauncherController.currentlyShooting():
            self.next_state('__driveBackwards__')
        return False

    @state(must_finish=True)
    def __driveBackwards__(self):
        self.SwerveDrive.goDistance(BACKUP_DISTANCE, 0, 0)
        print(f"[{time.time()}] ================================= I am moving =======================================")
        if self.SwerveDrive.atDistance():
            self.next_state('stop')
        return False
        
    @state(must_finish=True)
    def stop(self):
        print(f"[{time.time()}] ================================= Finished. =======================================")

        
        