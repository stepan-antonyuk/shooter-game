from Universe import Universe


class Action:
    def is_done(self):
        return False

    def change_universe(self, universe: Universe):
        pass


class DoneAction(Action):
    def is_done(self):
        return True


class NopAction(Action):
    pass


class DebugAction(Action):
    def __init__(self, message):
        self.message = message

    def change_universe(self, universe):
        print(self.message)


class ChangeModeAction(Action):
    def __init__(self, mode):
        self.mode = mode

    def change_universe(self, universe):
        universe.mode = self.mode


class AddBlockAction(Action):
    def change_universe(self, universe):
        pass


class JumpAction(Action):
    def change_universe(self, universe):
        print("jumping")
        universe.hero.state = "jumping"


class MoveAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def change_universe(self, universe):
        universe.hero.direction = self.direction
        universe.hero.move()


class RunAction(Action):
    @staticmethod
    def change_status_to_run(universe):
        print("run boy run")
        universe.hero.state = "running"


class StandAction(Action):
    @staticmethod
    def change_status_to_standing(universe):
        universe.hero.state = "standing"
        print("standing")


class CrouchAction(Action):
    def change_universe(self, universe):
        universe.hero.state = "crouch"
