from magicbot import StateMachine, timed_state, state

from components.climber.climber import Climber, ClimberPositions

class ClimberController(StateMachine):
    MODE_NAME = "Climber Controller"
    DEFAULT = False

    climber: Climber

    move_changed: bool = False

    __actionRaise__ = False
    __actionLower__ = False

    def raiseClimber(self):
        self.__actionRaise__ = True

    def lowerClimber(self):
        self.__actionaLower__ = True

    def run(self):
        self.engage()

    @state(first=True)
    def __wait__(self):
        if self.__actionLower__:
            self.next_state('__lowerIntake__')

        elif self.__actionRaise__:
            self.next_state('__raiseIntake__')

    @state(must_finish=True)
    def __raiseIntake__(self):
        if self.climber.ClimberPosition != ClimberPositions.RAISED:
            self.climber.raiseClimber()
        else:
            self.next_state('__wait__')

    @state(must_finish=True)
    def __lowerIntake__(self):
        if self.climber.ClimberPosition != ClimberPositions.LOWERED:
            self.climber.lowerClimber()
        else:
            self.next_state('__wait__')
