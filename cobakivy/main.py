from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

class MerangkaiKataApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)

        with layout.canvas.before:
            Color(0.8, 0.8, 0.8, 1)
            Rectangle(pos=layout.pos, size=layout.size)

        top_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.1))
        title_label = Label(
            text="MERANGKAI\nKATA",
            font_size='48sp',
            halign='left',
            valign='middle',
            color=(0, 0, 0, 1)
        )
        top_layout.add_widget(title_label)

        music_button = Button(
            text="Musik",
            font_size='18sp',
            size_hint=(0.1, 1)
        )
        music_button.bind(on_press=self.toggle_music)  # tambahkan fungsi toggle_music untuk tombol musik
        top_layout.add_widget(music_button, index=0)

        layout.add_widget(top_layout)

        start_button = Button(
            text="Mulai",
            font_size='24sp',
            size_hint=(1, 0.1)
        )
        layout.add_widget(start_button)

        exit_button = Button(
            text="Keluar",
            font_size='24sp',
            size_hint=(1, 0.1)
        )
        exit_button.bind(on_press=self.exit_app)  # tambahkan fungsi exit_app untuk tombol keluar
        layout.add_widget(exit_button)

        return layout

    def toggle_music(self, instance):
        # tambahkan kode untuk mengaktifkan atau menonaktifkan musik di sini
        pass

    def exit_app(self, instance):
        App.get_running_app().stop()

if __name__ == "__main__":
    MerangkaiKataApp().run()