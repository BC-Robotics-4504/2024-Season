from magicbot import AutonomousStateMachine, timed_state, state
import wpilib
from components.swerveDrive import swerveDrive

# this is one of your components



class DriveForward(AutonomousStateMachine):
    
    swerve : swerveDrive.SwerveDrive
    MODE_NAME = "Drive Backwards"
    DEFAULT = True

    # Injected from the definition in robot.py
   

    @timed_state(duration=3, first=True)
    def drive_backward(self):
        self.swerve.move(0, 0.25, 0)
        