from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.window import Window

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

class BuahLevel(Screen):
    def __init__(self, **kwargs):
        super(BuahLevel, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = Rectangle(source='gambar/buahbg.jpg', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Gambar pertanyaan (gantikan label pertanyaan dengan gambar)
        question_image = Image(
            source="gambar/pertanyaan_buah.png",  # Gambar yang berisi pertanyaan
            size_hint=(None, None),
            size=(400, 150),  # Sesuaikan ukuran gambar
            pos_hint={'center_x': 0.5, 'top': 0.85}
        )
        layout.add_widget(question_image)

        # Gambar buah di tengah
        buah_image = Image(
            source="gambar/apl.jpg", 
            size_hint=(None, None), 
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(buah_image)

        # Layout huruf untuk jawaban di bawah gambar
        letter_layout = FloatLayout(size_hint_y=None, height=100, pos_hint={'center_x': 0.5, 'center_y': 0.3})

        # Tombol huruf sebagai SoundImageButton
        letters = ['P', 'A', 'L', 'E']
        letter_positions = [0.19, 0.39, 0.59, 0.79]
        for i, letter in enumerate(letters):
            # Gunakan gambar berbeda untuk setiap huruf atau satu gambar untuk semua
            btn = SoundImageButton(
                source=f'gambar/level_buah/{letter.lower()}.png',  # Gambar huruf sebagai tombol
                size_hint=(None, None), 
                size=(200, 200),
                pos_hint={'center_x': letter_positions[i], 'center_y': 0.5}
            )
            letter_layout.add_widget(btn)

        layout.add_widget(letter_layout)

        # Tombol kembali
        back_button = SoundImageButton(source='gambar/undo.png', size_hint=(None, None), size=(100, 50), pos_hint={'left': 2, 'top': 0.96})
        back_button.bind(on_press=self.go_back_to_level_select)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_to_level_select(self, instance):
        self.manager.current = 'pick_screen'
