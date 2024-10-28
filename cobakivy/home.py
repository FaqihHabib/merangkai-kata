import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

# Set the window size
Window.size = (800, 600)

# Halaman awal (Start Screen)
class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)

        # Background image
        with self.canvas.before:
            self.bg = kivy.graphics.Rectangle(source='bg.jpg', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)
        
        # Title
        title = Label(text='MERANGKAI KATA', font_size=48, color=(1, 1, 1, 1))
        layout.add_widget(title)

        # Spacer to push the button down (optional)
        layout.add_widget(Label(size_hint_y=None, height=100))  # Spacer
        
        # Start Button
        start_button = Button(
            text='Mulai',
            font_size=32,
            size_hint=(None, None),
            size=(200, 100),
            pos_hint={'center_x': 0.5}  # Center horizontally
        )
        start_button.bind(on_press=self.go_to_difficulty)
        layout.add_widget(start_button)

        # Spacer to balance space (optional)
        layout.add_widget(Label(size_hint_y=None, height=100))  # Spacer
        
        self.add_widget(layout)
    
    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def go_to_difficulty(self, instance):
        self.manager.current = 'difficulty_screen'

# Halaman memilih tingkat kesulitan 
class pilihLevel(Screen):
    def __init__(self, **kwargs):
        super(pilihLevel, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', spacing=10, padding=50)
        
        # Title
        title = Label(text='Pilih Tingkat Kesulitan', font_size=48, color=(1, 1, 1, 1))
        layout.add_widget(title)
        
        # Difficulty Buttons
        easy_button = Button(text='Mudah', font_size=32)
        medium_button = Button(text='Sedang', font_size=32)
        hard_button = Button(text='Sulit', font_size=32)
        
        layout.add_widget(easy_button)
        layout.add_widget(medium_button)
        layout.add_widget(hard_button)
        
        # Spacer
        layout.add_widget(Label(size_hint_y=None, height=50))  # Spacer
        
        # Back Button
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

    def go_back_home(self, instance):
        self.manager.current = 'start_screen'

# Screen Manager untuk mengatur perpindahan antar halaman
class MerangkaiKata(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='start_screen'))
        sm.add_widget(pilihLevel(name='difficulty_screen'))
        return sm

if __name__ == '__main__':
    MerangkaiKata().run()
