class StatsManager():
    def __init__(self, Stats) -> None:
        self._stats = Stats

    def play(self):
        self._stats.changeBoredom(-50)

    def feed(self):
        self._stats.changeHunger(-50)
