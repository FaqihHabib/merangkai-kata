from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.core.window import Window

class SplashScreen(Screen):
    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background untuk Splash Screen
        with self.canvas.before:
            self.bg = Rectangle(source='gambar/splash_screen.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Tambahkan layout ke splash screen
        self.add_widget(layout)

        # Mainkan musik backsound khusus untuk splash screen
        self.music = SoundLoader.load('musik/splashsound.mp3')
        if self.music:
            self.music.play()

        # Jadwalkan pergantian ke halaman berikutnya setelah 3 detik
        Clock.schedule_once(self.go_to_home, 8)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_to_home(self, dt):
        self.manager.current = 'start_screen'  # Pergi ke halaman Home setelah splash screen
        if self.music:
            self.music.stop()  # Hentikan musik setelah beralih ke halaman Home
