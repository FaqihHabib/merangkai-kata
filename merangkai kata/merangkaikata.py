import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior  
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

#mengatur ukuran halaman
Window.size = (800, 600)

class ImageButton(ButtonBehavior, Image):
    pass

#halaman awal
class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)

        #bckground
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='background.jpg', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)
        
        #spasi sebelum judul
        layout.add_widget(Label(size_hint_y=None, height=100))  
        
        #gambar judul
        judul_gambar = Image(source='judul.jpg', size_hint=(None, None), size=(800, 400), pos_hint={'center_x': 0.5})
        layout.add_widget(judul_gambar)

        #spasi setelah judul
        layout.add_widget(Label(size_hint_y=None, height=50))  
        
        #tombol gambar mulai
        start_button = ImageButton(
            source='MULAI.jpg', 
            size_hint=(None, None),
            size=(400, 200),
            pos_hint={'center_x': 0.5}  
        )
        start_button.bind(on_press=self.go_to_difficulty)
        layout.add_widget(start_button)

        layout.add_widget(Label(size_hint_y=None, height=100)) 
        
        self.add_widget(layout)
    
    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_to_difficulty(self, instance):
        self.manager.current = 'difficulty_screen'

#halaman memilih level
class pilihLevel(Screen):
    def __init__(self, **kwargs):
        super(pilihLevel, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)

        #background
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='background.jpg', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        #spasi sebelum gambar
        layout.add_widget(Label(size_hint_y=None, height=100))  
        
        #gambar judul di halaman memilih level
        judul_gambar = Image(source='judul.jpg', size_hint=(None, None), size=(400, 100), pos_hint={'center_x': 0.5})
        layout.add_widget(judul_gambar)

        easy_button = Button(text='Mudah', font_size=32)
        medium_button = Button(text='Sedang', font_size=32)
        hard_button = Button(text='Sulit', font_size=32)
        
        layout.add_widget(easy_button)
        layout.add_widget(medium_button)
        layout.add_widget(hard_button)
        
        layout.add_widget(Label(size_hint_y=None, height=50))  
        
        back_button = Button(
            text='Kembali',
            font_size=32,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5}
        )
        back_button.bind(on_press=self.go_back_home)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_back_home(self, instance):
        self.manager.current = 'start_screen'

#untuk mengatur perpindahan antar halaman
class MerangkaiKata(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='start_screen'))
        sm.add_widget(pilihLevel(name='difficulty_screen'))
        return sm

if __name__ == '__main__':
    MerangkaiKata().run()
