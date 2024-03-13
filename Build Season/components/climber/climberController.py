from enum import Enum
from magicbot import StateMachine, state

from components.climber.climber import Climber

class ClimberActions(Enum):
    RAISE_ARMS = 1
    LOWER_ARMS = 2
    WAIT = 3

class ClimberController(StateMachine):
    MODE_NAME = "Climber Controller"
    DEFAULT = False
    
    target_action = ClimberActions.WAIT

    Climber: Climber

    move_changed: bool = False

    __actionRaise__ = False
    __actionLower__ = False

    def raiseClimber(self):
        self.target_action = ClimberActions.RAISE_ARMS

    def lowerClimber(self):
        self.target_action = ClimberActions.LOWER_ARMS

    def runClimber(self):
        self.engage()

    @state(first=True)
    def __wait__(self):
        if self.target_action:
            self.next_state('__lowerClimber__')

        elif self.target_action:
            self.next_state('__raiseClimber__')
            
        self.target_action = ClimberActions.WAIT

    @state()
    def __raiseClimber__(self):
        self.Climber.raiseClimber()
        self.next_state('__wait__')

    @state()
    def __lowerClimber__(self):
        self.Climber.lowerClimber()
        self.next_state('__wait__')
