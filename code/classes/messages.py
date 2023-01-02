from observer import Observer
class Messages(Observer):
    def __init__(self, petName) -> None:
        self._petName = petName

    def showBoredMsg(self):
        pass

    def showHungryMsg(self):
        pass

    def showFeedingMsg(self):
        pass

    def showPlayingMsg(self):
        pass
