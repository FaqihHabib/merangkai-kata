import random  #untuk pengacakan huruf
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import ButtonBehavior
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.animation import Animation
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

class BuahLevel(Screen):
    def __init__(self, **kwargs):
        super(BuahLevel, self).__init__(**kwargs)
        self.pick_screen = None
        self.levels = BUAH_QUESTIONS
        self.current_level_index = 0
        self.wrong_sound = SoundLoader.load('musik/wrong.mp3')  # Sound efek untuk jawaban salah
        self.lives = 3  # Inisialisasi jumlah nyawa

        layout = FloatLayout()

        # Background
        with self.canvas.before:
            self.bg = Rectangle(source='gambar/bgbuah.png', size=Window.size, pos=self.pos)
            self.bind(size=self.update_bg, pos=self.update_bg)

        # Gambar pertanyaan
        self.question_image = Image(
            source="",
            size_hint=(None, None),
            size=(400, 150),
            pos_hint={'center_x': 0.5, 'top': 0.85}
        )
        layout.add_widget(self.question_image)

        # Gambar buah di tengah
        self.buah_image = Image(
            source="",
            size_hint=(None, None),
            size=(200, 200),
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )
        layout.add_widget(self.buah_image)

        # Label untuk menampilkan jawaban pengguna
        self.answer_label = Label(
            text="",
            font_size=40,
            font_name='font/Cute_Dino.ttf',
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            size=(400, 50),
            pos_hint={'center_x': 0.5, 'center_y': 0.45}
        )
        layout.add_widget(self.answer_label)

        # Label untuk menampilkan nyawa
        self.hearts_container = FloatLayout(
            size_hint=(None, None),
            size=(150, 50),
            pos_hint={'right': 0.95, 'top': 0.95}
        )

        self.hearts = []
        heart_size = 40
        spacing = 60  # Jarak dalam piksel antara tiap hati

        for i in range(3):
            heart = Image(
                source='gambar/heart.png',
                size_hint=(None, None),
                size=(heart_size, heart_size),
                pos_hint={'right': 1 - (i * spacing/200), 'top': 1}
            )

            self.hearts.append(heart)
            self.hearts_container.add_widget(heart)
        
        layout.add_widget(self.hearts_container)

        # Layout huruf untuk jawaban
        self.letter_layout = FloatLayout(size_hint_y=None, height=100, pos_hint={'center_x': 0.5, 'center_y': 0.3})
        layout.add_widget(self.letter_layout)

        # Tombol kembali
        back_button = SoundImageButton(source='gambar/undo.png', size_hint=(None, None), size=(100, 50),
                                       pos_hint={'left': 2, 'top': 0.96})
        back_button.bind(on_press=self.go_back_to_level_select)
        layout.add_widget(back_button)

        # Tombol hapus huruf terakhir
        undo_button = SoundImageButton(source='gambar/delete.png', size_hint=(None, None), size=(100, 50),
                                       pos_hint={'x': 0.72, 'center_y': 0.45})
        undo_button.bind(on_press=self.undo_last_letter)
        layout.add_widget(undo_button)

        self.add_widget(layout)

        # Muat level pertama
        self.load_level(self.current_level_index)

    def set_pick_screen(self, pick_screen):
        """Set reference to pilihLevel screen for unlocking mechanism"""
        self.pick_screen = pick_screen

    def update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos

    def load_level(self, index):
        if index >= len(self.levels):
            self.show_all_levels_completed()
            return

        level = self.levels[index]
        self.correct_answer = level['correct_answer']
        print(self.correct_answer)
        self.user_answer = []
        self.answer_label.text = ""
        self.letter_buttons = []  # Menyimpan referensi tombol huruf

        # Update gambar pertanyaan
        self.question_image.source = level['question_image']

        # Update gambar buah
        self.buah_image.source = level['fruit_image']

        # Hapus tombol huruf sebelumnya
        self.letter_layout.clear_widgets()

        # Mengambil huruf dari jawaban yang benar
        letters = self.correct_answer.copy()  # Salin huruf jawaban yang benar
        random.shuffle(letters)  # Acak huruf

        # Jumlah huruf per baris
        max_letters_per_row = 5

        # Hitung jumlah baris yang dibutuhkan
        rows = (len(letters) + max_letters_per_row - 1) // max_letters_per_row

        for row in range(rows):
            # Posisi huruf pada baris
            row_letters = letters[row * max_letters_per_row:(row + 1) * max_letters_per_row]
            num_row_letters = len(row_letters)
            spacing = 1.0 / (num_row_letters + 1)
            letter_positions = [spacing * (i + 1) for i in range(num_row_letters)]

            for i, letter in enumerate(row_letters):
                btn = SoundImageButton(
                    source=f'gambar/huruf_buah/{letter.lower()}.png',
                    size_hint=(None, None),
                    size=(100, 100),
                    pos_hint={'center_x': letter_positions[i], 'center_y': 0.5 - (row * 1.0)} 
                )
                btn.letter = letter  # Menyimpan huruf pada button
                btn.bind(on_press=self.on_letter_press)
                self.letter_layout.add_widget(btn)

                self.letter_buttons.append(btn)
                

    def on_letter_press(self, instance):
        # Tambahkan huruf ke jawaban pengguna
        self.user_answer.append(instance.letter)
        self.answer_label.text = "".join(self.user_answer)

        
        # Hapus tombol setelah ditekan
        self.letter_layout.remove_widget(instance)

        # Periksa jika jawaban benar atau salah
        if len(self.user_answer) == len(self.correct_answer):
            if self.user_answer == self.correct_answer:
                self.show_correct_answer()
            else:
                self.show_wrong_answer()

    def show_wrong_answer(self):
        # Putar suara kesalahan
        if self.wrong_sound:
            self.wrong_sound.play()

        # Animasi getaran
        anim = Animation(pos_hint={'center_x': 0.48}, duration=0.05) + \
               Animation(pos_hint={'center_x': 0.52}, duration=0.05) + \
               Animation(pos_hint={'center_x': 0.5}, duration=0.05)
        anim.start(self.answer_label)

        # Kurangi nyawa dan update tampilan hati
        self.lives -= 1
        if self.lives > 0:
            # Hilangkan hati terakhir dengan animasi fade out
            fade_out = Animation(opacity=0, duration=0.3)
            fade_out.start(self.hearts[self.lives])

        # Periksa jika nyawa habis
        if self.lives <= 0:
            self.restart_game()
        else:
            # Reset jawaban setelah animasi selesai
            anim.bind(on_complete=lambda *x: self.reset_answer())
            # Kembalikan semua huruf ke posisi semula
            self.reset_all_letters()


    def reset_all_letters(self):
        """Mengembalikan semua tombol huruf ke layout setelah jawaban salah."""
        print("Number of buttons:", len(self.letter_buttons))
        print("Correct answer:", self.correct_answer)
        
        # Bersihkan layout huruf terlebih dahulu
        self.letter_layout.clear_widgets()

        # Kembalikan semua tombol ke layout
        for button in self.letter_buttons:
            if button not in self.letter_layout.children:
                self.letter_layout.add_widget(button)

    def reset_answer(self):
        self.user_answer = []
        self.answer_label.text = ""

    def undo_last_letter(self, instance):
        """Menghapus huruf terakhir yang dimasukkan oleh pengguna dan mengembalikan tombol huruf ke posisi semula."""
        if self.user_answer:
            # Ambil huruf terakhir yang dihapus
            last_letter = self.user_answer.pop()
            self.answer_label.text = "".join(self.user_answer)

            # Kembalikan tombol huruf ke layout
            for button in self.letter_buttons:
                if button.letter == last_letter and button not in self.letter_layout.children:
                    self.letter_layout.add_widget(button)
                    break

    def show_correct_answer(self):
    # Cek apakah ini level terakhir
        if self.current_level_index == 9 and self.pick_screen:
            print("Mencoba membuka level hewan...")  # Debug print
            PILIH_LEVEL['hewan'] = 'unlocked'
            self.pick_screen.level_status = PILIH_LEVEL
            print(f"Status level setelah update: {self.pick_screen.level_status}")  # Debug print
        
        # Tampilan notifikasi jawaban benar
        self.notif_layout = FloatLayout(size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        notif_bg = Image(source='gambar/benar.png', size_hint=(None, None), size=(600, 500),
                        pos_hint={'center_x': 0.5, 'center_y': 0.5})
        self.notif_layout.add_widget(notif_bg)

        # Tombol kembali ke pemilihan level
        btn_back = SoundImageButton(source='gambar/back.png', size_hint=(None, None), size=(100, 100),
                                    pos_hint={'center_x': 0.3, 'center_y': 0.2})
        btn_back.bind(on_press=self.go_back_to_level_select)
        self.notif_layout.add_widget(btn_back)

        # Tombol untuk lanjut ke level berikutnya
        if self.current_level_index < 9:  # Jika bukan level terakhir
            btn_next = SoundImageButton(source='gambar/next.png', size_hint=(None, None), size=(100, 100),
                                        pos_hint={'center_x': 0.7, 'center_y': 0.2})
            btn_next.bind(on_press=self.go_to_next_level)
            self.notif_layout.add_widget(btn_next)

        self.add_widget(self.notif_layout)

    def go_back_to_level_select(self, instance):
        # Debug print
        print(f"Current level index: {self.current_level_index}")
        print(f"Level status before going back: {self.pick_screen.level_status if self.pick_screen else 'No pick screen'}")
        
        # Hapus notifikasi jika ada
        if hasattr(self, 'notif_layout') and self.notif_layout in self.children:
            self.remove_widget(self.notif_layout)
        
        # Perbarui status di pick_screen jika ini adalah level terakhir
        if self.current_level_index == 9 and self.pick_screen:
            PILIH_LEVEL['hewan'] = 'unlocked'
            self.pick_screen.level_status = PILIH_LEVEL
            print("Level hewan dibuka sebelum kembali ke menu")
            print(f"Updated status: {PILIH_LEVEL}")
        
        self.manager.current = 'pick_screen'

    def go_to_next_level(self, instance):
        # Hapus notifikasi
        if hasattr(self, 'notif_layout') and self.notif_layout in self.children:
            self.remove_widget(self.notif_layout)

        print(f"Moving from level {self.current_level_index} to {self.current_level_index + 1}")
        
        # Pindah ke level berikutnya
        if self.current_level_index < len(self.levels) - 1:
            self.current_level_index += 1
            self.load_level(self.current_level_index)
        else:
            print("Ini adalah level terakhir")
            if self.pick_screen:
                PILIH_LEVEL['hewan'] = 'unlocked'
                self.pick_screen.level_status = PILIH_LEVEL
                print(f"Level status updated: {self.pick_screen.level_status}")
            self.manager.current = 'pick_screen'

    def restart_game(self):
       # Restart game dari level pertama
        self.current_level_index = 0
        self.lives = 3
        self.reset_answer()
        # Reset tampilan hati
        for heart in self.hearts:
            heart.opacity = 1  # Tampilkan kembali semua hati
        
        self.load_level(self.current_level_index)

    def on_enter(self, *args):
        """Method ini akan dipanggil setiap kali layar ini dimasuki kembali."""
        self.reset_answer()  # Reset jawaban saat masuk kembali ke level
        self.load_level(self.current_level_index)  # Reset tombol huruf
