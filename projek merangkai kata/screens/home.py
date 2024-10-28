from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.animation import Animation 

class SoundImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(SoundImageButton, self).__init__(**kwargs)
        # Muat sound effect klik
        self.click_sound = SoundLoader.load('musik/click.mp3')

    def on_press(self):
        # Mainkan sound effect ketika tombol ditekan
        if self.click_sound:
            self.click_sound.play()
        super(SoundImageButton, self).on_press()  

class ImageButton(ButtonBehavior, Image):
    pass

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = Rectangle(source='./gambar/bg.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)
        
        # Musik
        self.music_on = False
        self.music = SoundLoader.load('musik/kids_music.mp3')
        if self.music:
            self.music.loop = True

        # Tombol musik
        music_button = ImageButton(
            source='gambar/music_off.png',
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'right': 0.9, 'top': 0.96}
        )
        music_button.bind(on_press=self.toggle_music)
        layout.add_widget(music_button)

        # Gambar logo dan tombol
        layout.add_widget(Label(size_hint_y=None, height=100))  
        self.judul_gambar = Image(source='gambar/judul.png', size_hint=(None, None), size=(500, 250), pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(self.judul_gambar)

        layout.add_widget(Label(size_hint_y=None, height=50))

        self.start_button = SoundImageButton(
            source='gambar/mulai.png',
            size_hint=(None, None),
            size=(500, 250),
            pos_hint={'center_x': 0.5, 'center_y': 0.3}
        )
        self.start_button.bind(on_press=self.go_to_difficulty)
        layout.add_widget(self.start_button)

        layout.add_widget(Label(size_hint_y=None, height=100)) 
        self.add_widget(layout)

        self.animate_logo()
        self.animate_start_button()

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_to_difficulty(self, instance):
        self.manager.current = 'pick_screen'

    def toggle_music(self, instance):
        if self.music_on:
            self.music.stop()
            instance.source = 'gambar/music_off.png'
        else:
            self.music.play()
            instance.source = 'gambar/music_on.png'
        self.music_on = not self.music_on

    def animate_logo(self):
        # Animasi logo naik-turun
        anim = Animation(pos_hint={'center_y': 0.75}, duration=1.5) + Animation(pos_hint={'center_y': 0.7}, duration=1.5)
        anim.repeat = True  # Ulangi animasi
        anim.start(self.judul_gambar)

    def animate_start_button(self):
        # Animasi zoom in dan zoom out tombol "Mulai"
        anim = Animation(size=(520, 270), duration=1.2) + Animation(size=(500, 250), duration=1.2)
        anim.repeat = True  # Ulangi animasi secara terus menerus
        anim.start(self.start_button)
