from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from screens.constant import *
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
        
class pilihLevel(Screen):
    def __init__(self, **kwargs):
        super(pilihLevel, self).__init__(**kwargs)
        layout = FloatLayout()

        # Status level: buah terbuka, hewan dan kendaraan terkunci
        self.level_status = PILIH_LEVEL

        with self.canvas.before:
            self.bg = Rectangle(source='gambar/bg.png', size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        layout.add_widget(Label(size_hint_y=None, height=100))

        buah_button = SoundImageButton(source='gambar/buah.png', size_hint=(None, None), size=(500, 250),
                                       pos_hint={'center_x': 0.5, 'center_y': 0.8})
        buah_button.bind(on_press=self.go_buah)
        layout.add_widget(buah_button)

        # Tombol hewan, tetap terlihat dan tambahkan gembok jika terkunci
        hewan_button = SoundImageButton(source='gambar/hewan.png', size_hint=(None, None), size=(500, 250),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.55})
        hewan_button.bind(on_press=self.go_hewan)
        layout.add_widget(hewan_button)

        if self.level_status['hewan'] == 'locked':
            gembok_hewan = Image(source='gambar/gembok.png', size_hint=(None, None), size=(100, 100),
                                 pos_hint={'center_x': 0.5, 'center_y': 0.55})
            layout.add_widget(gembok_hewan)

        # Tombol kendaraan, tetap terlihat dan tambahkan gembok jika terkunci
        kendaraan_button = SoundImageButton(source='gambar/kendaraan.png', size_hint=(None, None), size=(500, 250),
                                            pos_hint={'center_x': 0.5, 'center_y': 0.3})
        kendaraan_button.bind(on_press=self.go_kendaraan)
        layout.add_widget(kendaraan_button)

        if self.level_status['kendaraan'] == 'locked':
            gembok_kendaraan = Image(source='gambar/gembok.png', size_hint=(None, None), size=(100, 100),
                                     pos_hint={'center_x': 0.5, 'center_y': 0.3})
            layout.add_widget(gembok_kendaraan)

        # Tombol kembali
        back_button = SoundImageButton(source='gambar/undo.png', size_hint=(None, None), size=(100, 50),
                                       pos_hint={'left': 2, 'top': 0.96})
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def on_enter(self, *args):
        """Method ini akan dipanggil setiap kali layar ini dimasuki"""
        print(f"Entering pick screen. Current level status: {self.level_status}")  # Debug print
        
        # Hapus semua widget
        self.clear_widgets()
        layout = FloatLayout()

        with self.canvas.before:
            self.bg = Rectangle(source='gambar/bg.png', size=self.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Tombol buah
        buah_button = SoundImageButton(source='gambar/buah.png', size_hint=(None, None), size=(500, 250),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.8})
        buah_button.bind(on_press=self.go_buah)
        layout.add_widget(buah_button)

        # Tombol hewan
        hewan_button = SoundImageButton(source='gambar/hewan.png', size_hint=(None, None), size=(500, 250),
                                        pos_hint={'center_x': 0.5, 'center_y': 0.55})
        hewan_button.bind(on_press=self.go_hewan)
        layout.add_widget(hewan_button)

        # Debug print untuk status gembok hewan
        print(f"Hewan level status: {self.level_status['hewan']}")
        
        if self.level_status['hewan'] == 'locked':
            print("Adding lock to hewan level")  # Debug print
            gembok_hewan = Image(source='gambar/gembok.png', size_hint=(None, None), size=(100, 100),
                                pos_hint={'center_x': 0.5, 'center_y': 0.55})
            layout.add_widget(gembok_hewan)

        # Tombol kendaraan
        kendaraan_button = SoundImageButton(source='gambar/kendaraan.png', size_hint=(None, None), size=(500, 250),
                                            pos_hint={'center_x': 0.5, 'center_y': 0.3})
        kendaraan_button.bind(on_press=self.go_kendaraan)
        layout.add_widget(kendaraan_button)

        # Debug print untuk status gembok hewan
        print(f"Kendaraan level status: {self.level_status['kendaraan']}")

        if self.level_status['kendaraan'] == 'locked':
            gembok_kendaraan = Image(source='gambar/gembok.png', size_hint=(None, None), size=(100, 100),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.3})
            layout.add_widget(gembok_kendaraan)

        # Tombol kembali
        back_button = SoundImageButton(source='gambar/undo.png', size_hint=(None, None), size=(100, 50),
                                    pos_hint={'left': 2, 'top': 0.96})
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
        if self.level_status['hewan'] == 'unlocked':
            print("Accessing hewan level")
            self.manager.current = 'Hewan'
        else:
            print("Hewan level is still locked")

    def go_kendaraan(self, instance):
        if self.level_status['kendaraan'] == 'unlocked':
            print("Accessing kendaraan level")  # Pastikan hanya bisa diakses jika terbuka
            self.manager.current = 'Kendaraan'

    #digunakan untuk membuka level berikutnya setelah buah selesai
    def unlock_next_level(self):
        if self.level_status['buah'] == 'unlocked':
            self.level_status['hewan'] = 'unlocked'  # Buka kunci level hewan setelah buah selesai
        elif self.level_status['hewan'] == 'unlocked':
            self.level_status['kendaraan'] = 'unlocked'  # Buka kunci level kendaraan setelah hewan selesai
