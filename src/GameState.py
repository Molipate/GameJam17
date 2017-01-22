
class GameState:
    def __init__(self):
        self.queue = []

    def addState(self, state):
        self.queue.append(state)

    def removeFirstState(self):
        self.queue.remove(self.getCurrentState())

    def getCurrentState(self):
        return self.queue[len(self.queue) - 1]
