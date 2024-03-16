from enum import Enum
from magicbot import StateMachine, state

from components.climber.climber import Climber

class ClimberActions(Enum):
    RAISE_ARMS = 1
    LOWER_ARMS = 2
    WAIT = 3
    HOLD = 4

class ClimberController(StateMachine):
    MODE_NAME = "Climber Controller"
    DEFAULT = False
    
    target_action = ClimberActions.WAIT

    Climber: Climber

    move_changed: bool = False

    # __actionRaise__ = False
    # __actionLower__ = False

    def raiseClimber(self):
        self.target_action = ClimberActions.RAISE_ARMS
        
    def holdClimber(self):
        self.target_action = ClimberActions.HOLD
        
    def lowerClimber(self):
        self.target_action = ClimberActions.LOWER_ARMS

    def runClimber(self):
        self.engage()

    @state(first=True)
    def __wait__(self):
        if self.target_action == ClimberActions.LOWER_ARMS:
            self.next_state('__lowerClimber__')

        elif self.target_action == ClimberActions.RAISE_ARMS:
            self.next_state('__raiseClimber__')
            
        self.target_action = ClimberActions.WAIT

    @state(must_finish=True)
    def __raiseClimber__(self):
        self.Climber.raiseClimber()
        if self.Climber.isAtPosition():
            self.next_state('__wait__')

    @state(must_finish=True)
    def __lowerClimber__(self):
        self.Climber.lowerClimber()
        if self.Climber.isAtPosition():
            self.next_state('__wait__')
            
    @state(must_finish=True)
    def __holdClimber__(self):
        self.Climber.lowerClimber()
        if self.Climber.isAtPosition():
            self.next_state('__wait__')
