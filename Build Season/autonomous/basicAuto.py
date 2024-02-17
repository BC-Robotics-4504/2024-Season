from magicbot import AutonomousStateMachine, timed_state, state
import wpilib
from components.swerveDrive.swerveDrive import SwerveDrive, SparkMaxDriving
import time

# this is one of your components



class DriveForward(AutonomousStateMachine):
    
    SwerveDrive : SwerveDrive
    MODE_NAME = "Drive Backwards"
    DEFAULT = True

    # Injected from the definition in robot.py

    @state(first=True, must_finish= True)
    def drive(self):
        self.SwerveDrive.goDistance(3.0, 0, 0)
        print(f"[{time.time()}] ================================= I am moving =======================================")
        if self.SwerveDrive.atDistance():
            self.next_state('stop')
        
    @state(must_finish=True)
    def stop(self):
        print(f"[{time.time()}] ================================= Finished. =======================================")

        
        