from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.popup import Popup

# Halaman Awal
class MainMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Tambahkan background lebih awal agar berada di bawah
        background = Image(source='bg.jpg',
                           allow_stretch=True,
                           keep_ratio=False,  # Mengisi seluruh layar tanpa mempertahankan rasio asli
                           size_hint=(1, 1),  # Ukuran gambar mengikuti seluruh layar
                           pos_hint={'center_x': 0.5, 'center_y': 0.5})
        layout.add_widget(background)

        # Tambahkan elemen UI setelah background agar berada di atas
        self.title = Label(text="MERANGKAI KATA", font_size=48, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        layout.add_widget(self.title)

        self.start_button = Button(text="Mulai", font_size=32, size_hint=(0.5, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.start_button.bind(on_press=self.start_game)
        layout.add_widget(self.start_button)

        self.add_widget(layout)

    def start_game(self, instance):
        self.manager.current = 'levelselect'

# Memilih Level
class LevelSelect(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        self.back_button = Button(text="Kembali", font_size=24, size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0.9})
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

        self.easy_button = Button(text="Mudah", font_size=32, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        self.easy_button.bind(on_press=self.go_easy)
        layout.add_widget(self.easy_button)

        self.medium_button = Button(text="Sedang", font_size=32, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.4})
        self.medium_button.bind(on_press=self.go_medium)
        layout.add_widget(self.medium_button)

        self.hard_button = Button(text="Sulit", font_size=32, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        self.hard_button.bind(on_press=self.go_hard)
        layout.add_widget(self.hard_button)

        self.add_widget(layout)

    def go_back(self, instance):
        self.manager.current = 'mainmenu'

    def go_easy(self, instance):
        self.manager.current = 'mudah'

    def go_medium(self, instance):
        self.manager.current = 'sedang'

    def go_hard(self, instance):
        self.manager.current = 'sulit'

# Fungsi umum untuk level (Mudah, Sedang, Sulit)
class GameLevel(Screen):
    def __init__(self, question, image_src, answer, **kwargs):
        super().__init__(**kwargs)
        self.answer = answer.upper()  # Jawaban benar
        self.user_answer = ""  # Jawaban yang dirangkai oleh user
        self.popup_opened = False  # Flag untuk melacak popup

        layout = FloatLayout()

        # Back button
        self.back_button = Button(text="←kembali", font_size=24, size_hint=(0.2, 0.1), pos_hint={'x': 0, 'y': 0.9})
        self.back_button.bind(on_press=self.go_back)
        layout.add_widget(self.back_button)

        # Pertanyaan
        self.question = Label(text=question, font_size=32, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        layout.add_widget(self.question)

        # Gambar
        self.image = Image(source=image_src, size_hint=(0.8, 0.4), pos_hint={'center_x': 0.5, 'center_y': 0.6})
        layout.add_widget(self.image)

        # Area untuk merangkai kata
        self.word_area = Label(text="", font_size=40, pos_hint={'center_x': 0.5, 'center_y': 0.4})
        layout.add_widget(self.word_area)

        # Huruf-huruf yang dapat dipilih
        self.letter_layout = GridLayout(cols=5, spacing=10, size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'center_y': 0.2})
        layout.add_widget(self.letter_layout)

        self.add_widget(layout)

        # Bind keyboard untuk menerima input Backspace dan Enter
        Window.bind(on_key_down=self.on_key_down)

    def on_enter(self):
        """Reset jawaban dan area jawaban ketika layar ini dimasuki."""
        self.user_answer = ""  # Reset jawaban pengguna
        self.update_word_area()  # Perbarui tampilan jawaban di layar

    def on_leave(self):
        # Unbind keyboard saat pindah screen
        Window.unbind(on_key_down=self.on_key_down)

    def update_word_area(self):
        self.word_area.text = self.user_answer

    def on_letter_press(self, instance):
        self.user_answer += instance.text
        self.update_word_area()

    def on_key_down(self, window, key, *args):
        if self.popup_opened:
            return  # Abaikan input saat popup terbuka
        if key == 8:  # Backspace
            self.user_answer = self.user_answer[:-1]
            self.update_word_area()
        elif key == 13:  # Enter
            # Cek apakah sudah ada popup terbuka, untuk menghindari double popup
            if not self.popup_opened:  # Cek flag popup
                self.check_answer()

    def check_answer(self):
        """Cek apakah jawaban benar atau salah dan tampilkan popup."""
        if self.user_answer == self.answer:
            self.show_popup("Selamat!", "Jawaban Anda benar!")
        else:
            self.show_popup("Salah!", "Aduh jawaban kamu salah nih, ayo coba lagi!")

    def show_popup(self, title, message):
        """Tampilkan popup notifikasi dengan pesan tertentu."""
        self.popup_opened = True  # Set flag popup terbuka
        content = Label(text=message)
        popup = Popup(title=title, content=content, size_hint=(0.6, 0.4))

        def close_popup(instance):
            self.popup_opened = False  # Set kembali flag popup terbuka setelah ditutup
            Window.bind(on_key_down=self.on_key_down)  # Re-bind keyboard input

        popup.bind(on_dismiss=close_popup)  # Bind dismiss event ke popup
        Window.unbind(on_key_down=self.on_key_down)  # Unbind sementara keyboard input
        popup.open()

    def go_back(self, instance):
        """Pindah kembali ke LevelSelect screen."""
        self.manager.current = 'levelselect'
        Window.unbind(on_key_down=self.on_key_down)

# Level Mudah
class EasyLevel(GameLevel):
    def __init__(self, **kwargs):
        super().__init__(question="Buah apakah ini?", image_src="apel.jpg", answer="APEL", **kwargs)
        letters = ['E', 'A', 'L', 'P']
        for letter in letters:
            btn = Button(text=letter, font_size=32)
            btn.bind(on_press=self.on_letter_press)
            self.letter_layout.add_widget(btn)

# Level Sedang
class MediumLevel(GameLevel):
    def __init__(self, **kwargs):
        super().__init__(question="Apa nama kendaraan ini?", image_src="helikopter.jpg", answer="HELIKOPTER", **kwargs)
        letters = ['E', 'L', 'P', 'O', 'H', 'I', 'K', 'T', 'R']
        for letter in letters:
            btn = Button(text=letter, font_size=32)
            btn.bind(on_press=self.on_letter_press)
            self.letter_layout.add_widget(btn)

# Level Sulit
class HardLevel(GameLevel):
    def __init__(self, **kwargs):
        super().__init__(question="Apa nama tempat ini?", image_src="perpustakaan.jpg", answer="PERPUSTAKAAN", **kwargs)
        letters = ['E', 'P', 'A', 'T', 'U', 'R', 'K', 'S', 'N']
        for letter in letters:
            btn = Button(text=letter, font_size=32)
            btn.bind(on_press=self.on_letter_press)
            self.letter_layout.add_widget(btn)

# Manajemen layar untuk berpindah antar screen
class WordPuzzleApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainMenu(name='mainmenu'))
        sm.add_widget(LevelSelect(name='levelselect'))
        sm.add_widget(EasyLevel(name='mudah'))
        sm.add_widget(MediumLevel(name='sedang'))
        sm.add_widget(HardLevel(name='sulit'))
        return sm

if __name__ == '__main__':
    WordPuzzleApp().run()
