from magicbot import StateMachine, timed_state, state

from components.climber.climber import Climber, ClimberPositions

class ClimberController(StateMachine):
    MODE_NAME = "Climber Controller"
    DEFAULT = False

    Climber: Climber

    move_changed: bool = False

    __actionRaise__ = False
    __actionLower__ = False

    def raiseClimber(self):
        self.__actionRaise__ = True

    def lowerClimber(self):
        self.__actionLower__ = True

    def runClimber(self):
        self.engage()

    @state(first=True)
    def __wait__(self):
        if self.__actionLower__:
            self.next_state('__lowerClimber__')

        elif self.__actionRaise__:
            self.next_state('__raiseClimber__')

    @state(must_finish=True)
    def __raiseClimber__(self):
        if self.Climber.ClimberPosition != ClimberPositions.RAISED:
            self.Climber.raiseClimber()
        else:
            self.next_state('__wait__')

    @state(must_finish=True)
    def __lowerClimber__(self):
        if self.Climber.ClimberPosition != ClimberPositions.LOWERED:
            self.Climber.lowerClimber()
        else:
            self.next_state('__wait__')
