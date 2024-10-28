import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.audio import SoundLoader  # Untuk memuat dan mengontrol musik

# Mengatur ukuran halaman
Window.size = (360, 640)

class ImageButton(ButtonBehavior, Image):
    pass

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='gambar/background.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)
        
        # Musik
        self.music_on = False
        self.music = SoundLoader.load('musik/kids_music.mp3')  # Pastikan Anda memiliki file musik di folder yang sama
        if self.music:
            self.music.loop = True  # Membuat musik berulang

        # Tambahkan tombol musik di pojok kanan atas
        music_button = ImageButton(
            source='gambar/music_off.jpg',  # Gambar tombol untuk musik
            size_hint=(None, None),
            size=(50, 50),
            pos_hint={'right': 0.9, 'top': 0.96}
        )
        music_button.bind(on_press=self.toggle_music)
        layout.add_widget(music_button)

        # Spasi sebelum logo
        layout.add_widget(Label(size_hint_y=None, height=100))  
        
        # Gambar logo
        judul_gambar = Image(source='gambar/logo2.jpg', size_hint=(None, None), size=(800, 400), pos_hint={'center_x': 0.5, 'center_y':0.7})
        layout.add_widget(judul_gambar)

        # Spasi setelah logo
        layout.add_widget(Label(size_hint_y=None, height=50))  
        
        # Tombol gambar play
        start_button = ImageButton(
            source='gambar/m.jpg', 
            size_hint=(None, None),
            size=(500, 250),
            pos_hint={'center_x': 0.5, 'center_y':0.3}  
        )
        start_button.bind(on_press=self.go_to_difficulty)
        layout.add_widget(start_button)

        layout.add_widget(Label(size_hint_y=None, height=100)) 
        self.add_widget(layout)
    
    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_to_difficulty(self, instance):
        self.manager.current = 'pick_screen'

    # Fungsi untuk menyalakan/mematikan musik
    def toggle_music(self, instance):
        if self.music_on:
            self.music.stop()
            instance.source = 'gambar/music_off.jpg'  # Ganti gambar tombol menjadi gambar musik off
        else:
            self.music.play()
            instance.source = 'gambar/music_on.jpg'  # Ganti gambar tombol menjadi gambar musik on
        self.music_on = not self.music_on  # Tukar status musik

class pilihLevel(Screen):
    def __init__(self, **kwargs):
        super(pilihLevel, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='gambar/background.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Spasi sebelum gambar
        layout.add_widget(Label(size_hint_y=None, height=100))  

        # Tombol-tombol pilihan level dengan gambar
        buah_button = ImageButton(
            source='gambar/buah.png',  # Gambar tombol untuk Buah
            size_hint=(None, None),
            size=(500, 250),
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )
        buah_button.bind(on_press=self.go_buah)
        layout.add_widget(buah_button)

        hewan_button = ImageButton(
            source='gambar/hewan.png',  # Gambar tombol untuk Hewan
            size_hint=(None, None),
            size=(500, 250),
            pos_hint={'center_x': 0.5, 'center_y': 0.55}
        )
        hewan_button.bind(on_press=self.go_hewan)
        layout.add_widget(hewan_button)

        kendaraan_button = ImageButton(
            source='gambar/kendaraan.png',  # Gambar tombol untuk Kendaraan
            size_hint=(None, None),
            size=(500, 250),
            pos_hint={'center_x': 0.5, 'center_y': 0.35}
        )
        kendaraan_button.bind(on_press=self.go_kendaraan)
        layout.add_widget(kendaraan_button)

        layout.add_widget(Label(size_hint_y=None, height=50))  

        # Tambahkan tombol musik di pojok kanan atas
        back_button = ImageButton(
            source='gambar/undo.png',  # Gambar tombol untuk musik
            size_hint=(None, None),
            size=(100, 50),
            pos_hint={'left': 2, 'top': 0.96}
        )
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_home(self, instance):
        self.manager.current = 'start_screen'

    def go_buah(self, instance):
        self.manager.current = 'Buah'
    
    def go_hewan(self, instance):
        self.manager.current = 'Hewan'

    def go_kendaraan(self, instance):
        self.manager.current = 'Kendaraan'

class BuahLevel(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='gambar/buahbg.jpg', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Pertanyaan
        question_label = Label(
            text="Buah apakah ini?", 
            font_size=32,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'top': 0.95}
        )
        layout.add_widget(question_label)

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

        # Tombol huruf
        letters = ['P', 'A', 'L', 'E']
        letter_positions = [0.3, 0.45, 0.6, 0.75]  # Mengatur posisi horizontal untuk huruf
        for i, letter in enumerate(letters):
            btn = Button(
                text=letter, 
                font_size=32, 
                size_hint=(None, None), 
                size=(50, 50),
                pos_hint={'center_x': letter_positions[i], 'center_y': 0.5}
            )
            letter_layout.add_widget(btn)

        layout.add_widget(letter_layout)

        # Tombol undo
        back_button = Button(
            text='Kembali',
            font_size=32,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'bottom': 0.05}
        )
        back_button.bind(on_press=self.go_back_to_level_select)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_to_level_select(self, instance):
        self.manager.current = 'pick_screen'

class HewanLevel(Screen):
    def __init__(self, **kwargs):
        super(HewanLevel, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='gambar/jalan.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Pertanyaan
        question_label = Label(
            text="Hewan apakah ini?", 
            font_size=32,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'top': 0.95}
        )
        layout.add_widget(question_label)

        # Gambar hewan di tengah
        hewan_image = Image(
            source="gambar/kucing.png", 
            size_hint=(None, None), 
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(hewan_image)

        # Layout huruf untuk jawaban di bawah gambar
        letter_layout = FloatLayout(size_hint_y=None, height=100, pos_hint={'center_x': 0.5, 'center_y': 0.3})

        # Tombol huruf
        letters = ['K', 'U', 'C', 'I', 'N', 'G']
        letter_positions = [0.2, 0.35, 0.5, 0.65, 0.8, 0.95]  # Mengatur posisi horizontal untuk huruf
        for i, letter in enumerate(letters):
            btn = Button(
                text=letter, 
                font_size=32, 
                size_hint=(None, None), 
                size=(50, 50),
                pos_hint={'center_x': letter_positions[i], 'center_y': 0.5}
            )
            letter_layout.add_widget(btn)

        layout.add_widget(letter_layout)

        # Tombol undo
        back_button = Button(
            text='Kembali',
            font_size=32,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'bottom': 0.05}
        )
        back_button.bind(on_press=self.go_back_to_level_select)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_to_level_select(self, instance):
        self.manager.current = 'pick_screen'

class KendaraanLevel(Screen):
    def __init__(self, **kwargs):
        super(KendaraanLevel, self).__init__(**kwargs)
        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='gambar/jalan.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Pertanyaan
        question_label = Label(
            text="Kendaraan apakah ini?", 
            font_size=32,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': 0.5, 'top': 0.95}
        )
        layout.add_widget(question_label)

        # Gambar kendaraan di tengah
        kendaraan_image = Image(
            source="gambar/mobil.png", 
            size_hint=(None, None), 
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(kendaraan_image)

        # Layout huruf untuk jawaban di bawah gambar
        letter_layout = FloatLayout(size_hint_y=None, height=100, pos_hint={'center_x': 0.5, 'center_y': 0.3})

        # Tombol huruf
        letters = ['M', 'O', 'B', 'I', 'L']
        letter_positions = [0.2, 0.35, 0.5, 0.65, 0.8]
        for i, letter in enumerate(letters):
            btn = Button(
                text=letter, 
                font_size=32, 
                size_hint=(None, None), 
                size=(50, 50),
                pos_hint={'center_x': letter_positions[i], 'center_y': 0.5}
            )
            letter_layout.add_widget(btn)

        layout.add_widget(letter_layout)

        # Tombol undo
        back_button = Button(
            text='Kembali',
            font_size=32,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5, 'bottom': 0.05}
        )
        back_button.bind(on_press=self.go_back_to_level_select)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_to_level_select(self, instance):
        self.manager.current = 'pick_screen'

class MerangkaiKata(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='start_screen'))
        sm.add_widget(pilihLevel(name='pick_screen'))
        sm.add_widget(BuahLevel(name='Buah'))
        sm.add_widget(HewanLevel(name='Hewan'))  # Tambahkan screen Hewan
        sm.add_widget(KendaraanLevel(name='Kendaraan'))  # Tambahkan screen Kendaraan
        return sm

if __name__ == '__main__':
    MerangkaiKata().run()
