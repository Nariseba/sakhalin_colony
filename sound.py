from PyQt5.QtCore import QThread, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent


class SoundThread(QThread):    
    def __init__(self):
        super(QThread, self).__init__()
        self.player = QMediaPlayer()
    def playMainTheme(self):
        self.player.setVolume(100)
        self.soundUrl = QUrl.fromLocalFile('sound/main-theme.mp3')
        self.content = QMediaContent(self.soundUrl)
        self.player.setMedia(self.content)
        self.player.play() 
    def slowMute(self, timer):
            self.muteTimer = self.startTimer(timer)
    def timerEvent(self, event):
        if event.timerId() == self.muteTimer:
            self.player.setVolume(self.player.volume() - 1)
            if not self.player.volume(): self.player.stop()
    def playTrack(self, trackUrl, volume, timer):
        if not self.player.volume():
            self.player.setVolume(volume)
            self.soundUrl = QUrl.fromLocalFile(trackUrl)
            self.content = QMediaContent(self.soundUrl)
            self.player.setMedia(self.content)
            self.player.play()
            self.slowMute(timer)
    def playMini(self, trackUrl):
        self.soundUrl = QUrl.fromLocalFile(trackUrl)
        self.content = QMediaContent(self.soundUrl)
        self.player.setMedia(self.content)
        self.player.play()